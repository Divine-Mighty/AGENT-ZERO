---
tags: [investor-vault, market, illustrative-model, new-eden]
---

# Market Opportunity (Illustrative Model)

> [!warning] This entire note is an unvalidated model
> No competitor names, no sourced market-size figures, and no cited industry reports were used to build New Eden's market case — that was a deliberate choice, not an oversight. Every number below is a **worked illustrative example**, chosen to show the *shape* of the model and make its arithmetic checkable — not a sourced or defensible figure. Nothing here should appear in an actual pitch deck or financial projection without being replaced by real data.

## Purpose of this note

New Eden sells into two structurally different markets off one chassis. This note builds a *framework* for sizing each — the variables that matter, how they interact, and where the real research needs to go — rather than asserting a number. Treat every figure as a slider to be moved once real data exists.

---

## Channel 1 — Residential ("30 New Ideas")

### The demand thesis
Australia has a well-known, persistent housing supply constraint (undersupply relative to population growth, elevated site-built construction costs and timelines, skilled-trade labor shortages in traditional construction). Modular/prefab construction is a category-level response to that constraint because it moves labor off a variable, weather-exposed, trade-dependent site into a controlled, robotic factory environment. New Eden's specific bet within that category is that a meaningful slice of demand exists not just for "cheaper/faster than site-built" but for a **premium, design-led, robotically-precise** modular product — i.e., modular construction sold on quality and identity, not just speed and cost.

### Model structure (worked illustrative example — replace every input)

| Variable | Illustrative example | Notes |
|---|---|---|
| Addressable annual new-dwelling starts (Australia) | ≈170,000 dwellings/yr | Round illustrative figure in the general range of recent Australian annual dwelling completions — not sourced from ABS building-approvals data here. Replace with a real, cited figure before use. |
| % of starts realistically addressable by modular/prefab (site access, planning, transport radius from Factory 01) | 8% | Illustrative. |
| % of that modular-addressable pool willing to pay a premium-brand price point | 10% | This is the real question the brand has to answer — see [[The Thesis]] point 1. Illustrative. |
| Resulting illustrative serviceable unit volume / year | 170,000 × 8% × 10% ≈ **1,360 units/yr** | Purely mechanical output of the placeholder inputs above — do not treat as a forecast. |
| Illustrative average selling price per module (residential) | ≈$200,500 | Carried from [[Unit Economics]]. |
| Illustrative annual residential revenue (mechanical output) | 1,360 × $200,500 ≈ **$273M/yr** | Not a forecast — see the capacity check immediately below. |

**Capacity check, not a demand validation**: [[Unit Economics]]'s robotics-amortization section puts Factory 01's realistic output at ≈245 units/year. The illustrative demand figure above (1,360 units/yr) is roughly **5.5× Factory 01's single-line capacity** — which means even directionally-plausible demand assumptions imply New Eden hits a *supply* ceiling long before a *demand* ceiling. That's the actual argument for [[Scaling Plan]]'s Factory 02+ playbook — not evidence that the demand number is right, just evidence that supply is very unlikely to be the binding constraint if the shape of this model is even roughly correct.

> ⚠️ Illustrative assumption, internally consistent within this vault — not sourced data. Validate with real data before use in an actual pitch.

### Demand drivers worth tracking (qualitative, not sized here)
- Australian housing undersupply and approval/construction timelines vs. site-built alternatives.
- Regional/remote and difficult-site demand, where ISO-compatible transport (road/rail/sea) is a genuine differentiator over site-built.
- Consumer willingness-to-pay for the "30 New Ideas" design language and finish options (copper ageing, woodgrain, exposed structural truss as a feature) versus standard steel-frame prefab or site-built equivalents.
- Expandable-module options as a way to widen the addressable buyer segment (smaller initial purchase, expand later) — a demand-smoothing lever worth modeling once real inputs exist.

### Segment risk
This channel is exposed to consumer credit conditions, discretionary housing spend, and general residential construction cycles — standard housing-market cyclicality. See [[Risks & Mitigations]].

---

## Channel 2 — Disaster Relief Pod (NE-DR-401)

### The demand thesis
Australian state and federal emergency services (SES, ambulance, and broader emergency-management agencies) periodically procure rapid-deployment infrastructure for disaster response — medical, command, accommodation, and support capacity that can be deployed in minutes rather than days. This is a **government tender / procurement-cycle market**, not a retail one: lumpy, RFP-driven, and dependent on agency budgets and disaster incidence rather than consumer sentiment. That is a feature for portfolio purposes (see [[The Thesis]]) but a distinct risk profile in its own right (see [[Risks & Mitigations]]).

### Model structure (worked illustrative example — replace every input)

| Variable | Illustrative example | Notes |
|---|---|---|
| Number of Australian state/territory + federal emergency-management agencies as potential buyers | 9 jurisdictions | This row is a structural fact (6 states + 2 mainland territories + a federal/national coordination body), not a demand estimate — everything below it is illustrative. |
| Illustrative pods procured per jurisdiction per multi-year budget cycle | 8 pods (midpoint of an illustrative 4–12 range) | Entirely unvalidated — depends on tender outcomes, agency budgets, disaster incidence. |
| Illustrative average selling price per pod (role-configured: Medical / Command / Accommodation / Support) | ≈$280,000 blended | Carried from the relief-pod cost range in [[Unit Economics]] plus an illustrative tender margin; role configuration changes this meaningfully — see [[Unit Economics]] role-by-role breakdown. |
| Illustrative addressable pod volume per year (steady-state, smoothed across a 4-year budget cycle) | 9 × 8 ÷ 4 ≈ **18 pods/yr** | Smoothing is a modeling convenience — real revenue will be lumpy, not smooth. See [[Risks & Mitigations]]. |
| Illustrative annual disaster-relief revenue | 18 × $280,000 ≈ **$5.0M/yr** | Small next to the residential channel's illustrative ceiling — this channel's value in the model is diversification and counter-cyclicality (see [[The Thesis]]), not primary revenue volume. |

> ⚠️ Illustrative assumption, internally consistent within this vault — not sourced data. Validate with real data before use in an actual pitch.

### Demand drivers worth tracking (qualitative, not sized here)
- Deployment speed (<30 min) and 25+ year service life as procurement-scoring criteria versus incumbent options (site-built temporary facilities, caravan/demountable rentals, tents).
- Rooftop solar and comms-mast self-sufficiency as differentiators for off-grid or infrastructure-degraded deployment scenarios.
- Role-reconfigurability (Medical/Command/Accommodation/Support) as a way to sell fleet flexibility to a single agency rather than single-purpose units.
- Tender cycles and budget-approval timelines specific to Australian emergency-management procurement — needs direct agency engagement to size, not desk research.

### Segment risk
This is the more volatile of the two channels by nature — a single missed or delayed tender can swing a year's revenue materially. It should be modeled and presented as a **lumpy, non-linear** revenue stream, never smoothed into a steady annual run-rate in real financial materials. See [[Risks & Mitigations]].

---

## How the two channels interact in the model

- **Uncorrelated demand drivers**: residential demand tracks housing-market and consumer-credit cycles; disaster-relief demand tracks government budget cycles and disaster incidence. A real model should treat these as (close to) independent variables, not blend them into one growth curve.
- **Shared capacity**: both channels draw on the same Factory 01 robotic line capacity (see [[Unit Economics]] and [[Scaling Plan]]), so a real model needs a capacity-allocation assumption between the two — currently unmodeled here and worth building out.
- **Cross-subsidized brand equity**: government-procured disaster-relief pods in the field are also a public, visible demonstration of build quality that plausibly supports residential brand trust — a qualitative effect, not one this model attempts to quantify.

## Related notes
[[The Thesis]] · [[Unit Economics]] · [[Moat & Defensibility]] · [[Scaling Plan]] · [[Risks & Mitigations]] · [[The Ask]] · [[Investor Home]]
