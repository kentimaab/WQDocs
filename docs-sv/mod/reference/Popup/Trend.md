---
title: Trend
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Trend

Trend-popupen visar livevärden för den valda objektets signaler i ett realtidsdiagram. Till skillnad från [Historik](./History.md)-popupen, som begränsas av hur ofta signaler loggas, läser Trend-popupen direkt från Datalager och uppdateras kontinuerligt. Den är alltid synlig i Tab-menyn oavsett vilka suffix objektet har.

![Trend popup](/Images/Popups/Trend.png)

## Diagram

Diagrammet visar livevärdena för de valda signalerna över tid. En förklaring till vänster visar namn, färg och aktuellt värde för varje aktiv signal.

## Signaler

Panelen **Signaler** till höger listar alla tillgängliga signaler för objektet. Valda signaler markeras med en grön bockmarkering. Använd pilknapparna för att navigera i listan, **Välj** för att välja en signal och **Tillämpa** för att uppdatera diagrammet. Panelen visar hur många signaler som för närvarande är valda av det totala antalet tillgängliga.

## Inställningar

Panelen **Inställningar** innehåller konfigurationsalternativ för Y-axeln:

* **Automatisk skalning** — när aktiverad skalas Y-axeln automatiskt för att passa synliga data. När inaktiverad kan värdena **Min** och **Max** anges manuellt.
* **Min** — det minsta värdet som visas på Y-axeln när automatisk skalning är inaktiverad.
* **Max** — det största värdet som visas på Y-axeln när automatisk skalning är inaktiverad.
<!-- --8<-- [end:body] -->
