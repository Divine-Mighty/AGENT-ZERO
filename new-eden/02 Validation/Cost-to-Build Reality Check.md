---
tags: [validation, cost, capex, new-eden]
---

# Cost-to-Build Reality Check

No supplier quotes, no competitor benchmarking, no real financial modeling has been done for this concept. Nothing in this note is a sourced figure — it is a list of the real capex and opex categories that a "robot-built" factory model creates, named honestly so they don't get glossed over between now and a business plan. The point isn't to guess numbers; it's to make sure the *categories* are on the table before capital gets committed.

## The capex categories, named honestly

### 1. Robotics cell (ABB arms + FrameCAD roll-forming line)
This is not "buy a robot." An ABB robotic wall-framing cell that hits the tolerance New Eden's design needs (see [[Engineering Feasibility]]) requires custom end-of-arm tooling, vision/metrology integration to correct for as-built chassis variance, safety cell infrastructure, and systems integration engineering — that integration work is typically a larger cost than the robot arms themselves. The FrameCAD-style roll-forming line is a separate, specialized capital purchase with its own coil-steel supply chain requirements. Treat this as a custom industrial integration project, not an equipment purchase off a catalog.

### 2. Purpose-built factory shell ("Factory 01")
The brand's own marketing commits to a purpose-built plant, not a leased shed — "Factory 01" branding implies a dedicated facility with the power supply robotics need, high-bay clearance for crane-assisted truss placement and stacking work, and road/rail access sized for 40ft ISO modules in and out. This is a real property and construction capex line in its own right, separate from the equipment inside it.

### 3. Digital-twin / QR infrastructure
The per-unit QR/digital-twin tag ("Module 000384, Factory 01, Scan for Digital Twin", "Inspection Passed") implies a real backend: a data pipeline capturing factory process and inspection data per unit, storage, a lookup/serving layer for the QR scan, and a system that stays live and correct for the lifetime of every unit sold — potentially decades, given the 25+ year lifespan claim on the disaster-relief line. **This is a software product with an ongoing operating cost, not a one-time capex line** — hosting, maintenance, and support don't stop after the factory opens. Budgeting it as a build-once cost is a modeling error worth catching early.

### 4. Certification and testing costs
As detailed in [[Compliance Feasibility]], certification is not a single line item — it likely multiplies across residential variants, material/finish combinations, BAL (bushfire) zone variants, and disaster-relief role configurations, each of which may need its own structural (AS/NZS 4600), wind-loading (AS/NZS 1170.2), and bushfire (AS 3959) engineering sign-off, plus an NCC alternative-solution pathway assessment where no deemed-to-satisfy route exists. This is a cost that scales with the breadth of "30 New Ideas" and the four-role disaster-relief configuration set, not a fixed number.

### 5. Working capital and inventory
Steel coil, cladding stock (four material finishes plus copper ageing variants), MEP components, and glazing held as inventory across two demand cycles (discretionary residential vs. counter-cyclical emergency-services demand) is a real, ongoing working-capital draw, distinct from the one-time capex above.

### 6. Specialist labor and facility overhead
Robotics maintenance technicians and FrameCAD line operators are a narrower, likely more expensive labor pool than general construction trades, and Stage 7–8 interior/QC labor (see [[Engineering Feasibility]]) still needs skilled trades at premium-finish quality regardless of how automated the structural stages are. The "Zero Human Input" banner should not be allowed to imply this line trends toward zero.

## Why this matters more than it would for a normal modular builder
A low-automation modular competitor can start with a leased shed, off-the-shelf tools, and hired tradespeople — low fixed capex, high variable cost, break-even at low volume. New Eden's model is the inverse: **high fixed capex (robotics cell, purpose-built factory, software platform, per-configuration certification) amortized against unit volume.** That's a legitimate strategy — it's the same logic that makes automotive manufacturing work — but it only pays off if unit volume is high enough, soon enough, to amortize the fixed cost before the business needs that capital for something else.

This means the single most important number in the entire financial case for New Eden is **units sold per year in the first 3–5 years, weighed against total factory capex** — and right now that number doesn't exist, because no market validation has been done (see [[Open Questions & Next Validation Steps]]). Every other number in this note is secondary to getting that one right, because a factory sized for volume that doesn't materialize is the single most common way capital-intensive manufacturing startups fail.

## What "exceeds the standard" costs
The founder's directive to treat AS/NZS/NCC compliance as a floor, not a target — especially for the life-safety disaster-relief line — is the right call ethically and probably right commercially (see the brand's premium positioning). It should also be modeled explicitly as a cost multiplier on certification and materials, not assumed to be free. "Exceeds code" is a real, recurring line item, not a slogan.

## Related
- [[Reality Check Summary]]
- [[Engineering Feasibility]]
- [[Compliance Feasibility]]
- [[Open Questions & Next Validation Steps]]
