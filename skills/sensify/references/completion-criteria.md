# Completion Criteria

Sensify does not aim for exhaustive knowledge. It aims for **decision-ready understanding**.

The process is complete when the remaining uncertainty is explicit and does not silently block the intended next work.

## Completion test

Evaluate the model across the following dimensions.

### Outcome clarity

- The intended outcome is explicit.
- The reason it matters is understood enough to resolve tradeoffs.
- Success criteria are sufficiently concrete for the intended next step.

### Mechanism clarity

- The model describes not only what the user wants but how they currently intend to achieve it.
- Major dependencies and causal assumptions in that mechanism are visible.

### Epistemic clarity

- Material claims are correctly distinguished as facts, private facts, assumptions, hypotheses, decisions, constraints, preferences, risks, or derived conclusions.
- Important evidence and provenance are recorded.
- Confidence is not overstated.

### Decision clarity

- Material decisions are explicit.
- Important decisions have rationale and tradeoffs.
- Hard-to-reverse decisions have appropriate scrutiny.
- Reconsideration triggers exist where useful.

### Assumption clarity

- Critical assumptions are explicit rather than embedded in prose.
- High-impact weak assumptions have been challenged.
- Validation/research needs are identified.

### Contradiction clarity

- Material contradictions are resolved, explained as temporal/superseded, or consciously accepted as unresolved.
- Definitions do not conflict in ways that would distort downstream work.

### Dependency clarity

- No unresolved high-leverage question blocks major downstream reasoning.
- Remaining open questions are categorized as validation work, low-priority detail, externally blocked, or deliberately deferred.

### Risk clarity

- Plausible failure modes that could invalidate the model have been considered.
- Material risks are visible and linked to the beliefs/decisions they threaten.

### Persistence clarity

- The current model is stored in the selected canonical backend when persistence is available.
- The persistent model is understandable without rereading the entire conversation.

## What does not block completion

Sensify can complete with:

- hypotheses that require future experiments;
- external events that cannot yet be known;
- deliberately deferred low-leverage choices;
- risks that cannot be eliminated;
- disagreement where the user consciously accepts the tradeoff;
- unknown numeric values that are not required for the next decision.

These must be explicit.

## What should block completion

Do not declare completion while any of these remain hidden or unresolved:

- a critical assumption masquerading as fact;
- a contradiction that changes the meaning of the plan;
- an undefined term that causes different interpretations;
- an unresolved decision on which major downstream work depends;
- a researchable fact being delegated to the user;
- a hard constraint that conflicts with the proposed mechanism;
- a core causal claim with no acknowledged evidence or validation need.

## Final confirmation

Before handoff, present a compact completion view:

- current understanding;
- critical decisions;
- critical assumptions/hypotheses;
- material risks;
- unresolved questions;
- validation/research still required;
- any decisions you still recommend reconsidering.

Ask the user to confirm that this is an adequate representation of their intent.
