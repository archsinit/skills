# Roadmap

The first release focuses on understanding-building rather than downstream production.

## Current

- `sensify`: general knowledge-work understanding engine
- `sensify-business`: startup and business specialization
- storage-neutral knowledge schema
- local Markdown persistence templates
- behavior-focused test scenarios

## Likely next layers

### Persistence adapters

Keep the logical model unchanged while adding adapters for:

- project/workspace files
- Notion
- Obsidian
- Git repositories
- other knowledge bases

An adapter should never change the meaning of the model. It only changes where and how it is stored.

### Downstream business skills

Possible consumers of a completed Business Understanding Model:

- business-plan
- business-plan-presentation
- financial-model
- validation-plan
- customer-discovery
- operating-model
- process-map
- sales-package
- implementation-plan

These skills should consume the persistent model first and ask new questions only when a material gap blocks their specific output.

### Additional Sensify specializations

Potential domain layers:

- `sensify-product`
- `sensify-strategy`
- `sensify-process`
- `sensify-research`
- `sensify-software`

The generic `sensify` skill should remain domain-neutral; specialized skills add domain coverage and failure modes without weakening the core method.
