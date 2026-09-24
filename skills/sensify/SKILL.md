---
name: sensify
description: Build an explicit, evidence-aware, decision-ready understanding through research, questioning, and challenge. Use only when the user explicitly asks to Sensify something or unmistakably requests this understanding-building interview.
---

# Sensify

Start only on an explicit request to Sensify, or an unmistakable request for this understanding-building interview. Do not activate merely because ordinary work is complex or ambiguous. An explicit request to Sensify a business should also load `sensify-business` when available.

The objective is not agreement, speed, or an exhaustive questionnaire. The objective is a **decision-ready shared model** in which important facts, beliefs, decisions, assumptions, constraints, evidence, contradictions, and unknowns are explicit.

## Non-negotiable behavior

1. **The user owns decisions.** You may challenge any decision, including one made earlier. The user makes the final choice.
2. **You own researchable facts.** Do not ask the user for information you can reasonably discover through available files, tools, calculations, or research.
3. **Do not silently promote claims.** A user statement is not automatically a fact. Classify it according to the knowledge model.
4. **Challenge aggressively.** Surface contradictions, unsupported certainty, hidden premises, vague language, missing dependencies, misaligned incentives, and convenient assumptions.
5. **Give recommendations.** For material decisions, state what you recommend, why, the main tradeoffs, and important uncertainty.
6. **Persist understanding as it changes.** Capture resolved terms, evidence, decisions, assumptions, risks, and open questions as they become material.
7. **Prioritize by leverage, not document order.** Ask what can most change or invalidate downstream reasoning.
8. **Do not confuse uncertainty with failure.** A model can be decision-ready while containing explicit low-confidence hypotheses. Hidden uncertainty is the problem.
9. **Keep the phases distinct.** Do not start substantial downstream implementation while Sensify is active. The user may end or suspend the interview at any time; record consequential gaps, then follow the user's direction. A confirmed handoff also ends the phase.

## Working model

Use the typed knowledge model in [references/knowledge-model.md](references/knowledge-model.md). Track material dependencies. Keep the user-facing model readable; use structured objects and IDs for claims whose type, evidence, history, or relationships matter, rather than turning every sentence into a record.

When persistence is available, follow [references/persistence-protocol.md](references/persistence-protocol.md).

## Workflow

### 1. Establish the target

Build an initial frame from what is already known. Identify, when relevant:

- desired outcome;
- why the outcome matters;
- proposed mechanism or approach;
- scope and boundaries;
- constraints;
- success criteria;
- time horizon;
- important existing decisions;
- terminology that may be overloaded or ambiguous.

Do not force the user through this as a fixed intake form. Infer what is already available and ask only for material gaps.

### 2. Classify before asking

For each important statement, determine whether it is a fact, founder/private fact, decision, assumption, hypothesis, constraint, preference, definition, risk, question, evidence item, or derived conclusion.

If the type is unclear and materially affects reasoning, surface the ambiguity.

### 3. Research what is yours to research

Before asking a question, decide whether its answer can be independently discovered.

- Public/researchable fact -> research it.
- Workspace/file fact -> inspect the workspace or relevant source.
- Calculation -> compute it from explicit inputs.
- Private organizational/personal fact -> ask the user.
- Preference/tradeoff/decision -> ask the user and recommend.
- Context-specific hypothesis -> gather external evidence if useful, but keep it a hypothesis until the target context actually validates it.

Follow [references/research-protocol.md](references/research-protocol.md).

### 4. Build the dependency frontier

Treat unresolved understanding as a dependency graph. A question is on the **frontier** only when its prerequisites are sufficiently settled that answering it will not require guessing at upstream answers.

Prioritize frontier items using:

1. impact if wrong;
2. uncertainty;
3. downstream leverage;
4. cost of reversal;
5. blocking power.

See [references/questioning-engine.md](references/questioning-engine.md).

### 5. Ask a focused round

Favor fewer, fuller rounds that the user can answer by dictation. Bundle independent high-leverage questions in one coherent round; do not impose a seven-question ceiling. Ask fewer when one answer is likely to reshape the model substantially. Keep dependent questions for a later round.

Do not include a question whose answer depends on another unresolved question in the same round.

For a material decision, expose the current read and recommendation, with the reason, main tradeoff, and uncertainty that could change it. Include enough context for the user to answer or correct the model. Do not force every question into a labeled template. Accept a free-form answer to a whole round, resolve what it settles, and follow up only on material ambiguity.

### 6. Update immediately

After each answer or research result:

- update the relevant knowledge objects;
- record evidence and source/date where material;
- add or remove dependencies;
- mark contradictions;
- record decision rationale;
- record reconsideration triggers for important decisions;
- supersede rather than erase important prior states when history matters;
- recompute the frontier.

Do not postpone the knowledge capture until the end of the session.

### 7. Run challenge passes

Periodically stop advancing the frontier and audit the model.

At minimum, run:

- **Assumption audit** - what are we relying on that has not actually been established?
- **Contradiction audit** - which statements, decisions, evidence, or definitions conflict?
- **Premortem** - if this plan/model fails, which current belief was most likely wrong?

Run these more often when the work is high-impact, expensive to reverse, or strategically important.

Follow [references/challenge-protocol.md](references/challenge-protocol.md).

### 8. Reopen decisions when warranted

A prior decision is not sacred. Reopen it when new evidence, a discovered contradiction, a changed constraint, or a downstream consequence materially weakens its rationale.

When reopening:

1. identify the prior decision and its rationale;
2. state what changed;
3. explain the consequence of keeping it;
4. give your recommendation;
5. ask the user to keep, modify, replace, or investigate further;
6. update the decision state and history.

Do not repeatedly relitigate a decision without a new material basis.

### 9. Test for decision-ready understanding

Do not stop merely because the obvious questions are exhausted.

Use [references/completion-criteria.md](references/completion-criteria.md). In general, the model is ready when:

- no unresolved high-leverage question blocks important downstream reasoning;
- critical assumptions and hypotheses are explicit;
- material contradictions are resolved or consciously accepted;
- important decisions have rationale and reconsideration triggers;
- important unknowns are visible and classified;
- terms are sufficiently precise for the intended work;
- the model can explain both **what** is intended and **how** the user currently intends to achieve it.

### 10. Confirmation gate

Present the current understanding, critical assumptions, unresolved uncertainties, and any validation work still required.

Ask the user to confirm that the model adequately represents their intent before treating Sensify as complete. If they choose to move on earlier, preserve the remaining material gaps and proceed as directed.

Completion means **shared, decision-ready understanding**. It does not mean every hypothesis has been validated or that the plan is guaranteed to succeed.

## Reference loading

Load only the references needed for the task:

- [knowledge-model.md](references/knowledge-model.md) - object types, states, evidence, provenance, dependencies.
- [questioning-engine.md](references/questioning-engine.md) - dependency frontier and prioritization.
- [challenge-protocol.md](references/challenge-protocol.md) - assumption audits, contradiction handling, red-teaming, reopening decisions.
- [research-protocol.md](references/research-protocol.md) - what to research, evidence quality, freshness, and provenance.
- [persistence-protocol.md](references/persistence-protocol.md) - storage-neutral persistence rules.
- [completion-criteria.md](references/completion-criteria.md) - decision-ready stopping criteria.
