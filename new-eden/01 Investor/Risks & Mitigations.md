---
tags: [investor-vault, risks, new-eden]
---

# Risks & Mitigations

> [!note] Purpose
> The thesis in [[The Thesis]] is genuinely strong on structure — robotics, dual-channel demand, ISO logistics, digital-twin lock-in. None of that makes the execution risks below smaller. This note is meant to be read honestly, not defensively.

## 1. Capex risk

**The risk:** Factory 01's robotics line (ABB arms + FrameCAD roll-forming) represents a large, front-loaded capital commitment before revenue at scale exists to support it. If throughput, quality, or demand come in below the assumptions in [[Unit Economics]], the fixed capex base doesn't shrink — the per-unit amortization simply gets worse, compressing or eliminating the premium margin the whole thesis depends on.

**Mitigation direction:**
- Phase-gate further capex (Factory 02+) behind proven Factory 01 performance — see the sequencing discipline in [[Scaling Plan]].
- Build the amortization model in [[Unit Economics]] with a realistic (not nameplate) utilization assumption from the start, so the margin case isn't quietly resting on optimistic uptime.
- Size [[The Ask]] against a capex plan with defined milestones, not a single lump sum with no accountability checkpoints.

## 2. Robotics reliability / uptime risk

**The risk:** The entire cost and speed advantage depends on the ABB robotic wall-framing and FrameCAD roll-forming stages actually running at high, consistent uptime. Industrial robotics lines, especially in early operating years, are exposed to unplanned downtime, calibration drift, part/material feed issues, and integration bugs between stages. Downtime here doesn't just slow production — it directly erodes the amortization math in [[Unit Economics]] and undercuts the "AI Powered Production | Zero Human Input" positioning if human intervention is frequently required to keep the line running.

**Mitigation direction:**
- Track uptime as a first-class operating metric from Factory 01's first production runs, not just after Phase 2 scaling begins (see [[Scaling Plan]]).
- Build maintenance/spare-parts and technical-support relationships with the robotics and roll-forming equipment vendors into the operating plan and cost stack explicitly, rather than treating equipment as "install and forget."
- Avoid overstating "Zero Human Input" in external-facing material beyond what the line actually achieves — the digital-twin/traceability brand promise depends on the company's own claims being accurate and auditable.

## 3. Standards-certification risk and timeline

**The risk:** The founder directive treats NCC/AS-NZS standards as a regulatory floor to be exceeded, which is the right long-term positioning — but certification against Australian building codes is a real gating process with its own timeline, and a robotically-built, novel-construction-method product may face closer scrutiny or a longer certification path than an incumbent construction method with an established compliance track record. Certification delay directly delays revenue in both channels — residential sale and government procurement both likely require (or strongly prefer) certified compliance.

**Mitigation direction:**
- Treat certification timeline as a critical-path item in go-to-market planning, not a background task running in parallel with sales.
- Engage certification bodies and NCC/AS-NZS compliance pathways early, ideally before Factory 01 is running at full production volume, so design changes required for compliance don't hit a line already tooled for a different spec.
- For the disaster-relief channel specifically, confirm procurement requirements with target agencies directly (SES, ambulance, emergency-management bodies) — government tender compliance requirements may differ from, or add to, residential NCC/AS-NZS certification.

## 4. Market-adoption risk

**The risk:** The premium positioning in [[The Thesis]] assumes a meaningful segment of the market will pay more for design identity, material quality, and digital-twin traceability over standard steel-frame prefab or site-built alternatives. This is currently an assumption, not a validated finding — see the explicit "no market research was done" framing in [[Market Opportunity (Illustrative Model)]]. It's possible the addressable premium segment is smaller than needed to support the capex base, or that residential buyers don't value the "30 New Ideas" feature set enough to pay the required premium over incumbent options.

**Mitigation direction:**
- Commission real market research (willingness-to-pay studies, segment sizing) before finalizing pricing and before [[The Ask]] is used in an actual raise — this vault deliberately did not do that work and flags it everywhere numbers appear.
- Consider a staged go-to-market (limited early releases, direct customer feedback loops) rather than committing full Factory 01 capacity to residential before demand is validated.
- Use the disaster-relief channel's government relationships as an early, lower-ambiguity revenue validation path while residential demand is being tested — tender requirements are more legible upfront than consumer willingness-to-pay.

## 5. Disaster-relief revenue is lumpy and tender-driven

**The risk:** Unlike a consumer sales channel, government emergency-services procurement is inherently lumpy — dependent on tender cycles, agency budget approvals, and disaster incidence, none of which produce a smooth, predictable revenue curve. [[Market Opportunity (Illustrative Model)]] explicitly warns against smoothing this into an annual run-rate for real financial planning. A single missed or delayed tender can create a material revenue gap in a given year, and building a cost base (including Factory 01 capacity commitments) around an assumed steady disaster-relief volume would be a planning error.

**Mitigation direction:**
- Model disaster-relief revenue with realistic lumpiness (scenario ranges, not point estimates) in any real financial plan — never smoothed.
- Keep Factory 01 capacity allocation flexible enough to absorb disaster-relief order lumpiness by flexing residential production up or down, rather than sizing the factory to disaster-relief peak or average demand alone.
- Build multiple concurrent agency relationships rather than depending on a single jurisdiction's tender cycle, to reduce single-point timing risk — see the jurisdiction-count variable in [[Market Opportunity (Illustrative Model)]].
- Treat early government contracts as reference-value wins (credibility, case studies, digital-twin field data) in addition to their direct revenue, since the revenue timing itself is uncertain.

## Cross-cutting note

Several of these risks compound each other if left unmanaged: certification delay (#3) extends the period before Factory 01 needs to prove itself (#1, #2), while market-adoption uncertainty (#4) and tender lumpiness (#5) both argue for keeping Factory 02+ capex (see [[Scaling Plan]]) firmly gated behind Factory 01 proof points rather than run in parallel.

## Related notes
[[The Thesis]] · [[Market Opportunity (Illustrative Model)]] · [[Unit Economics]] · [[Moat & Defensibility]] · [[Scaling Plan]] · [[The Ask]] · [[Investor Home]]
