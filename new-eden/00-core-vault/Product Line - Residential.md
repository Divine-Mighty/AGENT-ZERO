---
tags: [product, residential, architecture, new-eden]
---

# Product Line — Residential ("30 New Ideas. One Vision.")

The residential/architectural line is New Eden's premium product, built on the shared [[Dimensions & ISO Compatibility|40ft Hi-Cube chassis]] and produced through the same [[Manufacturing Process|8-stage robotic line]] as the [[Product Line - Disaster Relief Pod]]. Marketing presents 30 named signature features under the banner "30 New Ideas. One Vision." Below, the 30 are grouped into six functional clusters. For each feature: the marketing name, a plain description of what it looks/feels like, and the inferred real engineering implementation behind it — this is the back-engineering core of the vault. Material and finish specifics referenced throughout are detailed in [[Materials & Finishes]].

---

## Cluster A — Envelope & Weatherproofing (10 features)

Everything in this cluster exists to make the building envelope look seamless (no visible gutters, downpipes, or corner posts) while still shedding Australian weather — heavy rain, UV, and in many deployment regions, cyclonic wind — competently. See [[Premium-Beyond-Minimum Design Philosophy]] for how far above code minimums these details are pushed.

**1. Floating roof** — The roofline appears to hover above the wall plane with no visible eave-to-wall junction. *Implementation*: roof trusses (installed in [[Manufacturing Process]] stage 4) cantilever past the top wall plate/rim beam so the fascia line reads as structurally independent of the wall cladding plane below. The roof edge is finished in a slim folded-metal fascia with guttering concealed behind it (feature 4), and the underside soffit recess can host integrated lighting (feature 10).

**2. Recessed entry** — The front door is set back into a covered notch rather than sitting flush with the facade. *Implementation*: a bay of wall framing is pulled back from the main cladding plane, and the roof/floor cassette above cantilevers over the recess to act as a built-in awning. The recess floor is set with a fall to a discreet drain to shed wind-driven rain, and the threshold is detailed with a thermally broken sill.

**3. Vertical shadow gaps** — Vertical reveal lines divide the cladding into panel bays for a crafted, non-monolithic facade. *Implementation*: cladding panels are hung on a batten/rail sub-frame with a fixed ~10–15mm reveal joint; the gap is backed with a concealed flashing/drainage channel so it functions as a pressure-equalized rainscreen drainage cavity, not just a cosmetic line. Batten spacing is standardized to the tolerances of the robotic cladding-placement cell (see [[Factory & Automation Stack]]).

**4. Hidden gutters** — No visible box gutter or downpipe on the main elevations. *Implementation*: a parapet-integrated or fascia-concealed box gutter sits behind the roof edge trim, tied into the standing-seam roof drainage plane installed in [[Manufacturing Process]] stage 6. Downpipes are routed internally or through a corner post cavity to a below-floor stormwater connection point, part of the chassis's plug-and-play utility connection system (see [[Dimensions & ISO Compatibility]]).

**5. Secret rainheads** — Rainhead and overflow points are concealed rather than treated as visible ornamental features. *Implementation*: rainhead sumps are recessed into the parapet/box gutter, with overflow relief slots hidden behind the fascia trim. Overflow capacity is sized well above AS/NZS 3500.3 minimums (see [[Standards & Compliance Baseline]], [[Premium-Beyond-Minimum Design Philosophy]]) to prevent parapet overtopping in extreme rainfall.

**9. Floor-to-ceiling corner glass** — Glazing wraps an external corner with no visible corner post. *Implementation*: the structural corner post is moved inboard or replaced by an engineered steel corner spine (the same member exposed as feature 24), letting two glass panes butt-joint at the corner on a structural-silicone or minimal aluminium corner mullion. The glazing unit is a double-glazed IGU set in a gasketed, semi-floating frame — not rigid sealant — to accommodate the small amount of flex the module experiences under crane and road transport loads.

**11. Continuous window band** — A horizontal ribbon window runs along most of an elevation instead of punched openings. *Implementation*: a continuous structural lintel/header (steel top rail) spans the full bay so the wall studs below the band are non-load-bearing infill. The band is built from factory-glazed, unitized window modules robot-placed in one operation, with a single continuous head/sill flashing run rather than repeated per-window penetrations.

**12. Hidden roller shutters** — Security/blackout roller shutters disappear into the wall or roof line when retracted. *Implementation*: the shutter box is recessed into the window head within the wall cavity or floating-roof soffit (feature 1). The motorized roller is wired into the smart ceiling automation bus (feature 26), and guide rails are integrated into the window reveal so no surface-mounted housing is visible externally.

**19. Living roof option** — An optional vegetated roof finish. *Implementation*: a lightweight modular green-roof tray system (drainage cell, filter fabric, growing medium, low-profile planting) sits on a root-barrier membrane over the structural roof deck, replacing or overlaying a zone of the standing-seam roof. Because it adds significant dead load (typically 100–200kg/m² saturated), the roof trusses and roll-formed roof structure ([[Manufacturing Process]] stage 4) must be specified for this option before framing — it is a factory configuration choice, not a field retrofit. Drainage ties back into the hidden gutter system (feature 4).

**20. Glass garage door** — A garage/large-opening door that is fully glazed rather than a solid roller door. *Implementation*: the opening is framed with the same continuous-header logic as feature 11. The door leaf is an insulated glass sandwich panel or IGU-glazed sectional/panel-lift door on a track rated for the module's opening width, and — because units may be sited in cyclone-prone regions — the assembly must be a wind-load-rated glazed door product, not a standard glazed shed door (see [[Standards & Compliance Baseline]]).

---

## Cluster B — Structural & Robotics-Enabled Assembly (5 features)

These features are only economical or even possible because of the robotic assembly line described in [[Factory & Automation Stack]] — they trade site-labour flexibility for factory-repeatable precision.

**8. Black steel base** — A visually distinct dark steel base/plinth at the bottom of the module. *Implementation*: the exposed lower chassis rail and ISO 1161 corner-casting zone is finished in a durable dark powder-coat/corrosion-resistant coating, distinct from the upper cladding palette. This is the zone that actually carries stacking and lifting loads (see [[Dimensions & ISO Compatibility]]), so the coating spec is upgraded to a marine-duty corrosion system rather than standard architectural powder-coat — it is the component most exposed to transport abrasion and, on the [[Product Line - Disaster Relief Pod]], to floodwater.

**22. Magnetic cladding** — Cladding panels attach via a magnetic/quick-release system rather than being fully fixed. *Implementation*: cladding panels seat onto steel sub-battens with concealed magnetic alignment pins that snap the panel onto a mechanical retaining clip. The magnets handle alignment and initial hold (useful for the robotic placement cell); wind uplift and structural loads are carried by the mechanical clip, not the magnet, per standard cladding-fixing practice. This enables field-swappable panels for damage repair, finish upgrades, or service-cavity access.

**23. Robot lift points** — Dedicated pick-up points on the module for automated material handling in the factory. *Implementation*: lift/attachment points, positioned and load-rated for the factory's AGVs and gantry/robotic lifting cells, move the module between the eight production stages ([[Manufacturing Process]]). Point locations are surveyed into the module's digital twin model (feature 16) so handling equipment always picks up on engineered load paths rather than ad hoc slinging points.

**24. Internal steel sculpture** — An exposed structural steel truss/frame element treated as a visible design feature rather than hidden behind linings. *Implementation*: a portion of primary structural steel — a roof truss node, portal frame, or the same corner spine referenced in feature 9 — is deliberately left exposed and finished (ground welds, consistent bolt pattern, painted/blackened) to a visual-grade standard rather than a purely functional one. Interior linings and service runs are designed to route around the exposed member instead of boxing it in.

**28. Expandable modules** — The ability to join multiple 40ft units together or add modules over time. *Implementation*: standardized inter-module connection points (a bolted end-plate or ISO-casting-based coupler) at one or both 12,192mm end faces, with matched service stub-outs (power/data/plumbing) positioned identically across the range so two modules can be craned into place and joined on site. The join-face wall panel is a removable/knockout panel rather than permanent cladding, and a site-poured or pre-cast connecting slab/deck ties the two chassis frames together against differential settlement.

---

## Cluster C — Energy & Building Services (5 features)

**13. Solar roof skin** — PV integrated into the roof surface rather than rack-mounted panels. *Implementation*: building-integrated photovoltaic (BIPV) standing-seam-profile panels or thin-film laminate applied to (or replacing sections of) the standing-seam roof sheet from [[Manufacturing Process]] stage 6, wired through the roof deck to a factory-installed inverter/DC combiner in the services cavity. Contrast with the [[Product Line - Disaster Relief Pod]], which uses rack-mounted panels for rapid field serviceability instead of full integration.

**14. Robotic service dock** — A dedicated point where automated/robotic systems can dock with the module for servicing. *Implementation*: a standardized external panel with quick-connect ports for power, data/network, and diagnostic access to the module's switchboard, smart-ceiling bus, and HVAC controller — fixed at the same location on every unit so a technician (or, eventually, an automated diagnostic cart) can connect without opening wall cavities. The dock also exposes a physical connection to the digital twin controller for pulling sensor/fault logs on site.

**15. Magnetic service wall** — An interior/exterior panel that detaches (magnetically assisted, like feature 22) to expose service runs for maintenance. *Implementation*: a defined services chase behind a magnetic-clip removable panel gives access to plumbing manifolds, electrical home runs, and HVAC ductwork without cutting into finished linings. The panel is keyed to the module's digital twin drawing set via the QR tag (feature 16), so a technician scans the module and is shown exactly which panel to pull for a given fault.

**21. Hidden air conditioning** — No visible outdoor condenser or indoor head units. *Implementation*: a ducted reverse-cycle system with the condenser housed in a louvred, colour-matched enclosure integrated into the black steel base (feature 8) or a roof plant recess, rather than a wall-mounted box. Ductwork runs through the smart ceiling cavity (feature 26) to concealed linear diffusers — both outdoor and indoor units are absorbed into features that already exist on the module.

**26. Smart ceiling** — A ceiling integrating lighting, sensors, HVAC diffusion, and home-automation control rather than plain plasterboard. *Implementation*: a factory-fitted ceiling cassette combining the structural roof-truss soffit lining, integrated LED lighting circuits, PIR/environmental sensors, HVAC diffuser outlets, and a home-automation hub — pre-wired and tested at the factory (ties to feature 17) as one installed module during [[Manufacturing Process]] stage 7. This is the single feature that makes "zero human input" most plausible, since it collapses several normally site-based trades into one factory operation (see [[Factory & Automation Stack]]).

---

## Cluster D — Interior & Signature Finish (5 features)

**6. Woodgrain feature box** — A projecting or recessed volume finished in the Colorbond Woodland Grey woodgrain-effect steel. *Implementation*: a specific architectural volume (entry canopy, window box, balcony soffit) clad in roll-formed Woodland Grey woodgrain-finish steel panels (see [[Materials & Finishes]]) on its own sub-frame, used as a deliberate material contrast against the Zinc Monument body cladding to signal "feature," not structure.

**7. Copper portal** — An entry or window surround finished in copper. *Implementation*: a copper-clad portal frame (folded/roll-formed copper sheet over a steel sub-frame) surrounding the recessed entry (feature 2) or a feature window, specified in one of the three ageing finishes (see [[Materials & Finishes]]). The copper is isolated from dissimilar metals with a non-conductive underlay to prevent bimetallic (galvanic) corrosion against the steel/zinc chassis — standard architectural-copper detailing.

**10. Exterior lighting slots** — Linear lighting integrated as a recessed slot in the facade or soffit rather than surface-mounted fittings. *Implementation*: a continuous extruded aluminium light channel recessed into the shadow-gap joints (feature 3) or the floating-roof soffit (feature 1). IP65-rated LED strip is fitted during factory assembly and verified under the RGB factory testing stage (feature 17), wired back to the smart ceiling control bus (feature 26) for scene/security lighting control.

**18. Copper ageing options** — Customer choice of copper finish life-stage (New Copper / Weathered / Verdigris). *Implementation*: detailed fully in [[Materials & Finishes]]. Applied wherever copper is specified — the copper portal (feature 7) and any copper accent trims — as a premium personalization axis and margin lever at point of sale.

**29. Corner glass lounge** — An internal living space positioned at a glazed corner, the interior experience created by feature 9's structural solution. *Implementation*: the floor plan places a primary living zone directly at the floor-to-ceiling corner glass bay, requiring that bay's structural corner spine (features 9/24) and floor cassette to be engineered for a column-free sightline in both directions. HVAC diffusers and lighting in this bay are positioned off-axis from the two glazed faces so nothing breaks the corner sightline.

---

## Cluster E — Digital Traceability & Factory QA (3 features)

**16. Factory QR code** — A physical ID plate and QR code on every module (example: "Module 000384, Factory 01, Scan for Digital Twin"). *Implementation*: a laser-etched or engraved stainless/anodized ID plate riveted near the ISO corner casting — a location that survives the module's whole service life. The QR resolves to a per-serial digital twin record (as-built drawings, sensor test logs from stage 8, service history). The same serial number is used across the factory MES (manufacturing execution system), the factory signature wall plaque (feature 25), and after-sale service dispatch via the robotic service dock (feature 14).

**17. RGB factory testing** — Testing described with "RGB," most plausibly an automated electrical/lighting circuit test using colour-coded pass/fail signalling. *Implementation*: an automated test rig cycles every electrical circuit and smart-ceiling lighting zone (feature 26) through a red/green/blue test pattern so a machine-vision camera (or human QA inspector) can visually confirm every circuit and addressable fixture responds correctly in one automated pass. Results are logged against the module's serial number as part of the stage 8 QA gate (see [[Manufacturing Process]]).

**25. Factory signature wall** — A plaque reading "New Eden Factory 01, Module 000384, Built by Robotics, Inspection Passed." *Implementation*: a physical sign-off plaque installed at the end of stage 8, referencing the same serial number as the QR tag (feature 16), fitted only after the module clears every QC gate in [[Manufacturing Process]]. It functions both as a marketing signature ("built by robotics") and as a real regulatory compliance plate, analogous to the compliance/data plate required on manufactured/relocatable buildings.

---

## Cluster F — Customization & Outdoor Living Extension (2 features)

**27. New Eden deck system** — A proprietary modular decking system that attaches to the chassis. *Implementation*: a bolt-on deck frame that keys into the same ISO corner casting / robot lift point hard points (feature 23) used for transport, so the deck's structural connection to the module is pre-engineered at the factory rather than requiring bespoke site structural certification. The deck substructure is delivered flat-packed or as a pre-assembled cassette, craned and placed alongside the module on site.

**30. Signature architecture** — The overall design language that makes a New Eden home read as distinctively "New Eden" rather than a generic modular box. *Implementation*: this is a systems-integration feature rather than a discrete component — the codified combination of the floating roofline (feature 1), consistent shadow-gap reveal module (feature 3), fixed material palette (see [[Materials & Finishes]]), and a small set of allowed massing moves (recessed entry, corner glass, feature boxes) applied consistently across every configuration, so multi-module expandable builds (feature 28) still read as one coherent design. In practice this is enforced as a factory-side design ruleset/configurator constraint rather than free-form architecture.

---

## Cross-references
- Chassis and geometry underlying every structural feature above: [[Dimensions & ISO Compatibility]]
- Where each feature is actually installed on the line: [[Manufacturing Process]]
- Robotic cells enabling repeatable installation: [[Factory & Automation Stack]]
- Material specification detail: [[Materials & Finishes]]
- The design mandate that pushes every one of these implementations above code minimum: [[Premium-Beyond-Minimum Design Philosophy]]
