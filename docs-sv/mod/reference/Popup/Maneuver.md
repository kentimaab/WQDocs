---
title: Manöver
product: mod
page_type: reference
status: draft
last_reviewed: 2026-10-28
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->
# Manöver

Manöver-popupen tillhandahåller styrningsåtgärder för det valda objektet, till exempel
att växla mellan driftlägen eller ange manuella värden. Den visas endast i
Tab-menyn när objektet har signaler som matchar en eller flera av de konfigurerade
suffixaliaserna för Manöver-popupen.
<!-- --8<-- [end:body-1] -->

Popupen finns i två varianter, var och en med egna standardsuffixaliaser:
[Industri-varianten](#industry-variant) och [BMS-varianten](#bms-variant). Ett objekt
visar den variant vars suffixaliaser matchar objektets signaler.

## Industri-variant { #industry-variant }

<!-- --8<-- [start:industry] -->
![Manöver-popupen, Industri-varianten](/docs/sv/Images/Popups/ManeuverIndustry.png)

Industri-varianten (`ManoverIndustry.kvie`) är byggd för processutrustning såsom
pumpar och motorer. Förutom att växla läge låter den operatören ge ett manuellt
kommando och ett manuellt börvärde, visar varför ett objekt inte kan gå och kan
blockera ett objekt. Raderna som visas är:

* **Status** — ett kort överst som visar objektets aktuella tillstånd.
* **Driftläge** — växlar objektet mellan Auto och Manuell.
* **Manuell styrning** — knappar för Av och På för att styra objektet för hand. De
kan bara användas i Manuellt läge; tills dess anger raden att Manuell måste väljas.
* **Manuellt börvärde** — det börvärde operatören anger för hand. Det är gråat
medan objektet är i Auto eller blockerat.
* **Förregling** — en text som förklarar varför objektet inte kan gå just nu. Den
visas i orange under **Manuell styrning**, som "Interlock:" följt av orsaken, och
saknas när ingen förregling finns.
* **Blockering** — blockerar objektet så att det inte går, varken i Auto eller
Manuell. Raden visar om objektet är blockerat. För att blockera anger man en orsak
och trycker på **Blockera**; en orsak måste anges. Medan objektet är blockerat visar
raden **Blockerad**, orsaken, användaren som satte blockeringen och tiden, och
knappen byter till att häva blockeringen. När den hävs går objektet tillbaka till det
läge det hade.
* **Statusvärden** — skrivskyddade värden såsom varvtal och effekt.

![Blockeringsraden för ett blockerat objekt](/docs/sv/Images/Popups/ManeuverIndustryBlocked.png)

En styrning är aktiverad endast när användaren har den behörighet som krävs, objektet
inte är blockerat och, där en låssignal är konfigurerad, objektet är i Manuell.

Orsak, användare och tid för varje blockering sparas i tabellen `object_blocks` i
[Config-databasen](../database-schemas/config-db.md#blocking).

### Standardsuffixaliaser

Följande suffixaliaser är konfigurerade för Industri-varianten som standard:

| Suffixalias | Suffix | Skrivbar | Beskrivning |
|---|---|---|---|
| `mode` | `_MODE` | Ja | Driftläge (Auto / Manuell) |
| `manualCommand` | `_MANCMD` | Ja | Manuell styrning |
| `manualSetpoint` | `_MANSP` | Ja | Manuellt börvärde |
| `block` | `_BLOCK` | Ja | Blockering |
| `interlock` | `_ILKTXT` | Nej | Förregling |
| `analogOutputValue` | `_R` | Nej | Analog utgångssignal |
| `isOpen` | `_IO` | Nej | Öppet läge |
| `RPM` | `_RPM` | Nej | Varvtal |
| `Effekt` | `_Effekt` | Nej | Effekt |

!!! note
    Standardsuffixaliaserna kan ändras och utökas under
    **Inställningar → Suffix → Suffix - Popups**. Se [Skapa popup](../../guides/create-a-popup.md)
    för mer information.
<!-- --8<-- [end:industry] -->

## BMS-variant { #bms-variant }

![Maneuver popup](/docs/sv/Images/Popups/Maneuver.png)

<!-- --8<-- [start:body-2] -->
Den här varianten (`ManoverBMS.kvie`) är layouten som används för byggnadssystem. Den
visar ett avsnitt **Styrning** med de styrningsåtgärder som finns för objektet.
Layouten beror på vilka suffixaliaser som är konfigurerade och vilka signaler som
finns på objektet. Typiska element inkluderar:

* **Lägesknappar** — knappar för att växla mellan driftlägen som Auto,
Av och På. Det för närvarande aktiva läget visas med en grön statusindikator
ovanför motsvarande knapp.
* **Statusrader** — skrivskyddade indikatorer som visar aktuellt tillstånd för en signal
* **Värderader** — redigerbara fält för att ange manuella värden när en signal är
konfigurerad som skrivbar

### Standardsuffixaliaser

Följande suffixaliaser är konfigurerade för BMS-varianten som standard:

| Suffixalias | Suffix | Skrivbar | Beskrivning |
|---|---|---|---|
| `IO` | `_IO` | Ja | Av / På |
| `manualControl` | `_MAN` | Ja | Manuell styrning, digital utgång |
| `manualControlAnalogOutput` | `_MANA` | Ja | Manuell styrning, analog utgång |
| `manualAnalogOutputValue` | `_RMAN` | Ja | Manuell analog utgångssignal |
| `analogOutputValue` | `_R` | Nej | Analog utgångssignal |
| `commandOutput` | `_M` | Nej | Digital utgångssignal |
| `isOpen` | `_IO` | Nej | Öppet läge |
| `isClosed` | `_IS` | Nej | Stängt läge |
| `isActive` | `_IT` | Nej | Aktivt läge |
| `runningHours` | `_DT` | Nej | Drifttid |
| `runningHoursReset` | `_DTA` | Ja | Nollställning av drifttid |

!!! note
    Standardsuffixaliaserna kan ändras och utökas under
    **Inställningar → Suffix → Suffix - Popups**. Se [Skapa popup](../../guides/create-a-popup.md)
    för mer information.
<!-- --8<-- [end:body-2] -->
