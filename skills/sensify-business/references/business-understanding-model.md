# Business Understanding Model

The Business Understanding Model is a persistent, evidence-aware representation of how the business is intended to work.

It combines two layers:

1. **Business structure** - customers, problem, offer, economics, operations, etc.
2. **Epistemic structure** - which statements are facts, private facts, decisions, assumptions, hypotheses, constraints, risks, evidence, and unresolved questions.

The second layer prevents a polished business narrative from hiding weak premises.

Maintain one evolving model per business. Lead with a readable account of its purpose, customer, mechanism, important decisions, and present state. Use typed records for claims whose evidence, uncertainty, dependencies, or history affect decisions. Link related initiatives without merging their assumptions into this business as facts.

## Model sections

### 1. Purpose and founder outcomes

Capture:

- why this business should exist;
- founder objectives;
- desired personal/company outcomes when relevant;
- success criteria;
- time horizon;
- non-negotiable constraints;
- acceptable/unacceptable tradeoffs.

Challenge conflicts between founder goals and the business model. A model optimized for rapid scale may conflict with a founder preference for low complexity or low capital exposure.

### 2. Customer and buying system

Distinguish:

- customer segment;
- user;
- buyer/economic buyer;
- decision maker;
- approver;
- influencer;
- blocker;
- payer;
- beneficiary.

For B2B businesses, understand the account characteristics that make a prospect qualified.

Avoid vague segments such as "small businesses" unless the definition is decision-useful.

### 3. Problem

Capture:

- job/problem being addressed;
- frequency;
- severity;
- trigger events;
- current workaround;
- cost/consequence of the status quo;
- who experiences the pain;
- who notices it;
- what evidence shows it exists;
- what would make it not worth solving.

Do not confuse founder-observed inconvenience with customer purchase motivation.

### 4. Market and environment

Capture only market information that changes decisions.

Possible elements:

- number/type of reachable customers;
- geography;
- industry structure;
- trends;
- labor conditions;
- regulatory environment;
- channel structure;
- purchasing norms;
- technology adoption;
- market timing.

Do not use top-down market size as a substitute for understanding reachable demand.

### 5. Alternatives and competition

Competition includes:

- direct providers;
- adjacent providers;
- internal staff;
- spreadsheets/manual processes;
- bundled software;
- doing nothing;
- postponing the decision.

Capture why a customer would switch from each meaningful alternative and what switching costs exist.

### 6. Value proposition

Capture:

- outcome promised;
- target customer;
- relevant problem;
- differentiation;
- proof/credibility;
- reason to act now;
- reason the outcome matters economically or operationally.

A feature is not automatically a value proposition.

### 7. Offering

Capture:

- products/services;
- included scope;
- excluded scope;
- service levels;
- onboarding/implementation;
- customer responsibilities;
- dependencies;
- optional/add-on services;
- quality boundaries;
- termination/offboarding.

### 8. Revenue model and pricing

Capture:

- who pays;
- what unit they pay for;
- pricing structure;
- billing cadence;
- setup/implementation fees;
- minimums;
- discounts;
- contracts/commitments;
- expansion/contraction drivers;
- refund/credit exposure;
- expected price sensitivity;
- evidence for willingness to pay.

Treat pricing decisions separately from willingness-to-pay hypotheses.

### 9. Sales and acquisition

Capture:

- how prospects are identified;
- channel/source;
- qualification;
- sales process;
- buyer journey;
- proof required;
- sales cycle;
- roles/owners;
- compensation/incentives;
- conversion assumptions;
- acquisition costs;
- referral/partner mechanics;
- pipeline constraints.

Challenge incentives that optimize signed deals at the expense of fit, margin, retention, compliance, or service quality.

### 10. Delivery and operations

Capture:

- value-delivery workflow;
- onboarding;
- recurring operations;
- exception handling;
- roles and handoffs;
- customer inputs;
- capacity constraints;
- quality controls;
- continuity/backup;
- vendor dependencies;
- service recovery;
- offboarding;
- operational metrics.

Ask what happens when the normal process fails.

### 11. Economics and cash

Capture:

- revenue drivers;
- variable cost drivers;
- implementation/onboarding costs;
- commissions/partner shares;
- gross/contribution margin logic;
- acquisition cost;
- retention/churn;
- support/servicing cost;
- fixed costs;
- payment timing;
- working capital;
- cash requirements;
- break-even conditions;
- sensitivity to key assumptions.

Use the economics framework rather than relying only on a forecast.

### 12. Organization and resources

Capture:

- founder roles;
- employees/contractors;
- critical capabilities;
- hiring needs;
- partners/vendors;
- physical resources;
- key-person dependencies;
- decision rights;
- accountability.

### 13. Technology and data

Capture:

- systems required;
- build/buy decisions;
- integrations;
- data sources;
- data ownership;
- privacy/security requirements;
- access controls;
- backups/recovery;
- automation;
- manual fallback;
- vendor lock-in/dependency;
- technical feasibility assumptions.

### 14. Legal, regulatory, tax, and compliance

Capture the requirements relevant to the actual geography, industry, customer, service, employment model, and data handled.

Possible areas:

- licenses/registrations;
- contracts;
- employment law;
- taxes;
- payroll obligations;
- privacy/data protection;
- record retention;
- professional licensing;
- insurance;
- industry-specific rules;
- liability allocation.

Material claims in this section should be researched from appropriate authoritative sources and dated.

### 15. Risks and failure modes

Capture risks that threaten:

- demand;
- economics;
- operations;
- quality;
- compliance;
- security;
- cash;
- reputation;
- key people;
- vendors;
- concentration;
- customer retention;
- execution timing.

Link each risk to the assumptions/decisions it threatens.

### 16. Validation and evidence

Capture:

- what has actually been demonstrated;
- which evidence supports each critical claim;
- which high-impact hypotheses remain untested;
- validation priority;
- proposed experiments/interviews/research;
- evidence that would cause a decision to change.

### 17. Execution sequence

Capture only enough execution planning to understand feasibility and dependencies during Sensify.

Include:

- current stage;
- critical milestones;
- sequencing constraints;
- gating decisions;
- dependencies;
- earliest validation steps;
- items intentionally deferred to downstream planning.

Do not let implementation planning consume the interview before the business model is understood.

## Cross-cutting registers

The model should make the following easy to inspect regardless of business section:

- decision register;
- assumptions/hypotheses register;
- evidence register;
- risk register;
- contradiction log;
- open question backlog;
- validation agenda;
- definitions/glossary.

These may be represented as dedicated tables or generated views over the same underlying knowledge objects.
