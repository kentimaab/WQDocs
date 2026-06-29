---
title: Popups
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Popups

WideQuick innehåller en uppsättning inbyggda popups som ger detaljerad information och
styrning för enskilda objekt i processvyn. Popups öppnas genom att klicka på ett
`DynTouch`-objekt, vilket öppnar **Tab**-popupen som startpunkt. Därifrån kan
användaren navigera till de övriga tillgängliga popups via tabbmenyn längst upp.

Vilka popups som är tillgängliga för ett givet objekt beror på vilka signaler objektet
har. Vissa popups visas alltid oavsett objektets signaler, medan andra bara visas när
objektet har signaler som matchar de konfigurerade suffix-aliasena. För mer information
om hur suffix-alias fungerar, se
[Taggstruktur — Suffix-alias](../tag-structure.md#suffix-alias).

För att skapa en anpassad popup, se [Skapa popup](../../guides/create-a-popup.md).

---

### Alltid synliga

* [**Flik**](Tab.md) — startpunkten för alla popups. Visar en navigeringsmeny,
en objektöversikt samt en sammanfattning av aktiva larm och underhållsuppgifter.
* [**Historik**](History.md) — visar ett trenddiagram över loggade signaler för
det valda objektet.
* [**Trend**](Trend.md) — visar livevärdena för signaler för det valda objektet i ett
realtidsdiagram.
* [**Objektinfo**](ObjectInfo.md) — visar en rålista över alla signaler kopplade
till objektet, inklusive deras aktuella värden, enheter och typer.
* [**Underhåll**](Maintenance.md) — visar schemalagda underhållsuppgifter för
objektet och möjliggör att nya uppgifter skapas.
* [**Loggbok**](Logbook.md) — visar loggboksposter för objektet och möjliggör att
anteckningar skapas, redigeras och tas bort.
* [**Dokument**](Documents.md) — visar dokument kopplade till objektet och
möjliggör att nya dokument länkas.

---

### Suffixberoende

Dessa popups visas bara när objektet har signaler som matchar de konfigurerade
suffix-aliasena:

* [**Process**](Process.md) — visar processvärden och statussignaler för objektet.
* [**Manöver**](Maneuver.md) — ger styrningsåtgärder såsom att växla mellan
driftlägen eller ange manuella värden.
* [**Tidskanal**](Time-channel.md) — möjliggör att tidsbaserade scheman
konfigureras för objektet.
* [**Styrkurva**](Control%20curve.md) — en styrningskurveredigerare för att
konfigurera icke-linjära styrningsrelationer.
* [**Styrkurva Tid**](Control%20curveTime.md) — ett tidsbaserat styrkurveverktyg för att mappa utgångsvärden över ett dygn.
<!-- --8<-- [end:body] -->
