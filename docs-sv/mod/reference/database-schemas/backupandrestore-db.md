---
title: BackUpAndRestore.db
product: mod
page_type: reference
status: draft
last_reviewed: 2026-07-01
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# BackUpAndRestore-databas

BackUpAndRestore-databasen lagrar tillståndet för funktionen Säkerhetskopiering och återställning, som låter en användare spara det aktuella värdet för valda Datalager-variabler och återställa dem senare.

## Tabeller { #tables }

| Tabell | Beskrivning |
|---|---|
| `currentVariablesForBackUp` | Variablerna som för närvarande är valda inför nästa säkerhetskopiering — läggs till och tas bort via vyn för Säkerhetskopiering och återställning innan en säkerhetskopia tas. |
| `existingBackUps` | En rad per sparad säkerhetskopia — kopians tabellnamn, beskrivning, ursprungliga namn, vilken användare som skapade den, och skapandedatum. |

## Säkerhetskopietabeller { #backup-tables }

Varje gång en säkerhetskopia skapas genereras en ny tabell, namngiven efter kopian (i gemener), med två kolumner:

| Kolumn | Beskrivning |
|---|---|
| `variable` | Datalager-sökvägen för variabeln. |
| `value` | Variabelns värde vid tidpunkten för säkerhetskopieringen, lagrat som text. |

Dessa tabeller skapas och tas bort av `scBackUpAndRestore` och listas i `existingBackUps` via sitt `tableName`.

<!-- --8<-- [end:body] -->