# Persistence Protocol

Sensify treats persistent understanding as part of the work, but the reasoning model must not depend on a particular storage product.

## Storage-neutral rule

The canonical logical model is the set of material claims, relationships, evidence, decisions, risks, and unresolved questions defined by Sensify. Maintain one evolving model per business, project, or substantial initiative; link related models when useful.

A storage backend is an adapter. The user-facing view should read as a coherent account of the initiative. Use structured records where provenance, dependencies, history, links, or queries justify them; do not make every sentence a database object.

Examples include:

- local/project Markdown files;
- Notion;
- Obsidian;
- a wiki;
- a database;
- a knowledge graph;
- another connected system.

Changing the backend must not change the meaning of the model.

## Backend selection

Use this order:

1. Read the established canonical model for the current initiative, if one exists, and update it.
2. Use the backend the user has chosen when its read and write capabilities are actually available.
3. If a preferred backend (such as Notion) is unconnected or its needed capabilities are unverified, record that dependency and use a writable local fallback in the meantime. Do not claim that the systems are synchronized.
4. If no backend is available, maintain the model in-session and provide a reusable snapshot at completion.

Declare one authoritative location per initiative. Search that initiative and its explicit links first; consult other models only when relevant. Do not import an old assumption from another project as a current fact.

Do not repeatedly ask where to store the model when a reasonable fallback exists.

## Local Markdown fallback

For generic work in a writable project, prefer a visible root-level file named:

`UNDERSTANDING.md`

Start from [../assets/UNDERSTANDING.template.md](../assets/UNDERSTANDING.template.md) when useful.

The file is a **current model**, not a transcript. Make the purpose, proposed mechanism, and current decisions easy to read before the supporting registers.

It should contain, where material:

- purpose/scope;
- glossary/definitions;
- known facts and private facts;
- decisions and rationale;
- assumptions/hypotheses;
- constraints/preferences;
- risks;
- evidence references;
- open questions;
- contradictions;
- validation needs;
- change/decision history for material supersessions.

## Write timing

Update persistent knowledge when the understanding materially changes.

Do not wait until the end of a long interview. Delayed persistence increases the chance that resolved distinctions are lost or silently rewritten.

At the same time, avoid writing every conversational sentence. Persist model changes, not chatter.

## Canonical vs historical information

Keep the current state easy to read.

When history matters:

- mark old decisions `superseded` rather than leaving two active decisions;
- preserve the rationale for important changed choices;
- preserve meaningful contradictory evidence;
- summarize old states instead of keeping a full transcript.

## Source of truth

A project should have one declared canonical backend at a time.

If multiple systems mirror the model, identify which is authoritative. Otherwise future agents may update different copies and create invisible divergence.

## Handoff to downstream skills

A downstream skill should:

1. load the current initiative's canonical model first;
2. treat typed status and provenance seriously;
3. avoid asking the user to restate settled information;
4. reopen an item only when its own work exposes a material gap, contradiction, or changed basis;
5. write consequential discoveries and changed decisions back to the same model when it can do so, including what changed and why.

Downstream writeback does not itself restart a Sensify interview. Start that interview only on an explicit user request.
