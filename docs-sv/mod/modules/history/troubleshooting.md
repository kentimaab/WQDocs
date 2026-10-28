---
title: Historik — Felsökning
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-28
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
| En signal som loggas i flera loggenheter läses från fel loggenhet | Historik använder den första loggenheten i bokstavsordning. Se [Signaler som loggas i flera loggenheter](#signals-in-several-loggers). |

## Signaler som loggas i flera loggenheter { #signals-in-several-loggers }

Varje kurva i diagrammet läser från en loggenhet. När en signal loggas i mer än en går Historik igenom loggenheterna i bokstavsordning och använder den första som loggar signalen.

Det gäller i vyn Historik, det vyspecifika Historik-popupet och fliken Historik i objektpopuper. Varje signal väljs för sig, så kurvorna i ett diagram kan komma från olika loggenheter.

### Byta loggenhet i Runtime { #switching-logger-in-runtime }

I vyn Historik och det vyspecifika Historik-popupet kan en kurva flyttas till en annan loggenhet från diagrammets inbyggda inställningar:

1. Klicka på inställningsknappen i diagrammets nedre vänstra hörn.
2. Markera kurvan under **Grafer**.
3. Välj en annan loggenhet i **Loggenhet**.

Bytet är tillfälligt. Historik väljer loggenhet igen varje gång en kurva läggs till på nytt: **Verkställ** gör det för alla kurvor, och **Följ** och **Sluta följa** för den följda signalen. Bytet försvinner också när vyn stängs, och sparade signalgrupper behåller det inte.

Fliken Historik i objektpopuper har ingen inställningsknapp, så där går det inte att byta loggenhet.

### Byta namn på en loggenhet { #renaming-a-logger }

För att Historik alltid ska välja en viss loggenhet, byt namn på den i Designer så att den kommer först i bokstavsordning bland de loggenheter som loggar signalen. Namnbytet påverkar alla signaler som loggenheten delar med en annan loggenhet, inte bara den aktuella.

Den loggade datan finns kvar. En databasloggenhet sparar sin data i tabeller som är namngivna efter dess ID (`wq_<ID>_data0` och så vidare), och ID:t ändras inte med namnet.

Sök i projektet efter det gamla namnet innan du byter, och uppdatera det som hänvisar till det. Rapporter, rapportscheman och skript kan ange en loggenhet med namn, till exempel `Loggers["EnergyLogg"]`, och sparade rapportscheman lagrar loggenhetens namn i databasen.

!!! note "Dashboards använder samma regel"
    Historik- och stapeldiagramwidgets i dashboards läser också en signal från den första loggenheten i bokstavsordning, så ett namnbyte ändrar även vilken loggenhet de använder.

## Kända fel { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
