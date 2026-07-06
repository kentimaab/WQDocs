---
title: Larmlista.db
product: mod
page_type: reference
status: draft
last_reviewed: 2026-07-01
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Larmlista-databas

Larmlista-databasen har ingen fast uppsättning tabeller. Den skrivs till av larmloggenheter som konfigureras i **WideQuick® Designer** — se [Konfigurera en loggenhet](../../guides/Loggers.md) för hur loggenhetstyp och version påverkar vilka tabeller som skapas.

## Tabellnamn { #table-naming }

Tabellnamn och struktur beror på vilken loggenhetsversion som valts för larmloggenheten:

| Version | Tabeller |
|---|---|
| Version 1 | Två tabeller namngivna efter loggenheten. |
| Version 2 | Flera automatiskt genererade tabeller, beroende på antalet loggade larm. |

## Frågor { #querying }

Larmhistorik läses via det globala `Loggers`-objektet i stället för att fråga tabellerna direkt — till exempel `Loggers["Larmlogg"].data(...)`. Det gör frågorna oberoende av de underliggande tabellnamnen, som ändras om loggenheten byter namn eller version.

<!-- --8<-- [end:body] -->