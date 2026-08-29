#!/usr/bin/env python3
"""Generate the WATCHERS angel wings -> wing_frag.svg

    python3 wing2.py

Reads assets/angel_wings.glb, projects the mesh to a front view, and traces a
flat vector silhouette out of it. Feather and Wing submeshes are traced
separately, and the feathers are sliced into depth layers so the plumage keeps
its overlap instead of collapsing into one blob.

Deterministic: same input, same output. Never hand-edit wing_frag.svg -- change
the parameters here and re-run.
"""

import json
import math
import struct
import sys

GLB = "assets/angel_wings.glb"
OUT = "wing_frag.svg"

RES = 1100          # raster width in cells; height follows the aspect
PAD = 0.012         # fraction of width kept clear around the art
EPS = 1.70          # RDP tolerance, in raster cells
MIN_AREA = 75.0     # drop traced loops smaller than this (cells^2)
TONES = (0.52, 0.74, 1.0)   # back-to-front shading bands

COMPONENT = {5120: "b", 5121: "B", 5122: "h", 5123: "H", 5125: "I", 5126: "f"}
NCOMP = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4, "MAT4": 16}


# ---------------------------------------------------------------- glTF read

def load_glb(path):
    data = open(path, "rb").read()
    magic, _ver, _len = struct.unpack_from("<III", data, 0)
    if magic.to_bytes(4, "little") != b"glTF":
        raise SystemExit("{}: not a GLB".format(path))
    off, js, bin_ = 12, None, b""
    while off < len(data):
        ln, ty = struct.unpack_from("<II", data, off)
        off += 8
        chunk = data[off:off + ln]
        if ty == 0x4E4F534A:
            js = json.loads(chunk.decode("utf-8"))
        elif ty == 0x004E4942:
            bin_ = chunk
        off += ln
    return js, bin_


def read_accessor(gl, buf, index):
    acc = gl["accessors"][index]
    view = gl["bufferViews"][acc["bufferView"]]
    n = NCOMP[acc["type"]]
    fmt = COMPONENT[acc["componentType"]]
    size = struct.calcsize("<" + fmt)
    base = view.get("byteOffset", 0) + acc.get("byteOffset", 0)
    stride = view.get("byteStride") or size * n
    out = []
    for i in range(acc["count"]):
        o = base + i * stride
        out.append(struct.unpack_from("<" + fmt * n, buf, o))
    return out


def mat_mul(a, b):
    """Column-major 4x4 multiply: result applies b first, then a."""
    out = [0.0] * 16
    for c in range(4):
        for r in range(4):
            out[c * 4 + r] = sum(a[k * 4 + r] * b[c * 4 + k] for k in range(4))
    return out


def mat_apply(m, v):
    x, y, z = v
    return (m[0] * x + m[4] * y + m[8] * z + m[12],
            m[1] * x + m[5] * y + m[9] * z + m[13],
            m[2] * x + m[6] * y + m[10] * z + m[14])


IDENTITY = [1.0 if i % 5 == 0 else 0.0 for i in range(16)]


def collect_triangles(gl, buf):
    """Walk the scene graph, return {material_name: [(p0, p1, p2), ...]}."""
    groups = {}

    def visit(node_index, parent):
        node = gl["nodes"][node_index]
        local = node.get("matrix", IDENTITY)
        world = mat_mul(parent, local)
        if "mesh" in node:
            for prim in gl["meshes"][node["mesh"]]["primitives"]:
                if prim.get("mode", 4) != 4:
                    continue
                pos = read_accessor(gl, buf, prim["attributes"]["POSITION"])
                pts = [mat_apply(world, p) for p in pos]
                idx = [i[0] for i in read_accessor(gl, buf, prim["indices"])]
                name = gl["materials"][prim["material"]]["name"]
                tris = groups.setdefault(name, [])
                base = len(tris)
                for k in range(0, len(idx) - 2, 3):
                    tris.append((pts[idx[k]], pts[idx[k + 1]], pts[idx[k + 2]],
                                 (idx[k], idx[k + 1], idx[k + 2]), base))
        for child in node.get("children", []):
            visit(child, world)

    for root in gl["scenes"][gl.get("scene", 0)]["nodes"]:
        visit(root, IDENTITY)
    return groups


# ------------------------------------------------------------ raster + trace

def project(tris_by_mat):
    """Front view: X across, Y up (flipped for SVG), Z kept as depth."""
    xs, ys = [], []
    for tris in tris_by_mat.values():
        for tri in tris:
            for p in tri[:3]:
                xs.append(p[0])
                ys.append(p[1])
    lo_x, hi_x = min(xs), max(xs)
    lo_y, hi_y = min(ys), max(ys)
    span_x, span_y = hi_x - lo_x, hi_y - lo_y

    pad = RES * PAD
    scale = (RES - 2 * pad) / span_x
    height = int(round(span_y * scale + 2 * pad))

    def to_px(p):
        # keep the model-space depth alongside the screen position; shell
        # welding needs per-vertex z, not the triangle average
        return (pad + (p[0] - lo_x) * scale,
                pad + (hi_y - p[1]) * scale,
                p[2])

    out = {}
    for name, tris in tris_by_mat.items():
        flat = []
        for tri in tris:
            flat.append((to_px(tri[0]), to_px(tri[1]), to_px(tri[2]),
                         (tri[0][2] + tri[1][2] + tri[2][2]) / 3.0,
                         tri[3], tri[4]))
        out[name] = flat
    return out, RES, height


def rasterize(tris, w, h, ox=0.0, oy=0.0):
    """Scanline-fill triangles into a binary mask (bytearray, row-major)."""
    mask = bytearray(w * h)
    for tri in tris:
        p0 = (tri[0][0] - ox, tri[0][1] - oy)
        p1 = (tri[1][0] - ox, tri[1][1] - oy)
        p2 = (tri[2][0] - ox, tri[2][1] - oy)
        ymin = max(0, int(math.floor(min(p0[1], p1[1], p2[1]))))
        ymax = min(h - 1, int(math.ceil(max(p0[1], p1[1], p2[1]))))
        if ymax < ymin:
            continue
        edges = ((p0, p1), (p1, p2), (p2, p0))
        for y in range(ymin, ymax + 1):
            cy = y + 0.5
            hits = []
            for a, b in edges:
                ay, by = a[1], b[1]
                if (ay <= cy < by) or (by <= cy < ay):
                    t = (cy - ay) / (by - ay)
                    hits.append(a[0] + (b[0] - a[0]) * t)
            if len(hits) < 2:
                continue
            hits.sort()
            x0 = max(0, int(math.floor(hits[0] + 0.5)))
            x1 = min(w - 1, int(math.ceil(hits[-1] - 0.5)))
            if x1 < x0:
                continue
            row = y * w
            for x in range(x0, x1 + 1):
                mask[row + x] = 1
    return mask


# marching-squares crossings, keyed by filled-corner bits tl|tr|br|bl
CASES = {
    1: ((0, 3),), 2: ((0, 1),), 3: ((3, 1),), 4: ((1, 2),),
    5: ((0, 3), (1, 2)), 6: ((0, 2),), 7: ((3, 2),), 8: ((3, 2),),
    9: ((0, 2),), 10: ((0, 1), (2, 3)), 11: ((1, 2),), 12: ((3, 1),),
    13: ((0, 1),), 14: ((0, 3),),
}


def trace(mask, w, h):
    """Marching squares -> closed loops. Points are on half-cell coords,
    stored doubled so they hash exactly."""
    links = {}

    def add(a, b):
        links.setdefault(a, []).append(b)
        links.setdefault(b, []).append(a)

    for j in range(-1, h):
        for i in range(-1, w):
            def at(x, y):
                if x < 0 or y < 0 or x >= w or y >= h:
                    return 0
                return mask[y * w + x]

            tl, tr = at(i, j), at(i + 1, j)
            bl, br = at(i, j + 1), at(i + 1, j + 1)
            idx = tl * 1 + tr * 2 + br * 4 + bl * 8
            segs = CASES.get(idx)
            if not segs:
                continue
            # 0=top 1=right 2=bottom 3=left, doubled integer coords
            pts = ((2 * i + 2, 2 * j + 1), (2 * i + 3, 2 * j + 2),
                   (2 * i + 2, 2 * j + 3), (2 * i + 1, 2 * j + 2))
            for a, b in segs:
                add(pts[a], pts[b])

    loops = []
    seen = set()
    for start in links:
        if start in seen:
            continue
        nxt = None
        for cand in links[start]:
            if cand not in seen:
                nxt = cand
                break
        if nxt is None:
            continue
        loop = [start]
        seen.add(start)
        cur, prev = nxt, start
        while cur is not None and cur not in seen:
            loop.append(cur)
            seen.add(cur)
            step = None
            for cand in links.get(cur, ()):
                if cand != prev and cand not in seen:
                    step = cand
                    break
            prev, cur = cur, step
        if len(loop) >= 6:
            loops.append([(x / 2.0, y / 2.0) for x, y in loop])
    return loops


def area(poly):
    a = 0.0
    for i in range(len(poly)):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % len(poly)]
        a += x0 * y1 - x1 * y0
    return abs(a) / 2.0


def rdp(points, eps):
    if len(points) < 3:
        return points
    ax, ay = points[0]
    bx, by = points[-1]
    dx, dy = bx - ax, by - ay
    norm = math.hypot(dx, dy)
    best, at = -1.0, 0
    for i in range(1, len(points) - 1):
        px, py = points[i]
        if norm < 1e-9:
            d = math.hypot(px - ax, py - ay)
        else:
            d = abs(dy * px - dx * py + bx * ay - by * ax) / norm
        if d > best:
            best, at = d, i
    if best <= eps:
        return [points[0], points[-1]]
    return rdp(points[:at + 1], eps)[:-1] + rdp(points[at:], eps)




# -------------------------------------------------------------------- emit

def components(tris):
    """Split a triangle soup into connected shells (one per feather)."""
    parent = {}

    def find(a):
        root = a
        while parent[root] != root:
            root = parent[root]
        while parent[a] != root:
            parent[a], a = root, parent[a]
        return root

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    def key(tri, i):
        # weld on position: the export is not index-welded, so shells only
        # separate correctly when coincident corners are treated as one
        x, y, z = tri[i]
        return (tri[5], round(x, 2), round(y, 2), round(z, 3))

    for tri in tris:
        ids = [key(tri, i) for i in range(3)]
        for v in ids:
            parent.setdefault(v, v)
        union(ids[0], ids[1])
        union(ids[0], ids[2])

    shells = {}
    for tri in tris:
        shells.setdefault(find(key(tri, 0)), []).append(tri)
    return list(shells.values())


def shell_path(tris):
    """Outline one shell, rasterized in its own bounding box."""
    xs = [p[i] for t in tris for p in t[:3] for i in (0, )]
    ys = [p[1] for t in tris for p in t[:3]]
    ox = math.floor(min(xs)) - 2
    oy = math.floor(min(ys)) - 2
    w = int(math.ceil(max(xs)) - ox) + 3
    h = int(math.ceil(max(ys)) - oy) + 3
    if w < 3 or h < 3 or w * h > 8_000_000:
        return ""

    mask = rasterize(tris, w, h, ox, oy)
    if not any(mask):
        return ""

    parts = []
    for loop in trace(mask, w, h):
        if area(loop) < MIN_AREA:
            continue
        simple = rdp(loop, EPS)
        if len(simple) < 3:
            continue
        pts = [(x + ox, y + oy) for x, y in simple]
        d = "M{:.1f} {:.1f}".format(*pts[0])
        d += "".join("L{:.1f} {:.1f}".format(x, y) for x, y in pts[1:])
        parts.append(d + "Z")
    return "".join(parts)


def render():
    gl, buf = load_glb(GLB)
    groups = collect_triangles(gl, buf)
    projected, w, h = project(groups)

    shells = []
    for name in ("Wing", "Feather"):
        for tris in components(projected.get(name, [])):
            depth = sum(t[3] for t in tris) / len(tris)
            shells.append((depth, name, tris))

    # back to front, so nearer feathers overlap the ones behind them
    shells.sort(key=lambda s: s[0])
    total = max(1, len(shells) - 1)

    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {} {}" '
        'role="img" aria-hidden="true" fill-rule="evenodd">'.format(w, h),
        '<g fill="currentColor" stroke="var(--void,#0A0A0A)" '
        'stroke-width="1.2" stroke-linejoin="round">',
    ]
    drawn = 0
    for i, (_depth, _name, tris) in enumerate(shells):
        d = shell_path(tris)
        if not d:
            continue
        tone = TONES[min(len(TONES) - 1, int(i / total * len(TONES)))]
        out.append('<path opacity="{:.2f}" d="{}"/>'.format(tone, d))
        drawn += 1
    out.append("</g></svg>")
    print("  {} shells, {} drawn".format(len(shells), drawn), file=sys.stderr)
    return "".join(out)


if __name__ == "__main__":
    svg = render()
    with open(OUT, "w") as fh:
        fh.write(svg)
    print("{}  {:,} bytes".format(OUT, len(svg)))
