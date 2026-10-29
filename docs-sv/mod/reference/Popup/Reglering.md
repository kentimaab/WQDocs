---
title: Reglering
product: mod
page_type: reference
status: draft
last_reviewed: 2026-10-27
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Reglering

Popupen Reglering visar och ställer in det valda objektets regleringsparametrar, till
exempel börvärde och PID-värden. Den visas endast i flikmenyn när objektet har
signaler som matchar ett eller flera av de konfigurerade suffixaliasen för popupen
Reglering.

![Popupen Reglering](/docs/sv/Images/Popups/Reglering.png)

## Börvärde

Avsnittet för börvärde visar börvärdet, det beräknade börvärdet samt de gränser och
den förskjutning som tillämpas på det:

* **Börvärde** — det önskade värde som regulatorn styr mot.
* **Beräknat börvärde** — det börvärde som faktiskt används efter att gränser och
förskjutning har tillämpats. Det är skrivskyddat.
* **Börvärde låg / hög** — lägsta och högsta börvärde som kan användas.
* **Börvärdesförskjutning** — en förskjutning som läggs på börvärdet.

## Regleringsparametrar

Regleringsparametrarna är regulatorns inställningsvärden:

* **P-faktor** — proportionell förstärkning.
* **I-tid** — integrationstid.
* **D-tid** — derivatatid.
* **Samplingstid** — hur ofta regulatorn beräknar en ny utsignal.
* **Dödband** — området kring börvärdet inom vilket regulatorn inte agerar.

För regulatorer med två regleringssekvenser finns samma parametrar en gång till för
**sekvens 2**, tillsammans med en **dödzon** mellan sekvens 1 och sekvens 2. Endast
raderna för de signaler som objektet har visas.

## Standardsuffixalias

Följande suffixalias är konfigurerade för popupen Reglering som standard:

| Suffixalias | Suffix | Skrivbar | Beskrivning |
|---|---|---|---|
| `setpoint` | `_BV` | Ja | Börvärde |
| `setpointCalculated` | `_BB` | Nej | Beräknat börvärde |
| `limitLow` | `_BVL` | Ja | Börvärde låg |
| `limitHigh` | `_BVH` | Ja | Börvärde hög |
| `setpointShift` | `_BVF` | Ja | Börvärdesförskjutning |
| `pFactor` | `_CP` | Ja | P-faktor |
| `iTime` | `_CI` | Ja | I-tid |
| `dTime` | `_CD` | Ja | D-tid |
| `sampleTime` | `_CS` | Ja | Samplingstid |
| `deadband` | `_CH` | Ja | Dödband |
| `pFactor2` | `_2_CP` | Ja | P-faktor sekvens 2 |
| `iTime2` | `_2_CI` | Ja | I-tid sekvens 2 |
| `dTime2` | `_2_CD` | Ja | D-tid sekvens 2 |
| `sampleTime2` | `_2_CS` | Ja | Samplingstid sekvens 2 |
| `deadband2` | `_2_CH` | Ja | Dödband sekvens 2 |
| `deadZone` | `_CZ` | Ja | Dödzon sekvens 1-2 |

!!! note
    Standardsuffixaliasen kan ändras och utökas i
    **Inställningar → Suffix → Suffix - Popups**. Se [Skapa popup](../../guides/create-a-popup.md)
    för mer information.
<!-- --8<-- [end:body] -->
