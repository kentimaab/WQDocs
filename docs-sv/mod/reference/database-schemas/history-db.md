---
title: History.db
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# History.db

History.db har ingen fast uppsättning tabeller. Tabeller skapas automatiskt när loggrar konfigureras i **WideQuick Designer®**. Varje logger skapar ett par tabeller som identifieras av en hash som härleds från loggarnamnet.

## Tabellnamn { #table-naming }

Varje logger skapar två tabeller:

| Tabell | Beskrivning |
|---|---|
| `wq_<hash>_data0` | De loggade signalvärdena — en rad per mätvärde, med en tidsstämpel och det registrerade värdet för varje signal i loggaren. |
| `wq_<hash>_meta` | Metadata för loggaren — mappar kolumnnamn i datatabellen till deras signalnamn och enheter. |

Hashen genereras från loggarnamnet och förblir stabil så länge loggarnamnet inte ändras. Om en logger byter namn genereras en ny hash och ett nytt tabellpar — de gamla tabellerna tas inte bort automatiskt.

## Frågor { #querying }

Skriptet `scHistory` löser upp rätt tabellnamn vid körning genom att läsa metatabellen. Direkta frågor mot History.db bör använda metatabellen för att slå upp kolumnnamn i stället för att hårdkoda dem, eftersom kolumnlayouten varierar mellan loggrar.

<!-- --8<-- [end:body] -->
