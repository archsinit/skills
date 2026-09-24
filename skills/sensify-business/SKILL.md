---
name: sensify-business
description: Build a decision-ready Business Understanding Model through the Sensify interview. Use only when the user explicitly asks to Sensify a business or explicitly invokes Sensify on business work.
---

# Sensify Business

Use this skill after an explicit request to Sensify a business, whether the user names `sensify` or `sensify-business`. Do not start it automatically for an ordinary business request. If the environment can load skills compositionally, load `sensify` as the base skill. Otherwise enforce its core behavior directly: typed knowledge, autonomous research, dependency-frontier questioning, rigorous challenge, user-owned decisions, recommendations, persistence, and decision-ready completion.

The deliverable is a **Business Understanding Model**. It is not a traditional business plan and it is not a pitch deck.

The goal is to make the business understandable enough that future work can consume a coherent model instead of rebuilding founder intent from scattered conversations. Keep one evolving model for each business, with a readable overview and structured records for material claims and decisions.

## Core stance

Treat the proposed business as a set of interdependent claims, decisions, and mechanisms that must cohere.

Do not assume that because a founder has an answer, the answer is established.

In particular:

- distinguish customer/problem claims from validated customer evidence;
- distinguish strategic decisions from market facts;
- distinguish constraints from preferences;
- distinguish a plausible revenue model from proven willingness to pay;
- distinguish a price from viable unit economics;
- distinguish operational possibility from scalable delivery;
- distinguish legal assumptions from verified regulatory requirements;
- distinguish a useful feature from a reason to switch/buy;
- distinguish market size from reachable customers;
- distinguish confidence from evidence.

## Persistent output

Maintain the Business Understanding Model using [references/business-understanding-model.md](references/business-understanding-model.md).

When a file backend is the active persistence method, prefer `BUSINESS-UNDERSTANDING.md` using [assets/BUSINESS-UNDERSTANDING.template.md](assets/BUSINESS-UNDERSTANDING.template.md). When a connected knowledge system such as Notion is selected, maintain the same logical model there and verify that it can support the needed reads, updates, links, and history before treating it as canonical.

Do not fill every section mechanically. Build the model in the order that reduces the most consequential uncertainty.

## Business domains

The model should eventually cover the material parts of the business:

1. purpose and founder outcomes;
2. customer and buying system;
3. problem and current alternatives;
4. market and environment;
5. competition and status quo;
6. value proposition;
7. offering and boundaries;
8. revenue model and pricing;
9. sales and acquisition;
10. delivery and operations;
11. economics and cash requirements;
12. organization and resources;
13. technology and data;
14. legal, regulatory, tax, and compliance considerations;
15. risks and failure modes;
16. validation and evidence;
17. execution sequence and milestones.

Use [references/business-domains.md](references/business-domains.md) for prompts and failure modes within each domain.

## Interview behavior

### Start with leverage, not the table of contents

Establish enough context to identify the business's load-bearing beliefs.

Typical early candidates include:

- who has the problem;
- whether the problem is severe/frequent enough to motivate action;
- what the customer does today;
- why the proposed solution is meaningfully better than the status quo;
- who pays and why;
- whether delivery can be economically and operationally viable;
- whether regulation or dependencies could make the model infeasible.

Do not assume this exact order. Use the Sensify frontier and priority rules.

### Research automatically

Research public facts that materially affect the business without asking permission each time.

Examples:

- competitors and alternatives;
- published pricing;
- regulations;
- market structure;
- relevant labor/tax rules;
- software capabilities;
- demographic/business population data;
- industry benchmarks when suitable.

Record sources, dates, geography/population, and limitations for material external claims.

### Challenge founder assumptions explicitly

When the founder says something such as:

- "customers need this";
- "there is no competition";
- "we can charge X";
- "local service is our advantage";
- "salespeople will be motivated by this commission";
- "this will scale";
- "the software can handle it";

classify the statement before accepting it. It may be a decision, hypothesis, assumption, or private fact rather than a fact.

### Recommendations are expected

For material strategic and operating decisions, recommend a direction and show:

- basis;
- tradeoffs;
- confidence;
- missing evidence;
- what would cause you to change the recommendation.

The founder decides.

## Mandatory red-team passes

Use [references/red-team-framework.md](references/red-team-framework.md).

At minimum, run red-team passes against:

- customer/problem desirability;
- willingness to pay and switching behavior;
- competitive/status-quo alternatives;
- unit economics and cash dynamics;
- operating capacity and failure modes;
- incentives and governance;
- regulatory/legal feasibility;
- concentration/key-person dependencies;
- scalability assumptions;
- founder goals and business-model fit.

A red-team pass should create or update risks, assumptions, evidence needs, and frontier questions. It should not be performative skepticism.

## Economics discipline

Use [references/economics-framework.md](references/economics-framework.md) when economics become decision-relevant.

Do not allow a business to appear economically coherent merely because it has a price and a revenue forecast.

Where relevant, understand:

- revenue unit and timing;
- variable delivery costs;
- commissions/partner shares;
- support/servicing burden;
- gross/contribution margin;
- customer acquisition costs;
- retention/churn assumptions;
- implementation/onboarding cost;
- working capital/timing gaps;
- fixed operating cost;
- cash runway and break-even conditions;
- economics under plausible downside scenarios.

Use ranges/scenarios when precision is not justified.

## Validation discipline

Use [references/validation-framework.md](references/validation-framework.md).

The skill should identify what evidence or experiment is needed to test important hypotheses, but it should not automatically execute an entire validation program as part of the Sensify interview.

A future/customer-discovery or research skill may execute those tests.

## Completion

Business Sensify is complete when the model is **decision-ready**, not when the business is fully proven.

Use [references/completion-criteria.md](references/completion-criteria.md).

At handoff, the Business Understanding Model should make clear:

- what the business is trying to accomplish;
- how it is intended to work;
- who it serves and why they would act;
- how value is created, delivered, and captured;
- which claims are facts versus assumptions/hypotheses;
- which decisions have been made and why;
- whether the economics are at least internally coherent;
- major regulatory/operational dependencies;
- critical risks;
- what remains to be validated;
- which unresolved questions are intentionally deferred.

Present the critical assumptions, major risks, open questions, and any decisions you still recommend reconsidering. Ask the user to confirm that the model accurately represents their intended business before declaring the Sensify phase complete. If the user chooses to move on earlier, preserve the consequential gaps without claiming completion and follow their direction.

## Handoff contract

Downstream business skills should consume the Business Understanding Model first.

They should not restart generic founder discovery. Ask new questions only when:

- the requested output needs information the model does not contain;
- an existing item is too uncertain for the downstream decision;
- the downstream work exposes a contradiction;
- a material fact has become stale.

Write consequential discoveries, changed assumptions, and reopened decisions back to the canonical model when possible. This does not itself restart the Sensify interview.
