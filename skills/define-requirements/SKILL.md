---
name: define-requirements
description: Turn a settled product definition into testable release requirements through focused questioning. Use when the user wants to define what a product must do before UX, architecture, or implementation; do not use for initial product discovery or a technical build plan.
---

# Define requirements

Produce a requirements document that lets design and implementation proceed without inventing product behavior. Start from the current product definition and decision history. Preserve their scope and vocabulary; do not repeat settled product questions unless a concrete contradiction, missing case, or new evidence warrants reopening one.

## Find the decision frontier

Map the promised reader and operator journeys from trigger through outcome, including changes after the initial action. For each journey, identify the normal path, consequential alternatives, failure and recovery states, and what the person must see or control. Check cross-cutting needs where they matter to the product, including access, privacy, accessibility, reliability, content integrity, and operational recovery. Do not turn every possible concern into a requirement.

Separate four things: requirements supported by an existing decision, proposed requirements awaiting a product decision, assumptions needing validation, and choices that belong to UX, architecture, or implementation. Research facts that can be established from available sources. Ask the user for consequential product judgments. Prioritize questions by the decisions they unlock and the cost of guessing wrong; offer a recommendation and tradeoff for a material choice. Group independent questions into a manageable round, then update the document as answers arrive.

## Write the contract

Use one canonical requirements document in the project, or update the existing one. Give each substantive requirement a stable identifier. State the actor, condition, observable behavior or constraint, and a way to verify it. Link it to the source product decision or user answer. Record meaningful exceptions and recovery behavior. Write quality requirements only when a concrete risk or intended experience justifies them; make the intended threshold observable, or mark the threshold as open.

Keep requirements distinct from screen layouts, technology choices, task sequencing, and tests tied to a particular implementation. Put excluded scope and future compatibility constraints in their own sections instead of disguising them as current user behavior. Acceptance examples may describe inputs and visible results, but should not prescribe internal design. Maintain an explicit open-decisions section with owner, consequence, and the stage by which each decision must be made. Do not silently promote a plausible proposal to a confirmed requirement.

## Check readiness at the requested level

Trace each first-release promise to at least one requirement and each requirement back to a product goal or decision. Walk the complete journeys against the document, especially failure, correction, withdrawal, and other post-publication or post-submission changes relevant to the product. Check that each acceptance condition could fail in a broken product and can be observed by a user or verifier. Remove duplicates and speculative scope.

Distinguish **behavior-ready** from **build-ready**. Behavior-ready means consequential product behavior is settled and remaining choices are explicitly assigned to UX, architecture, or operations. Build-ready means a developer can implement and release the product without seeking another product, design, technical, or operating decision from the user. If the user asks for a no-guesswork build contract, audit all of those domains. Either record each required decision before implementation or record a clear delegation with constraints, decision owner, and where the chosen answer will be written. A list of feature checks alone never proves build readiness. Do not call either level complete while a consequential choice is hidden behind vague wording or an assumed default.

Present a compact review of the requirements, open decisions, delegated choices, and readiness level. Ask the user whether it matches their intent before calling it final. If the user stops earlier, preserve the working draft and identify what remains unresolved.
