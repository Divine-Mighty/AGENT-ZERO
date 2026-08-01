---
tags: [validation, compliance, standards, new-eden]
---

# Compliance Feasibility

The founder's directive is explicit: Australian NCC/AS-NZS standards are a *floor*, not a target, especially for the disaster-relief line, which is life-safety equipment used in emergencies, likely including bushfire-affected areas. This note doesn't cite clause numbers — no certifying engineer has looked at this design, and asserting specific clauses would be inventing authority this vault doesn't have. Instead, it maps the relevant standard *families* to specific tension points against the design as described in the core vault, and names which one is the biggest redesign risk.

## AS 3959 — bushfire construction
**What it governs**: construction requirements for buildings in bushfire-prone areas, scaled by Bushfire Attack Level (BAL), covering things like ember ingress prevention, gutter/valley debris accumulation, glazing protection, and combustibility of materials near the building envelope.

**Where it bites New Eden specifically**:
- **Hidden/concealed gutters** (feature of the residential envelope) are a known bushfire liability pattern in principle — concealed gutters are harder to clear of leaf litter and ember-catching debris than open, accessible gutters, and any bushfire-conscious design review is going to ask hard questions about ember accumulation and access-for-clearing in a concealed gutter detail.
- **Vertical shadow gaps and reveal details** create cavities and joints in the envelope. In higher BAL categories, envelope penetrations, gaps, and joints generally need ember-resistant treatment (screening, sealing) — a purely aesthetic shadow gap needs to be re-engineered as an ember-resistant detail, which may change its visual proportions.
- **Glazing** (corner glazing, and especially the glass garage door) is one of the most heavily regulated elements in higher BAL categories — bushfire-rated glazing and screening requirements get progressively stricter, and a large glass garage door is a hard element to make compliant at the top BAL categories without changing its size, glass spec, or adding shutters/screens that undercut the "glass garage door" as a signature feature.
- **Cladding materials**: the Colorbond and zinc claddings are metal and are generally the easier part of this problem; the "woodgrain" finish needs to be confirmed as a non-combustible printed/textured steel product (as implied by the Colorbond Woodland Grey material) and never allowed to drift toward an actual timber-look combustible product, which would be a straightforward bushfire compliance failure.

**Verdict**: this is plausibly solvable, but only with real redesign work on gutters, gap details, and glazing at the top BAL categories — and the disaster-relief line specifically should be assumed to need to perform at a high BAL category, because it's explicitly meant to be deployable in and near bushfire-affected parts of Australia. **This is flagged below as the single biggest compliance-driven redesign risk.**

## AS/NZS 1170 family — structural design actions (wind loading in particular)
**What it governs**: the loads a structure must be engineered to withstand, including wind actions, which scale with a structure's height, exposure, and geometry.

**Where it bites New Eden specifically**:
- A lightweight, relocatable steel module is inherently more wind-sensitive than a heavy site-built structure, and the brand's own aesthetic — a "floating roof" with shadow-gap reveals and cantilevered/overhanging elements — is exactly the kind of geometry that increases wind uplift and edge-loading risk versus a simple box roof.
- Stacking three-high changes the wind exposure category and load path for lower units versus a single-storey deployment; the ISO chassis's stacking rating (ISO 1161 corner castings) is proven for shipping/transport loads, but habitable-building wind and occupancy loading in a stacked configuration is a separate engineering question that needs its own sign-off, not an inherited one.
- The disaster-relief pod is explicitly meant to be deployed rapidly on ad hoc sites, which may not offer the sheltered, engineered footing of a permanent residential site — anchoring and wind performance for a temporary, rapidly-deployed unit is a harder problem than for a permanently sited one, and it has to be solved without adding so much anchoring hardware or weight that it undermines the <30-minute deployment claim.

**Verdict**: solvable with real structural engineering, but it will cost weight, cost engineering fees, and likely constrain some of the more cantilevered "floating roof" geometry — not a redesign-everything risk, but a real one for the disaster-relief pod's deployment claims specifically.

## AS/NZS 4600 — cold-formed steel structures
**What it governs**: design of structural members formed from cold-formed (roll-formed) steel, which is exactly what the FrameCAD line produces for wall framing and roof trusses.

**Where it bites New Eden specifically**: this isn't a design-language tension so much as a process one — every distinct structural configuration (residential module variants, expandable-module connections, disaster-relief pod variants) likely needs its own engineering certification against this standard family, because cold-formed steel structural performance is sensitive to member profile, connection detail, and span, all of which differ across the product range. See [[Cost-to-Build Reality Check]] for why this multiplies certification cost rather than being a one-time cost.

## AS 1428 series — accessibility
**What it governs**: accessible design requirements — circulation widths, turning space, doorway clearances, accessible sanitary facility dimensions.

**Where it bites New Eden specifically**: the disaster-relief pod's **Medical** and **Accommodation** role configurations are exactly the configurations where accessibility compliance matters most (patients, displaced people including those with mobility constraints, in an emergency-services context) — and they have to fit inside a fixed 2,352mm internal width. Accessible circulation and turning-space requirements are dimensionally demanding; a 2,352mm internal width leaves comparatively little margin once a turning circle, a doorway, and fixture clearances are all accounted for in the same footprint. This is a genuine, checkable numeric feasibility question, not a stylistic one, and it deserves a real accessibility-consultant review rather than an assumption either way — see [[Reality Check Summary]].

## AS/NZS 3000 (wiring rules) and AS/NZS 5601 (gas installations)
**What it governs**: electrical and gas installation safety.

**Where it bites New Eden specifically**: the "plug-and-play utility connections" feature is a real convenience claim, but every exterior service port (power, and gas if used) is a certified connection point that has to remain safe through repeated connect/disconnect cycles, field conditions (dust, moisture, physical knocks during transport and deployment), and — for the disaster-relief pod specifically — connection by emergency-services personnel who are not electricians. Quick-connect utility hardware exists in industrial/marine/caravan contexts, but "plug-and-play" as a headline claim needs the isolation, protection (RCD/earth fault), and ingress-protection details specified and tested, not left implicit.

## NCC approval pathway
Separate from any single standard family: the NCC likely does not have an off-the-shelf deemed-to-satisfy category that cleanly covers "stacked, relocatable, ISO-chassis habitable structure sold as both permanent residential and rapid-deployment emergency accommodation." That combination probably means a **performance-based / alternative-solution pathway**, assessed case by case per configuration, which is slower and more expensive per variant than a standard build — and it multiplies with every distinct configuration (see [[Cost-to-Build Reality Check]]).

## Biggest compliance-driven redesign risk
**AS 3959 bushfire construction, specifically the interaction between hidden gutters, shadow-gap reveals, and large glazing (the glass garage door above all).** This is the single point where the standard most directly attacks the design vocabulary the brand is built on — not a peripheral engineering fix, but a threat to the specific signature details ("30 New Ideas") that differentiate New Eden from a plain container conversion. It also can't be scoped away for the disaster-relief line, since that line is explicitly meant to serve bushfire-affected areas. If a BAL-40/Flame Zone-capable version of these details can't be found, the brand faces a choice between a bushfire-zone variant (fragmenting "One Vision") or quietly limiting where the flagship aesthetic can legally be sold and deployed.

## Related
- [[Reality Check Summary]]
- [[Engineering Feasibility]] — cladding registration accuracy (Stage 5) interacts directly with the ember-sealing detail work AS 3959 will require.
- [[Cost-to-Build Reality Check]]
- [[Open Questions & Next Validation Steps]]
