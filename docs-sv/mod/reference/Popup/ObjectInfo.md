---
title: Objektinfo
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Objektinfo

Popup-fönstret Objektinfo visar en rålista över alla signaler som är kopplade till det
valda objektet, hämtade direkt från DataStore. Det är alltid synligt i Tab-menyn
oavsett vilka suffix objektet har. Det är främst användbart för felsökning och
verifiering av att rätt signaler är kopplade till objektet.

![Objektinfo popup](/Images/Popups/ObjectInfo.png)

## Objektinformation

Tabellen visar alla signaler som tillhör objektet med följande kolumner:

* **Suffix** — signalens taggsuffix, till exempel `_MV` eller `_LG`
* **Suffixbeskrivning** — beskrivningen av suffixet enligt konfigurationen i
suffixaliasinställningarna
* **Värde** — signalens aktuella livevärde
* **Enhet** — signalens enhet enligt konfigurationen i suffixaliasinställningarna
* **Variabeltyp** — signalens datatyp, till exempel `number` eller `boolean`
* **Taggbeskrivning** — beskrivningen som angetts för taggen i **Taggeditorn**
