---
title: Styrkurva
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Styrkurva

Styrkurvans popup är en editor för styrkurvor som mappar indatavärden på
X-axeln till utdatavärden på Y-axeln med hjälp av ett antal draggbara noder
förbundna med linjer. Den används för att konfigurera icke-linjära
styrrelationer — till exempel för att mappa en utetemperatur till en
värmeventilinställning. Den visas endast i flikmenyn när objektet har
signaler som matchar de konfigurerade suffixaliaserna.

![Control Curve popup](/Images/Popups/Control%20Curve.png)

## Styrkurvegraf

Grafen **Styrkurva** visar den aktuella kurvan som en serie noder förbundna
med linjer. Noder kan dras för att justera kurvans form, eller redigeras
direkt i datapunktstabellen nedanför grafen. En referenssignal visas som en
horisontell linje i grafen och indikerar det aktuella indatavärdet.

* **Nodposition** — visar X- och Y-koordinaterna för den aktuellt valda noden
* **Lås X-axel för drag och släpp** — när detta är aktiverat kan noder bara
  flyttas vertikalt, vilket förhindrar oavsiktliga ändringar av X-axelns värden
* **Datapunktstabell** — visar X- och Y-värden för varje nod med tillhörande
  enheter. Värdena kan redigeras direkt i tabellen som ett alternativ till att
  dra

## Sparade recept

Panelen **Sparade recept** gör det möjligt att spara, läsa in och hantera
kurvkonfigurationer. Detta gör det enkelt att växla mellan olika
styrkurveinställningar eller återställa en känd fungerande konfiguration.

Följande åtgärder finns tillgängliga:

* **Hämta från graf** — läser in de aktuella live-kurvevärdena i
  receptredigeraren för förhandsvisning eller sparande
* **Spara recept** — sparar de aktuella värdena i receptredigeraren som ett
  namngivet recept i databasen
* **Använd recept** — tillämpar det inlästa receptet på livekurvan
* **Skapa nytt recept** — skapar en ny tom receptplats
* **Byt namn** — byter namn på det aktuellt valda receptet
* **Ta bort recept** — tar bort det aktuellt valda receptet från databasen
* **Autoskala axlar** — justerar automatiskt axlarnas skalor för att passa
  aktuell data

## Standardsuffixalias

Styrkurvans popup använder X- och Y-koordinatpar för att definiera
styrkurvans punkter. Upp till 19 punkter stöds (`_X0`/`_Y0` till
`_X18`/`_Y18`):

| Suffix | Skrivbar | Beskrivning |
|---|---|---|
| `_X0`, `_Y0` | Nej | Ankarpunkt — skrivskyddade referensvärden |
| `_X1`–`_X18`, `_Y1`–`_Y18` | Ja | Redigerbara kurvpunkter, kräver privilegiet `ControlCurve_ManualControl` |
| `_yMin` | Ja | Minsta Y-axelvärde |
| `_yMax` | Ja | Högsta Y-axelvärde |

!!! note
    Skrivning till kurvpunkter kräver privilegiet `ControlCurve_ManualControl`.
    Användare utan detta privilegium kan visa kurvan men kan inte ändra den.
