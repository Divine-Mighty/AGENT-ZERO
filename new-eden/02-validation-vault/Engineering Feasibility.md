---
tags: [validation, engineering, manufacturing, new-eden]
---

# Engineering Feasibility

The core vault's manufacturing process describes an 8-stage line: ISO chassis → floor cassette → ABB-robot wall framing → roll-formed roof trusses (lowered into place) → zinc/woodgrain cladding → standing-seam roof → interiors/MEP/finishes → QC & delivery, marketed as "AI Powered Production | ABB Robotics | Digital Twin Monitoring | Zero Human Input." This note walks the same eight stages and asks, honestly, what's hard, what's real, and what's marketing.

## Stage 1 — ISO chassis
Fabricating a 40ft Hi-Cube ISO-compatible steel chassis with 8× ISO 1161 corner castings is proven, well-understood heavy-fabrication work; shipping-container and container-derived structures are built at this scale every day. The risk here isn't whether it can be built — it's that this stage sets the geometric baseline every later stage has to live inside, and a *welded* steel chassis is not a machined part. Real-world dimensional variance unit-to-unit (squareness, twist, corner-casting alignment) needs to be measured and controlled early, because it becomes the input tolerance for every robotic stage downstream.

## Stage 2 — floor cassette
Comparatively low risk. This is a well-precedented modular-construction step (insulated floor panel, structural deck) and doesn't depend on novel robotics.

## Stage 3 — ABB-robot wall framing
This is where "precision" claims start being tested. Robotic arms are excellent at repeatable, programmed motion *relative to a fixed, known reference frame*. The open question is whether the reference frame here — the as-built chassis from Stage 1, not a CAD-ideal chassis — is consistent enough for the robot's programmed moves to land within the tolerance the design needs. Two things have to both be true for this stage to deliver what the brand promises: (1) the robot cell needs vision-guided or metrology-fed correction (not blind, open-loop programmed paths) to compensate for real chassis variance, and (2) the achievable repeatability needs to be quantified in millimetres, not asserted. "Robot built" is not automatically "precision built" — it's precision built only if the cell is closing the loop against the actual part in front of it.

## Stage 4 — roll-formed roof trusses, "lowered into place"
FrameCAD-style roll-forming of cold-formed steel truss members is real, mature technology — that part is credible. "Lowered into place" is the phrase doing the most unexamined work in the whole process description. Lowering a roof truss assembly onto a wall frame and achieving structural fixing (fastening, welding, or mechanical connection) with load-bearing accuracy is a materially harder robotics problem than roll-forming a linear member — it involves a large, non-rigid assembly, multi-point alignment, and likely fastening at multiple simultaneous points. This is plausible with a gantry/crane-assisted robotic or semi-robotic system, but it should be treated as **unproven and likely hybrid** (robot/crane-assisted placement, human-verified or human-completed fixing) until a pilot proves otherwise, not assumed as a lights-out robotic stage.

## Stage 5 — zinc/woodgrain cladding
This is the stage the brand's signature aesthetic lives or dies on. Features like "hidden gutters" and "vertical shadow gaps" are not forgiving design details — they only look intentional at tight, consistent reveal widths; loose or inconsistent reveals read as a workmanship defect, not a design language. That means cladding placement needs registration accuracy against the wall-framing output from Stage 3, which itself is only as accurate as its own tolerance stack against the Stage 1 chassis. This is a **tolerance stack-up problem across three stages**, not a single-stage precision problem, and it's the single most technically demanding claim embedded in the "30 New Ideas" feature list. It deserves a physical pilot before it's treated as solved (see [[Open Questions & Next Validation Steps]]).

## Stage 6 — standing-seam roof
Roll-forming and seaming straight roof pans is automatable. Real standing-seam roofing work that isn't automatable without significant custom tooling: valleys, penetrations (solar mounting hardware, the disaster-relief pod's comms mast, vents), edge/parapet flashing, and weatherproofing details. Realistically this is a **robot-plus-human hybrid stage**, with humans doing penetration flashing and final weatherproofing sign-off — both of which are exactly the details that cause leaks if done badly, so this isn't a corner worth cutting for the sake of the automation narrative.

## Stage 7 — interiors, MEP, finishes
This is overwhelmingly human labor with today's named technology stack. ABB arms and FrameCAD roll-forming are structural/framing tools — they have no obvious role in wiring terminations, plumbing connections, cabinetry installation, fixture mounting, or finish carpentry. Interior fit-out at this level of finish (the premium positioning the brand is selling) is skilled trade work. This stage should be modeled as **fully human** until there's a specific, named technology for factory-line MEP automation, which doesn't currently exist in the concept.

## Stage 8 — QC & delivery
Digital-twin monitoring can meaningfully log sensor data, robot process parameters, and inspection checkpoints — that's a legitimate use of the technology and supports the "Inspection Passed" plaque claim. But final sign-off on a habitable, life-safety-adjacent structure (especially the disaster-relief pod) is a liability-bearing decision. A human inspector accountable for that sign-off is not a nice-to-have, it's a legal and ethical necessity. This stage is **human by design, not by current limitation** — it should stay that way even if automation elsewhere improves.

## Honest read on "Zero Human Input"
Across the eight stages, the stages with a credible near-term path to low/no direct human touch are 1–2 (chassis/floor, largely conventional fabrication) and parts of 3–4 (framing and truss placement, with caveats above). Stages 5–6 are realistically hybrid. Stages 7–8 are human by necessity, not just by current technology limits — one because of finish-trade skill, the other because of accountability.

"Zero Human Input" is defensible as a description of the *structural framing* portion of the line. It is not defensible as a description of the manufacturing process end to end, and it should never be used in a way that implies unit labor cost trends toward zero — see [[Cost-to-Build Reality Check]] for why that matters for the capex/opex math, and [[Reality Check Summary]] for why this is flagged as a go/no-go item.

## Related
- [[Reality Check Summary]]
- [[Compliance Feasibility]] — several of the compliance tension points (AS/NZS 4600 cold-formed steel, wind loading) are directly downstream of whether Stage 3–4 actually deliver the structural precision and connection integrity they need to.
- [[Cost-to-Build Reality Check]]
- [[Open Questions & Next Validation Steps]]
