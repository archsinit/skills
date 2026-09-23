# Sensify Knowledge Model

Sensify stores understanding as typed knowledge objects rather than undifferentiated notes.

The purpose of typing is epistemic hygiene: future agents should know not only *what the model says* but *what kind of claim it is, why it is believed, and how strongly it should be trusted*.

## Object types

### FACT

Externally verifiable information supported by evidence.

Examples:

- a published regulation;
- a product's documented feature;
- a market statistic from an identified source;
- a date or contractual term found in a source document.

A fact should carry source and freshness metadata when either can affect downstream use.

### FOUNDER_FACT / PRIVATE_FACT

Information supplied by the user or organization that may be true in their context but is not independently verifiable through available sources.

Examples:

- available budget;
- current team capacity;
- an internal customer count;
- a private operational limitation.

Do not relabel these as external FACTs merely because the user states them confidently.

### DECISION

A deliberate choice among alternatives.

Important decisions should record:

- rationale;
- alternatives considered;
- tradeoffs accepted;
- decision owner;
- dependencies;
- reconsideration triggers;
- current status.

### ASSUMPTION

Something the model is currently relying on without adequate evidence or explicit validation.

An assumption may have been made consciously or unconsciously. Sensify should actively convert hidden assumptions into explicit ASSUMPTION objects.

### HYPOTHESIS

A claim intentionally framed for validation.

Hypotheses should state what evidence would support or contradict them. External research can inform a hypothesis without necessarily validating it in the target context.

### CONSTRAINT

A boundary that the work must respect unless explicitly changed.

Examples:

- legal limitations;
- budget ceilings;
- geographic scope;
- time deadlines;
- required technology;
- non-negotiable user choices.

Distinguish actual constraints from preferences presented as constraints.

### PREFERENCE

A desired property that can be traded off if needed.

Preferences should not silently become hard constraints.

### DEFINITION

The canonical meaning of a term within the model.

Definitions are especially important when a term is overloaded, vague, domain-specific, or used differently by different stakeholders.

### RISK

A plausible adverse condition or failure mode with meaningful impact.

A risk should identify, where useful:

- trigger/cause;
- consequence;
- likelihood or uncertainty;
- detectability;
- mitigation or response;
- related assumptions/decisions.

Avoid false precision when probability is unknown.

### QUESTION

An unresolved issue that may require research, user input, validation, or a decision.

Questions should carry dependencies and priority so the interview engine can determine whether they belong on the current frontier.

### EVIDENCE

A source, observation, calculation, experiment, interview result, file, or other item that supports or contradicts a claim.

Evidence should not be stored without the claim(s) it bears on.

### DERIVED_CONCLUSION

A conclusion produced from explicit premises, calculations, or combined evidence.

Record the premises. If a premise changes, the conclusion should be reconsidered.

## Suggested object fields

Use only fields that add value; this is a logical schema, not a requirement to fill every field for every object.

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

## States

Different object types use different useful states.

### Decisions

- `proposed`
- `decided`
- `validated` - later evidence supports the decision's underlying rationale; do not interpret this as permanently correct
- `reopened`
- `superseded`
- `invalidated`

### Assumptions and hypotheses

- `untested`
- `partially-supported`
- `supported`
- `contradicted`
- `unknown`
- `retired`

### Questions

- `open`
- `researching`
- `blocked`
- `answered`
- `deferred`
- `not-material`

### Facts/evidence

When relevant, track:

- `current`
- `stale`
- `superseded`
- `disputed`

## Confidence

Confidence is not the same as truth.

Use confidence to communicate the quality of the current basis:

- **High** - strong, relevant evidence and low material uncertainty.
- **Medium** - useful evidence exists, but important uncertainty remains.
- **Low** - weak, indirect, incomplete, or highly context-dependent evidence.
- **Unknown** - there is not yet a reasonable basis for confidence.

Do not invent numeric probabilities merely to make the model look rigorous.

## Importance

Importance reflects the damage or downstream distortion if the item is wrong or misunderstood.

Use `critical` sparingly for items capable of invalidating the core objective, business model, architecture, economics, legal feasibility, or another central dependency.

## Provenance rules

1. Preserve whether a claim came from the user, external evidence, a document, a calculation, or inference.
2. Do not merge claims from different provenance into a single "fact" unless the resulting statement is genuinely supported.
3. For time-sensitive facts, store the date observed or published.
4. For geographically or population-specific evidence, record the relevant geography/population.
5. When evidence conflicts, store both sides and mark the conflict rather than choosing silently.

## Contradictions

A contradiction is first-class knowledge.

When two material items conflict:

- link them;
- explain the nature of the conflict;
- determine whether it is a terminology problem, outdated information, a changed decision, incompatible constraints, or genuinely conflicting evidence;
- resolve it or keep it explicitly open.

Never erase a contradiction by rewriting history without explanation.

## Reconsideration triggers

For important decisions, record what future condition should cause the decision to be reopened.

Examples:

- a cost exceeds a threshold;
- regulation changes;
- target customer behavior differs from the assumption;
- a dependency becomes unavailable;
- a performance requirement cannot be met;
- new evidence undermines the original rationale.

This lets future agents challenge decisions intelligently instead of either treating them as permanent or relitigating them arbitrarily.
