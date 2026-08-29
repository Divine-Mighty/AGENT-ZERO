// Live 3D hero wings. Bundled by build.py via esbuild into watchers-site.html.
//
// The GLB arrives base64 on window.__WINGS_GLB__. Its own materials carry a
// blue emissive and full-colour textures, so both are overridden here: the
// palette stays bone on black.

import {
  Scene, PerspectiveCamera, WebGLRenderer, Box3, Vector3, Color,
  DirectionalLight, HemisphereLight, ACESFilmicToneMapping, Group,
} from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const BONE = new Color(0xE9DFC8);
const FOV = 34;

// Where the wings meet along the spine, as a fraction down their bounding
// box, and where the figure's shoulders sit as a fraction down his. Both were
// measured off the assets. Lining these two points up is what makes the pair
// read as growing out of his back rather than floating behind him.
const WING_ANCHOR = 0.30;
const FIG_SHOULDER = 0.32;

const host = document.getElementById('wings');
const figure = document.querySelector('.figure');
const fallback = document.getElementById('wings-flat');
const reduced = matchMedia('(prefers-reduced-motion: reduce)');

function fail() {
  if (host) host.hidden = true;
  if (fallback) fallback.hidden = false;
}

function toBuffer(b64) {
  const bin = atob(b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return bytes.buffer;
}

// Grey the sampled texture, then tint it bone, so the model can never bring a
// third colour onto the page.
function boneify(material) {
  material.color = new Color(0xffffff);
  if (material.emissive) material.emissive.setRGB(0, 0, 0);
  material.metalness = 0;
  material.roughness = 0.72;
  material.onBeforeCompile = (shader) => {
    shader.fragmentShader = shader.fragmentShader.replace(
      '#include <map_fragment>',
      `#include <map_fragment>
       float _lum = dot( diffuseColor.rgb, vec3( 0.2126, 0.7152, 0.0722 ) );
       diffuseColor.rgb = vec3( _lum ) * vec3( ${BONE.r}, ${BONE.g}, ${BONE.b} );`
    );
  };
  material.needsUpdate = true;
}

function start() {
  let renderer;
  try {
    renderer = new WebGLRenderer({
      alpha: true, antialias: true, powerPreference: 'high-performance',
    });
  } catch (e) { return fail(); }
  if (!renderer.getContext()) return fail();

  renderer.setClearAlpha(0);
  renderer.toneMapping = ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;
  host.appendChild(renderer.domElement);

  const scene = new Scene();
  const camera = new PerspectiveCamera(FOV, 1, 0.1, 100);
  const pivot = new Group();
  scene.add(pivot);

  // neutral lights: the bone tint comes from the shader patch, so anything
  // coloured here just drags the palette off
  const key = new DirectionalLight(0xffffff, 2.4);
  key.position.set(-2.2, 2.6, 3.4);
  const rim = new DirectionalLight(0xffffff, 1.6);
  rim.position.set(1.8, 0.6, -2.8);
  scene.add(key, rim, new HemisphereLight(0x181818, 0x000000, 0.7));

  let model = null;
  const dims = new Vector3(1, 1, 1);

  function resize() {
    const w = host.clientWidth || 1;
    const h = host.clientHeight || 1;
    renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    if (!model) return;
    // The figure stands in front of these, so the pair is deliberately wider
    // than the viewport: what should read is the span either side of him, not
    // the whole wing. Vertical overflow is fine and expected.
    const half = Math.tan((FOV * Math.PI) / 360);
    const coverW = camera.aspect < 1 ? 1.45 : 1.02;
    camera.position.z = dims.x / coverW / (2 * half * camera.aspect);
    camera.updateProjectionMatrix();

    // Put the wings' spine on the figure's shoulders. Measured off his live
    // box rather than assumed, so this holds at every breakpoint where his
    // height changes.
    const visibleH = 2 * camera.position.z * half;
    let target = 0.40;
    if (figure) {
      const box = figure.getBoundingClientRect();
      if (box.height) target = (box.top + box.height * FIG_SHOULDER) / h;
    }
    pivot.position.y = (0.5 - target) * visibleH
      - (0.5 - WING_ANCHOR) * dims.y;
  }

  new GLTFLoader().parse(toBuffer(window.__WINGS_GLB__), '', (gltf) => {
    model = gltf.scene;
    model.traverse((o) => {
      if (!o.isMesh) return;
      (Array.isArray(o.material) ? o.material : [o.material]).forEach(boneify);
    });

    const box = new Box3().setFromObject(model);
    const size = box.getSize(new Vector3());
    const mid = box.getCenter(new Vector3());
    model.position.sub(mid);
    dims.copy(size);
    // sit the pair a little high, so the headline crosses the plumage
    model.position.y -= size.y * 0.06;
    pivot.add(model);

    delete window.__WINGS_GLB__;
    resize();
    host.classList.add('ready');
    loop();
  }, fail);

  let raf = 0;
  const t0 = performance.now();

  function frame(now) {
    const t = (now - t0) / 1000;
    pivot.rotation.y = Math.sin(t * 0.24) * 0.14;
    pivot.rotation.x = Math.sin(t * 0.19) * 0.035;
    pivot.scale.setScalar(1 + Math.sin(t * 0.7) * 0.014);
    renderer.render(scene, camera);
    raf = requestAnimationFrame(frame);
  }

  function loop() {
    cancelAnimationFrame(raf);
    if (reduced.matches) { renderer.render(scene, camera); return; }
    raf = requestAnimationFrame(frame);
  }

  addEventListener('resize', () => { resize(); if (reduced.matches) loop(); });
  // his box drives the wing placement, so re-fit once he has real dimensions
  if (figure && !figure.complete) {
    figure.addEventListener('load', () => { resize(); loop(); }, { once: true });
  }
  reduced.addEventListener('change', loop);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) cancelAnimationFrame(raf);
    else loop();
  });
}

if (window.__WINGS_GLB__) start(); else fail();
