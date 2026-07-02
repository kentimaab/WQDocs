---
title: EventList.db
product: mod
page_type: reference
status: draft
last_reviewed: 2026-07-01
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# EventList-databas

EventList-databasen lagrar systemhändelser och konfigurationen för funktionen Spårningslogg.

## Tabeller { #tables }

| Tabell | Beskrivning |
|---|---|
| `events` | Systemets händelselogg. En rad per händelse — gruppnamn, händelsetext, UTC-tidsstämpel, användare, systemnamn, användardata och kontext. Fylls i av `System.logEvent()`, inklusive värdeändringar loggade av Spårningslogg. |
| `auditTrail` | Listan över Datalager-variabler som för närvarande bevakas av Spårningslogg. Hanteras av `scAuditTrail` — lagrar bara vilka variabler som bevakas, inte deras historiska värden. |

## Spårningslogg { #audit-trail }

Spårningsloggen bevakar variablerna som listas i `auditTrail`. När en bevakad variabels värde ändras skriver `scAuditTrail` en rad till `events` med gruppnamnet `"Audit trail"`, och registrerar variabelnamnet samt det gamla och nya värdet. Historiska poster läses tillbaka från `events`, inte från `auditTrail`.

<!-- --8<-- [end:body] -->