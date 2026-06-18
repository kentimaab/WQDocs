---
title: Historik — Felsökning
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Historik

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Signalträdet är tomt | Signalträdet fylls i genom att skanna projektets loggenheter. Om inga loggenheter är konfigurerade kommer trädet att vara tomt. Kontrollera att minst en loggenhet är aktiv i projektkonfigurationen. |
| En signal saknas i trädet | Endast signaler med en aktiv loggenhet visas i trädet. Använd **Visa variabler som inte loggas** i den projektövergripande vyn för att bekräfta om signalen finns men inte loggas. |
| Diagrammet är tomt efter att ha klickat på Verkställ | Kontrollera att det valda tidsintervallet innehåller loggad data för dessa signaler. Om signalerna nyligen lades till kan det hända att det ännu inte finns tillräckligt med data att visa. |
| Sparade signalgrupper saknas | Projektövergripande sparade grupper lagras i tabellen `History_SavedSignals_Project`. Vyspecifika grupper lagras i `History_SavedSignals_View`. Om grupper saknas efter en projektuppdatering, kontrollera om relevant tabell skrevs över under uppdateringen. |
| Y-axelns skalning är oväntad | När **Skala Y-axlar** är avstängd används standardgränserna för varje signals enhet på Y-axeln. Aktivera **Skala Y-axlar** i panelen **Inställningar** för att anpassa diagrammet till faktiska data. |

## Kända fel { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
