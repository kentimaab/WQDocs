---
title: Symbolbibliotek
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Symbolbibliotek {#symbol-libraries}

WideQuick innehåller två typer av symbolbibliotek för att bygga processvyer —
grundläggande symboler och färdigkopplade symboler. Tillsammans täcker de de
vanligaste komponenterna inom byggautomation och processtyrningstillämpningar.

**Grundläggande symboler** finns i objektbiblioteket **COMPONENTS** och består av
geometriska former som representerar fysiska komponenter såsom motorer, pumpar, ventiler
och givare. De är byggstenarna för att skapa anpassade processobjekt.

**Färdigkopplade symboler** finns i objektbiblioteken **DAMPERS**, **MOTORS**,
**SENSORS**, **VALVES** och **OTHERS**. Dessa är helt förkonfigurerade objekt som
kombinerar en grundläggande symbol med ett `DynTouch`-objekt, värdevisningar och
statusindikatorer. I de flesta fall är färdigkopplade symboler den rekommenderade
startpunkten eftersom de bara kräver en taggkoppling för att fungera direkt.

!!! tip "Migrering från äldre projekt"
    När en vy importeras från ett äldre WideQuick-projekt uppgraderas alla symboler
    automatiskt till de nya versionerna. De nya symbolerna använder samma objekt-ID:n
    som de gamla, så ingen manuell ersättning krävs.

## Varför de nya symbolerna {#why-the-new-symbols}

De nya symbolerna ger rikare visuell återkoppling än sina föregångare genom ett
tvålageranimationssystem byggt av två koncentriska cirklar. GIF-bilden nedan visar
den nya symbolen som växlar mellan larm-, varnings- och aktiva tillstånd:

![New symbol](/Images/Symbol_Libraries/new_symbol.gif)

De äldre symbolerna stödde grundläggande dynamik — till exempel en enkel
färgändring vid larm. De nya symbolerna går längre och tillhandahåller två
oberoende animationslager:

* **Yttre cirkel** — visar en heltäckande färg när ett larm är aktivt, vilket ger
en tydlig bakgrundmarkering som förblir synlig även när den inre cirkeln inte blinkar
* **Inre cirkel** — blinkar i färgen för den aktiva kategorin med högst prioritet,
och växlar mellan larm-, varnings- och servicetillstånd

Det innebär att en användare direkt kan se både att ett larm är aktivt och dess
larmklass, utan att behöva öppna popup-fönstret. Tvålagersystemet innebär
också att flera tillstånd kan kommuniceras samtidigt — till exempel en aktiv
varning med en bakgrundslarmsmarkering.

Alla nya symboler är fullt kompatibla med
[Arbetsvy Animation](../../../guides/workview-animations.md)-systemet, vilket innebär
att de automatiskt svarar på alla konfigurerade animationskategorier utan någon
ytterligare konfiguration.

## Grundläggande symboler - COMPONENTS {#components}

Objektbiblioteket **COMPONENTS** innehåller bassymbolerna som används för att
representera fysiska komponenter i processvyer. Varje symbol inkluderar redan
tvålagersanimationssystemet, vilket gör dem redo att använda som byggstenar för
anpassade objekt.

Använd grundläggande symboler när de förkonfigurerade färdigkopplade symbolerna
inte passar dina behov och du vill bygga ett helt anpassat objekt. I de flesta fall
är de färdigkopplade symbolerna i biblioteken **DAMPERS**, **MOTORS**, **SENSORS**,
**VALVES** och **OTHERS** den rekommenderade startpunkten.

<div markdown style="display: flex; justify-content: center; align-items: center; gap: 1.5rem;">

![Components library1](/Images/Symbol_Libraries/componets1.png)

![Components  library2](/Images/Symbol_Libraries/componets2.png)

</div>

Följande symboler finns tillgängliga:

| Symbol | Beskrivning |
|---|---|
| `dynMeterUnit` | Energimätenhet |
| `dynRevolvingHeatExchanger` | Roterande värmeväxlare |
| `dynSYMBOL_KLOCKA` | Ursymbol |
| `dynSensorDifference` | Differentialgivare |
| `dynSensorDifferenceFar` | Differentialgivare — fjärrmonterad |
| `dynSensorDifferenceNear` | Differentialgivare — närmonterad |
| `dynSymbolDamper` | Digital spjäll |
| `dynSymbolDamperAnalog` | Analogt spjäll |
| `dynSymbolExpansionVessel` | Expansionskärl |
| `dynSymbolFlowMeter` | Flödesmätare |
| `dynSymbolFreq` | Frekvensomriktare |
| `dynSymbolGeneric` | Generisk symbol |
| `dynSymbolMotorCompressor` | Motorkompressor |
| `dynSymbolMotorFan` | Motorfläkt |
| `dynSymbolMotorPump` | Motorpump |
| `dynSymbolPushbutton` | Tryckknappar |
| `dynSymbolRotarySwitch` | Vredomkopplare — 2 lägen |
| `dynSymbolRotarySwitch3State` | Vredomkopplare — 3 lägen |
| `dynSymbolSensor` | Givare |
| `dynSymbolSensorDuctPipe` | Kanal-/rörmonterad givare |
| `dynSymbolSensorOutdoor` | Utomhusgivare |
| `dynSymbolTimer` | Timer |
| `dynSymbolValve2WayActuator` | 2-vägsventil med ställdon |
| `dynSymbolValve3WayActuator` | 3-vägsventil med ställdon |


Biblioteket **COMPONENTS** innehåller också en uppsättning stödobjekt såsom
statustexter, värdevisningar och indikatorer. Dessa är användbara när man bygger
anpassade objekt och kompletterar bassymbolerna. För mer information om att bygga
anpassade objekt, se [Skapa objekt](../../../guides/create-an-object.md).

## DAMPERS {#dampers}

Objektbiblioteket **DAMPERS** innehåller förkonfigurerade spjällobjekt för både
digitala och analoga spjäll. Varje objekt levereras med ett `DynTouch`-objekt,
statusindikatorer, en indikator för manuellt läge och en namnsetikett — redo att
kopplas till taggar genom att fylla i egenskaperna **Connection**, **Device**,
**Sys** och **ObjectName** på `DynTouch`-objektet.

![DAMPERS library](/Images/Symbol_Libraries/dampers_library.png)

Varje spjällobjekt finns i fyra orienteringar — **000**, **090**, **180** och
**270** grader — för att matcha layouten i processvyn.

Följande objekt finns tillgängliga:

| Objekt | Beskrivning |
|---|---|
| `dynDamperAnalog_000` | Analogt spjäll — 0° |
| `dynDamperAnalog_090` | Analogt spjäll — 90° |
| `dynDamperAnalog_180` | Analogt spjäll — 180° |
| `dynDamperAnalog_270` | Analogt spjäll — 270° |
| `dynDamper_000` | Digitalt spjäll — 0° |
| `dynDamper_090` | Digitalt spjäll — 90° |
| `dynDamper_180` | Digitalt spjäll — 180° |
| `dynDamper_270` | Digitalt spjäll — 270° |

### Förkonfigurerade indikatorer

Varje spjällobjekt innehåller följande förkonfigurerade visuella element:

* **Indikator för manuellt läge** — visar symbolen **H** när spjället är i manuellt
läge
* **Larmindikator** — övre statuscirkel blir röd när ett larm är aktivt
* **Varningsindikator** — nedre statuscirkel blir orange när en varning är aktiv
* **Statustext** — visar **Öppen** eller **Stängd** för digitala spjäll
* **Namnsetikett** — visar objektnamnet

De analoga spjällobjekten är förkonfigurerade för suffixaliaset `analogOutputValue`.
Spjällstrecket roterar för att återspegla det aktuella värdet av `analogOutputValue`
och anger visuellt öppningsläget. Linjens startposition kan ställas in för att
matcha om spjället är normalt öppet eller normalt stängt. Den aktuella
öppningsprocenten visas bredvid symbolen, till exempel `42 %`.

## MOTORS {#motors}

Objektbiblioteket **MOTORS** innehåller förkonfigurerade motorobjekt för
kompressorer, fläktar, pumpar, frekvensomriktare och roterande värmeväxlare. Varje
objekt levereras med ett `DynTouch`-objekt, statusindikatorer och en namnsetikett —
redo att kopplas till taggar genom att fylla i egenskaperna **Connection**,
**Device**, **Sys** och **ObjectName** på `DynTouch`-objektet.

<div markdown style="display: flex; justify-content: center; align-items: center; gap: 1.5rem;">

![MOTORS library1](/Images/Symbol_Libraries/motor_library1.png)

![MOTORS library2](/Images/Symbol_Libraries/motor_library2.png)

![MOTORS library3](/Images/Symbol_Libraries/motor_library3.png)

</div>

Varje motorobjekt finns i flera orienteringar för att matcha layouten i
processvyn. Suffixbokstaven anger riktningen för motorsymbolen:
**D** (ned), **L** (vänster), **R** (höger), **U** (upp).

Följande objekt finns tillgängliga:

| Objekt | Beskrivning |
|---|---|
| `dynMotorCompressor_000` | Motorkompressor — 0° |
| `dynMotorCompressor_090` | Motorkompressor — 90° |
| `dynMotorCompressor_180` | Motorkompressor — 180° |
| `dynMotorCompressor_270` | Motorkompressor — 270° |
| `dynMotorFanD_090` | Motorfläkt — riktad nedåt |
| `dynMotorFanD_270` | Motorfläkt — riktad nedåt, spegelvänd |
| `dynMotorFanL_000` | Motorfläkt — riktad vänster |
| `dynMotorFanL_180` | Motorfläkt — riktad vänster, spegelvänd |
| `dynMotorFanR_000` | Motorfläkt — riktad höger |
| `dynMotorFanR_180` | Motorfläkt — riktad höger, spegelvänd |
| `dynMotorFanU_090` | Motorfläkt — riktad uppåt |
| `dynMotorFanU_270` | Motorfläkt — riktad uppåt, spegelvänd |
| `dynMotorPumpD_090` | Motorpump — riktad nedåt |
| `dynMotorPumpD_270` | Motorpump — riktad nedåt, spegelvänd |
| `dynMotorPumpL_000` | Motorpump — riktad vänster |
| `dynMotorPumpL_180` | Motorpump — riktad vänster, spegelvänd |
| `dynMotorPumpR_000` | Motorpump — riktad höger |
| `dynMotorPumpR_180` | Motorpump — riktad höger, spegelvänd |
| `dynMotorPumpU_090` | Motorpump — riktad uppåt |
| `dynMotorPumpU_270` | Motorpump — riktad uppåt, spegelvänd |
| `dynRevolvingHeatExchanger1` | Roterande värmeväxlare |
| `dynFreq_000` | Frekvensomriktare — 0° |
| `dyn_Freq_090` | Frekvensomriktare — 90° |
| `dyn_Freq_180` | Frekvensomriktare — 180° |
| `dyn_Freq_270` | Frekvensomriktare — 270° |

### Förkonfigurerade indikatorer

Varje motorobjekt innehåller följande förkonfigurerade visuella element:

* **Larmindikator** — varningstriangel blir röd när ett larm är aktivt
* **Varningsindikator** — varningstriangel blir orange när en varning är aktiv
* **Statusindikatorer** — cirklar som visar aktiva tillstånd
* **Namnsetikett** — visar objektnamnet

Frekvensomriktarobjekten är dessutom förkonfigurerade för suffixaliaset
`analogOutputValue` och visar det aktuella utgångsvärdet med dess enhet,
till exempel `42 %`.

## SENSORS {#sensors}

Objektbiblioteket **SENSORS** innehåller förkonfigurerade givarobjekt för ett
brett urval av givarstyper, inklusive standardgivare, dubbla givare,
differentialgivare, digitala givare och utomhusgivare. Varje objekt levereras med
ett `DynTouch`-objekt, värdevisningar, statusindikatorer och en namnsetikett —
redo att kopplas till taggar genom att fylla i egenskaperna **Connection**,
**Device**, **Sys** och **ObjectName** på `DynTouch`-objektet.

<div markdown style="display: flex; justify-content: center; align-items: center; gap: 1.5rem;">

![Sensor library1](/Images/Symbol_Libraries/sensor_library1.png)

![Sensor library2](/Images/Symbol_Libraries/sensor_library2.png)

![Sensor library3](/Images/Symbol_Libraries/sensor_library3.png)

</div>

Varje givarobjekt finns i fyra orienteringar — **000**, **090**, **180** och
**270** grader — för att matcha layouten i processvyn.

Följande objekt finns tillgängliga:

| Objekt | Beskrivning |
|---|---|
| `dynSensorOutdoor` | Utomhusgivare |
| `dynSensor_000` | Standardgivare — 0° |
| `dynSensor_090` | Standardgivare — 90° |
| `dynSensor_180` | Standardgivare — 180° |
| `dynSensor_270` | Standardgivare — 270° |
| `DynSensorDual_000` | Dubbel givare — 0° |
| `DynSensorDual_090` | Dubbel givare — 90° |
| `dynSensorDual_180` | Dubbel givare — 180° |
| `dynSensorDual_270` | Dubbel givare — 270° |
| `dynSensorHeater_000` | Givare med värmeelement — 0° |
| `dynSensorSimple_000` | Enkel givare — 0° |
| `dynSensorSimple_090` | Enkel givare — 90° |
| `dynSensorSimple_180` | Enkel givare — 180° |
| `dynSensorSimple_270` | Enkel givare — 270° |
| `dynSensorDigital_000` | Digital givare — 0° |
| `dynSensorDigital_090` | Digital givare — 90° |
| `dynSensorDigital_180` | Digital givare — 180° |
| `dynSensorDigital_270` | Digital givare — 270° |
| `dynSensorDiff_000` | Differentialgivare — 0° |
| `dynSensorDiff_090` | Differentialgivare — 90° |
| `dynSensorDiff_180` | Differentialgivare — 180° |
| `dynSensorDiff_270` | Differentialgivare — 270° |
| `dynSensorDigitalDiffShort_000` | Kort digital differentialgivare — 0° |
| `dynSensorDigitalDiffShort_090` | Kort digital differentialgivare — 90° |
| `dynSensorDigitalDiffShort_180` | Kort digital differentialgivare — 180° |
| `dynSensorDigitalDiffShort_270` | Kort digital differentialgivare — 270° |
| `dynSensorDigitalDiff_000` | Digital differentialgivare — 0° |
| `dynSensorDigitalDiff_090` | Digital differentialgivare — 90° |
| `dynSensorDigitalDiff_180` | Digital differentialgivare — 180° |
| `dynSensorDigitalDiff_270` | Digital differentialgivare — 270° |
| `dynSensorDiff2_000` | Differentialgivare 2 — 0° |
| `dynSensorDiff2_090` | Differentialgivare 2 — 90° |
| `dynSensorDiff2_180` | Differentialgivare 2 — 180° |
| `dynSensorDiff2_270` | Differentialgivare 2 — 270° |

### Förkonfigurerade indikatorer

Varje givarobjekt innehåller följande förkonfigurerade visuella element:

* **Värdevisning** — visar det aktuella givarvärdet med dess enhet, till exempel
`21.5 °C`, kopplad till suffixaliaset `processValue`
* **Statusindikatorer** — cirklar som visar aktiva larm- och varningsstillstånd
* **Namnsetikett** — visar objektnamnet

Dubbla och differentiella givarobjekt visar två oberoende värdevisningar, var och
en kopplad till sitt eget suffixalias.

## VALVES {#valves}

Objektbiblioteket **VALVES** innehåller förkonfigurerade ventolobjekt för tvåvägs-
och trevägsventiler. Varje objekt levereras med ett `DynTouch`-objekt, värdevisningar,
statusindikatorer och en namnsetikett — redo att kopplas till taggar genom att fylla
i egenskaperna **Connection**, **Device**, **Sys** och **ObjectName** på
`DynTouch`-objektet.

![VALVES library](/Images/Symbol_Libraries/valves_library.png)

Varje ventolobjekt finns i fyra orienteringar — **000**, **090**, **180** och
**270** grader — för att matcha layouten i processvyn.

Följande objekt finns tillgängliga:

| Objekt | Beskrivning |
|---|---|
| `dynValveTwoWay_000` | Tvåvägsventil — 0° |
| `dynValveTwoWay_090` | Tvåvägsventil — 90° |
| `dynValveTwoWay_180` | Tvåvägsventil — 180° |
| `dynValveTwoWay_270` | Tvåvägsventil — 270° |
| `dynValveThreeWay_000` | Trevägsventil — 0° |
| `dynValveThreeWay_090` | Trevägsventil — 90° |
| `dynValveThreeWay_180` | Trevägsventil — 180° |
| `dynValveThreeWay_270` | Trevägsventil — 270° |

### Förkonfigurerade indikatorer

Varje ventolobjekt innehåller följande förkonfigurerade visuella element:

* **Positionsvisning** — visar den aktuella ventilpositionen som en procentandel,
till exempel `75 %`, kopplad till suffixaliaset `analogOutputValue`
* **Larmindikator** — varningstriangel blir röd när ett larm är aktivt
* **Varningsindikator** — varningstriangel blir orange när en varning är aktiv
* **Statusindikatorer** — cirklar som visar aktiva tillstånd
* **Namnsetikett** — visar objektnamnet

## OTHERS {#others}

Objektbiblioteket **OTHERS** innehåller förkonfigurerade objekt för komponenter
som inte passar in i de övriga fyra kategorierna. Varje objekt levereras med ett
`DynTouch`-objekt och relevanta visningar — redo att kopplas till taggar genom att
fylla i egenskaperna **Connection**, **Device**, **Sys** och **ObjectName** på
`DynTouch`-objektet.

![OTHERS library](/Images/Symbol_Libraries/other_library.png)

Följande objekt finns tillgängliga:

| Objekt | Beskrivning |
|---|---|
| `dynServiceCoupler_0-1` | Servicekoppling — 2 lägen |
| `dynServiceCoupler_0-1-2` | Servicekoppling — 3 lägen |
| `dynExpansionVessel` | Expansionskärl |
| `dynTimer` | Timer |
| `dynPushButton` | Tryckknapp |
| `dynFlowMeter` | Flödesmätare med två värdevisningar |
| `dynEnergyMeterSimple` | Energimätare — enkel, två värdevisningar |
| `dynEnergyMeter2` | Energimätare — kompakt |
| `dynEnergyMeter` | Energimätare — full, flera värdevisningar |

### Förkonfigurerade indikatorer

* **Servicekoppling** — visar en digital textetikett som anger det aktuella läget.
3-lägsvarianten stöder ytterligare ett mellanläge.
* **Flödesmätare** — visar två värdevisningar kopplade till egna suffixalias,
till exempel flödeshastighet och ackumulerad volym.
* **Energimätare** — visar energiförbrukningsvärden med enheter. Den fullständiga
`dynEnergyMeter` visar flera avläsningar medan `dynEnergyMeterSimple` och
`dynEnergyMeter2` visar en mer kompakt vy.
* **Timer**, **Tryckknapp** och **Expansionskärl** — inkluderar statusindikatorer
och en namnsetikett.


<!-- --8<-- [end:body] -->
