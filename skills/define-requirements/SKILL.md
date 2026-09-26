---
name: define-requirements
description: Turn a settled product definition into testable release requirements. Resolve all non-UI/UX requirements before UI/UX, the final requirements pass. Use before architecture or implementation, not for initial product discovery.
---

# Define requirements

Produce a requirements record that lets later stages proceed without guessing what the product must do. Start with the settled product definition and decision history. Do not reopen a choice unless a contradiction, missing case, or new evidence makes it necessary.

## Map the whole journey

List each actor's path from first entry to the promised result and later use. Include access, creating and resuming work, approval, public and private states, changes, withdrawal, failure, and recovery where they apply. For each handoff, record the normal path, consequential alternatives, what can fail, and the decision or requirement that covers it. Mark gaps. A feature list or a set of screen mockups cannot establish end-to-end coverage.

Check concerns that cross the journey: privacy, security, accessibility, evidence or content integrity, reliability, data retention, operating cost, and recovery. Include a concern only when the product needs it, but do not omit a necessary transition because it seems routine or technical.

## Settle non-UI/UX requirements first

Work through the product's editorial or business rules, actor responsibilities, data and content lifecycle, access, integrations, rights, failure behavior, operating constraints, and release and recovery requirements before asking about UI/UX. Trace each decision back through the full journey. Separate an accepted decision from a proposal, an assumption that needs validation, and an implementation choice.

Research facts that can be established from sources. Ask the user for consequential judgments the sources cannot settle. Give a recommendation, the effect of each choice, and a manageable group of independent questions. Record each answer before moving on. Do not turn the recommendation into a decision without the user's answer. If a decision affects several steps, update all of them.

Use text or a simple flow to explain non-UI/UX choices. Defer screen layouts, navigation, interaction details, visual style, responsive treatment, and UI prototypes until the other requirements are settled. When a behavior has a visible consequence, record the behavior now and leave its presentation for the UI/UX pass.

## Do UI/UX last

Once the non-UI/UX decisions are complete, work through the reader and operator experience from entry to completion and recovery. Settle screens, navigation, controls, content presentation, empty and error states, accessibility, responsive behavior, and visual direction. Build viewable prototypes where seeing a choice would help the user judge it. Revisit the complete journey after the UI/UX pass; a polished screen can still hide a missing handoff.

## Write and check the contract

Keep one canonical requirements document or update the existing one. Give each substantive requirement a stable ID. State the actor, condition, observable behavior or constraint, and a check that could fail in a broken product. Link it to the product decision or user answer. Include meaningful exceptions and recovery paths. Set measurable quality thresholds when the product needs them; otherwise mark the threshold open. Keep future scope separate from launch behavior.

Trace every first-release promise and journey transition to a requirement or an explicit open decision. Trace requirements back to product goals or decisions. Review scenarios that cross private and public states, including failure and recovery. Remove duplicates and speculative scope.

State readiness accurately. **Requirements-ready** means product behavior and UI/UX choices are settled, with technical choices assigned to their later stage. **Build-ready** means no product, design, technical, or operating decision remains for the builder to guess; record each answer or an explicit delegation with constraints and an owner. Do not call the package complete while a consequential transition is missing or an assumption is presented as fact.

Give the user a compact account of settled decisions, remaining gaps, and readiness. If work stops early, preserve the draft and identify the next unresolved decision.

