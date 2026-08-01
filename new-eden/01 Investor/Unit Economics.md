---
tags: [investor-vault, economics, illustrative-model, new-eden]
---

# Unit Economics

> [!warning] Worked illustrative example, not a costed BOM
> No real supplier quotes, no signed equipment pricing, and no labor-market data went into this note. Every dollar figure below is a **worked illustrative example** — internally consistent with the rest of this vault, chosen to show the *shape* of the model, and not sourced from any real quote. Replace every figure with a real number as quotes land, in the order listed under [[#What needs to happen before this note is investment-grade]].

## Purpose

Before real supplier quotes exist, the useful thing to build is the *shape* of the per-module cost stack: what categories exist, how robotics amortization actually gets allocated per unit (a question a lot of modular-housing pitches get wrong), and where the premium-materials line sits relative to a standard steel-frame prefab cost base. This note is that shape, with illustrative numbers plugged in so the arithmetic is checkable — not because any of them are real.

---

## Per-module cost stack (illustrative structure)

Applies to a single 40ft Hi-Cube ISO module (external 12,192 x 2,438 x 2,896mm), before role-specific fitout (residential finish tier or disaster-relief role configuration).

| Cost category | What it covers | Illustrative example (AUD) | Status |
|---|---|---|---|
| **1. Raw steel & chassis materials** | ISO 1161 corner castings, structural steel for the 40ft Hi-Cube chassis and internal exposed truss | $18,000 | Needs steel-supplier quote at volume |
| **2. Floor cassette materials & assembly** | Floor cassette stage of the 8-stage line | $6,500 | Needs supplier + line-time quote |
| **3. Robotics-line time (ABB wall framing)** | Machine-hour allocation of ABB robotic arms for wall framing | $4,500 | See amortization note below — this is the line item most pitches get wrong |
| **4. Roll-formed roof trusses (FrameCAD)** | FrameCAD roll-forming line time + material | $5,500 | Needs FrameCAD line throughput data |
| **5. Cladding & finish premium** | Zinc Monument / Colorbond Woodland Grey (woodgrain) / Copper Natural (New/Weathered/Verdigris) / Colorbond Night Sky | $22,000 (blended — see tier range below) | Copper almost certainly the highest-variance line — needs its own sensitivity table once sourced |
| **6. Standing-seam roof** | Roofing stage of the 8-stage line | $9,000 | |
| **7. Interiors & MEP** | Mechanical/electrical/plumbing, hidden A/C, smart ceiling, interior finish | $48,000 | Likely the largest single labor-driven line — needs trade-labor costing |
| **8. QC & delivery, digital-twin tagging** | Inspection, QR/digital-twin tag issuance ("Module 000384, Factory 01"), transport to site or deployment point | $7,000 | Digital-twin tagging cost itself is likely near-zero marginal; transport cost is the real variable here and depends on distance from Factory 01 |
| **9. Direct labor (non-robotic stages)** | Human labor across stages not automated (interiors/MEP, QC, finishing touches) | $16,000 | "Zero Human Input" is a production-line automation claim for the robotic stages, not a claim that zero labor exists across the whole 8-stage process — model labor honestly here |
| **10. Factory overhead allocation** | Facility, utilities, non-production staff, allocated per unit at assumed production volume | $12,000 | Sensitive to Factory 01 utilization rate — see [[Scaling Plan]] |
| **Subtotal: Cost to produce** | Sum of 1–10 | **$148,500** | |
| **11. Target margin** | Premium-positioning margin target (see [[The Thesis]]), modeled as 35% cost-plus | $52,000 | This is the number that has to beat standard steel-frame prefab and site-built margins to validate the premium thesis |
| **Illustrative selling price** | Subtotal + margin | **≈$200,500** | Feeds [[Market Opportunity (Illustrative Model)]] ASP assumptions |

Cladding tier range behind row 5's blended figure: **≈$16,000** at the base Zinc Monument / Colorbond tier, up to **≈$31,000** for a full Copper Natural specification with a Weathered or Verdigris ageing treatment. $22,000 is a rough midpoint, not a sales-mix-weighted average — that mix doesn't exist yet.

> ⚠️ Illustrative assumption, internally consistent within this vault — not a sourced quote. Validate with real data before use in an actual pitch.

---

## Robotics amortization — the line item to get right

The single most common mistake in a modular-housing cost model is treating robotics capex as a sunk cost that disappears after purchase, rather than amortizing it correctly per unit. A defensible model needs, at minimum:

- **Equipment capex**: ABB wall-framing/truss-assembly cell ≈ **$2,200,000**, plus a FrameCAD roll-forming line ≈ **$1,300,000**, fully installed and commissioned at Factory 01 — **≈$3,500,000 combined**. Illustrative figure; requires real equipment vendor quotes.
- **Useful life / depreciation schedule**: **10 years**, straight-line. Illustrative.
- **Assumed annual throughput at full nameplate utilization**: **350 units/year**. Illustrative.
- **Assumed realistic utilization rate** (not nameplate capacity — actual expected uptime accounting for maintenance, changeovers, ramp period): **70%** blended (illustratively, ~65% during a Year 1–2 ramp rising to ~85% at steady state — see [[Scaling Plan]]).
- **Resulting $/unit robotics amortization** = (capex ÷ useful life) ÷ (throughput × utilization) = (capex ÷ 10) ÷ (350 × 0.70) = capex ÷ 2,450 units.
  - ABB cell: $2,200,000 ÷ 2,450 ≈ **$898/unit** in pure capital amortization.
  - FrameCAD line: $1,300,000 ÷ 2,450 ≈ **$531/unit** in pure capital amortization.
  - Combined capital amortization ≈ **$1,429/unit** — the remainder of line items 3 and 4 above (≈$8,571/unit combined) is machine operating cost, consumables (steel coil, tooling wear), power, and robotic-cell supervision labor, not capital charge. Collapsing those into "robotics amortization" is exactly the kind of blending this note exists to avoid.

This calculation is the load-bearing number for the whole premium-margin thesis in [[The Thesis]] — it should not be left as a rough guess once real vendor numbers are available. Robotics reliability/uptime risk (see [[Risks & Mitigations]]) directly attacks the 70% utilization assumption in this formula: every point of utilization lost raises the $/unit amortization figure.

---

## Residential vs. disaster-relief cost delta

The two products share the base chassis and most of the 8-stage line, but diverge at fitout:

| | Residential ("30 New Ideas") | Disaster Relief Pod (NE-DR-401) |
|---|---|---|
| Base chassis (stages 1–4, 6) | Shared | Shared |
| Cladding/finish tier | Premium finish options (copper ageing, woodgrain) — see category 5 above, ≈$22,000 blended | Durability/cost-optimized tier, not the premium residential palette — illustratively ≈**$14,000/unit** |
| Interiors/MEP | Residential fitout (kitchen, bath, smart ceiling, hidden A/C) ≈$48,000 | Role-specific fitout, illustratively: Medical ≈$62,000 (medical equipment integration, highest) · Command ≈$50,000 (comms/IT fitout) · Accommodation ≈$40,000 (bunks, basic fitout) · Support ≈$35,000 (storage/logistics, lowest fitout complexity) |
| Additional systems | N/A | Rooftop solar array + comms mast/antenna hardware — illustratively **+$9,000/unit** base, with Command configs likely carrying extra comms equipment above that |
| Target buyer / pricing logic | Consumer premium pricing | Government tender pricing — likely benchmarked against incumbent options (site-built temporary facilities, caravan/demountable rentals) rather than against residential ASP |

Rough illustrative relief-pod cost stack (swap cladding + interiors/MEP + additional systems into the shared-chassis subtotal from the table above): base chassis + shared stages (items 1–4, 6, 8–10 from the main stack, excluding the residential-specific cladding/interiors lines) ≈$78,500, plus role-specific fitout (≈$35,000–$62,000) and solar/comms (≈$9,000), lands in a **≈$122,500–$149,500/unit** illustrative cost range depending on role — before the margin applied in tender pricing.

> ⚠️ Illustrative assumption, internally consistent within this vault — not a sourced quote. Validate with real data before use in an actual pitch.

---

## What needs to happen before this note is investment-grade

1. Signed or quoted pricing for ABB robotics and FrameCAD roll-forming equipment at the Factory 01 scale.
2. Steel and cladding material quotes at production volume (not one-off/retail pricing).
3. A real labor-cost model for the non-robotic stages (interiors/MEP, QC), sourced from Australian trade-labor rates.
4. A validated utilization-rate assumption for the robotics line, ideally from a pilot run rather than a nameplate-capacity assumption.
5. Separate cost models per residential finish tier and per disaster-relief role configuration, rather than one blended number.

## Related notes
[[The Thesis]] · [[Market Opportunity (Illustrative Model)]] · [[Moat & Defensibility]] · [[Scaling Plan]] · [[Risks & Mitigations]] · [[The Ask]] · [[Investor Home]]
