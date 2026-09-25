# Skills

This repository contains reusable Agent Skills for rigorous knowledge work.

**Sensify** turns incomplete or contradictory thinking into an evidence-aware, decision-ready model. **Define Requirements** carries an established product definition into testable release behavior.

Invoke it explicitly, for example with `$sensify` or `$sensify-business`. Sensify does not start automatically for an ordinary request.

## Why Sensify exists

LLMs are good at filling gaps. That is useful until the gaps contain assumptions the user never intended to make. In complex knowledge work, a plausible hidden assumption can quietly become a requirement, a strategy, a financial premise, or an operating constraint.

Sensify changes the agent's job from "infer the missing pieces and proceed" to:

1. build an explicit model of what is known, believed, decided, constrained, and still unknown;
2. research facts the agent can discover independently;
3. challenge unsupported assumptions and contradictions;
4. ask the user only for private facts, judgments, preferences, and decisions;
5. persist the evolving understanding;
6. finish when the model is decision-ready, not merely when the conversation runs out of questions, while allowing the user to move on earlier with consequential gaps recorded.

## Skills

### `sensify`

The domain-neutral reasoning primitive. It can be used for software, strategy, operations, product work, research, process design, planning, requirements elicitation, and other knowledge work.

It defines:

- knowledge typing and epistemic status;
- dependency/frontier-based questioning;
- research responsibility;
- aggressive assumption and contradiction challenges;
- recommendation format;
- persistence behavior;
- completion and confirmation gates.

### `sensify-business`

A business and startup specialization built on top of `sensify`.

It produces and maintains a **Business Understanding Model** rather than a conventional business plan. The model records the business itself plus the epistemic state of the claims inside it: facts, founder facts, decisions, assumptions, hypotheses, constraints, risks, evidence, and unresolved questions.

Downstream skills can later turn that model into business plans, presentations, financial models, process maps, operating documents, sales material, validation programs, or implementation work without reconstructing the founder's intent from scratch.

### `define-requirements`

A focused bridge from a settled product definition to a first-release requirements document. It traces user and operator journeys, probes consequential failure and recovery cases, distinguishes confirmed behavior from open decisions, and checks that each requirement can be verified. It leaves screen layouts, technical architecture, and task sequencing to later work.

## Repository layout

```text
skills/
├── sensify/
│   ├── SKILL.md
│   ├── references/
│   └── assets/
├── sensify-business/
│   ├── SKILL.md
│   ├── references/
│   └── assets/
└── define-requirements/
    └── SKILL.md

tests/
├── sensify/
└── sensify-business/
```

The main `SKILL.md` files are intentionally compact. Detailed behavior is split into references so agents can load only what they need.

## Core design principles

- **The user owns decisions.** The agent may challenge any decision, including old ones, but the user remains the decision-maker.
- **The agent owns researchable facts.** Do not ask the user for information the agent can reasonably discover itself.
- **Agreement is not the goal.** The agent should surface weak logic, contradictions, hidden assumptions, missing dependencies, and inconvenient evidence.
- **Uncertainty is acceptable; hidden uncertainty is not.** A low-confidence hypothesis can remain in the model if it is explicitly labeled and its consequences are understood.
- **Question priority follows leverage, not document order.** High-impact, uncertain, hard-to-reverse, blocking questions come first. Related independent questions can be bundled into fuller, dictation-friendly rounds.
- **Persistence is part of reasoning.** Important knowledge should be captured as it is established rather than reconstructed later from conversation history.
- **The output is a model, not a transcript.** Sensify stores what the current understanding is, why it is believed, what contradicts it, and what could cause it to be reconsidered.

## Persistence

Sensify is storage-neutral. Maintain one readable, evolving model per initiative and link related models. A deployment may persist it in project files, Notion, Obsidian, a wiki, a database, or another knowledge system. The logical schema is the same regardless of backend. Downstream work should read the model and write consequential discoveries back.

When no connected backend has been verified and a writable workspace exists, the included file templates provide a local fallback. Notion is a candidate for a growing knowledge system, pending verification of the connection's read and write capabilities.

## Status

This repository contains Sensify, its business specialization, and Define Requirements. Storage adapters and other downstream skills remain future work.

## Attribution

Sensify was inspired in part by Matt Pocock's `grilling`, `grill-me`, `grill-with-docs`, and `domain-modeling` skills. See [ATTRIBUTION.md](ATTRIBUTION.md).

No repository license has been selected yet.
