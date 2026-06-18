---
title: Historik — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Historik — Utöka

## Öppna vyspecifik historik { #opening-view-specific-history }

Den vyspecifika historikpopupen öppnas från en arbetsvy med hjälp av ett skript. Vyn skickar med sitt eget länknamn så att popupen vet vilka objekt som ska inkluderas:

```javascript
app.popOut.newData = { linkName: view.linkName };
app.popOutVisible = true;
app.popOut.setView("Pop_Outs/VySpecifikHistorik.kvie");
```

Popupen läser tabellen `ObjectList` i konfigurationsdatabasen och filtrerar till de rader där `View` matchar det angivna `linkName`. Den resulterande uppsättningen objekt avgör vilka signaler som visas i signalträdet.

Sparade signalgrupper i den vyspecifika popupen lagras per vy i tabellen `History_SavedSignals_View`. Grupper som sparas här syns inte i den projektövergripande vyn **Historik**, och vice versa.

## Signaler som inte loggas { #signals-not-logged }

Knappen **Visa variabler som inte loggas** i den projektövergripande vyn öppnar ett separat fönster med ett träd över alla signaler som finns i systemet men saknar en aktiv logger. Fönstret är skrivskyddat — det används endast för att identifiera saknade loggers.

I objektpopupens flik [**Historik**](../../reference/Popup/History.md) visas ologgade signaler alltid på höger sida under **Taggar som inte loggas**, utan att behöva öppna något extra fönster.

<!-- --8<-- [end:body] -->
