---
title: Manover
description: Overview of the Manover popup in WideQuick.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-05-29
---
<!-- --8<-- [start:body] -->

# Manover

The Manover popup provides control actions for the selected object, such as
switching between operating modes or setting manual values. It only appears in the
Tab menu when the object has signals matching one or more of the configured suffix
aliases for the Manover popup.

![Manover popup](/Images/Popups/Manover.png)

## Control

The **Control** section displays the available control actions for the object. The
layout depends on which suffix aliases are configured and which signals are present
on the object. Typical elements include:

* **Mode buttons** — buttons for switching between operating modes such as Auto,
Off, and On. The currently active mode is indicated by a green status indicator
above the corresponding button.
* **Status rows** — read-only indicators showing the current state of a signal
* **Value rows** — editable fields for entering manual values when a signal is
configured as writable

## Default suffix aliases

The following suffix aliases are configured for the Manover popup by default:

| Suffix alias | Suffix | Writable | Description |
|---|---|---|---|
| `analogOutputValue` | `_R` | Yes | Analog output signal |
| `commandOutput` | `_M` | Yes | Digital output signal |
| `manualControl` | `_MAN` | Yes | Manual digital output |

!!! note
    The default suffix aliases can be modified and extended in
    **Settings → Suffix → Suffix - Popups**. See [Create Popup](../../guides/create-a-popup.md)
    for more information.