---
title: Dashboards — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

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

![Alarm Status](/Images/Dashboard/AlarmStatus.png){align=center}

**Parametrar**

* `Grupp` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmrad { #alarm-row }

En kompakt larmindikator i en enda rad. Avsedd att placeras överst eller underst på en dashboard som ett tunt statusband.

![Alarm Row](/Images/Dashboard/AlarmRow.png){align=center}

**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmlista { #alarm-list }

Visar aktiva larm i en rullningsbar lista.

![Alarm List](/Images/Dashboard/AlarmList.png){align=center}

**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmlogg { #alarm-log }

Visar historiska larm i en rullningsbar lista.

![Alarm Log](/Images/Dashboard/AlarmLog.png){align=center}

**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmfrekvens { #alarm-frequency }

Visar hur ofta larm har utlösts.

![Alarm Frequency](/Images/Dashboard/AlarmFrequency.png){align=center}

**Parametrar**

* `Grupper` — Filtrera larm efter gruppnamn. Lämna tomt för att visa alla larm.

---

### Larmgraf { #alarm-graph }

En större graf för larmtrender och larmfördelning. Lämpar sig för dashboards där larmanalys är i fokus.

![Alarm Graph](/Images/Dashboard/AlarmGraph.png){align=center}

---

### Historik { #history }

Visar historiska signalvärden som en trendgraf. Legenden visar aktuella värden med enheter och decimalprecision.

![History](/Images/Dashboard/History.png){align=center}

Fälten **Från** och **Till** längst upp på dashboarden anger tidsintervallet. Hur intervallet tillämpas beror på vilken knapp som används:

* **Tillämpa** — tillämpar Från/Till-intervallet på alla Historik-widgetinstanser på dashboarden.
* **Kalenderikon** (på en enskild widget) — tillämpar Från/Till-intervallet enbart på den widgetinstansen, utan att påverka de övriga.
* **Återställ** — återställer alla Historik-widgetinstanser till standardfönstret på 5 minuter.

**Parametrar**

* `Signaler` — Signalsökväg eller array av signalsökvägar att visa.

---

### Nyckelvärde { #key-value }

Visar ett enskilt livevärde med konfigurerad enhet och decimalprecision. Accepterar vilket värde som helst i Datalager — interna variabler, drivsignaler och systemvariabler.

![Key Value](/Images/Dashboard/KeyValue.png){align=center}

**Parametrar**

* `KeyValue` — Direkt variabelreferens (inte en sträng). Ange variabelns sökväg utan citattecken: `MB.AS01.LB01_P`, inte `"MB.AS01.LB01_P"`.

---

### Signalvärdesvisning { #signal-value-display }

Visar aktuella livevärden för en eller flera signaler. Löser automatiskt upp enheter och decimalprecision från Datalager.

![Signal Value Display](/Images/Dashboard/SignalValueDisplay.png){align=center}

**Parametrar**

* `Signaler` — Signalsökväg eller array av signalsökvägar att visa.

---

### Cirkeldiagram { #pie-chart }

Visar realtidsfördelning av signaler som ett cirkeldiagram. Inkluderar en expanderingsknapp som öppnar en fullskärmsvy.

![Pie Chart](/Images/Dashboard/PieChart.png){align=center}

**Parametrar**

* `Signaler` — Array av signalsökvägar att visa.

---

### Stapeldiagram { #bar-chart }

Visar jämförelser av signalvärden som ett stapeldiagram över konfigurerbara tidsperioder. Lämpar sig för energijämförelser över tid. Inkluderar en expanderingsknapp som öppnar en fullskärmsvy.

![Bar Chart](/Images/Dashboard/Widget.png){align=center}

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

![Maintenance](/Images/Dashboard/Maintenance.png){align=center}

## Nästa steg { #next-steps }

* [Utöka](extending.md) — egna widgetar, designmönster och felsökning
<!-- --8<-- [end:body] -->
