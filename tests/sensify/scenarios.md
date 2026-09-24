# Sensify Behavior Scenarios

These are behavior tests, not golden-response tests. A future implementation should preserve the invariants even if wording changes.

## Scenario 1: vague build request

### Input

> Build me an internal AI tool that reads all our documents and answers employee questions. I want it to be accurate and secure.

### Expected Sensify behavior

The agent should not immediately produce architecture or code.

It should identify that "all our documents," "employee questions," "accurate," and "secure" are underspecified. It should research available workspace facts if accessible, then ask a small frontier covering high-leverage issues such as intended users/use cases, authoritative sources, sensitivity/access boundaries, acceptable failure modes, and how answers should be grounded.

It should distinguish:

- user decisions about scope/security tradeoffs;
- discoverable facts about existing systems;
- assumptions about document quality and retrieval accuracy;
- constraints imposed by regulation or internal policy.

## Scenario 2: confident causal assumption

### Input

> Our support team is slow because they have too many tools. We should replace everything with one system.

### Expected behavior

Do not accept the causal claim as fact.

Create at least:

- an assumption that tool fragmentation causes the slowness;
- a decision proposal to consolidate tools;
- research/inspection tasks for workflow metrics or available evidence.

Challenge alternative causes such as staffing, handoffs, policy, training, ticket mix, or approval latency before locking the solution.

## Scenario 3: researchable fact

### Input

> I think Vendor X supports SAML and data residency in Singapore. Should we use it?

### Expected behavior

Research Vendor X's current documented capabilities rather than asking the user to confirm them. Store sources/date. Then separate the factual capability question from the user's decision criteria and recommend based on those criteria.

## Scenario 4: prior decision becomes weak

### Initial decision

The user decides that the project must launch with Provider A because the team already knows it.

### Later evidence

Provider A cannot meet a newly discovered regulatory requirement.

### Expected behavior

Reopen the prior decision even though it was previously settled. Explain what changed, consequence, alternatives, recommendation, and ask the user to keep/modify/replace/investigate. Do not silently switch providers or silently keep the old decision.

## Scenario 5: too many possible questions

### Input

A complicated transformation program has dozens of open issues.

### Expected behavior

Maintain a large internal backlog but ask only roughly 3-7 independent, high-leverage frontier questions. Do not dump every question into one round. Prefer decisions that unlock many downstream branches.

## Scenario 6: acceptable uncertainty

### Situation

A new product concept has no retention data because it has not launched.

### Expected behavior

Do not block Sensify completion solely because retention is unknown. Record retention as a critical hypothesis, define evidence/validation needed, identify downstream decisions that should wait if necessary, and make the uncertainty visible in the completion summary.

## Scenario 7: private fact

### Input

> How much runway do we have available for this initiative?

### Expected behavior

If the budget/cash position is not available in connected data, ask the user. Do not fabricate it or treat it as a public research task.

## Scenario 8: user rejects recommendation

### Situation

The agent recommends Option A and presents evidence/tradeoffs. The user chooses Option B for a strategic reason.

### Expected behavior

Record Option B as the user's decision, including rationale and accepted tradeoff/risk. Do not keep pressuring the same issue without new evidence. Preserve appropriate reconsideration triggers.

## Scenario 9: explicit invocation only

### Input

> Build a plan for this complicated initiative.

### Expected behavior

Do the requested work using ordinary judgment and clarification as needed. Do not automatically activate Sensify or require its completion gate solely because the work is complex. If the user explicitly says “Sensify this initiative” or unmistakably asks for the Sensify interview, start the method.

## Scenario 10: business routing

### Input

> Sensify my payroll outsourcing business.

### Expected behavior

Start the explicit Sensify interview and apply the business specialization automatically when available. Do not make the user invoke a second skill name.

## Scenario 11: dictated answers and fuller rounds

### Situation

The user prefers dictation and answers a coherent batch of questions in free form, including corrections and qualifications out of order.

### Expected behavior

Parse which issues the answer settles, update the model, and ask another substantial round only for remaining material frontier questions. Do not insist on numbered responses or repeat questions already answered. A round may contain more than seven independent questions when that reduces unnecessary back-and-forth.

## Scenario 12: growing knowledge and downstream writeback

### Situation

A canonical understanding model exists for an initiative. Later financial work finds that an earlier cost assumption is wrong.

### Expected behavior

Read the model before the financial work; record the new evidence and its effect in that same model, preserving the old rationale and marking any reopened decision. Link related models only when relevant. Do not restart a Sensify interview without an explicit request.

## Scenario 13: user moves on early

### Situation

A critical hypothesis remains untested, but the user says to stop the interview and draft the requested artifact.

### Expected behavior

Record the remaining consequential uncertainty, avoid declaring Sensify complete, and follow the user's direction. The resulting artifact should not silently treat the hypothesis as fact.

## Scenario 14: preferred knowledge system unavailable

### Situation

The user prefers Notion, but its connector is not installed or its needed read and update capabilities have not been verified. A writable project exists.

### Expected behavior

Use a local model for now, identify it as the current source of truth, and record Notion migration as an open integration decision. Do not imply that Notion and the local copy are synchronized.
