---
title: Loggbok — Felsökning
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Loggbok

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Poster visas inte efter sparning | Kontrollera att `loggWildCardReload` är inställt på `true` i DataStore. När värdet är `true` laddar hanteraren om alla poster under ämnet med en jokerteckensökning efter varje sparning, vilket gör att nyligen skapade underposter visas omedelbart. När värdet är `false` laddas endast poster med exakt ämne om. |
| Ämnesträdet är tomt | Ämnesträdet fylls i från poster i databasen. Om det inte finns några poster för hanterarens ämne kommer trädet att vara tomt. Skapa minst en post för att verifiera att anslutningen fungerar, och kontrollera sedan `Config`-databasanslutningen om ingenting visas. |
| Poster från andra ämnen visas i en vybegränsad hanterare | Kontrollera att `load()` anropas med `false` om endast exakta ämnesmatchningar önskas. Att anropa `load(true)` inkluderar alla underämnen via en jokerteckenfråga. |

## Kända fel { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
