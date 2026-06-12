---
title: SuffixConfig.db
description: Table reference for SuffixConfig.db — stores the suffix object configuration for WideQuick MOD.
product: mod
page_type: reference
doc_id: DOC-D3
size: M
priority: p0
status: draft
last_reviewed: 2026-06-11
---
<!-- --8<-- [start:body] -->

# SuffixConfig.db

SuffixConfig.db contains a single table that stores the suffix object configuration for the project.

## Tables { #tables }

| Table | Description |
|---|---|
| `SuffixObj` | Stores the full suffix object configuration as a single JSON blob. Each row represents one serialized suffix object definition. |

The JSON structure mirrors the suffix object model used by the suffix system at runtime. See [Suffix System](../suffix-system.md) for details on how suffix objects are configured and used.

<!-- --8<-- [end:body] -->
