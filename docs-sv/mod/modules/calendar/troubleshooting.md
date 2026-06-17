---
title: Kalender
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Kalender

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Inga händelser visas i kalendern | Kontrollera att anslutningen till underhållsdatabasen är aktiv. Både anpassade kalenderhändelser och underhållsdeadlines läses från samma databas. Om anslutningen är nere läses kalendern in men inga händelser visas. |
| Underhållshändelser visas inte | Kontrollera att skriptet `scMaintenance` körs. Kalendern hämtar underhållsdeadlines genom att anropa funktioner i `scMaintenance` vid laddningstillfället. Om `scMaintenance` inte är tillgängligt hoppas underhållshändelserna över. |
| Händelser från en tidigare period visas kvar efter navigering | Kalendern rensar och återrenderar alla händelser vid navigering till en ny period. Om inaktuella händelser visas, ladda om vyn. Om problemet kvarstår, kontrollera om flera `CalendarManager`-instanser har skapats för samma vy, eftersom detta kan orsaka dubbelrendering. |
| Kalendern är tom efter öppning | `CalendarManager` initieras vid laddning av vyn. Om vyn laddas innan anslutningen till underhållsdatabasen är klar kan steget för händelseladdning misslyckas utan felmeddelande. Kontrollera `scAlert`-loggen för fel från `CalendarService` eller `CalendarManager`. |

## Kända buggar { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
