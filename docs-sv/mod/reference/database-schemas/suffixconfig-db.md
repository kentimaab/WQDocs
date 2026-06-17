---
title: SuffixConfig.db
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# SuffixConfig.db

SuffixConfig.db innehåller en enda tabell som lagrar suffix-objektkonfigurationen för projektet.

## Tabeller { #tables }

| Tabell | Beskrivning |
|---|---|
| `SuffixObj` | Lagrar den fullständiga suffix-objektkonfigurationen som ett enda JSON-klump. Varje rad representerar en serialiserad suffix-objektdefinition. |

JSON-strukturen speglar suffix-objektmodellen som används av suffixsystemet vid körning. Se [Suffixsystem](../suffix-system.md) för mer information om hur suffix-objekt konfigureras och används.
<!-- --8<-- [end:body] -->
