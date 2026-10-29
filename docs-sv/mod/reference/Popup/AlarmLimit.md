---
title: Larmgränser
product: mod
page_type: reference
status: draft
last_reviewed: 2026-10-27
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Larmgränser

Popupen Larmgränser samlar det valda objektets larmgränser och larmfördröjningar på
ett ställe, så att de kan läsas av och justeras utan att lämna processvyn. Den visas
endast i flikmenyn när objektet har signaler som matchar ett eller flera av de
konfigurerade suffixaliasen för popupen Larmgränser.

![Popupen Larmgränser](/docs/sv/Images/Popups/AlarmLimit.png)

## Gränser och fördröjningar

Varje rad visar signalens beskrivning och dess aktuella värde. Värdena kan redigeras
direkt i raden, eftersom standardsuffixaliasen är konfigurerade som skrivbara. Endast
raderna för de signaler som objektet har visas. Raderna delas in i två grupper:

* **Gränser** — det värde vid vilket ett larm utlöses, till exempel övre eller undre
gräns för en regleravvikelse, eller drifttidsgränsen.
* **Fördröjningar** — den tid ett tillstånd måste bestå innan larmet utlöses, till
exempel för ett fel eller för en ventil som inte når sitt öppna eller stängda läge.

För hur larm konfigureras och hanteras, se [Larm](../../modules/Core/alarms/index.md).

## Standardsuffixalias

Följande suffixalias är konfigurerade för popupen Larmgränser som standard:

| Suffixalias | Suffix | Skrivbar | Beskrivning |
|---|---|---|---|
| `alarmHighLimit` | `_LAH_GL` | Ja | Larmgräns regleravvikelse hög |
| `alarmHighDelay` | `_LAH_FL` | Ja | Larmfördröjning regleravvikelse hög |
| `alarmLowLimit` | `_LAL_GL` | Ja | Larmgräns regleravvikelse låg |
| `alarmLowDelay` | `_LAL_FL` | Ja | Larmfördröjning regleravvikelse låg |
| `lowAlarmLimit` | `_LL_GL` | Ja | Larmgräns låg |
| `lowAlarmDelay` | `_LL_FL` | Ja | Larmfördröjning låg |
| `positionLimit` | `_LA_GL` | Ja | Larmgräns avvikande läge |
| `positionDelay` | `_LA_FL` | Ja | Larmfördröjning avvikande läge |
| `notOpenDelay` | `_LAO_FL` | Ja | Larmfördröjning öppnar ej |
| `notCloseDelay` | `_LAS_FL` | Ja | Larmfördröjning stänger ej |
| `runTimeLimit` | `_DTL_GL` | Ja | Larmgräns drifttidslarm |
| `faultDelay` | `_LD_FL` | Ja | Larmfördröjning driftfel |
| `notAutoDelay` | `_LM_FL` | Ja | Larmfördröjning ej i auto |
| `alarmDelay` | `_L_FL` | Ja | Larmfördröjning |

!!! note
    Standardsuffixaliasen kan ändras och utökas i
    **Inställningar → Suffix → Suffix - Popups**. Se [Skapa popup](../../guides/create-a-popup.md)
    för mer information.
<!-- --8<-- [end:body] -->
