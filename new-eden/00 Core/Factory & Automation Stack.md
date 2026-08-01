---
tags: [manufacturing, automation, robotics, digital-twin, new-eden]
---

# Factory & Automation Stack

The factory floor render shows four concrete technology elements: **FrameCAD roll-forming machines**, **ABB industrial robotic arms** assembling steel roof trusses, **steel coil raw-material racks**, and **finished module shells staged for transport**. The factory building itself is branded "New Eden — Building Tomorrow" in black cladding with gold vertical accent striping (matching the brand mark — see [[Brand & Positioning]]), with multiple loading dock doors for the transport-ready modules produced in [[Manufacturing Process]] stage 8. This note reverse-engineers a plausible automation architecture from those elements and gives an honest assessment of the "Zero Human Input" marketing claim.

## The real technology components, and what they actually are
- **FrameCAD** is a real light-gauge steel (LGS) roll-forming brand/system: structural steel coil is fed through a roll-former that profiles it into C-studs, tracks, and truss chords to a CAD-driven cutting/punching pattern, producing the wall studs, floor joists, and roof truss chords used across [[Manufacturing Process]] stages 2–4. FrameCAD-class systems are commercially available today and are a credible basis for New Eden's framing output — this is the one part of the "AI Powered Production" banner with a strong real-world precedent, since these machines already run from digital building models with minimal manual intervention.
- **ABB robotics** refers to ABB's industrial articulated-arm robot lines (commonly used in automotive and heavy-fabrication robotic welding/assembly cells). In New Eden's context, these are the plausible actors behind: wall-frame erection/fastening (Stage 3), truss placement (Stage 4), and cladding panel pick-and-place using the magnetic alignment system (Stage 5, see [[Product Line - Residential]] feature 22). ABB arms are well suited to repetitive, high-precision fastening and placement tasks with a fixed part geometry — which is exactly what a standardized 40ft Hi-Cube chassis (see [[Dimensions & ISO Compatibility]]) provides.
- **Steel coil racks** confirm the factory is vertically integrated from raw coil rather than buying pre-cut framing components — consistent with the "Raw Steel to Finished Home" framing of the process banner.
- **Digital Twin Monitoring**: given every module carries a serialized QR/ID tag resolving to a per-unit record (see [[Product Line - Residential]] feature 16, and the factory signature wall, feature 25), the plausible architecture is a Manufacturing Execution System (MES) that assigns a digital twin record to each chassis at Stage 1 and appends data at every subsequent stage — robot placement logs, QC gate results (per [[Manufacturing Process]]), material batch/coil traceability, and final RGB factory test results (feature 17) — so that by Stage 8 the "digital twin" is a complete as-built + as-tested record tied to the physical serial number, usable later for warranty service (robotic service dock, feature 14) and, for the [[Product Line - Disaster Relief Pod]], for emergency-services maintenance assurance.

## Inferred architecture layers
1. **Design/configuration layer** — the customer or dealer configuration (residential feature selections, or disaster-relief role configuration) generates a per-unit digital model (the same model referenced throughout [[Product Line - Residential]] and [[Product Line - Disaster Relief Pod]]).
2. **CAM/roll-forming layer** — that model drives the FrameCAD-class roll-formers' cut/punch patterns directly, eliminating a manual drafting-to-shop-floor handoff for framing members.
3. **Robotic execution layer** — ABB robotic cells at Stages 3–5 execute placement and fastening against the same digital model, using the robot lift points (feature 23) and standardized chassis geometry as consistent reference datums.
4. **MES/digital twin layer** — every stage's actual (not just planned) data — QC results, serials, coil batch numbers, robot cycle logs — is written back to the module's twin record, closing the loop between "what was designed" and "what was actually built," which is what lets the Stage 8 QA gate certify "Inspection Passed" with real supporting data rather than a spot check.
5. **Service/lifecycle layer** — post-delivery, the digital twin record is queried via the QR code and physically accessed via the robotic service dock (feature 14) and magnetic service wall (feature 15), closing the loop from factory into decades of field service.

## Honest assessment of "Zero Human Input"
Marketing banners compress a real, defensible automation story into a slogan. Some parts of that slogan hold up; others do not, and this vault should not let downstream (especially investor and government) materials overstate the claim.

**Plausibly near-zero human input:**
- Roll-forming of structural members (FrameCAD-class systems already run largely unattended from digital models).
- Robotic wall-frame and truss placement/fastening on a fixed, standardized chassis geometry (ABB-class robotic cells are proven for this kind of repetitive fixed-geometry assembly).
- Robotic cladding placement using the magnetic self-locating panel system, which was very likely designed specifically to be robot-friendly (see [[Product Line - Residential]] feature 22).
- Automated electrical/lighting circuit testing (RGB factory testing, feature 17) via machine-vision pass/fail verification.
- MES/digital twin data capture itself, which is inherently software-automated once instrumented.

**Almost certainly still requires human input, and downstream vaults should say so plainly:**
- **Final integration and finishing** — trades work like plumbing/electrical connection to fixtures, sealant and flashing detailing at penetrations, and interior joinery/finish carpentry ([[Manufacturing Process]] Stage 7) involve variable, fine-motor tasks (routing flexible conduit/pipe around obstructions, caulking, punch-list touch-ups) that remain outside the reliable range of current fixed-cell industrial robotics without a much more expensive dexterous-robotics investment than an ABB arm on a rail.
- **Quality assurance and sign-off** (Stage 8) — an "Inspection Passed" claim tied to a named factory and traceable serial number is, for both brand-trust and likely regulatory reasons, far more credible with a human inspector's accountability behind it than a fully automated pass/fail, particularly for the [[Product Line - Disaster Relief Pod]] where the plaque's credibility underwrites a life-safety product.
- **Line changeovers, maintenance, and exception handling** — any robotic cell needs human technicians for calibration, tooling changeover between configuration variants, and handling out-of-tolerance parts that the automated QC gates in [[Manufacturing Process]] flag but cannot themselves fix.
- **Materials handling edge cases** — coil loading into the FrameCAD-class line and staging finished shells for transport (visible in the render) plausibly involve forklift/overhead crane operators, even if the robot lift points (feature 23) are designed for maximum handling automation.

**Recommended framing for other vaults**: describe the line as "robotics-led" or "highly automated" rather than literally "zero human input" in any document making a claim that could be checked against an actual factory tour, audit, or regulatory inspection (this matters most for the government/disaster-relief vault, where a false "no human quality control" claim would be a serious liability on a life-safety product).

## Cross-references
- Stage-by-stage equipment mapping: [[Manufacturing Process]]
- Chassis geometry that standardizes every robotic cell's reference datum: [[Dimensions & ISO Compatibility]]
- Features whose feasibility depends directly on this automation stack: [[Product Line - Residential]] (features 16, 17, 22, 23, 25, 26)
- Proposed (unbuilt) closed-loop metrology/registration architecture that feeds the digital twin layer above and directly addresses the Stage 1→3→5 tolerance stack-up: [[Tolerance Management Architecture (R&D)]]
