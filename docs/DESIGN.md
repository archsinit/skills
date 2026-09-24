# Sensify Design

This document records the behavioral decisions behind the first Sensify implementation.

## Name

The skill is called **Sensify**: a verb meaning to make an incomplete or implicit body of thinking explicit, coherent, evidence-aware, and decision-ready.

## Problem being solved

LLMs often produce useful work by filling gaps in user instructions with plausible assumptions. In high-consequence knowledge work, those silent assumptions can become invisible inputs to strategy, requirements, operations, economics, or implementation.

Sensify inserts an explicit understanding-building phase before downstream execution.

## Locked design decisions

### Understand both outcome and mechanism

Sensify is not complete when it merely understands what the user wants. It must also understand how the user currently intends to achieve the outcome, including the major causal assumptions, constraints, dependencies, and tradeoffs behind that approach.

### Persistent knowledge is part of the method

Important understanding should survive the conversation. Sensify therefore maintains a persistent model as the interview/research progresses.

The logical model is storage-neutral. Project files, Notion, Obsidian, wikis, databases, or other stores are adapters rather than part of the reasoning method.

### The agent is expected to challenge

Sensify should not optimize for agreement. It has standing authority to challenge:

- current assumptions;
- hidden assumptions;
- prior decisions;
- causal claims;
- definitions;
- incentives;
- contradictions;
- weak evidence;
- premature solutions.

The user retains final decision authority.

### Decisions can be reopened

No prior choice becomes immune to challenge. A decision should be reopened when new evidence, changed constraints, contradictions, or downstream consequences materially weaken its rationale.

Sensify should not relitigate settled decisions without a new material basis.

### Recommendations are expected

The agent should not offload analytical work back onto the user. For material choices it should normally provide a recommendation with its basis, tradeoffs, confidence, and important uncertainty.

### Researchable facts belong to the agent

Do not ask the user to retrieve public information, inspect available project files, perform calculations, or look up material the agent can reasonably obtain itself.

Private facts and decisions remain with the user when they cannot be discovered through available connected sources.

### Facts and beliefs must be distinguished

The model must preserve the epistemic type of important statements. Core types include facts, private facts, decisions, assumptions, hypotheses, constraints, preferences, definitions, risks, evidence, questions, and derived conclusions.

A confident statement is not automatically a fact.

### Question ordering follows decision leverage

Sensify uses a dependency frontier rather than a document-order questionnaire.

A round should bundle independent, high-leverage questions whose prerequisites are sufficiently settled. Favor fewer, fuller dictation-friendly rounds; questions that depend on answers still open in the round wait for a later frontier.

Priority is driven by impact if wrong, uncertainty, downstream leverage, reversibility, and blocking power.

### Red-teaming is mandatory

The method periodically performs assumption audits, contradiction audits, and premortems. Business Sensify adds domain-specific red-team lenses for desirability, willingness to pay, economics, operations, incentives, compliance, concentration, scalability, and other failure modes.

### Sufficient understanding means decision-ready, not exhaustive

There will always be more questions.

Sensify can complete when there is no unresolved high-leverage issue silently blocking the intended next work and when important uncertainty is explicit.

Unknowns and unvalidated hypotheses can remain, provided the model records their importance, evidence state, consequences, and validation needs.

### Business output is a Business Understanding Model

`sensify-business` does not write the traditional business plan as its primary output.

It builds a canonical Business Understanding Model containing both:

1. how the business is intended to work; and
2. the epistemic state of the claims inside that model.

Business plans, presentations, financial models, operating plans, process maps, sales materials, and validation programs are downstream products that should consume the model.

### Validation planning is in scope; full execution is downstream

Sensify should identify which experiments, customer interviews, pilots, or other evidence are needed to test critical hypotheses. Executing a substantial validation program is a separate downstream workflow.

## Decisions from the follow-up interview

### Explicit invocation

Sensify starts only when the user names it or unmistakably requests its understanding-building interview. Complexity alone does not activate it. An explicit Sensify request about a business brings in the business specialization.

### Dictation-friendly interview rounds

Prefer fewer, fuller rounds of independent high-leverage questions. Do not impose a seven-question ceiling or a fixed labeled form on each question. Accept free-form answers, update the model, and ask a later round only for material gaps.

### Readable, evolving knowledge

Keep one canonical evolving model per business, project, or substantial initiative, with links to related models. The user should be able to read a coherent account; typed records are reserved for material claims that need provenance, dependencies, or history. Downstream work should read the model and write consequential discoveries back to it without automatically restarting Sensify.

### Storage direction

A growing knowledge system is the desired home. Notion is a preferred candidate because a ChatGPT plugin exists, but suitability of its read, update, link, and history capabilities is unverified. Keep the logical model storage-neutral and use an available local fallback until a connected backend is proven suitable. Maintain one declared source of truth per initiative.

### User-controlled exit

The user may end or suspend an interview before decision-ready completion. Preserve consequential gaps and follow their direction without labeling the model complete.

## Completion philosophy

The key distinction is:

> Sensify does not need to remove uncertainty. It needs to remove hidden uncertainty.

A statement such as "customers will pay for this" is unsafe when silently treated as fact.

The same statement is decision-usable when represented as a high-impact, low-confidence hypothesis with explicit supporting evidence, contradictory evidence, and a validation plan.
