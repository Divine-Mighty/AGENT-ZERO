---
tags: [validation, reality-check, new-eden, go-no-go]
---

# Reality Check Summary

This is a go/no-go checklist, not a pitch. Every line below is a claim that is currently *assumed* somewhere in the New Eden concept — in the "30 New Ideas" feature list, the 8-stage manufacturing banner, the NE-DR-401 spec sheet, or the "exceeds NCC/AS-NZS" directive — and that has not been tested against physical, regulatory, or financial reality. Each one is written so it can fail. If more than two or three of these fail outright, the concept needs a redesign before it needs a factory.

Detail and reasoning for each item lives in [[Engineering Feasibility]], [[Compliance Feasibility]], [[Cost-to-Build Reality Check]], and [[Open Questions & Next Validation Steps]].

## Manufacturing precision
- [ ] **Robotic wall-framing tolerance must be tight and repeatable enough** — on the order of low single-digit millimetres, held consistently across every unit — for the cladding reveals and vertical shadow gaps to read as a deliberate design language at production scale, not as visibly inconsistent gaps that make the product look like a defective container. See [[Engineering Feasibility]].
- [ ] **The ISO chassis itself must not be the tolerance bottleneck.** A welded steel shipping-container-class chassis is not machined to furniture tolerances. If the chassis geometry varies unit to unit more than the cladding system can absorb, every downstream "precision" claim breaks regardless of how good the robots are. See [[Engineering Feasibility]].
- [ ] **"Roof trusses lowered into place" and "standing-seam roof installed" must be genuinely robot-executable stages at the claimed cycle time** — or the 8-stage line's throughput and capex-per-unit assumptions are wrong from day one. See [[Engineering Feasibility]].
- [ ] **"Zero Human Input" must not be load-bearing in the cost model.** Final MEP terminations, interior fit-out, and QA sign-off are almost certainly human-executed for the foreseeable future. If the unit-economics spreadsheet anywhere assumes near-zero labor cost per unit, it is wrong. See [[Engineering Feasibility]] and [[Cost-to-Build Reality Check]].

## Compliance
- [ ] **AS 3959 bushfire-construction compliance must be achievable without abandoning the core aesthetic** — hidden gutters, vertical shadow gaps, exposed glazing (including the glass garage door) — especially since the disaster-relief line is explicitly meant to operate in and near bushfire-affected parts of Australia. If it can't, the flagship design language needs a bushfire-zone variant, which fragments "One Vision" into at least two products. See [[Compliance Feasibility]].
- [ ] **Wind-loading performance (the AS/NZS 1170.2 family) must be provable for a lightweight, relocatable, stackable steel module**, including the disaster-relief pod deployed on an exposed, possibly damaged site — without engineering markup so heavy it erodes the tare-weight and rapid-deployment claims. See [[Compliance Feasibility]].
- [ ] **A compliant accessible configuration must fit inside the fixed 2,352mm internal width** for the Medical and Accommodation relief-pod roles. If accessibility clearances (circulation, turning space, fixture zones) don't fit, either the pod needs a widened/expandable variant for those roles or the "Medical/Command/Accommodation/Support" reconfiguration claim overstates what's actually deployable. See [[Compliance Feasibility]].
- [ ] **There must be a credible NCC approval pathway for a stacked, relocatable, ISO-chassis habitable structure.** The NCC does not have an obvious off-the-shelf category for this; it likely means a case-by-case performance/alternative-solution pathway per configuration, which is slower and more expensive than a standard deemed-to-satisfy build. See [[Compliance Feasibility]].

## Economics
- [ ] **Factory capex (robotics cell, FrameCAD line, purpose-built shell, digital-twin software build) must be recoverable within a realistic unit volume at realistic early-year sales**, not at an optimistic ramp. If break-even volume is implausible for years 1–3, the automation bet doesn't pay for itself before the business needs the cash for something else. See [[Cost-to-Build Reality Check]].
- [ ] **The digital-twin/QR infrastructure must be budgeted as an ongoing operating cost (hosting, data pipeline, per-unit lifecycle records), not a one-time build line.** It's software with a long tail, not a plaque. See [[Cost-to-Build Reality Check]].
- [ ] **Certification cost must be modeled per distinct configuration, not once.** Residential variants × material finishes × BAL (bushfire attack level) zones × disaster-relief role configs could multiply into a large number of engineering sign-offs before a single unit is legally sellable in every claimed market. See [[Compliance Feasibility]] and [[Cost-to-Build Reality Check]].

## Operational / mission claims
- [ ] **The disaster-relief pod's <30-minute deployment claim must hold with a realistic emergency-services crew** (not factory robotics technicians) at an actual field site, including hookup through the exterior plug-and-play service ports — not just an idealized factory-yard demonstration. See [[Compliance Feasibility]] and [[Open Questions & Next Validation Steps]].
- [ ] **The 25+ year lifespan claim must hold for a unit that is transported, stacked, unstacked, and relocated**, not just for a static-site building — repeated handling and transport is a fatigue and seal-integrity question that ordinary building lifespan assumptions don't cover. See [[Engineering Feasibility]].

## How to read this
Every unchecked box above is an open risk, not a confirmed failure — none of these have been tested yet. The purpose of this list is to make sure none of them get quietly assumed true on the way to a factory build-out. See [[Open Questions & Next Validation Steps]] for the concrete next step attached to each one.
