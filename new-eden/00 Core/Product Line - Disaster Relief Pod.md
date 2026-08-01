---
tags: [product, disaster-relief, emergency-services, new-eden]
---

# Product Line — Disaster Relief Pod (NE-DR-401)

**Unit ID format**: NE-DR-401 (New Eden – Disaster Relief – model 401). **Name**: Rapid Response Unit. **Tagline**: "Deploy. Connect. Protect. Recover." Built on the same [[Dimensions & ISO Compatibility|40ft Hi-Cube ISO chassis]] and produced on the same [[Manufacturing Process|8-stage robotic line]] as [[Product Line - Residential]], but purpose-built for Australian emergency services deployment (branding references "DIAL 000 IN EMERGENCY" and SES/ambulance operating context). Where the residential line sells design signature, the Disaster Relief Pod sells speed, reliability, and role flexibility on the same underlying platform — see [[Brand & Positioning]] for why this is a feature-parity product, not a downmarket one.

## Spec sheet

| Spec | Value |
|---|---|
| Unit ID | NE-DR-401 |
| Chassis | 40ft Hi-Cube ISO-compatible module (see [[Dimensions & ISO Compatibility]]) |
| Tare weight (approx.) | 6,800 kg |
| Deployment time | Under 30 minutes from arrival on site to operational |
| Role configurations | Medical / Command / Accommodation / Support |
| Design lifespan | 25+ years |
| Fitted equipment | Rooftop solar panels, comms mast/antenna, entry awning, exterior power/data/plumbing service ports, first-aid signage, egress steps |
| Transport modes | Road, rail, sea (per shared ISO 668/1161 chassis compatibility) |
| Stacking | Engineered stackable up to 3 high (shared chassis rating) |

## Deployment envelope — reverse-engineering "under 30 minutes"

A sub-30-minute deployment claim constrains the design in specific, checkable ways. To be credible it implies:

- **No wet trades on site.** All plumbing, electrical, and HVAC connections must be pre-terminated at the factory to quick-connect fittings at the exterior service port cluster — the same "plug-and-play utility connection system" used across the platform (see [[Dimensions & ISO Compatibility]]). Site work is limited to: place unit (crane or heavy transporter set-down), extend/lock egress steps, unfold/raise the entry awning, connect external services (power tie-in or genset, water, sewer/holding tank, comms), and raise the mast.
- **Levelling, not footings.** A 30-minute target rules out a poured or engineered footing system. The chassis's own ISO corner castings almost certainly sit on adjustable screw jacks or pre-positioned modular pads/blocks rather than a site-specific slab, trading long-term footing engineering for rapid, reversible levelling — appropriate for a relocatable emergency asset, though it does mean the unit's long-term siting (for a multi-week deployment) needs a follow-up geotechnical check that a "30 minute" first-response deployment would not have time for.
- **Comms mast is likely a pneumatic or crank-up telescoping mast** (not a bolted lattice tower) so a two-person crew can raise it without cranes or engineering sign-off on site, carrying either a two-way radio repeater, satellite (VSAT/BGAN-class) terminal, or cellular booster — critical because disaster deployments frequently occur where terrestrial networks are down.
- **Rooftop solar plus a factory-integrated battery/inverter and likely a small diesel or dual-fuel genset input** is the plausible power stack: solar and battery cover baseline hotel loads (lighting, comms, refrigeration) indefinitely off-grid, with the genset input as backup/surge capacity for the Medical configuration's higher continuous draw.

## Role configurations

All four roles share the same chassis, envelope, and exterior service port cluster; they differ in interior fit-out, which is installed at [[Manufacturing Process]] stage 7 (Interiors & Services) as a configuration selected before the unit enters that stage — this is the same "common platform, configurable interior" logic used for expandable modules in the residential line (see [[Product Line - Residential]] feature 28).

### Medical
- Interior fitted as a mobile clinical space: examination/treatment bay(s), a clean/sterile supply zone, medical gas or oxygen concentrator provision, higher-capacity electrical circuit (imaging/diagnostic equipment, refrigeration for medication/vaccines), and a dedicated clinical waste storage point accessible from an exterior service port for external collection without transiting the clean zone.
- Likely holds the tightest internal environmental control (temperature/humidity-controlled zone for medication and specimen storage) of the four roles, drawing most heavily on the platform's hidden/ducted HVAC approach (see [[Product Line - Residential]] feature 21) adapted for clinical-grade filtration.
- First-aid signage (listed as fitted equipment) is most directly tied to this role but is standard across all four for public-facing wayfinding during a multi-unit deployment.

### Command
- Interior fitted as an incident command post: workstations, situational-display screens, and the primary termination point for the comms mast — this configuration is the one most likely to carry the full communications suite (repeater, satellite terminal, network switch gear) since it is the coordination hub other units and field crews connect back to.
- Requires the highest continuous power draw for electronics and the most robust data infrastructure (server/network cabinet), making it the configuration most dependent on the genset backup input described above.
- Likely retains the most flexible open floor plan of the four roles to accommodate variable incident-management team sizes.

### Accommodation
- Interior fitted for crew/displaced-person rest: bunks or fold-down beds, storage, and a compact wet area (shower/toilet) drawing on the platform's plumbing stub-out and holding-tank provisions.
- Lowest power/data intensity of the four roles; HVAC sizing prioritizes occupant comfort over the equipment-cooling loads seen in Medical or Command.
- Most likely to be deployed in multiples (several Accommodation units per incident) alongside a smaller number of Medical/Command/Support units, which is consistent with a manufacturing strategy that wants one dominant interior fit-out variant to maximize production-line repeatability.

### Support
- The catch-all/logistics configuration: likely fitted as flexible storage, equipment/supply staging, a field kitchen/amenity block, or power/water distribution hub (holding larger battery banks, water tanks, or fuel storage than the other three roles, since it is not constrained by clinical, command-electronics, or habitability fit-out).
- Reasonable to infer this is also the configuration used to test and pre-position new equipment types before they're formalized into a fifth role, given "Support" is the only role name broad enough to absorb miscellaneous mission needs.

## What is fixed across all four roles
- Exterior envelope, chassis, ISO castings, transport/stacking rating (see [[Dimensions & ISO Compatibility]])
- Rooftop solar, entry awning, egress steps, exterior service port cluster, first-aid signage — all listed as standard fitted equipment regardless of role
- Design lifespan of 25+ years and the "exceeds NCC/AS-NZS floor" posture (see [[Standards & Compliance Baseline]] and [[Premium-Beyond-Minimum Design Philosophy]]) — non-negotiable given this line is life-safety equipment, not discretionary housing
- Digital twin traceability (QR/serial tagging, per [[Product Line - Residential]] feature 16) — arguably more operationally critical here than on the residential line, since emergency services need to know a specific unit's maintenance and inspection history before trusting it in an active incident

## Why 25+ years matters here specifically
A 25-year design life on a unit that may sit in storage for years between deployments, then be trucked into an active disaster zone and expected to function within 30 minutes, implies the platform's corrosion protection, structural fatigue allowance, and service systems are specified for worst-case intermittent-use degradation (UV/corrosion during storage, vibration fatigue during repeated transport cycles), not steady-state occupancy — a materially harder engineering target than a residential unit's 25-year expectation under continuous, maintained occupancy. See [[Premium-Beyond-Minimum Design Philosophy]] for how this shapes material and coating choices.
