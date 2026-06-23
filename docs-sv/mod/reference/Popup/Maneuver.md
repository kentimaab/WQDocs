---
title: Manöver
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Manöver

Manöver-popupen tillhandahåller styrningsåtgärder för det valda objektet, till exempel
att växla mellan driftlägen eller ange manuella värden. Den visas endast i
Tab-menyn när objektet har signaler som matchar en eller flera av de konfigurerade
suffixaliaserna för Manöver-popupen.

![Maneuver popup](/docs/sv/Images/Popups/Maneuver.png)

## Styrning

Avsnittet **Styrning** visar tillgängliga styrningsåtgärder för objektet. Layouten
beror på vilka suffixaliaser som är konfigurerade och vilka signaler som finns på
objektet. Typiska element inkluderar:

* **Lägesknappar** — knappar för att växla mellan driftlägen som Auto,
Av och På. Det för närvarande aktiva läget visas med en grön statusindikator
ovanför motsvarande knapp.
* **Statusrader** — skrivskyddade indikatorer som visar aktuellt tillstånd för en signal
* **Värderader** — redigerbara fält för att ange manuella värden när en signal är
konfigurerad som skrivbar

## Standardsuffixaliaser

Följande suffixaliaser är konfigurerade för Manöver-popupen som standard:

| Suffixalias | Suffix | Skrivbar | Beskrivning |
|---|---|---|---|
| `analogOutputValue` | `_R` | Ja | Analog utgångssignal |
| `commandOutput` | `_M` | Ja | Digital utgångssignal |
| `manualControl` | `_MAN` | Ja | Manuell digital utgång |

!!! note
    Standardsuffixaliaserna kan ändras och utökas under
    **Inställningar → Suffix → Suffix - Popups**. Se [Skapa popup](../../guides/create-a-popup.md)
    för mer information.
