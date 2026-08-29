# WATCHERS(R) — site

Single-page drop site. Dark, print-shop aesthetic. Bone on black.

## Build

```bash
python3 wing2.py     # assets/angel_wings.glb -> wing_frag.svg
python3 build.py     # PIECES + wing_frag.svg -> watchers-site.html
```

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

## The wings

`wing2.py` reads `assets/angel_wings.glb`, projects the mesh to a front view,
and traces a flat vector silhouette from it. Feather and Wing submeshes are
split into connected shells so each of the ~850 feathers becomes its own path,
sorted back to front and shaded in three tonal bands.

The export is not index-welded, so shells are welded on vertex position before
the split. Deterministic: same input, same output. Do not hand-edit
`wing_frag.svg` — change the parameters at the top of `wing2.py` and re-run.

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
- Three loops only: the wing breathe and the live-drop REC dot. Alarm red is
  used for nothing else.
- Responsive to 360px, visible `:focus-visible` throughout,
  `prefers-reduced-motion` kills the loops and leaves everything visible.

## Open work

- Real cart + checkout (Shopify Storefront API or Stripe).
- Per-piece pages with proper OG images instead of modal-only.
- Size guide and a Darwin/AU shipping table.
