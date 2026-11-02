---
title: Rapporter
description: Översikt över modulen Rapporter i WideQuick MOD, som genererar, schemalägger och anpassar rapporter baserade på larm- och energidata.
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-12
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Rapporter
WideQuick Modular Framework inkluderar en inbyggd rapportmodul för att generera, schemalägga och anpassa rapporter baserade på larm- och energidata. Det här avsnittet
täcker allt från att använda standardmallarna till att skapa helt egna mallar.

## Innehåll { #contents }

### [Kom igång](get-started.md) { #get-started }
* [**Konfigurera rapportverktyget**](get-started.md#setting-up-the-reporter) — Hur rapportmallar läggs till och konfigureras i **WideQuick® Designer**.
* [**Använda rapportverktyget**](get-started.md#using-the-reporter-in-widequick-runtime) —
Introduktion till att generera rapporter i **WideQuick® Runtime**.
* [**Schemalägga en rapport**](get-started.md#scheduling-a-report-in-widequick-runtime) — Hur återkommande schemalagda rapporter ställs in.
* [**Hantera scheman**](get-started.md#managing-schedules) — Redigera och ta bort scheman, och panelen SMTP och GSM.

---

### [Konfigurering](configuring.md) { #configuring }
* [**Larmrapport**](configuring.md#alarm-report) — Hur den fungerar och hur den konfigureras om.
* [**Larmrapport ett larm**](configuring.md#alarm-report-one-alarm) — Hur den fungerar och hur den konfigureras om.
* [**Energirapport**](configuring.md#energy-report) — Hur den fungerar och hur den konfigureras om.
* [**Energirapport vecka**](configuring.md#energy-report-week) — Hur den fungerar och hur den konfigureras om.
* [**Rapporthistorik**](configuring.md#report-history) — Var den finns och hur den används.

---

### [Utöka](extending.md) { #extending }
* [**Skapa mallar**](extending.md#creating-templates) — Hur en egen rapportmall designas och konfigureras.
* [**Skapa en ReportController**](extending.md#creating-the-reportcontroller-view) — Hur en ReportController-vy skapas för en egen mall.
* [**Ändra maximalt antal signaler**](extending.md#changing-the-maximum-of-signals-to-be-selected) — Hur signalgränsen för rapportgenerering ökas.
* [**Lägg till en basenhet**](extending.md#adding-a-base-unit) — Hur egna enheter läggs till i enhetssystemet.
* [**Behörigheter**](extending.md#privileges) — De behörigheter som styr scheman och SMTP.

---

### [Felsökning](troubleshooting.md) { #troubleshooting }
* [**Vanliga problem**](troubleshooting.md) — Vanliga problem och hur de löses.
<!-- --8<-- [end:body] -->
