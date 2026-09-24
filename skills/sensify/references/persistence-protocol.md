# Persistence protocol

Understanding should survive the interview. Keep one evolving model for each business, project, or substantial initiative, with links to related models where they help. A storage product holds the model; it does not define what its claims mean.

The user-facing view should explain the initiative coherently. Give material claims structured records when their source, status, dependencies, links, or history matter. Do not turn every sentence into a database entry.

## Choose one source of truth

Read and update the established model for the initiative if one exists. Otherwise use the backend the user has chosen, provided its needed read and write capabilities are available. A connected system such as Notion, a project file, Obsidian, a wiki, or a database can hold the same logical model.

If the preferred system is disconnected or its capabilities are unverified, record that limitation and use a writable local project as the current home. Do not imply the two places are synchronized. If no durable store is available, maintain the model during the session and give the user a reusable snapshot at the end.

Declare which location is authoritative. Search that initiative and its explicit links first; consult other models only when relevant. A claim from another project remains a claim from that project until its relevance here is established.

For a local Markdown fallback, use a visible `UNDERSTANDING.md` in the project root. [The template](../assets/UNDERSTANDING.template.md) is a starting point, not a form to fill mechanically. Put the purpose, proposed mechanism, and current decisions where a reader can find them. Add definitions, sources, assumptions, risks, contradictions, questions, validation needs, and history when material.

## Update as understanding changes

Write when an answer or research finding materially changes the model. Do not wait for a final summary or save every conversational sentence.

Keep the current state easy to read. When a decision changes, mark the old one as superseded, retain the reason for the change, and leave consequential contrary evidence visible. Summarize history; do not store a transcript in place of a model.

## Carry knowledge into later work

A downstream skill should read the canonical model first and respect the type, source, and confidence of its claims. It should not ask the user to repeat settled information. Reopen an item when the new work exposes a material gap, contradiction, or changed basis, and write consequential discoveries and decisions back to the same model when possible.

Writing back does not restart the Sensify interview. That requires a new explicit request.
