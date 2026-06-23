---
title: Spårningslogg — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Spårningslogg — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Spårningsloggen och all
    relaterad funktionalitet som beskrivs i guiderna för Spårningsloggen:
    
    * `scAuditTrail`
    * `scAlert`

Spårningsloggen registrerar ändringar av valda Datalager-variabler och underhållsuppgifter. Den finns under **Historik → Loggar → Spårningslogg**.

## Visa loggen { #viewing-the-log }

Navigera till **Historik → Loggar → Spårningslogg → Spårningslogg**.

![Audit trail view](/docs/sv/Images/Audit_Trail/audit-trail-log.png){align=center}

Loggen visar alla registrerade ändringar med följande kolumner:

* **Tid** — när ändringen gjordes.
* **Händelse** — det gamla värdet och det nya värdet, visas som `old → new`.
* **Kontext** — den fullständiga variabelsökvägen i Datalager.
* **Användare** — den inloggade användaren när ändringen gjordes.

Använd panelen **Filter** till vänster för att begränsa loggen:

* **Objekt** — filtrera på ett specifikt objekt eller variabelsökväg.
* **Tid** — visa alla händelser, händelser inom ett valt tidsintervall eller enbart de senaste händelserna.
* **Användare** — filtrera på en specifik användare.
* **Antal rader** — begränsa hur många poster som visas.

Klicka på **Filter** för att tillämpa. Klicka på **Rensa spårningslogg** för att permanent ta bort alla loggposter.
## Underhållsändringslogg { #maintenance-change-log }

Navigera till **Historik → Loggar → Spårningslogg → Spårningslogg - Underhåll**.

![Audit Trail - Maintenance view](/docs/sv/Images/Audit_Trail/audit-trail-maintenance.png){align=center}

Den här vyn visar en fullständig historik över ändringar av underhållsuppgifter. Varje statusändring, uppdatering av deadline, prioritetsändring, tilldelningsändring och beskrivningsredigering registreras automatiskt. Ingen konfiguration krävs.

Varje rad visar:

* **Uppgift** — underhållstypen.
* **Objekt** — det objekt som uppgiften tillhör.
* **Ändrad av** — den användare som gjorde ändringen, eller **System** för automatiska ändringar såsom övergångar vid missad deadline.
* **Ändringstid** — när ändringen gjordes.
* **Tidigare status** — statusen före ändringen.
* **Aktuell status** — statusen efter ändringen.

Markera en rad och klicka på **Öppna** för att se det fullständiga detaljerna för ändringen, inklusive tilldelad person, prioritet, deadline och beskrivning.

## Nästa steg { #next-steps }

* [Konfigurering](configuring.md) — välja vilka variabler som ska spåras
<!-- --8<-- [end:body] -->
