---
tags: [investor-vault, economics, illustrative-model, new-eden]
---

# Unit Economics

> [!warning] Fillable model, not a costed BOM
> No real supplier quotes, no signed equipment pricing, and no labor-market data went into this note. Every dollar figure is a **placeholder to be replaced** once quotes exist for steel, roll-forming/robotics equipment, cladding materials, and Factory 01 labor. Treat this as the *structure* of the cost stack — the categories and how they roll up — not the numbers themselves.

## Purpose

Before real supplier quotes exist, the useful thing to build is the *shape* of the per-module cost stack: what categories exist, how robotics amortization actually gets allocated per unit (a question a lot of modular-housing pitches get wrong), and where the premium-materials line sits relative to a standard steel-frame prefab cost base. This note is that shape. Fill in `[INSERT]` fields once quotes land.

---

## Per-module cost stack (illustrative structure)

Applies to a single 40ft Hi-Cube ISO module (external 12,192 x 2,438 x 2,896mm), before role-specific fitout (residential finish tier or disaster-relief role configuration).

| Cost category | What it covers | Illustrative placeholder | Status |
|---|---|---|---|
| **1. Raw steel & chassis materials** | ISO 1161 corner castings, structural steel for the 40ft Hi-Cube chassis and internal exposed truss | `[INSERT $/unit]` | Needs steel-supplier quote at volume |
| **2. Floor cassette materials & assembly** | Floor cassette stage of the 8-stage line | `[INSERT $/unit]` | Needs supplier + line-time quote |
| **3. Robotics-line time (ABB wall framing)** | Machine-hour allocation of ABB robotic arms for wall framing | `[INSERT $/unit]` | See amortization note below — this is the line item most pitches get wrong |
| **4. Roll-formed roof trusses (FrameCAD)** | FrameCAD roll-forming line time + material | `[INSERT $/unit]` | Needs FrameCAD line throughput data |
| **5. Cladding & finish premium** | Zinc Monument / Colorbond Woodland Grey (woodgrain) / Copper Natural (New/Weathered/Verdigris) / Colorbond Night Sky | `[INSERT $/unit, varies by finish tier]` | Copper almost certainly the highest-variance line — needs its own sensitivity table once sourced |
| **6. Standing-seam roof** | Roofing stage of the 8-stage line | `[INSERT $/unit]` | |
| **7. Interiors & MEP** | Mechanical/electrical/plumbing, hidden A/C, smart ceiling, interior finish | `[INSERT $/unit]` | Likely the largest single labor-driven line — needs trade-labor costing |
| **8. QC & delivery, digital-twin tagging** | Inspection, QR/digital-twin tag issuance ("Module 000384, Factory 01"), transport to site or deployment point | `[INSERT $/unit]` | Digital-twin tagging cost itself is likely near-zero marginal; transport cost is the real variable here and depends on distance from Factory 01 |
| **9. Direct labor (non-robotic stages)** | Human labor across stages not automated (interiors/MEP, QC, finishing touches) | `[INSERT $/unit]` | "Zero Human Input" is a production-line automation claim for the robotic stages, not a claim that zero labor exists across the whole 8-stage process — model labor honestly here |
| **10. Factory overhead allocation** | Facility, utilities, non-production staff, allocated per unit at assumed production volume | `[INSERT $/unit]` | Sensitive to Factory 01 utilization rate — see [[Scaling Plan]] |
| **Subtotal: Cost to produce** | Sum of 1–10 | `[INSERT $/unit]` | |
| **11. Target margin** | Premium-positioning margin target (see [[The Thesis]]) | `[INSERT % or $/unit]` | This is the number that has to beat standard steel-frame prefab and site-built margins to validate the premium thesis |
| **Illustrative selling price** | Subtotal + margin | `[INSERT $/unit]` | Feeds [[Market Opportunity (Illustrative Model)]] ASP assumptions |

> ⚠️ Illustrative assumption — validate with real data before use in an actual pitch.

---

## Robotics amortization — the line item to get right

The single most common mistake in a modular-housing cost model is treating robotics capex as a sunk cost that disappears after purchase, rather than amortizing it correctly per unit. A defensible model needs, at minimum:

- **Equipment capex**: ABB robotic arm(s) for wall framing + FrameCAD roll-forming line(s), fully installed and commissioned at Factory 01. `[INSERT — requires equipment vendor quotes]`
- **Useful life / depreciation schedule**: years of productive life assumed for the robotics line. `[INSERT]`
- **Assumed annual throughput at full utilization**: units/year the line can produce running at target uptime. `[INSERT]`
- **Assumed realistic utilization rate** (not nameplate capacity — actual expected uptime accounting for maintenance, changeovers, ramp period): `[INSERT %]`
- **Resulting $/unit robotics amortization** = (capex ÷ useful life) ÷ (throughput × utilization).

This calculation is the load-bearing number for the whole premium-margin thesis in [[The Thesis]] — it should not be left as a rough guess once real vendor numbers are available. Robotics reliability/uptime risk (see [[Risks & Mitigations]]) directly attacks the utilization assumption in this formula.

---

## Residential vs. disaster-relief cost delta

The two products share the base chassis and most of the 8-stage line, but diverge at fitout:

| | Residential ("30 New Ideas") | Disaster Relief Pod (NE-DR-401) |
|---|---|---|
| Base chassis (stages 1–4, 6) | Shared | Shared |
| Cladding/finish tier | Premium finish options (copper ageing, woodgrain) — see category 5 above | Likely a durability/cost-optimized finish tier, not the premium residential palette — `[INSERT — confirm actual spec]` |
| Interiors/MEP | Residential fitout (kitchen, bath, smart ceiling, hidden A/C) | Role-specific fitout (Medical / Command / Accommodation / Support) — each role likely has a distinct cost profile, `[INSERT per role]` |
| Additional systems | N/A | Rooftop solar, comms mast — additive cost line, `[INSERT]` |
| Target buyer / pricing logic | Consumer premium pricing | Government tender pricing — likely benchmarked against incumbent options (site-built temporary facilities, caravan/demountable rentals) rather than against residential ASP |

> ⚠️ Illustrative assumption — validate with real data before use in an actual pitch.

---

## What needs to happen before this note is investment-grade

1. Signed or quoted pricing for ABB robotics and FrameCAD roll-forming equipment at the Factory 01 scale.
2. Steel and cladding material quotes at production volume (not one-off/retail pricing).
3. A real labor-cost model for the non-robotic stages (interiors/MEP, QC), sourced from Australian trade-labor rates.
4. A validated utilization-rate assumption for the robotics line, ideally from a pilot run rather than a nameplate-capacity assumption.
5. Separate cost models per residential finish tier and per disaster-relief role configuration, rather than one blended number.

## Related notes
[[The Thesis]] · [[Market Opportunity (Illustrative Model)]] · [[Moat & Defensibility]] · [[Scaling Plan]] · [[Risks & Mitigations]] · [[The Ask]] · [[Home]]
