---
title: Maneuver
description: Overview of the Maneuver popup in WideQuick.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-10-28
tags: 
 - MOD
---
<!-- --8<-- [start:body-1] -->
# Maneuver

The Maneuver popup provides control actions for the selected object, such as
switching between operating modes or setting manual values. It only appears in the
Tab menu when the object has signals matching one or more of the configured suffix
aliases for the Maneuver popup.
<!-- --8<-- [end:body-1] -->

The popup comes in two variants, each with its own default suffix aliases: the
[BMS variant](#bms-variant) and the [Industry variant](#industry-variant). An object
shows the variant whose suffix aliases match its signals.

## BMS variant { #bms-variant }

![Maneuver popup](/docs/Images/Popups/Maneuver.png)

<!-- --8<-- [start:body-2] -->
This variant (`ManoverBMS.kvie`) is the layout used for building systems. It
displays a **Control** section with the control actions available for the object. The
layout depends on which suffix aliases are configured and which signals are present
on the object. Typical elements include:

* **Mode buttons** — buttons for switching between operating modes such as Auto,
Off, and On. The currently active mode is indicated by a green status indicator
above the corresponding button.
* **Status rows** — read-only indicators showing the current state of a signal
* **Value rows** — editable fields for entering manual values when a signal is
configured as writable

### Default suffix aliases

The following suffix aliases are configured for the BMS variant by default:

| Suffix alias | Suffix | Writable | Description |
|---|---|---|---|
| `IO` | `_IO` | Yes | Off / On |
| `manualControl` | `_MAN` | Yes | Manual control, digital output |
| `manualControlAnalogOutput` | `_MANA` | Yes | Manual control, analog output |
| `manualAnalogOutputValue` | `_RMAN` | Yes | Manual analog output signal |
| `analogOutputValue` | `_R` | No | Analog output signal |
| `commandOutput` | `_M` | No | Digital output signal |
| `isOpen` | `_IO` | No | Open state |
| `isClosed` | `_IS` | No | Closed state |
| `isActive` | `_IT` | No | Active state |
| `runningHours` | `_DT` | No | Running hours |
| `runningHoursReset` | `_DTA` | Yes | Reset of running hours |

!!! note
    The default suffix aliases can be modified and extended in
    **Settings → Suffix → Suffix - Popups**. See [Create Popup](../../guides/create-a-popup.md)
    for more information.
<!-- --8<-- [end:body-2] -->

## Industry variant { #industry-variant }

<!-- --8<-- [start:industry] -->
The Industry variant (`ManoverIndustry.kvie`) is built for process equipment such as
pumps and motors. In addition to switching mode, it lets the operator give a manual
command and a manual setpoint, shows why an object cannot run, and can block an
object. The rows it shows are:

* **Mode** — switches the object between Auto and Manuell.
* **Manual command** and **manual setpoint** — values the operator sets when the
object is in manual mode.
* **Interlock** — a text explaining why the object cannot run at the moment. The
row is empty when there is no interlock.
* **Blocking** — blocks the object so that it does not run, in either Auto or
Manuell. A reason must be entered to block an object, and lifting the block
returns the object to the mode it had.
* **Status values** — read-only values such as speed and power.

A control is enabled only when the user has the required privilege, the object is not
blocked and, where a locking signal is configured, the object is in Manuell.

The reason, the user and the time of each block are stored in the `object_blocks`
table in the [Config database](../database-schemas/config-db.md#blocking).

### Default suffix aliases

The following suffix aliases are configured for the Industry variant by default:

| Suffix alias | Suffix | Writable | Description |
|---|---|---|---|
| `mode` | `_MODE` | Yes | Operating mode (Auto / Manuell) |
| `manualCommand` | `_MANCMD` | Yes | Manual control |
| `manualSetpoint` | `_MANSP` | Yes | Manual setpoint |
| `block` | `_BLOCK` | Yes | Blocking |
| `interlock` | `_ILKTXT` | No | Interlock text |
| `analogOutputValue` | `_R` | No | Analog output signal |
| `isOpen` | `_IO` | No | Open state |
| `RPM` | `_RPM` | No | Speed |
| `Effekt` | `_Effekt` | No | Power |

!!! note
    The default suffix aliases can be modified and extended in
    **Settings → Suffix → Suffix - Popups**. See [Create Popup](../../guides/create-a-popup.md)
    for more information.
<!-- --8<-- [end:industry] -->
