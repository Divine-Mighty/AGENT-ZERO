# WATCHERS(R) — site

Single-page drop site. Dark, print-shop aesthetic. Bone on black.

## Build

```bash
npm install                       # three + esbuild, first time only
npx esbuild src/wings.js --bundle --format=iife --minify \
    --target=es2019 --outfile=src/wings.bundle.js
python3 cutout.py                 # hero-source.png -> hero-model.webp
python3 wing2.py                  # angel_wings.glb -> wing_frag.svg
python3 build.py                  # -> watchers-site.html
```

`cutout.py` and `wing2.py` only need re-running when their source assets
change; `build.py` is the one you run after editing `PIECES`.

The output is ~4.6MB: the three.js bundle is inlined (~590KB) and the GLB is
base64'd into the page (~3.6MB), so it stays a single self-contained file with
no network dependency but the webfonts.

`watchers-site.html` is a generated artifact with every image base64-inlined.
Never edit it directly; it gets overwritten. Product data lives in the `PIECES`
list at the top of `build.py` and is the single source of truth.

## Layout

Follows the MotionSites "Obsidian" composition: one non-scrolling fullscreen
stage, overlaid nav bar, headline block top-left, floating labels, a vertical
scroll cue, and a full-screen menu overlay with staggered link entrance.

The reference's two staggered product cards were dropped by decision, so the
wings carry the right-hand side alone. Pieces stay reachable through the
headline CTA and their `?piece=` links.

Where that reference collides with the brand rules it was followed anyway, by
decision: the full-width nav bar (rather than a floating pill) and the
backdrop-blurred overlays.

## The hero figure

`assets/hero-source.png` is the lookbook shot. `cutout.py` mattes the figure
out of it with u2net (`rembg`) and writes `assets/hero-model.webp`, which
`build.py` inlines.

Segmentation rather than a key: the hoodie is black on a near-black gradient,
so a luminance or difference key tears straight through the hood and
shoulders. The matte also ends on a flat cut at the hem, so the last tenth is
feathered and he dissolves into the void instead of stopping on a line.

He stands in front of the wings, which is why the wings are deliberately wider
than the viewport and lifted to shoulder height -- what should read is the
span either side of him, not the whole wing.

## The wings

The hero renders `assets/angel_wings.glb` live in three.js: real geometry, its
own textures, a key and rim light, and a slow yaw/scale drift. The model ships
with a blue emissive and full-colour textures, so `src/wings.js` overrides
both -- emissive is zeroed and a shader patch converts each sampled texel to
luminance and multiplies it by bone, which means the model can never put a
third colour on the page.

`wing2.py` is still live, but now only builds the **fallback**. It reads the
same GLB, projects the mesh to a front view and traces a flat silhouette:
shells are welded on vertex position (the export is not index-welded), split
into connected components, and each of the ~850 feathers becomes its own path
across three tonal bands. That SVG sits behind the canvas and is revealed if
WebGL is unavailable or the model fails to load.

Deterministic: same input, same output. Do not hand-edit `wing_frag.svg` --
change the parameters at the top of `wing2.py` and re-run.

## Placeholders — replace before launch

Two things in here are stand-ins, and both are flagged in the source:

- **The mark.** The blackletter W + WATCHERS lockup with the drip was never
  supplied to this repo, so `MARK` in `build.py` is a plain geometric eye. Drop
  the real asset in and replace that function. Do not re-letter the wordmark by
  hand and do not substitute a font for it.
- **Piece art.** `plate_svg()` generates abstract halftone print plates, seeded
  per slug, shown in the piece modal. They are not photography. Replace with
  real per-product lookbook shots when they land.

## Conventions kept

- Every piece is addressable at `?piece=<slug>`. Opening that URL cold opens
  the modal on mount; `popstate` closes it.
- Sold out is permanent. A new run gets a new slug, never a restock in place.
- Buttons say what happens: `Add to bag` -> `Added`, sold out -> `Notify me`.
- Two loops only: the wing drift and the live-drop REC dot. Alarm red is used
  for nothing else.
- Responsive to 360px, visible `:focus-visible` throughout.
  `prefers-reduced-motion` renders a single static frame of the wings instead
  of animating, and leaves everything visible. Rendering also pauses while the
  tab is hidden.

## Open work

- Real cart + checkout (Shopify Storefront API or Stripe).
- Per-piece pages with proper OG images instead of modal-only.
- Size guide and a Darwin/AU shipping table.
