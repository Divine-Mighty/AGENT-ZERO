---
tags: [chassis, dimensions, iso, logistics, new-eden]
---

# Dimensions & ISO Compatibility

Both [[Product Line - Residential]] and [[Product Line - Disaster Relief Pod]] are built on a single shared chassis platform: a **40ft Hi-Cube ISO-compatible module**, matching real-world ISO 668 40HC (High Cube) shipping container geometry.

## Geometry

| Dimension | External | Internal |
|---|---|---|
| Length | 12,192 mm | 12,032 mm |
| Width | 2,438 mm | 2,352 mm |
| Height | 2,896 mm | 2,698 mm |

Wall/floor/roof buildup (cladding, insulation, structural framing, floor/ceiling cassettes — see [[Manufacturing Process]] stages 2–6) accounts for the ~160mm difference in length, ~86mm in width, and ~198mm in height between external and internal dimensions.

## ISO hardware
- **8x ISO 1161 corner castings** — fitted at Stage 1 of manufacturing ([[Manufacturing Process]]), these are the standardized fittings that let the module be lifted (via spreader bar or crane hook), stacked, and secured with standard container twist-locks.
- **Engineered stackable up to 3 high** — a structural rating on the chassis's vertical load path through the corner castings, meaning the base frame and corner posts of every unit are engineered to carry two more units' worth of dead/live/wind load stacked above them, not just their own.
- **Road, rail & sea freight compatible** — a direct consequence of matching real ISO 668 geometry: the module can move on standard container chassis trailers, intermodal rail wagons, and container ships without bespoke handling equipment.
- **Plug-and-play utility connection system** — referenced across the platform (concealed downpipe/stormwater routing in [[Product Line - Residential]] feature 4, the Disaster Relief Pod's exterior service port cluster in [[Product Line - Disaster Relief Pod]]) — standardized power/data/water/waste connection points positioned consistently across every unit so site connection does not require bespoke trade work to locate and terminate services.

## Why 40ft Hi-Cube specifically

1. **Regulatory transport envelope, not just container-industry convention.** A standard 40ft ISO length and 2,438mm (8ft) width sit within ordinary road transport envelopes across Australian states without triggering the escort/permit regime that wider modular units require — this is a meaningful cost and scheduling advantage, especially for the Disaster Relief Pod's "under 30 minutes to deploy" promise (see [[Product Line - Disaster Relief Pod]]), where a unit that requires a wide-load escort convoy cannot plausibly hit a rapid-response timeline.
2. **The "Hi-Cube" (extra-height) variant specifically** buys the internal ceiling height (2,698mm internal) needed for the residential line's "Signature architecture" feel — floor-to-ceiling glazing, floating rooflines, and a smart ceiling cassette all consume vertical space, and a standard (non-Hi-Cube) 40ft container's lower internal height would leave little room for those buildups once floor and ceiling cassette thickness is subtracted.
3. **Global handling-equipment compatibility.** Because the chassis matches real ISO 668/1161 geometry rather than a bespoke modular-building footprint, every port, rail yard, container terminal, and heavy-haul trucking company already owns equipment (spreaders, twist-lock trailers, container cranes, forklift/reach-stacker attachments) rated for this exact size and corner-casting pattern. This is a substantial and unusual advantage for a modular building product: New Eden does not need to build or contract a bespoke logistics network the way most modular/relocatable building categories do — it can plug into the existing global container logistics system, which is also directly relevant to disaster-relief deployability into remote or infrastructure-degraded areas.
4. **Manufacturing standardization.** A single fixed chassis geometry across two very different product lines (luxury residential and emergency-services) is what makes the shared factory line in [[Manufacturing Process]] and the robotic cell architecture in [[Factory & Automation Stack]] economically viable — every robotic cell's reference datum (fastening positions, robot lift points, service stub-out locations) is the same regardless of which product rolls off the line, so tooling and cell programming amortizes across both product lines' volume rather than each needing its own dedicated line.

## Load-path implications for the feature set
Several signature features are only possible *because* of this chassis choice, and should be read in conjunction with this note:
- Stacking to 3 high (see above) is why the "black steel base" finish (feature 8) deliberately foregrounds the corner-casting zone — it is genuinely the most structurally loaded part of the building, and the finish choice makes a structural fact into a visual design statement.
- Robot lift points (feature 23) and the New Eden deck system (feature 27) both key into the same ISO 1161 hard points, meaning any load applied by a bolt-on deck or handling equipment is going through a point in the structure that was already engineered for the far higher loads of stacked transport and crane-lifting — it is inherently conservative bolt-on engineering rather than a new load path.
- Expandable modules (feature 28) join at the 12,192mm end faces or along the long wall, meaning a two-module or larger New Eden building is really two (or more) independently transportable, independently ISO-rated chassis units joined on site — not a single continuous structure poured or built in place.

See [[Standards & Compliance Baseline]] for how this chassis geometry interacts with Australian transport and structural regulation, and [[Premium-Beyond-Minimum Design Philosophy]] for how the stacking/lifespan ratings are deliberately engineered above the minimum this geometry would technically require.
