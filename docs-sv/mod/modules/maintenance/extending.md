---
title: Underhåll — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Underhåll — Utöka

## Kalenderintegration { #calendar-integration }

Underhållsuppgifter med kommande deadlines visas automatiskt som händelser i kalendermodulen. Det ger en tidsbaserad översikt över planerat underhåll i hela projektet utan att behöva öppna underhållslistan.

Kalendern läser uppgifter från underhållsdatabasen och visar dem utifrån deras deadline-datum. Uppgifter med status **Done**, **Done - Delayed** eller **Removed** exkluderas.

En påminnelsehändelse visas i kalendern ett visst antal dagar före varje uppgifts deadline. Standardförskjutningen för påminnelser är 3 dagar. Förskjutningen och påminnelseväxeln per mall kan båda konfigureras via ett skript — se [Kalender — Utöka](../calendar/extending.md#reminder-configuration).

![Underhållsuppgifter synliga som händelser i kalendervyn](/docs/sv/Images/Maintenance/maintenance-in-calendar.png){align=center}

## Ändringshistorik { #change-history }

Varje ändring av en underhållsuppgift — status, deadline, ansvarig, prioritet och beskrivning — registreras automatiskt och kan visas under **Historia → Loggar → Spårningslogg → Spårningslogg - Underhåll**. Ingen konfiguration krävs. Se [Spårningslogg](/mod/modules/audit-trail/get-started/#maintenance-change-log) för mer information.

<!-- --8<-- [end:body] -->
