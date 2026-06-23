---
title: Process
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Process

Processp-popupen visar processvärden och statussignaler kopplade till det
valda objektet. Den visas endast i flikmenyn när objektet har signaler som
matchar ett eller flera av de konfigurerade suffixaliasen för Process-popupen.

För en guide om hur du skapar och konfigurerar en anpassad Process-popup, se
[Skapa popup](../../guides/create-a-popup.md).

![Process popup](/docs/sv/Images/Popups/Process.png)

## Värden

Avsnittet **Värden** listar alla processsignaler kopplade till objektet. Varje rad
visar signalbeskrivningen, dess aktuella värde och enhet. Utseendet på varje rad
beror på signaltypen och om den är konfigurerad som skrivbar i
**Inställningar → Suffix → Suffix - Popups**:

* **Numeriska värden** — visas som ett skrivskyddat värde med sin enhet. Om
konfigurerat som skrivbart kan värdet redigeras direkt i raden.
* **Booleska värden** — visas som en statusindikator när skrivskyddade, eller som en
växlingsknapp när konfigurerade som skrivbara.

## Standardsuffixalias

Följande suffixalias är konfigurerade för Process-popupen som standard:

| Suffixalias | Suffix | Beskrivning |
|---|---|---|
| Flöde | `_LPM` | Flöde |
| Grumlighet | `_TURB` | Grumlighet |
| Kemisk Syreförbrukning | `_COD` | Kemisk syreförbrukning |
| Konduktivitet | `_COND` | Konduktivitet |
| Nivå | `_LEVEL` | Nivå |
| Temperatur | `_TEMP` | Temperatur |
| Tryck | `_PRESS` | Tryck |
| Upplöst Syre | `_DO` | Löst syre |
| Uppsuspenderade partiklar | `_TSS` | Totalt suspenderade partiklar |
| pH | `_pH` | pH |

!!! note
    Standardsuffixaliasen kan ändras och utökas i
    **Inställningar → Suffix → Suffix - Popups**. Se [Skapa popup](../../guides/create-a-popup.md)
    för mer information.
