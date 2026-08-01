---
tags: [moc, home, new-eden]
---

# New Eden — Core Technical Vault

This is the ground-truth product and engineering reference for **New Eden**, a premium Australian modular-home brand ("Building Tomorrow", "Designed without compromise") built on a common 40ft Hi-Cube ISO-compatible steel chassis and produced on a robotic manufacturing line. Every other New Eden vault — investor materials, internal self-validation/red-team, and the government/disaster-relief pitch — should treat the notes in this vault as the single source of truth and should not introduce numbers, claims, or features that contradict what is written here. Where marketing copy is aspirational or ambiguous, the notes here commit to a specific, defensible engineering interpretation so downstream teams argue from the same facts.

The vault is organized into five groups: brand framing, the two product lines, how the products get made, the physical/material platform they share, and the standards posture that governs (and is deliberately exceeded by) all of it.

## Brand
- [[Brand & Positioning]]

## Product Lines
- [[Product Line - Residential]] — the "30 New Ideas. One Vision." architectural line
- [[Product Line - Disaster Relief Pod]] — NE-DR-401 Rapid Response Unit

## Manufacturing & Factory
- [[Manufacturing Process]] — the 8-stage production line
- [[Factory & Automation Stack]] — ABB / FrameCAD / digital twin architecture, and an honest read on "Zero Human Input"
- [[Tolerance Management Architecture (R&D)]] — proposed (unbuilt, unvalidated) closed-loop tolerance-budget architecture for the Stage 1→3→5 chassis→framing→cladding stack-up

## Shared Physical Platform
- [[Dimensions & ISO Compatibility]] — the 40ft Hi-Cube chassis geometry and why it was chosen
- [[Materials & Finishes]] — the four-material palette and copper ageing options

## Standards & Design Philosophy
- [[Standards & Compliance Baseline]] — the regulatory floor (NCC + AS/NZS families)
- [[Premium-Beyond-Minimum Design Philosophy]] — how New Eden is engineered to sit above that floor, and by how much

## How to use this vault
- Treat every dimension, weight, ID format, and named feature in this vault as fixed. Do not restate marketing language without pairing it with the underlying engineering explanation — that pairing is the point of this vault.
- Cross-reference liberally with `[[Wikilinks]]` rather than duplicating content between notes.
- The disaster-relief line and the residential line share one chassis platform ([[Dimensions & ISO Compatibility]]) and one factory ([[Manufacturing Process]], [[Factory & Automation Stack]]) but have separate spec sheets and separate compliance emphases — do not merge them.
