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

# History-databas

History-databasen har ingen fast uppsättning tabeller. Tabeller skapas automatiskt när loggenheter konfigureras i **WideQuick® Designer**. Varje loggenhet skapar ett par tabeller som identifieras av en hash som härleds från loggenhetens namn.

## Tabellnamn { #table-naming }

Varje loggenhet skapar två tabeller:

| Tabell | Beskrivning |
|---|---|
| `wq_<hash>_data0` | De loggade signalvärdena — en rad per mätvärde, med en tidsstämpel och det registrerade värdet för varje signal i loggenheten. |
| `wq_<hash>_meta` | Metadata för loggenheten — mappar kolumnnamn i datatabellen till deras signalnamn och enheter. |

Hashen genereras från loggenhetens namn och förblir stabil så länge loggenhetens namn inte ändras. Om en loggenhet byter namn genereras en ny hash och ett nytt tabellpar — de gamla tabellerna tas inte bort automatiskt.

## Frågor { #querying }

Skriptet `scHistory` löser upp rätt tabellnamn vid körning genom att läsa metatabellen. Direkta frågor mot History-databasen bör använda metatabellen för att slå upp kolumnnamn i stället för att hårdkoda dem, eftersom kolumnlayouten varierar mellan loggenheter.

<!-- --8<-- [end:body] -->
