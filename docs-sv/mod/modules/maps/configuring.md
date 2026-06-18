---
title: Kartor och indikatorer — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Kartor och indikatorer — Konfigurering

Det här avsnittet beskriver hur du konfigurerar de mer avancerade kartindikatorerna, inklusive Pin
Status, klusterpinnar, linjer och filter. För att komma igång med att sätta upp ett **Map View**-objekt och
lägga till grundläggande indikatorer, se [Kartor och indikatorer — Kom igång](get-started.md).

## Konfigurera indikatorer { #configuring-indicators }

Följande indikatorer finns tillgängliga i objektbiblioteket **Map Indicators** och
läggs till på samma sätt som beskrivs i
[Kartor och indikatorer — Kom igång](get-started.md). Varje indikator har egenskaper som
måste konfigureras för att fungera korrekt — dessa beskrivs i avsnitten nedan.

### Pin Status { #pin-status }
Pin Status-objekt är nyckeln till att koppla en **Map View** till **arbetsvyer**. De
implementeras på samma sätt som en vanlig pinne, men med mer logik bakom sig. När
de är korrekt länkade till en **arbetsvy** kan användaren navigera direkt till den
**arbetsvy** med ett klick. Pinnens bakgrundsfärg visar också den aktiva statusen
för **arbetsvy** — om den är aktiv, har en varning eller har ett larm. Pinnen kan
dessutom visa antalet aktiva larm och varningar. Tillsammans gör dessa funktioner
`PinStatus`-objekt till grunden för systemkontroll via en karta.

![Pin Status](/Images/Map_Indicators/PinStatus.png)

!!! note
    Om du vill visa en annan ikon på `PinStatus`-objektet, ändra dess SVG eller gör en
    kopia av objektet och ändra SVG på kopian.

För att integrera ett **Alarm**-objekt med en karta och statuspinnar, se
[Koppla Alarm till Map View](extending.md#connecting-alarm-to-map-view).

### Klusterpinnar { #cluster-pins }
Klusterpinnar kan användas för att gruppera underliggande pinnar till en, vilket minskar röran på
kartan och förbättrar navigationen. En klusterpinne skapas på samma sätt som en vanlig pinne,
men med ytterligare egenskaper.

![Clusterpin](/Images/Map_Indicators/Cluster.png)

![Cluster Settings](/Images/Map_Indicators/Cluster%20Pin.png)

Följande egenskaper måste konfigureras:

* **areaName** — Namnet som visas i verktygstipset och hjälper användaren med navigationen.
* **zoomTarget** — Styr zoomnivån när pinnen trycks in. I kombination
med kartans zoomintervall ger detta en sömlös navigering — de underordnade
pinnarna visas när man trycker och klusterpinnen döljs.
* **roi** — Kärnan i klusterpinnen. Bestämmer det område inom vilket klustret
samlar andra pinnar som sina underordnade. Om en pinne befinner sig inom **roi** för två kluster-
pinnar, kommer den närmaste att ta den som sin underordnade.

Klusterpinnen återspeglar också sina underordnade barns status genom sin bakgrundsfärg
och visar antalet anslutna underordnade.

För att aktivera klusterpinnefunktionen, lägg till följande i **Map View**:s onLoad-
skript:

```javascript title="Map View — onLoad"
scMap.mapView = this;
scMap.initClusters(this);
if (scMap.alarmList) scMap.updateAlarmList(this, scMap.alarmList);
```

![Pin and Cluster](/Images/Map_Indicators/ClusterStatusMap.gif)

### Linjer { #lines }
Linjer är användbara för att visualisera stigar eller rör i en applikation. Eftersom rör sträcker sig över
flera koordinater kräver de mer konfiguration än andra indikatorer. Linjer finns
i tre storlekar: `SmallPipeLines`, `MediumPipeLines` och `MainPipeLines`.

Följande egenskaper är tillgängliga:

* **pipeColor** — Linjens färg. Färger kan väljas från
temat **mapIndicators**, som finns i projektträdet under **Themes**. För att
lägga till anpassade färger, lägg till dem i temat **mapIndicators** och referera till färgnamnet här.
* **lineWidth** *(valfritt)* — Ändrar linjebredden. Det här värdet påverkas av
zoomning, så det fungerar som ett startvärde snarare än en konstant.
* **linkSize** *(valfritt)* — Varje linjesegment är anslutet av en ellips som kallas
Link. Ändrar storleken på länken.
* **filterType** — Används av applikationen för att filtrera olika nätverk. Det här
behöver inte fyllas i manuellt.
* **popupWidth** *(valfritt)* — Popupens bredd.
* **popupHeight** *(valfritt)* — Popupens höjd.
* **popupTextSize** *(valfritt)* — Ändrar teckenstorlek för popuptexten.
* **fileName** — Pekar på CSV-filen som innehåller koordinaterna för linje-
nätverket. Det finns ett maximum på 50 segment per nätverk.
* **origoLatitude** *(valfritt)* — Anger en startpunktens latitud för nätverket.
* **origoLongitude** *(valfritt)* — Anger en startpunktens longitud för nätverket.
* **Caption** — Rubriken som visas i kartindikatorn.

Exempelkonfiguration:

![Lines configuration](/Images/Map_Indicators/MapLines.png)

#### CSV-fil med koordinater
För att länka ett linjesnätverk till en CSV-fil, skapa filen i mappen `mapPaths` i ditt
projektbibliotek. Om den här mappen inte finns, skapa den.

CSV-filen använder två kolumner separerade av ett kommatecken — latitud och longitud — som definierar
sträckan från start till slut. Följande exempel täcker ett nätverk över Malmö, Sverige:

```csv title="example.csv"
lat,long
55.60993454611365,13.067280081496149
55.60754066940655,13.068012894315629
55.59706293405991,13.064900367032141
55.586229083148936,13.06210645824121
55.575010991019305,13.049196672585212
55.56406209265025,13.023184417468679
55.56771206450431,12.986285551858925
55.57070805669029,12.948037902764336
55.58835253553419,12.947941561647154
55.597117367875725,12.970678198813472
55.603812162853316,12.994474594377622
55.607077501929616,13.02193197387472
55.607186342050994,13.0452466622596
55.61529406922991,13.083397968508196
```

För att länka CSV-filen till en linjegrupp såsom `MainPipeLines`, ange egenskapen **fileName**
till filnamnet:

![fileName configuration](/Images/Map_Indicators/fileNameCSV.png)

### Filter { #filter }
Filter låter användare fokusera på en specifik uppsättning linjer eller nätverk genom att växla deras
synlighet. Alla linjennätverk registreras automatiskt med filtret, så ingen
ytterligare konfiguration krävs. Lägg till ett `Filter`-objekt i din vy på samma sätt
som vilket annat objekt som helst.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — skapa anpassade kartindikatorer
<!-- --8<-- [end:body] -->
