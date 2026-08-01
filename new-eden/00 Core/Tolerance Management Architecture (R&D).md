---
tags: [manufacturing, process, engineering, r&d, new-eden]
---

# Tolerance Management Architecture (R&D)

*Status: proposed engineering architecture for R&D evaluation only — not built, tested, or validated. This note exists to answer the question [[Engineering Feasibility]] leaves open: cladding placement (Stage 5 of [[Manufacturing Process]]) needs registration accuracy against the wall-framing output (Stage 3), which is itself only as accurate as its tolerance stack against the Stage 1 welded-steel ISO chassis — a **tolerance stack-up problem across three stages**, flagged there as "the single most technically demanding claim" in the whole concept and something that "deserves a physical pilot before it's treated as solved." This note is a proposed pre-pilot engineering hypothesis, drafted through a structured propose → critique → revise process (an initial proposal, an adversarial technical review, and a revision addressing every review point below), not a settled design. All mm and cost figures are illustrative engineering estimates for budgeting discussion, not measured New Eden data, vendor quotes, or sourced industry citations unless stated otherwise.*

## The core idea
Don't let Stage 3 and Stage 5 execute open-loop against nominal CAD. Instead, each stage measures the *actual* output of the stage before it and re-registers its robot program to that as-built geometry — converting a naive three-stage error stack into a chain of correction residuals, rather than passing raw chassis variance straight through to the visible cladding reveal.

## 1. Two distinct error terms, and what closed-loop correction can and can't fix
- **Scan/instrument noise** — the metrology system's own measurement repeatability (structured-light/laser-line scanners, typ. ~0.1–0.3mm at close range for this equipment class). Small, and *not* the dominant error term.
- **Unregistered shape/warp residual** — a 12.2m welded chassis is not rigid the way a stamped or machined automotive part is; welding introduces bow, twist, and local pull that a **rigid best-fit registration** (6-DOF translate/rotate, the standard automotive body-in-white technique) cannot remove, because rigid registration only corrects whole-part pose error, not continuous curvature. This is the term that actually dominates the Stage 3 residual below.

**Registration algorithm assumption (stated explicitly):** the budget below assumes a *dense* as-built survey (roughly one point every 200–300mm along the chassis rails, not just the 8 corner-casting points) combined with a **piecewise/local rigid registration** — each wall-bay's robot path is registered against the nearest local survey points rather than a single global 6-DOF fit for the full 12.2m length. This meaningfully reduces, but does not eliminate, warp residual, because each local segment still assumes local rigidity. A full **deformable/spline surface registration** would close more of the gap but is itself unproven software/engineering work for this application — an open risk, not an assumed win.

## 2. Tolerance budget — one consistent stacking methodology
**Stacking rule used throughout:** independent random error sources are combined by root-sum-square (RSS) — applied consistently at every step, rather than mixing an optimistic near-cancellation assumption at one step with a pessimistic linear sum at another.

| Stage | Error term | Illustrative magnitude | Correctable by rigid registration? |
|---|---|---|---|
| 1 — ISO chassis fab | Rigid-body offset/rotation (position within jig, overall squareness) | Majority of ±3–5mm raw fabrication variance (illustrative) | Yes — becomes ~scan-noise-level after registration |
| 1 — ISO chassis fab | Non-rigid warp/bow/twist (weld-pull) | ±1.0–1.5mm over a wall-bay span (illustrative, unsourced) | **No** — persists through rigid registration |
| 3 — Wall-frame placement | Scan noise | ±0.1–0.3mm | n/a (already at the floor) |
| 3 — Wall-frame placement | **Residual (RSS of warp + scan noise; warp dominates)** | **≈ ±1.0–1.5mm** | — |
| 5 — Cladding placement | Local warp of Stage-3 output over a panel-width span (smaller span than full chassis) | ±0.4–0.8mm (illustrative) | No — same limitation, smaller magnitude |
| 5 — Cladding placement | Scan noise + magnetic-pin mechanical self-centering | ±0.1–0.3mm scan, ~±0.2–0.3mm mechanical snap | n/a |
| 5 — Cladding placement | **Residual (RSS of above)** | **≈ ±0.5–1.0mm** | — |
| **End-to-end (reveal-facing), RSS(Stage 3, Stage 5)** | | **≈ ±1.1–1.8mm nominal (no fallback engaged)** | |
| Mechanical fallback (slotted/shimmed batten fixings) | Physical safety net, not part of the "working as intended" figure | up to ±2–3mm available travel | separate band — see §5 |

## 3. Benchmark against reveal tolerance — an honest, not-yet-closed gap
An illustrative (unsourced, order-of-magnitude estimate) premium architectural reveal tolerance is roughly ±1–1.5mm. Our nominal expected residual of ±1.1–1.8mm **overlaps but extends above** that band. **This architecture does not demonstrate that the reveal will read as intentional** — at best it narrows the gap from an uncorrected multi-stage stack (which would be several times larger) to a band that is *close to but not confidently inside* a plausible premium-reveal tolerance. Closing the remaining gap requires either reducing Stage 1 warp at the source (tighter welding fixturing/jigging, stress-relief sequencing — a fabrication-process question, not a metrology one) or upgrading to deformable/spline registration at Stage 3/5. Both are open engineering work, not assumed wins. See [[Manufacturing Process]] Stage 5 for why loose or inconsistent reveals read as a workmanship defect rather than a design language.

## 4. Correction mechanism
1. **Stage 1 → digital twin:** dense as-built survey (laser tracker or portable CMM arm) written to the unit's digital twin record — see [[Factory & Automation Stack]].
2. **Stage 3:** the wall-framing robot registers to that as-built data via local/piecewise rigid registration (§1), not nominal CAD.
3. **Stage 3 → Stage 5 handoff:** a second dense scan of the actual batten/stud surface after framing becomes the Stage 5 reference.
4. **Physical fallback:** slotted/shimmed batten fixings plus the magnetic self-locating cladding pins (see [[Product Line - Residential]] feature 22) absorb residual beyond what vision correction closes — but fallback engagement is a *logged exception*, not a silent absorption (§6).

## 5. Illustrative capex and cycle-time (explicitly flagged placeholder)
No New Eden line takt time is documented anywhere in this vault; the figure below is invented solely for this budgeting exercise and should not be treated as a production commitment.

| Item | Illustrative capex (order of magnitude, not a vendor quote) | Illustrative cycle time | Against placeholder takt time (assumed 45–60 min/module, invented for this exercise only) |
|---|---|---|---|
| Stage 1 laser tracker/CMM dense survey | ~US$50k–150k instrument-class cost | ~20–40 min/unit (dense survey, not a sparse 8-point check) | Consumes a large fraction of takt — flagged as a possible line-rate bottleneck |
| Stage 3 robot-mounted structured-light scan | ~US$20k–60k/scan head | ~2–5 min/pass | Comfortably within takt |
| Stage 5 robot-mounted structured-light scan | ~US$20k–60k/scan head | ~2–5 min/pass | Comfortably within takt |
| Digital-twin registration software/integration (NRE) | ~US$100k–300k+, one-time | n/a | Per [[Cost-to-Build Reality Check]]'s existing warning, this integration/software line is likely to exceed the cost of the robot arms themselves, not the scanners |

**Total illustrative capex order:** roughly US$300k–700k+ across the three metrology systems and integration — dominated by the software/registration NRE, not hardware. Stage 1's dense-survey cycle time is the most likely throughput risk and would need a faster capture method (e.g., a fixed multi-station photogrammetry rig instead of a single roving tracker) evaluated in a pilot.

## 6. Failure mode and disposition path — reconciled with the existing Stage 1 gate
This proposal **does not replace** [[Manufacturing Process]]'s Stage 1 hard-stop QC gate. That gate remains the non-negotiable check on **structural** tolerance (ISO 1161 corner-casting position, squareness, stacking/lifting rating) — a chassis failing it does not proceed, full stop, regardless of anything below.

This proposal adds a **second, narrower band**: a chassis can pass the structural gate and still carry enough residual warp to threaten *cosmetic reveal consistency* specifically. That requires new QC gates and an explicit disposition path:
- **New QC checkpoint at Stage 3 output and Stage 5 output:** measured residual (post-correction) compared against the reveal-tolerance band from §3.
- **Within band:** proceeds normally.
- **Outside band but within mechanical fallback travel (±2–3mm shim range):** proceeds, but the fallback engagement is logged to the digital twin as an exception, not hidden inside a "pass."
- **Outside band and beyond fallback travel:** unit is held for human disposition — options are hand-rework/re-shim at Stage 5 (consistent with [[Factory & Automation Stack]]'s existing assessment that fine-tolerance visible cladding work is a likely manual-assist point), downgrade to a lower cosmetic-grade finish tier (a business decision, not an engineering one), or — only if the same warp also threatens the structural tolerance band — escalation back to the Stage 1 hard-stop criteria.
- **Adjudication:** a named Stage 5 QC technician/inspector role with defined sign-off authority, not an automated accept/reject decision — consistent with this vault's existing position ([[Engineering Feasibility]], Stage 8) that human accountability belongs at final quality decisions on a life-safety-adjacent structure.

## 7. Precedent: technique vs. numbers, explicitly separated
- **Technique-precedented:** "measure the as-built part, register the robot path to it rather than nominal CAD" is proven practice in automotive body-in-white and aerospace assembly.
- **Numbers NOT precedented:** those industries work with dimensionally stable stamped/machined parts, not a 12.2m field-welded steel weldment — their achieved mm figures do not transfer to this application.
- **Randek/British Offsite (closest real precedent identified, from [[docs/AutovolImplementationPlan.pdf]]):** validates robotic light-gauge-steel wall-panel assembly automation as a Stage 3 technique analog. It says nothing about achieving sub-2mm cladding-reveal tolerance at a Stage 5 equivalent — no precedent, real or claimed, supports that specific number for this application.

## Review history
1. **Initial proposal** — closed-loop scan-and-register architecture with a tolerance budget, but attributed the Stage 3 residual to scan/registration error alone (5–10x too small to explain the claimed residual) and mixed stacking methodologies between steps.
2. **Adversarial review** — flagged the math inconsistency (unregistered warp/shape error, not scan noise, is the real dominant term), an unsupported "looks intentional" claim against no stated reveal benchmark, a missing capex/cycle-time model despite [[Cost-to-Build Reality Check]] already warning that metrology integration is typically pricier than the robot arms themselves, precedent overreach (technique-precedented ≠ numbers-precedented), and a silently-implied change to the Stage 1 hard-stop QC philosophy with no reject/rework path. Verdict: approve the core strategy, with required changes.
3. **This revision** — addresses all five points: separates warp residual from scan noise and states the registration algorithm assumption, applies RSS stacking consistently, softens the reveal claim to an honest "narrows but does not close" gap, adds an explicitly-flagged illustrative capex/cycle-time table, re-scopes precedent claims, and adds a disposition path that sits alongside (not instead of) the existing Stage 1 gate.

## Related
- [[Manufacturing Process]] — Stage 3 (wall framing) and Stage 5 (exterior cladding), the two stages this architecture directly governs.
- [[Factory & Automation Stack]] — the MES/digital twin layer this architecture's survey data feeds into, and the existing "almost certainly still requires human input" read on fine-tolerance cladding work.
- [[Engineering Feasibility]] — the validation-vault note that originally flagged this as the single most technically demanding claim in the concept.
- [[Cost-to-Build Reality Check]] — the existing capex-category warning this note's illustrative metrology/software line items are consistent with.
- [[Open Questions & Next Validation Steps]] — item 2, the physical pilot this architecture should be tested against before being treated as solved.
