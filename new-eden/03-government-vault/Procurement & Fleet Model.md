---
tags: [new-eden, government, procurement, fleet, logistics, ne-dr-401]
aliases: [Fleet Model, Procurement Model]
---

# Procurement & Fleet Model

← [[Home]]

This note outlines how an emergency-management agency might structure acquisition, depot storage, and fleet maintenance for a reserve of NE-DR-401 units. It describes an operating model, not a costed proposal — see [[Total Cost of Ownership Model]] for the illustrative budget framework.

## Standing reserve fleet at regional depots

The premise behind holding a reserve fleet rather than procuring on-demand is straightforward for an emergency-response asset: disasters do not wait for a supply chain to respond, and a unit that deploys in under 30 minutes only delivers that speed if it is already positioned within reach of likely incident areas (see [[Deployment Value Proposition]]).

A regional depot model — units held in state or regional emergency-services depots, pre-positioned ahead of known-risk seasons (cyclone season in the north, bushfire season in the south-east, flood-prone river catchments) — is the natural fit. This mirrors how agencies already stage other emergency equipment (vehicles, pumps, generators) at regional bases rather than centrally.

## ISO stackability as a depot-planning input

Because the chassis stacks three-high using the same ISO corner-casting load path as standard container stacking, depot footprint for a given reserve size drops roughly threefold versus single-layer storage. This is directly relevant to two procurement questions:

1. **How large a reserve can we justify given depot land constraints?** A compact footprint makes it more realistic to hold a fleet sized for a genuine worst-case event rather than a token number of units.
2. **Can we co-locate the reserve with existing depot infrastructure** (vehicle bays, generator storage, existing container-handling equipment) rather than requiring a purpose-built site? The ISO-standard handling requirements mean existing container-handling equipment at ports, rail yards, or logistics depots is usable without a bespoke handling fleet.

## Rapid mobilisation logistics

The road/rail/sea compatibility described in [[Deployment Value Proposition]] gives an agency more than one path to move units from depot to incident area:

- **Pre-positioning by rail or road** ahead of a forecast event (e.g. moving units toward a cyclone-warning region days ahead of landfall), using standard intermodal freight capacity rather than a dedicated emergency-transport contract.
- **Last-leg road movement** from a regional depot to the actual staging area, using standard container trucks.
- **Sea transport** for island communities or remote coastal regions not efficiently reached by road, using existing port handling infrastructure.

A fleet plan should specify, per region, which combination of these paths is the primary mobilisation route and what the realistic time-to-stage is for each — a logistics planning exercise outside the scope of this vault but directly enabled by the chassis's intermodal compatibility.

## Fleet maintenance and compliance tracking via the digital twin

Every unit is factory-tagged with a QR digital-twin ID as part of the standard 8-stage build process (see [[Home]]), showing "Inspection Passed" status at time of manufacture. For a distributed reserve fleet, this is the mechanism that turns a one-time factory compliance check into an ongoing fleet-management capability:

- **Per-unit inspection history.** Each unit's digital twin can carry its inspection record forward — factory QC, delivery inspection, and subsequent periodic inspections while in depot storage or after a deployment cycle — rather than relying on paper records held separately from the physical asset.
- **Compliance status at a glance across a distributed fleet.** An agency operating units across multiple regional depots can use the QR/digital-twin system to verify, unit by unit, that each is current on the inspection and compliance requirements described in [[Compliance for Emergency Life-Safety Use]] — particularly relevant for the electrical and gas service-port connections that undergo repeated field connect/disconnect cycles.
- **Post-deployment reconditioning tracking.** After a unit is used in the field (particularly in the Medical configuration, where post-use hygiene reconditioning is a return-to-depot requirement), the digital twin provides a record of what reconditioning or inspection was completed before the unit re-enters ready-reserve status.
- **Asset lifecycle planning.** Over the unit's 25+ year design life, the digital-twin record supports the maintenance and eventual refresh/retirement scheduling that feeds the total cost of ownership picture in [[Total Cost of Ownership Model]].

## A mixed-fleet consideration

Realistically, a reserve fleet is likely to combine a core of NE-DR-401 units with surge capacity from lower-cost, faster-to-source incumbent options (tents, hired demountables) for the tail of a large event that exceeds the standing reserve. The comparison in [[Comparison vs Incumbent Options]] is relevant to sizing that mix: NE-DR-401 units are the higher-capability, higher-reusability core (particularly for Medical and Command roles where standards compliance and comms infrastructure matter most), with incumbent options as the flexible surge layer for lower-criticality Accommodation or Support overflow.

## Open questions for a procurement conversation

- What reserve fleet size, per region, corresponds to a defensible worst-case planning scenario?
- What is the target time-to-stage from depot to incident area for each region's primary mobilisation route?
- What role-configuration mix (Medical / Command / Accommodation / Support) should the standing reserve hold, and does that ratio change seasonally?
- What contractual model — outright purchase, standing lease, or a hybrid reserve-plus-surge-lease arrangement — best matches the agency's capital and operating budget structure? See [[Total Cost of Ownership Model]] for the framework to evaluate this against.
