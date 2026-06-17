---
title: Tidkanal
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Tidkanal

Tidkanal-popup:en låter användare konfigurera tidsbaserade scheman för det valda
objektet. Varje veckodag kan ha upp till två aktiva tidsperioder definierade av
på- och av-tider. Den visas bara i Tab-menyn när objektet har en signal
med suffixet `_TK`.

![Time Channel popup](/Images/Popups/Time-channel.png)

## Kanalstatus

Panelen uppe till höger visar tidkanalens aktuella status — om den är
aktiv eller inaktiv — tillsammans med en klocka som visar aktuell tid.

## Veckodagar

Avsnittet **Veckodagar** visar ett schema för varje veckodag. Varje dag
stöder två oberoende aktiva perioder, var och en definierad av en **På-tid** och
**Av-tid** i formatet `hhmm`. Kolumnen **Drifttid** visar den totala aktiva
tiden för den dagen. En rad **Total drifttid** längst ned visar den sammanlagda drifttiden
för alla veckodagar.

## Specialdagar

Avsnittet **Specialdagar** gör det möjligt att definiera olika scheman för specifika
datum. Följande typer av specialdagar finns tillgängliga:

* **Helgdagsafton** — dagen före en allmän helgdag
* **Helgdag** — allmänna helgdagar
* **Specialdag 1**, **Specialdag 2**, **Specialdag 3** — anpassade datum som kan
definieras genom att ange ett datum i formatet `MM-DD`

Varje specialdag stöder samma schema med två perioder som veckodagar.

## Manuell styrning

Panelen **Manuell styrning** gör det möjligt att åsidosätta tidkanalen manuellt:

* **Auto** — tidkanalen följer det konfigurerade schemat
* **Manuell** — tidkanalen styrs manuellt och schemat ignoreras

Tidkanalens aktuella utgångsstatus visas också:

* **Från** — tidkanalens utgång är för närvarande av
* **Till** — tidkanalens utgång är för närvarande på

## Spara och hämta

Knapparna **Spara** och **Hämta** gör det möjligt att spara den aktuella
schemakonfigurationen till databasen eller hämta en tidigare sparad konfiguration.

## Standardsuffix-alias

Tidkanal-popup:en använder ett stort antal suffix för att mappa varje tidsintervall till en
specifik signal. De viktigaste suffixen är:

| Suffixalias | Suffix | Beskrivning |
|---|---|---|
| `timechannelIsActive` | `_TK` | Anger om tidkanalen är aktiv |
| `timechannelManualControl` | `_TK1_0` | Växlar mellan Auto- och Manuellt läge |
| `timechannelManualCommand` | `_TK4_5` | Ställer in utgångsstatus i manuellt läge |

Varje dag och tidsintervall mappas till ett dedikerat suffix enligt mönstret
`_TK[register]_[index]`. Alla tidsintervallsuffix är skrivbara.
