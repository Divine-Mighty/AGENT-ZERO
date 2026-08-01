---
tags: [new-eden, government, tco, budget, illustrative, ne-dr-401]
aliases: [TCO Model, Total Cost of Ownership]
---

# Total Cost of Ownership Model

← [[Government Home]]

> **This is an illustrative framework, not a costed proposal.** No real acquisition price, maintenance cost, or incumbent-option cost data has been sourced for this model. It exists to show the *shape* of the total-cost-of-ownership question an agency should ask, and the variables that a real quote-based model would need to fill in. Every dollar figure an agency uses in an actual budget submission should come from a formal quote, not from this document.

## Why lifespan changes the acquisition conversation

Standard emergency-stock budgeting tends to treat field infrastructure as a **consumable**: bought relatively cheaply, expected to have a short service life or single-deployment lifespan, and replaced or written off on a short cycle. The NE-DR-401's stated 25+ year design life reframes it instead as a **capital infrastructure asset**, which is a different budget category with a different cost logic — closer to how an agency budgets for a vehicle fleet or a building than how it budgets for consumable relief supplies.

The illustrative comparison below shows why that reframing matters financially, without asserting real numbers.

## The illustrative model structure

A defensible TCO comparison would need to model, for each option, at minimum:

| Cost variable | What it captures |
|---|---|
| **Acquisition cost per unit** | Purchase or lease-establishment cost |
| **Service life** | Years before replacement or major refurbishment is needed |
| **Deployment cycles supported** | How many separate emergency deployments a unit can realistically be used for over its life |
| **Storage/depot cost per unit per year** | Land, footprint, and depot overhead — directly affected by stackability, see [[Procurement & Fleet Model]] |
| **Transport/mobilisation cost per deployment** | Cost to move the unit from depot to incident area and back |
| **Maintenance and inspection cost per year** | Ongoing compliance and upkeep cost, see [[Compliance for Emergency Life-Safety Use]] |
| **Reconditioning cost per deployment cycle** | Cost to return a unit to ready-reserve status after use, particularly for Medical configuration hygiene reconditioning |
| **Residual/disposal value at end of life** | What, if anything, the asset is worth at retirement |

## Illustrative shape of the comparison, not sourced figures

Using the categories from [[Comparison vs Incumbent Options]], the qualitative shape of a TCO curve typically looks like this — again, **directional only**:

- **Canvas tents and low-cost temporary options** tend to have a low acquisition cost per unit but a short service life and low or zero reusability across multiple deployment cycles, meaning the effective annualised cost is driven almost entirely by replacement frequency rather than acquisition price. A tent bought cheaply but replaced or discarded after one or two uses may have a higher effective cost-per-deployment-year than its sticker price suggests.
- **Converted containers, caravans, and demountables** sit in a middle band: higher acquisition cost and moderate service life, with maintenance and reconditioning cost that can be unpredictable if the unit was not engineered for repeated field redeployment.
- **A purpose-engineered, 25+ year design-life unit** carries a higher upfront acquisition cost, but amortises that cost over a much longer service life and, if it genuinely supports many deployment cycles without major rebuild, a lower cost per deployment-year over the full ownership period — provided maintenance and reconditioning costs stay in line with expectations.

The crossover point — the deployment frequency and time horizon at which the higher-upfront-cost, long-life option becomes cheaper per year than the lower-upfront-cost, short-life option — is the single most important number in this entire model, and it **cannot be stated without real acquisition and maintenance quotes for both sides of the comparison.** This document deliberately does not estimate it.

## How to complete this model for a real procurement decision

1. Obtain a formal quote from New Eden for acquisition cost per unit, by role configuration, at the fleet size under consideration (volume pricing is a reasonable question to ask about, given the [[Procurement & Fleet Model]] reserve-fleet framing).
2. Obtain the agency's own historical cost data for its current incumbent options — replacement frequency, storage cost, transport cost, and reconditioning cost for whatever mix of tents, containers, caravans, or demountables it currently fields.
3. Model depot storage cost per unit using actual regional land/depot costs, applying the stackability factor from [[Procurement & Fleet Model]] to the NE-DR-401 side of the comparison.
4. Model a realistic deployment-frequency assumption per region (how many events per year is a unit likely to be called on for, on average, over a multi-decade horizon) — this assumption drives the crossover point above and should be stress-tested against both a low-frequency and high-frequency scenario.
5. Include a maintenance and compliance-inspection cost line item informed by the digital-twin tracking model in [[Procurement & Fleet Model]] and the standards obligations in [[Compliance for Emergency Life-Safety Use]].
6. Decide the appropriate discount rate and budget horizon per the agency's own capital-budgeting policy — a 25+ year asset life is long enough that the choice of discount rate materially affects the comparison, and should follow whatever methodology the agency's finance function already uses for other long-life capital assets (vehicles, buildings).

## What this note is not

It is not a cost justification for procuring the NE-DR-401, and should not be cited as one. It is a checklist for building that justification once real quotes and agency cost data are available, structured around the same operational facts covered in [[Deployment Value Proposition]], [[Comparison vs Incumbent Options]], and [[Procurement & Fleet Model]].
