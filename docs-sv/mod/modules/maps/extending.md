---
title: Kartor och indikatorer — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Kartor och indikatorer — Utöka

Det här avsnittet beskriver hur du utökar modulen Kartor och indikatorer med anpassad
funktionalitet. Det inkluderar att koppla ett **Alarm**-objekt till en **Kartvy** för
livefiltrering av larm, samt att skapa anpassade kartindikatorer med zoomnavigering,
länkning och statushantering.

Innan du börjar, se till att du är bekant med grunderna i modulen Kartor och indikatorer.
Om inte, se [Kartor och indikatorer — Kom igång](get-started.md).


## Koppla Alarm till Kartvy { #connecting-alarm-to-map-view }

Ett **Alarm**-objekt kan kopplas till en **Kartvy** så att det filtrerar larm
baserat på vilka statuspinnar eller klusterpinnar som är synliga för tillfället. Det ger
användaren både en fullständig systemöversikt och stationsspecifik kontroll.

Lägg till följande onLoad-skript i den **Arbetsvy** som innehåller både
**Kartvyn** och **Alarm**-objektet. Detta aktiverar alla systemlarm i larmlistan:

```javascript title="arbetsvy — onLoad"
var local = alarmNames.split(",");

for (var index = 0; index < local.length; index++) {
    this.view.Alarm1.addGroup(local[index]);
}

app.alarmView = this.view;
scMap.alarmList = this.view.Alarm1;
scMap.updateAlarmList(scMap.mapView, scMap.alarmList);
```

!!! note
    Ersätt `Alarm1` med namnet på det **Alarm**-objekt som är placerat i vyn.
    `alarmNames` är en intern Datalager-variabel som innehåller en kommaseparerad
    sträng med alla larmgruppsnamn i systemet. Den behöver inte konfigureras manuellt.

Nästa steg: onLoad-skriptet för **Kartvyn** hanterar redan uppdateringar av larmlistan
om `scMap.alarmList` är satt. Se till att onLoad-skriptet för **Kartvyn** är konfigurerat
enligt följande:

```javascript title="Map View — onLoad"
scMap.mapView = this;
scMap.initClusters(this);
if (scMap.alarmList) scMap.updateAlarmList(this, scMap.alarmList);
```

**Alarm**-objektet är nu fullt kopplat till **Kartvyn** och visar
aktiva larm baserat på vad som för tillfället är synligt på kartan.

![ConnectedAlarm](/Images/Map_Indicators/AlarmConnected.gif)

## Skapa anpassade kartindikatorer { #creating-custom-map-indicators }

Följande avsnitt förklarar de viktigaste koncepten bakom de inbyggda indikatorerna och
hur de tillämpas när du skapar egna. Snarare än att dokumentera ett specifikt
objekt ligger fokus på de underliggande mönstren — zoomnavigering, länkning, statushantering
och klustring — så att integratören fritt kan tillämpa dem på valfri
anpassad indikator.

!!! tip
    För komplexa indikatorer som statuspinnar och klusterpinnar rekommenderas det starkt
    att kopiera det befintliga objektet och modifiera det istället för att bygga
    från grunden. Det bevarar all befintlig logik och tillåter samtidigt full visuell
    anpassning.

### Zoomnivåer och navigering { #zoom-levels-and-navigation }

**Kartvy**-objekt stöder zoomintervall, som styr vid vilken zoomnivå varje
objekt är synligt. Det är ett kraftfullt verktyg för att minska röran — objekt på en
högre nivå kan guida användaren till mer detaljerade vyer på lägre zoomnivåer genom
att ange en målzoomnivå vid klick.

För att implementera detta, lägg till en **zoomTarget**-egenskap på din anpassade indikator och
använd följande onClick-skript:

```javascript title="Custom indicator — onClick"
var mv = this.geo.mapView;
mv.zoomLevel = this.zoomTarget || 15;
mv.latitude = this.geo.latitude;
mv.longitude = this.geo.longitude;
```

Det här skriptet gör tre saker när indikatorn klickas:

* Sätter kartans zoomnivå till värdet av **zoomTarget**. Om inget värde är angivet används
standardvärdet `15`.
* Centrerar kartan på indikatorns latitud.
* Centrerar kartan på indikatorns longitud.

Genom att kombinera zoomintervall med en **zoomTarget**-egenskap kan indikatorer på högre
zoomnivåer fungera som navigeringshjälpmedel — ett klick zoomar in och avslöjar de mer
detaljerade indikatorerna nedanför.

!!! tip
    En bra praxis är att ange **zoomTarget** för en indikator på högre nivå till den
    lägsta zoomnivå vid vilken dess underordnade indikatorer blir synliga. Det skapar en
    sömlös navigeringsupplevelse.

### Länkning { #linking }

Anpassade indikatorer kan länkas till en **Arbetsvy**, en katalog eller ett specifikt objekt
beroende på användningsfallet. Det styrs genom att lägga till en **linkedView**- eller
**targetObject**-egenskap på indikatorn.

#### Länka till en Arbetsvy
För att länka en indikator till en **Arbetsvy**, lägg till en **linkedView**-egenskap och sätt
dess värde till sökvägen för den önskade **Arbetsvy** som slutar med `.kvie`. Lägg sedan
till följande onClick-skript:

```javascript title="Custom indicator — onClick (arbetsvy)"
app.MultiViewer.setView(this.linkedView);
```

#### Länka till en katalog
För att länka en indikator till en katalog, lägg till en **linkedView**-egenskap och sätt dess värde
till en katalogsökväg som `System/Videdal`. Vid klick öppnas helskärmsmenyn
på den katalogen, vilket gör att användaren kan navigera till önskad **Arbetsvy**.

```javascript title="Custom indicator — onClick (directory)"
var _parts = this.linkedView.split("/");
var root = _parts[0];
var dir = _parts[_parts.length - 1];
app._subNavTarget = { root: root, dir: dir };
```

!!! note
    Kataloglänkning kräver att helskärmsmenyn är tillgänglig. Se
    [Navigation — Kom igång](../Core/Navigation/get-started.md) för mer information.

#### Länka till ett specifikt objekt
För att länka en indikator direkt till ett specifikt objekt, lägg till en **targetObject**-egenskap
och sätt dess värde till namnet på målobjektet. Lägg sedan till följande onClick-skript:

```javascript title="Custom indicator — onClick (object)"
scLinking.goTo(this.targetObject);
```

Det navigerar till den **Arbetsvy** som innehåller målobjektet och markerar det.
För mer information om GoTo, se [Navigation — Utöka](../Core/Navigation/extending.md#goto).

!!! tip
    Använd **linkedView** med en `.kvie`-sökväg för att navigera till en specifik **Arbetsvy**,
    använd **linkedView** med en katalogsökväg för att öppna helskärmsmenyn på den
    platsen, och använd **targetObject** när du vill ta användaren direkt till
    ett specifikt objekt som en sensor eller ett styrelement.

### Pinnstatus { #pin-status }

`PinStatus`-objektet är det mest komplexa av de inbyggda indikatorerna. Det gör automatiskt
två saker när det länkas till en **Arbetsvy**:

* **Larmräkning** — frågar databasen efter alla larm kopplade till den länkade
**Arbetsvy** och lyssnar på ändringar. Resultatet återspeglas i pinnens `alarmCount`-egenskap.
* **Statusfärg** — frågar alla objekt i den länkade **Arbetsvy** och mappar deras
suffixsignaler till en statusnivå med hjälp av skriptet `scSuffix`. Pinncirkelns färg
uppdateras automatiskt för att återspegla den högsta aktiva statusen:

| Status | Färg |
|---|---|
| Larm / Fel | Röd |
| Varning | Gul |
| Aktiv / OK | Grön |
| Ingen status | Grå |

Statusmappningen konfigureras i skriptet `scSuffix` via
objektet `suffixObj.Views`, som definierar vilka objektsuffix som motsvarar vilken
statuskategori. Det behöver inte ändras när du skapar en anpassad indikator.

!!! tip "Rekommendation"
    Snarare än att bygga en anpassad statusindikator från grunden rekommenderas det starkt
    att kopiera det befintliga `PinStatus`-objektet och modifiera det efter dina
    behov. Skriptet är tätt kopplat till skriptet `scSuffix` och databasstrukturen,
    vilket gör det komplext att replikera korrekt. Kopiering säkerställer att all
    befintlig logik bevaras och tillåter samtidigt full visuell anpassning.

### Klusterhantering { #cluster-awareness }

Klustringssystemet i **Kartvy** drivs helt av funktionen `initClusters()` i skriptet `scMap`.
Den identifierar objekt genom att söka efter två specifika egenskaper:

* Ett objekt med en `roi`-egenskap — behandlas som ett **kluster**
* Ett objekt med en `status`-egenskap — behandlas som en **pin** och potentiellt underordnat element

Det innebär att valfri anpassad indikator kan delta i klustringssystemet enbart
genom att ha rätt egenskap. Det finns inget krav på ett specifikt objektnamn
eller en specifik typ.

!!! note
    `initClusters()` måste anropas i onLoad-skriptet för **Kartvyn** för att klustring
    ska fungera. Se [Kartor och indikatorer — Kom igång](get-started.md#setting-up-a-map-view-object).

#### Göra en anpassad indikator klustermedveten

För att en anpassad indikator ska plockas upp som ett underordnat element av klustringssystemet
behöver den en `status`-egenskap. För det inbyggda `PinStatus`-objektet hanteras detta automatiskt
av dess skript — `status` uppdateras av en `DatalagerListener` när den länkade
**Arbetsvy** ändrar tillstånd.

För en anpassad indikator måste `status` underhållas av ett skript. Värdet ska
följa samma statushierarki som används av de inbyggda indikatorerna:

| Värde | Betydelse |
|---|---|
| `3` | Larm / Fel |
| `2` | Varning |
| `1` | Aktiv / OK |
| `0` | Ingen status |

!!! tip "Rekommendation"
    Snarare än att bygga ett anpassat kluster från grunden rekommenderas det starkt
    att kopiera det befintliga klusterobjektet och modifiera det efter dina behov. Klustringslogiken
    hanteras helt av skriptet `scMap` — kopiering säkerställer att ditt objekt
    identifieras korrekt av `initClusters()` och tillåter samtidigt full
    visuell anpassning.
