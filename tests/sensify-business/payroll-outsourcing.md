# Business Sensify Test: Payroll Outsourcing Startup

This scenario is intentionally close to a real founder-style discussion. The point is to test whether `sensify-business` challenges the model rather than simply organizing the founder's statements.

## Starting prompt

> I want to start a payroll outsourcing company serving small businesses in Guam and Saipan, especially businesses that cannot justify a full payroll team and depend on one payroll employee, accountant, or owner. I am thinking of clients up to roughly 200 employees. A major value proposition is continuity and reduced fraud/key-person risk. I want a commission-based sales model where salespeople earn 30% of revenue for the lifetime of the customer relationship. We can onboard clients by collecting employee/payroll history and tax filings, setting up employees in our system, running payroll in parallel, training employees/managers, and taking over fully once everything matches.

## What the skill must not do

It should not simply rewrite this into a polished business plan.

It should not mark the following as facts merely because the founder stated them:

- target companies perceive single-person payroll dependency as a purchase-worthy problem;
- outsourcing reduces total risk enough to justify switching;
- the target market prefers a local provider;
- the target segment should be capped at 200 employees;
- 30% lifetime commission is economically sustainable;
- parallel payroll is operationally sufficient to de-risk migration;
- the chosen payroll system can satisfy all relevant Guam/CNMI requirements.

## Expected early model objects

### Decisions / proposals

- target geography: Guam and Saipan/CNMI;
- initial service concept: outsourced payroll;
- proposed segment ceiling: about 200 employees;
- proposed lifetime sales commission: 30% of revenue;
- proposed onboarding approach: data collection -> setup -> parallel run -> training -> cutover.

### Hypotheses / assumptions

- key-person payroll dependency creates meaningful customer pain;
- customers will pay to reduce that risk;
- local service creates sufficient differentiation;
- switching costs/trust concerns can be overcome;
- target customers prefer outsourcing over hiring/training internal backup;
- 30% lifetime commission leaves adequate long-term contribution margin;
- onboarding effort is recoverable under the pricing model;
- operating controls can reduce fraud/error exposure rather than merely transferring it.

### Researchable facts

The agent should independently investigate, as relevant:

- payroll/tax/employment filing obligations in Guam and CNMI;
- employer/payroll record obligations;
- relevant local business population data if available;
- major payroll alternatives operating in the territories;
- published competitor/service pricing when available;
- data/privacy/security obligations relevant to payroll data;
- requirements/limitations of the proposed payroll software once a product is selected.

### Private facts to ask the founder

Examples may include:

- available startup capital/runway;
- founder/team payroll expertise;
- existing customer relationships or pipeline;
- intended operating involvement;
- privately known cost structure or software quotes;
- risk tolerance and desired business scale.

## Expected high-leverage challenges

### Problem / willingness to pay

The agent should challenge whether continuity/fraud risk is:

- frequent enough;
- visible enough to the buyer;
- expensive enough;
- urgent enough;
- better solved through outsourcing than internal controls/backups.

### Competition / status quo

The agent should treat the status quo, accountants/bookkeepers, national payroll providers, payroll modules bundled with accounting/HR systems, and hiring/training internal staff as alternatives.

### 30% lifetime commission

The agent should flag this as a high-impact proposed decision and investigate its economics before normalizing it.

Questions should connect commission to:

- price;
- gross/contribution margin;
- onboarding cost;
- ongoing servicing cost;
- churn/retention;
- account expansion;
- salesperson behavior;
- ownership of the customer relationship;
- what happens when salesperson involvement ends.

A good challenge might conclude that the commission structure cannot be judged until the economic unit and cost structure are clearer.

### Onboarding

The agent should explore:

- cutoff/deadline risk;
- completeness/correctness of historical data;
- year-to-date reconciliation;
- prior filings and amendments;
- employee access/training;
- parallel-run acceptance criteria;
- handling discrepancies;
- authorization/approvals;
- customer responsibilities;
- cutover and rollback;
- liability for historical errors.

### Operations and control

The value proposition is partly risk reduction, so the agent should demand an operating model that itself addresses:

- segregation of duties;
- approvals;
- access controls;
- audit trail;
- backup coverage;
- error correction;
- data security;
- business continuity;
- vendor/platform outages;
- fraud prevention/detection;
- payroll deadlines.

### Local differentiation

"Local" should remain a hypothesis until the model explains what tangible customer outcome local presence creates: trust, response time, local law knowledge, onsite onboarding, language/cultural familiarity, relationship accountability, or another benefit.

## Expected red-team premortem

The model should eventually consider failure paths such as:

- target businesses acknowledge the risk but will not pay enough to outsource;
- national/bundled providers are cheaper and "good enough";
- onboarding/service labor makes small accounts unprofitable;
- 30% lifetime commissions consume too much contribution margin;
- one payroll error creates outsized liability/reputational damage;
- regulatory complexity is underestimated;
- the company itself develops key-person dependency;
- customer concentration creates cash risk;
- software/vendor limitations prevent the promised service level;
- founder-led sales does not translate into repeatable acquisition.

## Completion expectation

The skill may complete even if customer willingness to pay has not yet been validated, provided the model clearly labels it as critical/unvalidated and defines the evidence needed.

It should not complete if the business economics depend on the 30% commission yet the relevant revenue and servicing-cost logic remains completely unmodeled.
