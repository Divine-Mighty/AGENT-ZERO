---
tags: [manufacturing, process, robotics, new-eden]
---

# Manufacturing Process — "From Raw Steel to Finished Home"

Marketing banner: **"AI Powered Production | ABB Robotics | Digital Twin Monitoring | Zero Human Input."** Both [[Product Line - Residential]] and [[Product Line - Disaster Relief Pod]] are built down the same eight-stage line, diverging only in fit-out selections applied at Stage 7. See [[Factory & Automation Stack]] for the underlying automation architecture and an honest assessment of the "Zero Human Input" claim, and [[Dimensions & ISO Compatibility]] for the chassis geometry referenced throughout.

## Stage 1 — ISO Chassis
**What happens**: the 40ft Hi-Cube base frame is assembled with 8x ISO 1161 corner castings, matching real-world ISO 668 40HC container geometry (12,192 x 2,438 x 2,896mm external — see [[Dimensions & ISO Compatibility]]).
**Equipment/cell**: heavy steel fabrication — CNC plasma/laser cutting of chassis rail steel, a robotic or semi-automated welding cell for the main longitudinal/cross rails, and precision jigging to position the 8 corner castings within the tight dimensional tolerance ISO handling equipment (spreaders, twist-locks, crane slings) requires.
**QC gate**: dimensional survey of the completed chassis against ISO 668 tolerances and corner-casting position/squareness check before the frame is allowed to proceed — a chassis that is out of tolerance here compromises every downstream stacking, transport, and lifting claim for the unit's entire service life, so this is the least negotiable gate on the line.

## Stage 2 — Floor Cassette
**What happens**: a roll-formed floor structure is installed onto the chassis.
**Equipment/cell**: a FrameCAD-class roll-forming line feeds structural steel coil through a roll-former to produce floor joists/bearers to the module's exact 12,032 x 2,352mm internal span, which a robotic or semi-automated placement arm lays and fixes onto the chassis rails; flooring substrate (structural sheet flooring) is then fixed over the joists.
**QC gate**: joist spacing/fixing verification and a load-deflection or at minimum a visual/dimensional floor-flatness check, since floor-to-ceiling glazing units and continuous window bands installed later ([[Product Line - Residential]] features 9, 11) are intolerant of floor deflection or unevenness telegraphing into wall-frame alignment.

## Stage 3 — Wall Framing
**What happens**: wall frames are erected "by ABB robots."
**Equipment/cell**: roll-formed steel wall studs (again FrameCAD-class output) are picked, positioned, and fastened (screwed/riveted) by ABB articulated-arm robots working from the module's digital model, forming door/window rough openings — including the continuous structural lintel needed for the continuous window band and glass garage door features.
**QC gate**: robotic vision-guided dimensional check of every rough opening against the digital twin model before cladding/glazing crews (or the equivalent robotic cells) are scheduled, since an out-of-tolerance opening cascades into every glazing feature downstream.

## Stage 4 — Roof Trusses
**What happens**: roll-formed roof trusses are lowered into place.
**Equipment/cell**: trusses are roll-formed off the same FrameCAD-class line, then set using an overhead gantry or robotic lift (tied to the "robot lift points" designed into the chassis — see [[Product Line - Residential]] feature 23) rather than manual crew lifting, given truss spans approaching the 2,352mm internal width plus any cantilever needed for the floating-roof detail (feature 1).
**QC gate**: truss alignment and fixing torque/fastener verification, plus — where the living-roof option (feature 19) or solar roof skin (feature 13) has been selected upstream in the order configuration — a load-path check confirming the truss spec matches the selected roof option's dead load.

## Stage 5 — Exterior Cladding
**What happens**: zinc and woodgrain panels are installed.
**Equipment/cell**: the magnetic cladding system (feature 22) is designed specifically to be robot-friendly — panels are picked and placed onto the batten sub-frame by a robotic arm using the magnetic alignment pins for self-locating placement, then the mechanical retaining clip is engaged (potentially robotically, or as one of the more likely manual-assist points on the line given the fine tolerance of visible shadow-gap reveals — see [[Factory & Automation Stack]]).
**QC gate**: reveal/shadow-gap width consistency check (feature 3) and a finish/colour-match inspection across the Zinc Monument, Woodland Grey, and Night Sky palette (see [[Materials & Finishes]]) before the roof stage seals the envelope.

## Stage 6 — Roof & Flashings
**What happens**: a standing-seam roof is installed.
**Equipment/cell**: standing-seam roof sheet is roll-formed and seamed (often via a mobile roll-seaming machine that runs the panel profile and folds the standing seam in one pass), flashings and the concealed box gutter/rainhead system (features 4, 5) are fitted, and where specified, BIPV solar roof skin (feature 13) is integrated at this stage rather than retrofitted.
**QC gate**: watertightness testing — a realistic implementation is a flood/spray test on the completed roof plane and gutter system before the module moves to interior fit-out, since any leak found after Stage 7's interior linings go in is vastly more expensive to trace and repair.

## Stage 7 — Interiors & Services
**What happens**: interior modules, MEP (mechanical/electrical/plumbing), and finishes are installed.
**Equipment/cell**: this is the most labour-and-trade-dense stage regardless of automation elsewhere on the line — the smart ceiling cassette (feature 26) is installed as a pre-built unit, plumbing manifolds and electrical switchboards are connected to the pre-run chassis-level service risers, magnetic service wall panels (feature 15) are fitted over the wet-wall chase, and — for the [[Product Line - Disaster Relief Pod]] — the role-specific fit-out (Medical/Command/Accommodation/Support) is installed here as a configuration decision made before the module enters this stage.
**QC gate**: full services commissioning — pressure-test plumbing, continuity/insulation-resistance test electrical circuits, and run the RGB factory testing sequence (feature 17) across every lighting/electrical zone before the module is sealed up for delivery.

## Stage 8 — Quality & Delivery
**What happens**: final inspection, testing, and transport-ready sign-off.
**Equipment/cell**: a dedicated QA bay where the module undergoes final dimensional, weatherproofing, and services verification against its digital twin record, the factory ID plate/QR code (feature 16) and factory signature wall plaque (feature 25) are fitted only once the module clears every prior gate, and the unit is prepared for road/rail/sea transport (tie-down points, protective transit coverings over glazing and exterior finishes).
**QC gate**: this stage *is* the final QC gate — final inspection sign-off is what the "Inspection Passed" wording on the signature plaque certifies, and it is the point at which the module's full digital twin record (every prior stage's QC data) is closed out and linked to the serial number for the module's entire subsequent service life (see [[Product Line - Disaster Relief Pod]] on why this matters for emergency-services trust).

## Cross-reference
See [[Factory & Automation Stack]] for the equipment/software architecture that ties these eight stages together (ABB robotics, FrameCAD roll-forming, MES/digital twin), and for a direct discussion of which stages above are plausibly "zero human input" and which almost certainly are not.
