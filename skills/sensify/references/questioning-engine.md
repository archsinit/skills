# Questioning Engine

Sensify is not a fixed questionnaire. It is a dependency-aware elicitation process.

## The understanding graph

Represent the work as a graph of material knowledge objects and unresolved questions.

An unresolved question can depend on:

- another user decision;
- a private fact;
- external research;
- a calculation;
- a definition;
- an earlier unresolved contradiction.

A question belongs on the current **frontier** only when its prerequisites are settled enough that answering it will not require guessing at upstream answers.

## Why frontier ordering matters

Asking downstream questions too early causes accidental commitments.

Example:

- Q1: Which customer segment are we targeting?
- Q2: What onboarding workflow should that customer receive?

If the customer segment is unresolved, Q2 should normally wait. Otherwise the user and agent may design a workflow for a customer that is later discarded.

## Priority factors

Prioritize frontier questions using qualitative judgment across five dimensions.

### 1. Impact if wrong

How much damage would a wrong answer cause?

High-impact answers can invalidate strategy, architecture, economics, compliance, feasibility, or major downstream work.

### 2. Uncertainty

How weak is the current basis?

A high-impact question with high uncertainty generally deserves early attention.

### 3. Downstream leverage

How many other choices depend on this answer?

Resolve high-leverage branching decisions before details.

### 4. Cost of reversal

How expensive, slow, disruptive, or politically difficult would it be to change later?

Hard-to-reverse choices deserve more scrutiny before commitment.

### 5. Blocking power

Does the unresolved issue prevent useful reasoning elsewhere?

Questions that unblock multiple branches should move forward.

## Round size

Favor fewer, fuller rounds. Ask a coherent batch of independent, high-leverage questions that the user can answer in one dictated response; a round may exceed seven questions when that reduces repetition without burying a consequential choice.

Use fewer when:

- one decision is likely to reshape most of the model;
- the question is cognitively demanding;
- the answer may invalidate assumptions behind the rest of the frontier;
- a contradiction needs to be resolved before useful progress.

Use a larger batch only when the questions belong on the current frontier and none depends on an answer still open in the same round. Group related questions, keep each concise, and let the user answer in free form.

Do not dump the full internal backlog on the user.

## Question construction

A strong question contains enough analysis that the user can decide rather than perform the agent's reasoning work. For a material choice, briefly give the current read, recommendation, basis, and consequential tradeoff or uncertainty. Use labels only when they make a complex choice easier to answer. The user should be able to answer a whole round naturally, disagree, or provide missing context.

## Avoid lazy questions

Do not ask:

- "What do you think?" when a narrower decision can be formulated;
- "Can you tell me about X?" when specific unknowns are identifiable;
- for facts available in the workspace or public sources;
- multiple questions that secretly depend on the first answer;
- implementation details before the objective or governing constraints are understood;
- questions whose only purpose is to fill a document section.

## Recommendations are part of elicitation

A recommendation exposes the agent's current mental model. The user can correct not only the answer but the reasoning behind it.

Recommendations should distinguish:

- evidence;
- inference;
- preference/tradeoff;
- uncertainty.

Do not use confidence theater. A firm tone is not a substitute for strong evidence.

## Recompute after every meaningful answer

The frontier is dynamic.

A single answer may:

- settle several questions;
- create new questions;
- invalidate old questions;
- change priority;
- reveal an assumption;
- create a contradiction;
- trigger research;
- reopen an earlier decision.

Do not continue mechanically through a prewritten questionnaire after the model changes.
