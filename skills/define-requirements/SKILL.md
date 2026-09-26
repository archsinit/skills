---
name: define-requirements
description: Turn a settled product definition into testable release requirements through focused questioning. Use when the user wants to define what a product must do before UX, architecture, or implementation; do not use for initial product discovery or a technical build plan.
---

# Define requirements

Produce a requirements document that lets design and implementation proceed without inventing product behavior. Start from the current product definition and decision history. Preserve their scope and vocabulary; do not repeat settled product questions unless a concrete contradiction, missing case, or new evidence warrants reopening one.

## Find the decision frontier

Before drafting or extending feature requirements, make a visible end-to-end flow inventory for every actor. Start where each person first arrives, including access or sign-in, and follow every handoff to the promised outcome and later changes. Include how a record is created, resumed, approved, viewed, revised, withdrawn, and recovered wherever those actions apply. For each transition, note the normal path, consequential alternative, failure and recovery state, what the person sees or controls, and the current decision or requirement that covers it. Mark missing coverage explicitly; a feature list, collection of isolated screens, or generic open-decisions heading does not replace this inventory. Keep the inventory proportionate to the product and revisit it after material decisions.

Check cross-cutting needs along those flows, including access, privacy, accessibility, reliability, content integrity, and operational recovery. Trace private data and actions separately from public pages. Do not turn every imaginable concern into a requirement, but do not omit an entry point or transition merely because it seems routine or belongs to a later design or architecture stage. Record its decision owner and deadline instead.

Separate four things: requirements supported by an existing decision, proposed requirements awaiting a product decision, assumptions needing validation, and choices that belong to UX, architecture, or implementation. Research facts that can be established from available sources. Ask the user for consequential product judgments. Prioritize questions by the decisions they unlock and the cost of guessing wrong; offer a recommendation and tradeoff for a material choice. Group independent questions into a manageable round, then update the document as answers arrive.

## Write the contract

Use one canonical requirements document in the project, or update the existing one. Give each substantive requirement a stable identifier. State the actor, condition, observable behavior or constraint, and a way to verify it. Link it to the source product decision or user answer. Record meaningful exceptions and recovery behavior. Write quality requirements only when a concrete risk or intended experience justifies them; make the intended threshold observable, or mark the threshold as open.

Keep requirements distinct from screen layouts, technology choices, task sequencing, and tests tied to a particular implementation. Put excluded scope and future compatibility constraints in their own sections instead of disguising them as current user behavior. Acceptance examples may describe inputs and visible results, but should not prescribe internal design. Maintain an explicit open-decisions section with owner, consequence, and the stage by which each decision must be made. Do not silently promote a plausible proposal to a confirmed requirement.

## Check readiness at the requested level

Trace each first-release promise and each inventoried flow transition to at least one requirement or an explicit open decision, and each requirement back to a product goal or decision. Walk the journeys from first arrival through final outcome and later use, including access, creation, failure, correction, withdrawal, and recovery where relevant. Exercise representative end-to-end scenarios that cross screens and private/public boundaries; isolated screen reviews cannot establish flow completeness. Check that each acceptance condition could fail in a broken product and can be observed by a user or verifier. Remove duplicates and speculative scope.

Distinguish **behavior-ready** from **build-ready**. Behavior-ready means consequential product behavior is settled and remaining choices are explicitly assigned to UX, architecture, or operations. Build-ready means a developer can implement and release the product without seeking another product, design, technical, or operating decision from the user. If the user asks for a no-guesswork build contract, audit all of those domains. Either record each required decision before implementation or record a clear delegation with constraints, decision owner, and where the chosen answer will be written. A list of feature checks alone never proves build readiness. Do not call either level complete while a consequential choice or inventoried transition is hidden behind vague wording, a missing screen, or an assumed default.

Present a compact review of the requirements, open decisions, delegated choices, and readiness level. Ask the user whether it matches their intent before calling it final. If the user stops earlier, preserve the working draft and identify what remains unresolved.

