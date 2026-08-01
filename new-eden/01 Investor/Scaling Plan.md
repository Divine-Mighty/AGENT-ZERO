---
tags: [investor-vault, scaling, new-eden]
---

# Scaling Plan

> [!note] One line
> Factory 01 isn't just a name — it's a serial number, and the plan is to make Factory 02, 03, ... a repeatable playbook rather than a bespoke rebuild each time.

## Why "Factory 01" is a scaling asset, not just a label

New Eden already bakes per-unit factory-and-line provenance into the product identity — every module's digital-twin tag records which factory built it ("Module 000384, **Factory 01**, Scan for Digital Twin"). This isn't cosmetic. It means the brand, the QC/traceability system, and the customer-facing digital-twin product are all designed from day one to scale across *multiple* factories with each one identifiable in the data, rather than needing to be retrofitted for multi-site operation later. Factory 02 slots into the existing tagging and tracking scheme without a redesign.

---

## Phase 1 — Prove Factory 01

Before any replication conversation is credible, Factory 01 needs to demonstrate:

- The 8-stage line (ISO chassis → floor cassette → ABB-robot wall framing → roll-formed roof trusses → cladding → standing-seam roof → interiors/MEP → QC & delivery) running at a **validated, repeatable throughput and quality level** — not a one-off demo unit.
- A real utilization/uptime track record for the ABB robotics and FrameCAD roll-forming stages, feeding back into the amortization assumptions in [[Unit Economics]].
- At least initial traction in **both** channels — residential sales and/or a disaster-relief pilot deployment or first agency relationship — so Phase 2 isn't scaling a single-channel bet. See [[Market Opportunity (Illustrative Model)]].
- A stable NCC/AS-NZS certification position for the residential product (see [[Risks & Mitigations]] on certification timeline risk) — replicating a factory before the product itself is certified compounds risk rather than reducing it.

**Phase 1 exit criteria (illustrative targets — update Status as milestones are actually hit):**

| Criterion | Illustrative target | Status |
|---|---|---|
| Units produced at Factory 01 | ≥150 cumulative units | Not yet started |
| Validated robotics-line uptime % | ≥80%, sustained over a full production quarter | Not yet started |
| Residential units sold | ≥80 units | Not yet started |
| Disaster-relief pods deployed/contracted | ≥6 pods (pilot + first agency relationship) | Not yet started |
| Certification status | Full NCC/AS-NZS certification for the residential product, plus at least one relief-pod role configuration | Not yet started |

> ⚠️ Illustrative assumption, internally consistent within this vault — not sourced data. Validate with real data before use in an actual pitch.

---

## Phase 2 — Codify the playbook

The goal of this phase is to convert "how we built Factory 01" from institutional knowledge into a transferable playbook, specifically:

- **Equipment specification package**: a standardized bill of equipment (ABB robotic arm models/counts, FrameCAD line configuration, supporting fixtures) that a new factory build can order against directly, rather than re-deriving from scratch.
- **Line-layout and commissioning documentation**: the sequencing and calibration process that got Factory 01's 8 stages running at target throughput, written up as a repeatable commissioning runbook.
- **Digital-twin/QR infrastructure as shared, multi-factory software**: the tagging and tracking system needs to be architected (if it isn't already) so "Factory 02" is just a new value in the same schema — this should be close to zero incremental engineering if done correctly at Factory 01, given the brand already treats factory identity as a first-class data field.
- **Quality/QC standard**: the QC step that produces "Inspection Passed" needs to be codified as a portable standard, not tribal knowledge held by Factory 01's specific QC team.

## Phase 3 — Factory 02 and site selection logic

Site selection for a second factory should weigh, at minimum:

- **Freight/logistics position**: given the ISO-compatibility advantage (see [[Moat & Defensibility]]), Factory 02's location should be chosen to extend road/rail/sea reach into currently underserved regions, not simply duplicate Factory 01's catchment.
- **Channel balance**: consider whether Factory 02 is positioned to serve a specific concentration of disaster-relief demand (e.g., a region with distinct disaster-risk profile from Factory 01's catchment) alongside residential — reinforcing the dual-channel logic rather than just adding capacity to one channel.
- **Labor market for the non-automated stages**: interiors/MEP and QC remain labor-driven per [[Unit Economics]] — site selection needs real regional labor-market input, not just a robotics/logistics lens.
- **Capex funding**: Factory 02's build-out is a direct line item in [[The Ask]] — this plan and that fundraising ask should stay in sync as real numbers develop.

**Phase 3 exit criteria (illustrative targets — update Status as milestones are actually hit):**

| Criterion | Illustrative target | Status |
|---|---|---|
| Factory 02 site selected | Site secured under option or LOI, meeting the logistics/channel-balance/labor criteria above | Not yet started |
| Factory 02 capex committed | Full Factory 02 build capex funded, sized from real Factory 01 cost data (not the illustrative figures in [[Unit Economics]]) | Not yet started |
| Factory 02 commissioning timeline | ≤18 months from site selection to first unit off the line | Not yet started |

> ⚠️ Illustrative assumption, internally consistent within this vault — not sourced data. Validate with real data before use in an actual pitch.

## Phase 4 — Steady-state multi-factory operation

At this stage the model shifts from "prove and replicate" to "operate a network":

- Centralized digital-twin/data platform aggregating all factories' units over their full lifecycle — this is where the moat described in [[Moat & Defensibility]] compounds fastest, since data volume and history depth both scale with factory count and time in service.
- Cross-factory capacity allocation between the residential and disaster-relief channels, informed by the demand model in [[Market Opportunity (Illustrative Model)]] once it's backed by real data.
- A feedback loop where field performance data from the digital twin informs design iteration on the "30 New Ideas" catalog and NE-DR-401 role configurations over time.

## Sequencing discipline

The core scaling risk is replicating capex before Factory 01's throughput, quality, and dual-channel demand are actually proven — this would compound the capex risk flagged in [[Risks & Mitigations]] rather than reduce it. Phase gates above exist specifically to prevent that.

## Related notes
[[The Thesis]] · [[Market Opportunity (Illustrative Model)]] · [[Unit Economics]] · [[Moat & Defensibility]] · [[Risks & Mitigations]] · [[The Ask]] · [[Investor Home]]
