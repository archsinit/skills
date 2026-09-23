# Persistence Protocol

Sensify treats persistent understanding as part of the work, but the reasoning model must not depend on a particular storage product.

## Storage-neutral rule

The canonical logical model is the set of typed knowledge objects, relationships, evidence, decisions, risks, and unresolved questions defined by Sensify.

A storage backend is an adapter. Examples include:

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

1. If the user/project has an established Sensify backend, use it.
2. If the user explicitly chooses a backend, use it when available.
3. If a writable workspace exists but no backend is selected, use the local Markdown fallback.
4. If persistence is unavailable, maintain the model in-session and provide a canonical snapshot at completion.

Do not repeatedly ask where to store the model when a reasonable fallback exists.

## Local Markdown fallback

For generic work, prefer a visible root-level file named:

`UNDERSTANDING.md`

Start from [../assets/UNDERSTANDING.template.md](../assets/UNDERSTANDING.template.md) when useful.

The file is a **current model**, not a transcript.

It should contain:

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

1. load the current Sensify model first;
2. treat typed status/provenance seriously;
3. avoid asking the user to restate settled information;
4. reopen an item only when its own work exposes a material gap or contradiction;
5. write back new material discoveries if the workflow permits.
