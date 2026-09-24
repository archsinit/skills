# Knowledge model

Record material understanding as claims whose meaning and basis remain clear to a later reader. Type a claim when the distinction affects a decision; do not turn ordinary prose into a database.

## Claim types

| Type | Use it for |
|---|---|
| `FACT` | Externally verifiable information supported by evidence. Note its source and date when it may change. |
| `PRIVATE_FACT` or `FOUNDER_FACT` | Information supplied by the user or organization that available sources cannot independently verify, such as budget or team capacity. |
| `DECISION` | A choice among alternatives. Record why it was made, what it gives up, who owns it, and what could cause reconsideration when those details matter. |
| `ASSUMPTION` | A premise the model relies on without adequate evidence or validation. Make hidden premises visible. |
| `HYPOTHESIS` | A claim deliberately left open for testing. State what would support or contradict it. Research elsewhere may inform it without validating this setting. |
| `CONSTRAINT` | A boundary the work must respect unless changed, such as a legal requirement, deadline, or non-negotiable choice. |
| `PREFERENCE` | Something desirable but open to tradeoff. Do not silently treat it as a constraint. |
| `DEFINITION` | The agreed meaning of a term that might otherwise be vague or used differently. |
| `RISK` | A plausible adverse condition. Capture its cause, consequence, detectability, response, and threatened claims or decisions where useful. Avoid invented probabilities. |
| `QUESTION` | An unresolved matter requiring research, user input, validation, or a decision. Track what must be settled first and what it blocks. |
| `EVIDENCE` | A source, observation, calculation, document, or experiment that supports or challenges a claim. Link it to that claim. |
| `DERIVED_CONCLUSION` | A conclusion drawn from stated premises or calculations. Revisit it when a premise changes. |

Confidence describes the quality of a claim's current basis, not whether it is true. Use `high` for strong relevant evidence with little material uncertainty; `medium` when useful evidence still leaves an important gap; `low` for weak or indirect support; and `unknown` when there is no sound basis. Do not invent numeric probabilities. Importance describes the damage if the claim is wrong. Reserve `critical` for claims able to invalidate the central outcome or mechanism.

## Record only useful fields

The following is a logical schema, not a form to complete for every claim:

```yaml
id: K-001
statement: "..."
type: FACT | PRIVATE_FACT | DECISION | ASSUMPTION | HYPOTHESIS | CONSTRAINT | PREFERENCE | DEFINITION | RISK | QUESTION | EVIDENCE | DERIVED_CONCLUSION
status: ...
confidence: high | medium | low | unknown
importance: critical | high | medium | low
source:
  kind: user | research | document | calculation | experiment | observation | tool
  reference: "..."
  observed_at: "YYYY-MM-DD"
evidence_for: []
evidence_against: []
depends_on: []
blocks: []
contradicts: []
rationale: "..."
alternatives: []
tradeoffs: []
reconsider_if: []
validation_required: true
owner: user | agent | shared | external
notes: "..."
```

Use a status that fits the type:

- Decisions: `proposed`, `decided`, `validated`, `reopened`, `superseded`, `invalidated`. `Validated` means later evidence supports the rationale, not that the choice is permanently correct.
- Assumptions and hypotheses: `untested`, `partially-supported`, `supported`, `contradicted`, `unknown`, `retired`.
- Questions: `open`, `researching`, `blocked`, `answered`, `deferred`, `not-material`.
- Facts and evidence, when useful: `current`, `stale`, `superseded`, `disputed`.

## Preserve where claims came from

Keep user statements, documents, outside research, calculations, and inference distinct. Do not combine them into a single fact unless the resulting claim is supported. Date claims that may go stale; record the geography, population, and period when those limits matter. When credible evidence conflicts, retain both sides and lower confidence as appropriate.

Treat contradictions as part of the model. Link the conflicting claims and determine whether the cause is terminology, outdated information, a changed decision, incompatible constraints, or disputed evidence. Resolve the conflict or leave it visibly open. Do not erase it by rewriting the history.

For consequential decisions, record a reconsideration trigger. A cost crossing a threshold, a changed regulation, a failed dependency, or evidence that users behave differently can justify reopening the choice. Without such a trigger, a later agent may either accept a weak decision forever or keep questioning it without cause.
