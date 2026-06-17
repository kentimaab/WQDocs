---
title: maintenance.db
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# maintenance.db

maintenance.db lagrar allt som rör modulerna Underhåll och Kalender, inklusive uppgiftskonfigurationer, uppgiftsloggen, ändringshistorik, kalenderhändelser och registret över kända fjärrsystem.

## Underhåll { #maintenance }

| Tabell | Beskrivning |
|---|---|
| `maintenance_configs` | Återkommande underhållskonfigurationer — definierar objekt, typ, intervall, prioritet, tilldelad person och huruvida missade deadlines automatiskt genererar en uppföljningsuppgift. |
| `maintenanceLog` | Uppgiftsloggen — en rad per underhållsuppgiftsinstans, med status, skapare, tilldelad person, inmatningsdatum, deadline och en referens tillbaka till dess konfiguration. |
| `maintenanceLog_templates` | Mallar för underhållsuppgiftstyper — definierar standardprioritet, deadlinetyp och -värde samt huruvida påminnelser är aktiverade. |
| `maintenance_events` | Ändringslogg för underhållsuppgifter — registrerar varje statusändring, omtilldelning, beskrivningsredigering och prioritetsändring på en loggpost. |

## Kalender { #calendar }

| Tabell | Beskrivning |
|---|---|
| `CalendarEvents` | Anpassade kalenderhändelser — titel, objekt, färg, skapare, beskrivning samt start- och sluttidsstämplar i millisekunder. |
| `calendar_config` | Nyckel-värde-konfiguration för kalendern, till exempel påminnelseförskjutningen. |

## Fjärrsystem { #remote-systems }

| Tabell | Beskrivning |
|---|---|
| `known_systems` | Register över fjärranslutna WideQuick-noder — systemnamn, värdnamn och tidsstämpel för senast sedd. Används för att spåra vilka fjärrsystem som är anslutna. |
<!-- --8<-- [end:body] -->
