---
title: Styrkurva Tid
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Styrkurva tid

Styrkurva tid-popup är ett tidsbaserat styrkurveverktyg som mappar tid på dygnet
på X-axeln mot utgångsvärden på Y-axeln med hjälp av ett antal dragbara noder
förbundna med linjer. Den används för att konfigurera utgångsvärden som varierar
under dagen — till exempel för att variera ett trycksbörvärde eller övervaka
förväntade processvärden under ett dygn. Den visas bara i Tab-menyn när objektet
har signaler som matchar de konfigurerade suffixaliasen.

För den vanliga styrkurvan där X-axeln är ett numeriskt processvärde i stället för
tid, se [Styrkurva](Control%20curve.md).

![Styrkurva tid-popup](/docs/sv/Images/Popups/Control_CurveTime.png)

## Styrkurvegrafen

Grafen visar den aktuella kurvan som ett antal noder förbundna med linjer längs en
fast tidsaxel från 00:00 till 24:00. En blå vertikal linje markerar aktuell tid på
dygnet och en rosa horisontell linje visar det aktuella procesvärdet som referens.

När en sparad profil läses in visas den som en streckad linje bredvid den aktiva
kurvan, vilket gör det möjligt att jämföra de två innan profilen tillämpas. Den
rosa streckade ramen visar det konfigurerade klämintervallet för Y-axeln (se [Klämintervall](#klamintervall)).

Noder på den aktiva kurvan kan dras för att justera kurvans form, eller redigeras
direkt i datapunktstabellen nedanför grafen.

* **Nodposition** — visar aktuell tid och Y-värde för den valda noden
* **Lås X-axeln för drag och släpp** — när aktiverat kan noder bara förflyttas
vertikalt, vilket förhindrar oavsiktliga ändringar av tidsvärdena
* **Datapunktstabellen** — visar tid- och Y-värden för varje nod med sina enheter.
Värden kan redigeras direkt i tabellen som ett alternativ till att dra noderna

## Klämintervall

Ett klämintervall anger hårda gränser för Y-axeln på kurvan. När ett klämintervall
är konfigurerat kan noder inte flyttas ovanför det högsta eller nedanför det lägsta
klämvärdet, vilket begränsar redigeringen till ett definierat driftintervall.

Klämbegränsningarna visas som en rosa streckad ram i grafen.

Klämvärdena lagras som en del av profilen och sparas och läses in tillsammans med
den. Fälten **Kläm min** och **Kläm max** i profilpanelen kräver privilegiet
`ControlCurve_EditProfiles` för att redigeras.

## Sparade profiler

Panelen **Sparade profiler** gör det möjligt att spara, läsa in och hantera
kurvkonfigurationer. Det gör det enkelt att växla mellan olika dagliga scheman
eller återställa en känd konfiguration.

Följande åtgärder är tillgängliga:

* **Hämta från graf** — läser in den aktiva kurvans värden i profilredigeraren
för förhandsgranskning eller sparande
* **Spara recept** — sparar profilredigerarens aktuella värden som ett namngivet
recept i databasen
* **Använd recept** — tillämpar det inlästa receptet på den aktiva kurvan
* **Skapa nytt recept** — skapar en ny tom profilplats
* **Byt namn** — byter namn på det valda receptet
* **Ta bort recept** — tar bort det valda receptet från databasen
* **Autoskala axlar** — justerar automatiskt Y-axelns intervall för att passa
aktuell data

## Standardsuffixalias

Styrkurva tid-popup stöder upp till 17 tidsbaserade kurvpunkter
(`_FS_X0`/`_FS_Y0` till `_FS_X16`/`_FS_Y16`). X-axeln är fast låst till
00:00–24:00 och kan inte ändras.

| Suffix | Skrivbar | Beskrivning |
|---|---|---|
| `_FS_X0`, `_FS_Y0` | Nej | Ankarpunkt — skrivskyddade referensvärden |
| `_FS_X1`–`_FS_X16`, `_FS_Y1`–`_FS_Y16` | Ja | Redigerbara kurvpunkter, kräver privilegiet `ControlCurve_ManualControl` |
| `_FS_yMin` | Ja | Minsta Y-axelvärde |
| `_FS_yMax` | Ja | Högsta Y-axelvärde |

!!! note
    Skrivning till kurvpunkter kräver privilegiet `ControlCurve_ManualControl`.
    Användare utan detta privilegium kan visa kurvan men inte ändra den.

<!-- --8<-- [end:body] -->