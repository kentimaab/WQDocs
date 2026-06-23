---
title: Historik
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Historik

Historik-popupen visar ett trenddiagram för det valda objektet och presenterar historiska värden för dess loggade signaler. Den är alltid synlig i flikmenyn oavsett vilka suffix objektet har. Mer information om hur historiksystemet fungerar finns under [Historik](../../modules/history/index.md).

![History popup](/docs/sv/Images/Popups/History.png)

## Signaler

Panelen **Signaler** till höger listar alla signaler som tillhör objektet och som för närvarande loggas. Signaler kan slås på och av i grafen med pilknapparna, och knappen **Välj** möjliggör manuellt urval. Klicka på **Använd** för att uppdatera grafen.

Signaler som tillhör objektet men inte loggas listas separat under **Taggar som inte loggas** i den nedre högra panelen.

## Graf

Grafen visar de historiska värdena för de valda signalerna under det valda tidsintervallet. Y-axelns enhet hämtas automatiskt från signalens suffixaliaskonfiguration.

## Inställningar

Panelen **Inställningar** till höger erbjuder följande alternativ:

* **Visa legend** — slår på eller av signallegenden i grafen
* **Visa linjal** — slår på eller av en vertikal linjal som kan dras längs tidsaxeln för att inspektera värden vid en specifik tidpunkt
* **Skala Y-axlar** — slår på eller av automatisk skalning av Y-axeln för att passa synliga data

### Uppdateringsintervall

Styr hur ofta grafen uppdateras med ny data:

* **0 s** — uppdateras kontinuerligt
* **1 s** — uppdateras varje sekund
* **5 s** — uppdateras var 5:e sekund
* **10 s** — uppdateras var 10:e sekund

### Tidsintervall

Styr det tidsintervall som visas i grafen:

* **30 s**, **5 min**, **1 h**, **6 h**
* **1 dag**, **7 dagar**, **14 dagar**, **30 dagar**
