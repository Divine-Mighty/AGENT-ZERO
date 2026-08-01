---
tags: [validation, open-questions, next-steps, new-eden]
---

# Open Questions & Next Validation Steps

This is the punch list. Nothing in the other four notes in this vault gets resolved by more thinking — it gets resolved by going and checking. Each item below is ordered roughly by how cheap it is to do relative to how much uncertainty it removes. Do the cheap, high-signal ones first.

## 1. Get real robotics-cell quotes — not list prices
Approach two or three industrial automation integrators (not just ABB or FrameCAD themselves) for a scoped quote: robotic wall-framing cell with vision-guided correction for as-built chassis variance, integrated with a roll-forming line, sized for the target throughput. Ask specifically for installed/integrated cost, not equipment list price — integration is usually the larger number. This single step turns [[Cost-to-Build Reality Check]] from a category list into an actual capex figure.

## 2. Build one physical pilot module (or at minimum a full-scale cladding/reveal mockup)
Before trusting the "30 New Ideas" aesthetic at production scale, build a real section — ideally a full module, at minimum a full-scale wall/roofline mockup — through the actual proposed fabrication sequence (real chassis, real robotic or robot-simulated framing, real cladding installation) and physically measure the achievable tolerance on the shadow-gap reveals and hidden-gutter detail. This is the direct test of the [[Engineering Feasibility]] tolerance stack-up concern, and it's the cheapest way to find out whether the signature aesthetic actually survives contact with real fabrication before committing to a factory line built around it.

## 3. Commission an AS 3959-experienced engineer or bushfire consultant to review the design specifically
Bring the actual envelope details — hidden gutters, shadow-gap reveals, the glass garage door, corner glazing, the woodgrain cladding spec — to someone who does BAL assessments professionally, and ask directly: at what BAL categories do these details fail as drawn, and what's the minimum redesign to pass at BAL-40/Flame Zone (the level the disaster-relief line likely needs). This resolves the single biggest compliance risk flagged in [[Compliance Feasibility]] before it becomes a factory-floor rework.

## 4. Get real freight, logistics, and stacking quotes
Confirm with an actual heavy-haul/freight and crane-lift provider that a *habitable, fitted-out* 40ft Hi-Cube module — not an empty steel box — can actually be stacked three-high and transported by road/rail/sea within the ISO 1161 corner-casting rating, at the tare and gross weights the finished product will actually have. Also get a real quote for the disaster-relief pod's transport/deployment logistics specifically, since the <30-minute deployment claim depends on it. This tests whether the "road/rail/sea compatible, stackable 3-high" claim in the core vault's chassis spec holds for the real, built product rather than the empty chassis.

## 5. Talk to one actual emergency-services procurement contact
Find a real contact in SES, ambulance service logistics/fleet, or a state emergency management authority and ask directly: what does their real procurement process for rapid-deployment infrastructure look like, what deployment-time do they actually measure (truck arrival vs. fully operational and connected), what would make them trust a private manufacturer's disaster-relief claims, and what's a realistic order size and cadence. This is the cheapest possible test of whether the entire disaster-relief line's demand assumption is real, and it should happen before any of the more expensive validation steps above.

## 6. Get a structural engineer's read on the AS/NZS 4600 certification burden
Ask a cold-formed-steel structural engineer how many genuinely distinct structural configurations the current product concept implies (residential variants × expandable-module connections × disaster-relief role configs × BAL zone variants) and what a realistic certification cost and timeline looks like per configuration. This turns the "certification multiplies" concern in [[Compliance Feasibility]] and [[Cost-to-Build Reality Check]] into an actual number.

## 7. Build a bottom-up labor estimate for Stages 7–8
Independent of the robotics narrative, cost out interior fit-out, MEP terminations, and QC/inspection labor per unit as if the structural stages were fully automated — because they might be. This directly tests the [[Reality Check Summary]] item that "Zero Human Input" must not be load-bearing in the cost model, and it's a desk exercise, not a field trip — it should happen early and cheaply.

## 8. Scope the digital-twin/QR platform as a software product, not a plaque
Get a real estimate (even an internal engineering estimate) for building and *operating* — for decades, given the 25+ year lifespan claim — a per-unit digital-twin data platform: data capture, storage, a public-facing QR lookup, and ongoing hosting. Decide explicitly whether this is needed for a minimum viable first factory run or can be deferred past pilot scale.

## 9. Get an accessibility consultant's read on the Medical/Accommodation pod configurations
Ask directly whether a compliant accessible layout (circulation, turning space, accessible fixture clearances) fits inside the fixed 2,352mm internal width for those two role configurations, or whether they need a widened or expandable variant. This is a specific, checkable dimensional question, not a design judgment call, and it's answerable without building anything.

## 10. Model break-even unit volume against real capex, once items 1 and 6 have real numbers
Once the robotics-cell quote (item 1) and certification cost estimate (item 6) produce real figures, build the one financial model that actually matters: total factory capex against a realistic 3–5 year unit-volume ramp, informed by whatever demand signal comes out of item 5. If break-even volume is implausible given zero market validation to date, that's the finding that should slow everything else down, regardless of how well the engineering and compliance questions resolve.

## Sequencing note
Items 3, 5, and 7 are desk/consultation exercises and should happen first — they're cheap and each one can independently kill or reshape the concept. Item 2 (physical pilot) is the most expensive item on this list and should only happen after the compliance review (item 3) has already reshaped the envelope details it would otherwise test, so the pilot isn't built against a design that's about to change.

## Related
- [[Reality Check Summary]]
- [[Engineering Feasibility]]
- [[Compliance Feasibility]]
- [[Cost-to-Build Reality Check]]
