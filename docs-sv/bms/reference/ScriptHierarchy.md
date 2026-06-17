---
title: Skriptberoenden
product: bms
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - BMS
---

# Skriptberoenden

Den här sidan listar alla skript i WideQuick BMS och deras beroenden.
Ett skript som listas under **Kräver** måste finnas och köra för att skriptet ska
fungera korrekt.

## Beroendegraf

Grafen nedan visar alla skript grupperade efter beroendeskikt — från fristående
skript högst upp till de mest komplexa kedjorna längst ner. Klicka på en nod för att
markera dess direkta beroenden och beroende skript. Använd lagerknapparna för att fokusera
på en specifik nivå.

<div markdown>

--8<-- "mod/reference/Script_Widget.html"

</div>

## Referenstabeller

### Inga beroenden

Följande skript har inga beroenden och kan köra fristående:

* `scAlert`
* `scQuickSort`
* `scKeybindings`
* `scModem`
* `scOSK`

### Enkelt beroende

| Skript | Kräver |
|---|---|
| `scDatabase` | `scAlert` |
| `scObjectFinder` | `scAlert` |
| `scUsers` | `scAlert` |
| `scPrototypes` | `scAlert` |
| `scPlatform` | `scAlert` |
| `scThemes` | `scAlert` |
| `scSuffix` | `scAlert` |
| `scLogBook` | `scAlert` |
| `scAuditTrail` | `scAlert` |
| `scRemoteClients` | `scAlert` |
| `scRemoteSystems` | `scAlert` |
| `scTimeChannel` | `scAlert` |
| `scToolTip` | `scAlert` |
| `scTrend` | `scAlert` |
| `scWM` | `scAlert` |
| `scWeather` | `scAlert` |
| `scMapObjects` | `scAlert` |
| `scButtons` | `scAlert` |
| `scInit` | `scAlert` |
| `scSimMB` | `scAlert` |
| `scMail` | `scAlert` |
| `scReports` | `scAlert` |

### Flera beroenden

| Skript | Kräver |
|---|---|
| `scMaintenance` | `scAlert`, `scDatabase` |
| `scSubNav` | `scAlert`, `scUsers`, `scSuffix` |
| `scHistory` | `scAlert`, `scPrototypes`, `scQuickSort`, `scThemes` |
| `scNav` | `scAlert`, `scThemes` |
| `scFilePicker` | `scAlert`, `scThemes` |
| `scAlarm` | `scAlert`, `scPrototypes` |
| `scMap` | `scAlert`, `scThemes`, `scMaintenance` |
| `scSubNavPopup` | `scAlert`, `scUsers`, `scSubNav` |
| `scLinking` | `scAlert`, `scPrototypes`, `scSubNav`, `scObjectFinder` |
| `scSmartPopup` | `scAlert`, `scPrototypes`, `scUsers`, `scSuffix` |
| `scStyrkurva` | `scAlert`, `scSuffix` |
| `scStyrkurvaTid` | `scAlert`, `scSuffix` |
| `scWorkviewAnimation` | `scAlert`, `scSuffix` |
| `scRemoteAlarms` | `scAlert`, `scAlarm` |
| `scReportScheduler` | `scAlert`, `scReports` |
| `scAlarmSender` | `scAlert`, `scMail` |
| `scCalendar` | `scAlert`, `scThemes`, `scMaintenance` |
| `scDashboard` | `scAlert`, `scHistory` |
| `scDoc` | `scAlert`, `scThemes`, `scLinking` |
| `scAlarmFinder` | `scAlert`, `scObjectFinder`, `scLinking`, `scMap` |
| `scDayViewManager` | `scAlert`, `scThemes`, `scCalendar` |
| `scWeekViewManager` | `scAlert`, `scThemes`, `scCalendar` |
