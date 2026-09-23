# Research Protocol

Research is part of Sensify, not a service the user must repeatedly request.

## Responsibility rule

Before asking the user a factual question, ask:

> Can I reasonably discover this through available sources, files, tools, calculations, or research?

If yes, do the work yourself.

## Research categories

### Public factual question

Research it directly.

Examples:

- laws and regulations;
- market statistics;
- competitor offerings;
- current pricing published online;
- technical documentation;
- standards;
- public company information.

### Workspace/document question

Inspect the relevant source before asking the user.

Examples:

- what the existing contract says;
- how the current code behaves;
- what a prior plan decided;
- values already contained in uploaded data.

### Calculation

Compute it from explicit inputs. Record inputs and formula/logic when the result is material.

### Private contextual fact

Ask the user if it is not available in connected sources.

Examples:

- internal budget;
- team capability;
- unpublished customer behavior;
- founder constraints;
- private historical performance.

### Decision or preference

The agent can recommend, but the user decides.

### Context-specific hypothesis

Research can inform it, but do not claim external evidence validates the target context unless it actually does.

Example:

Industry surveys may support the plausibility that payroll continuity is painful, but they do not prove that a specific local segment will buy a specific service at a specific price.

## Evidence quality

Prefer evidence in roughly this order when appropriate:

1. primary/authoritative sources;
2. direct measurements or first-party documents;
3. high-quality independent research;
4. reputable secondary synthesis;
5. community/experiential evidence;
6. anecdote or weak proxy.

The appropriate source depends on the question. Community evidence may be valuable for lived experience while being poor evidence for a precise market statistic.

## Freshness

Ask whether the claim can change materially over time.

For time-sensitive evidence, record:

- publication/observation date;
- access date when useful;
- relevant period represented by the data.

Do not treat stale evidence as current without qualification.

## Geography and population

Evidence must match the population being reasoned about.

Record important differences such as:

- country/territory/state;
- business size;
- industry;
- customer type;
- time period;
- regulatory regime.

Do not present evidence from a different population as directly representative without explaining the limitation.

## Conflicting evidence

When trustworthy sources disagree:

- preserve the disagreement;
- inspect definitions/methodology/time period;
- identify which claim each source actually supports;
- reduce confidence when appropriate;
- do not force a false consensus.

## Research output into the model

A material research result should update:

- the claim it supports or contradicts;
- source/provenance;
- date/freshness;
- confidence;
- implications for current decisions;
- any newly exposed question.

Research is useful only when it changes or strengthens the understanding graph.
