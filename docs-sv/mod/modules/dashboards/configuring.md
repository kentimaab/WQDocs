---
title: Dashboards — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Dashboards — Konfigurering

## Parametrar — Gemensamma inställningar för alla widgetar { #parameters-common-settings-shared-by-all-widgets }

Alla widgetar delar en `Header`-parameter, en sträng, som anger den rubrik som visas på widgeten. Om den lämnas tom har widgeten en standardrubrik.

Parametrar som accepterar flera signaler eller grupper tar antingen en enskild sträng eller en array av strängar.

```javascript title="Single signal"
"MB.AS01.VS10_VMM1_E"
```

```javascript title="Multiple signals"
["MB.AS01.VS10_VMM1_E", "MB.AS01.VS10_VMM1_P"]
```

Vissa widgetar har en expanderingsknapp i det övre högra hörnet. Genom att klicka på den öppnas en fullskärmsversion av widgeten för en mer detaljerad vy.

Widgetar som visar en signallegende hanterar automatiskt överfyllnad. När det finns fler signaler än vad som får plats i legenden visas en knapp som anger hur många som är dolda. Genom att klicka på den öppnas fullskärmsvyn med alla signaler listade.

## Widgetar — Alla tillgängliga widgetar och deras parametrar { #widgets-all-available-widgets-and-their-parameters }

### Larmstatus { #alarm-status }

Visar larmantal — totalt, kvitterade och okvitterade.
<!-- --8<-- [end:body-1] -->

![Alarm Status](/docs/sv/Images/Dashboard/AlarmStatus.png){align=center}

<!-- --8<-- [start:body-2] -->
**Parametrar**

* `Grupp` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmrad { #alarm-row }

En kompakt larmindikator i en enda rad. Avsedd att placeras överst eller underst på en dashboard som ett tunt statusband.
<!-- --8<-- [end:body-2] -->

![Alarm Row](/docs/sv/Images/Dashboard/AlarmRow.png){align=center}

<!-- --8<-- [start:body-3] -->
**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmlista { #alarm-list }

Visar aktiva larm i en rullningsbar lista.
<!-- --8<-- [end:body-3] -->

![Alarm List](/docs/sv/Images/Dashboard/AlarmList.png){align=center}

<!-- --8<-- [start:body-4] -->
**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmlogg { #alarm-log }

Visar historiska larm i en rullningsbar lista.
<!-- --8<-- [end:body-4] -->

![Alarm Log](/docs/sv/Images/Dashboard/AlarmLog.png){align=center}

<!-- --8<-- [start:body-5] -->
**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmfrekvens { #alarm-frequency }

Visar hur ofta larm har utlösts.
<!-- --8<-- [end:body-5] -->

![Alarm Frequency](/docs/sv/Images/Dashboard/AlarmFrequency.png){align=center}

<!-- --8<-- [start:body-6] -->
**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmgraf { #alarm-graph }

En större graf för larmtrender och larmfördelning. Lämpar sig för dashboards där larmanalys är i fokus.
<!-- --8<-- [end:body-6] -->

![Alarm Graph](/docs/sv/Images/Dashboard/AlarmGraph.png){align=center}

<!-- --8<-- [start:body-7] -->
---

### Historik { #history }

Visar historiska signalvärden som en trendgraf. Legenden visar aktuella värden med enheter och decimalprecision.
<!-- --8<-- [end:body-7] -->

![History](/docs/sv/Images/Dashboard/History.png){align=center}

<!-- --8<-- [start:body-8] -->
Fälten **Från** och **Till** längst upp på dashboarden anger tidsintervallet. Hur intervallet tillämpas beror på vilken knapp som används:

* **Tillämpa** — tillämpar Från/Till-intervallet på alla Historik-widgetinstanser på dashboarden.
* **Kalenderikon** (på en enskild widget) — tillämpar Från/Till-intervallet enbart på den widgetinstansen, utan att påverka de övriga.
* **Återställ** — återställer alla Historik-widgetinstanser till standardfönstret på 5 minuter.

**Parametrar**

* `Signaler` — Signalsökväg eller array av signalsökvägar att visa.

---

### Nyckelvärde { #key-value }

Visar ett enskilt livevärde med konfigurerad enhet och decimalprecision. Accepterar vilket värde som helst i Datalager — interna variabler, drivsignaler och systemvariabler.
<!-- --8<-- [end:body-8] -->

![Key Value](/docs/sv/Images/Dashboard/KeyValue.png){align=center}

<!-- --8<-- [start:body-9] -->
**Parametrar**
<!-- --8<-- [end:body-9] -->

* `KeyValue` — Direkt variabelreferens (inte en sträng). Ange variabelns sökväg utan citattecken: `MB.AS01.LB01_P`, inte `"MB.AS01.LB01_P"`.

<!-- --8<-- [start:body-10] -->
---

### Signalvärdesvisning { #signal-value-display }

Visar aktuella livevärden för en eller flera signaler. Löser automatiskt upp enheter och decimalprecision från Datalager.
<!-- --8<-- [end:body-10] -->

![Signal Value Display](/docs/sv/Images/Dashboard/SignalValueDisplay.png){align=center}

<!-- --8<-- [start:body-11] -->
**Parametrar**

* `Signaler` — Signalsökväg eller array av signalsökvägar att visa.

---

### Cirkeldiagram { #pie-chart }

Visar realtidsfördelning av signaler som ett cirkeldiagram. Inkluderar en expanderingsknapp som öppnar en fullskärmsvy.
<!-- --8<-- [end:body-11] -->

![Pie Chart](/docs/sv/Images/Dashboard/PieChart.png){align=center}

<!-- --8<-- [start:body-12] -->
**Parametrar**

* `Signaler` — Array av signalsökvägar att visa.

---

### Stapeldiagram { #bar-chart }

Visar jämförelser av signalvärden som ett stapeldiagram över konfigurerbara tidsperioder. Lämpar sig för energijämförelser över tid. Inkluderar en expanderingsknapp som öppnar en fullskärmsvy.
<!-- --8<-- [end:body-12] -->

![Bar Chart](/docs/sv/Images/Dashboard/Widget.png){align=center}

<!-- --8<-- [start:body-13] -->
**Parametrar**

* `Signaler` — Array av signalsökvägar att visa.
* `Typ` — Aggregeringsläge. Bestämmer hur varje periods stapelvärde beräknas. Standardvärde är `Add`.
* `TimePeriod` — Tidsenheten för varje stapel: `"Day"`, `"Week"`, `"Month"` eller `"Year"`. Standardvärde är `"Month"`.
* `TimeSpan` — Antal perioder att visa. Standardvärde är `12`.

| `Typ` | Beskrivning |
|---|---|
| `Add` | Summerar alla loggade värden inom varje period. Används för momentana signaler såsom effekt, där summan representerar total förbrukad energi. |
| `Average` | Beräknar medelvärdet av alla loggade värden inom varje period. Används för kontinuerliga signaler såsom temperatur. |
| `Trend` | Visar skillnaden mellan det sista värdet i innevarande period och det sista värdet i föregående period. Används för signaler där förändringen från en period till nästa är det viktiga. |
| `Result` | Visar det senaste loggade värdet inom varje period. Används för signaler där tillståndet vid periodens slut är det viktiga. |

---

### Underhåll { #maintenance }

Visar underhållsuppgiftsstatus — aktiva, planerade och missade uppgifter. Ansluter direkt till underhållsmodulen. Ingen signalinmatning krävs.
<!-- --8<-- [end:body-13] -->

![Maintenance](/docs/sv/Images/Dashboard/Maintenance.png){align=center}

<!-- --8<-- [start:body-14] -->
## Nästa steg { #next-steps }

* [Utöka](extending.md) — egna widgetar, designmönster och felsökning
<!-- --8<-- [end:body-14] -->
