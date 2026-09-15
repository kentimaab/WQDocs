---
title: Kalender
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Kalender

Kalendermodulen ger en visuell översikt över händelser och kommande underhållsdeadlines. Den stöder tre vyer (månad, vecka och dag) och kan navigeras framåt och bakåt i tid.

Händelser hämtas från tre källor: händelser som skapas direkt i kalendern, underhållsdeadlines som hämtas automatiskt från [Underhållsmodulen](../maintenance/index.md), samt händelser som importeras från en lokal `.ics`-fil. En konfigurerbar påminnelse visas ett angivet antal dagar innan varje underhållsdeadline.

Dagar kan markeras som helgdagar och helgdagsaftnar. Kalendern publicerar den klassificeringen till två interna variabler, som kan skickas vidare till ett PLC eller DUC så att dess egna scheman kan ta hänsyn till dagtypen.

!!! info "Direktanslutna kalenderflöden ingår inte i den här versionen"
    Att prenumerera på en ICS-länk och att importera ett lands röda dagar kräver båda REST-insticksmodulen, som inte ingår. Import från en lokal `.ics`-fil är tillgänglig, och helgdagar markeras i kalendern själv. Se [Importera en kalender](configuring.md#importing-a-calendar).

## Innehåll { #contents }

### [Kom igång](get-started.md) { #get-started }
* [**Vyer**](get-started.md#views) — Vy för månad, vecka och dag.
* [**Sidopanel**](get-started.md#sidebar) — Minikalender och lista över kommande händelser.
* [**Skapa en händelse**](get-started.md#creating-an-event) — Så lägger man till en ny kalenderhändelse.

---

### [Konfigurera](configuring.md) { #configuring }
* [**Händelser**](configuring.md#events) — Skapa, redigera och ta bort händelser.
* [**Underhållshändelser**](configuring.md#maintenance-events) — Hur underhållsdeadlines visas och vad färgerna betyder.
* [**Påminnelser**](configuring.md#reminders) — Konfigurera påminnelseförskjutning för underhållsdeadlines.
* [**Helgdagar och helgdagsaftnar**](configuring.md#holidays-and-holiday-eves) — Markera en dag och skicka klassificeringen till ett PLC.
* [**Importera en kalender**](configuring.md#importing-a-calendar) — Lägga till händelser från en lokal `.ics`-fil.
* [**Hantera importerade kalendrar**](configuring.md#managing-imported-calendars) — Byta namn, färg, filtrera och ta bort.
* [**Exportera en kalender**](configuring.md#exporting-a-calendar) — Skriva händelser till en fil eller skicka dem med e-post.

---

### [Utöka](extending.md) { #extending }
* [**Påminnelsekonfiguration**](extending.md#reminder-configuration) — Ändra påminnelseförskjutningen och inställningen per mall.
* [**Helgdagsvariabler**](extending.md#holiday-variables) — `isHoliday`, `isHolidayEve` och hur de uppdateras.
* [**Lagring av prenumerationer**](extending.md#subscription-storage) — Tabellen `ics_subscriptions` och vad varje kolumn innehåller.
* [**Skriptreferens**](extending.md#script-reference) — Funktionerna i `scHoliday` bakom import, export och helgdagsklassificering.

---

### [Felsökning](troubleshooting.md) { #troubleshooting }
* [**Vanliga problem**](troubleshooting.md) — Vanliga problem och hur man löser dem.
<!-- --8<-- [end:body] -->
