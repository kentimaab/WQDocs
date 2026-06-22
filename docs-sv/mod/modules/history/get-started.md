---
title: Historik — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Historik — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Historik och all
    relaterad funktionalitet som täcks i historikguiderna:
    
    * `scHistory`
    * `scPrototypes`
    * `scThemes`
    * `scAlert`
    * `scQuickSort`

Historikmodulen visar loggade signaldata som interaktiva linjediagram. Det finns tre sätt att komma åt den: den projektövergripande vyn **Historik** från huvudmenyn, ett vyspecifikt **Historik**-popup som öppnas från en Arbetsvy, och fliken [**Historik**](../../reference/Popup/History.md) i valfritt objektpopup.

## Historik-vyn { #the-history-view }

Den projektövergripande vyn **Historik** är tillgänglig från huvudmenyn. Den visar signaler från hela projektet.

![Historik-vy med en plottad signal](/Images/History/history-view.png){align=center}

Vyn har ett diagram längst upp och tre paneler längst ned:

* **Signaler** — ett träd med alla loggade signaler i projektet, grupperade efter system. Signaler väljs här och appliceras på diagrammet.
* **Spåra signal** — alternativ för att spåra en livesignal i diagrammet. Innehåller även avsnittet **Sparade grupper** för att spara och läsa in namngivna signalgrupper.
* **Inställningar** — växlar för teckenförklaring, linjal och Y-axelskalning, samt kontroller för tidsintervall och uppdateringsintervall.

Knappen **Visa variabler som inte loggas** i det övre högra hörnet öppnar ett separat fönster som visar alla signaler som inte är anslutna till en loggenhet.

## Välja signaler { #selecting-signals }

1. Expandera trädet **Signaler** för att hitta signalen. Klicka på **Expandera alla** för att öppna alla noder på en gång.
2. Klicka på signalen för att markera den. Flera signaler kan markeras samtidigt. Knappen **Applicera** visar hur många signaler som för närvarande är valda.
3. Klicka på **Applicera** för att plotta de valda signalerna i diagrammet.
4. För att rensa alla signaler från diagrammet, klicka på **Rensa val**.

Den andra kolumnen i trädet visar linjetypen för varje vald signal. Att klicka på linjetypssymbolen växlar mellan tillgängliga stilar (heldragen eller streckad).

## Inställningar { #settings }

Panelen **Inställningar** styr hur diagrammet ser ut och hur ofta det uppdateras.

![Inställningspanelen med växlar och intervallkontroller](/Images/History/history-panels.png){align=center}

| Inställning | Beskrivning |
|---|---|
| Visa teckenförklaring | Växlar signalförklaringen i diagramområdet. |
| Visa linjal | Växlar en vertikal linjalslinje som följer markören. |
| Skala Y-axlar | Aktiverar automatisk skalning av alla Y-axlar för att passa synliga data. |

**Tidsintervall** anger hur mycket historik som visas:


**Uppdateringsintervall** anger hur ofta diagrammet uppdateras med nya data:

| Knapp | Beskrivning |
|---|---|
| 0 s | Ingen automatisk uppdatering |
| 1 s | Uppdatera varje sekund |
| 5 s | Uppdatera var 5:e sekund |
| 10 s | Uppdatera var 10:e sekund |

## Vyspecifik historik { #view-specific-history }

Menyn **SpeedDial** på processvyer innehåller en knapp som öppnar ett vyspecifikt historikpopup. Det fungerar precis som den projektövergripande vyn men visar bara signaler från objekt som tillhör den vyn.

![Vyspecifikt historikpopup](/Images/History/history-view-specific.png){align=center}

Signalval, tidskontroller, inställningar och sparade signalgrupper fungerar på samma sätt. Sparade signalgrupper i detta popup lagras per vy och är separata från projektövergripande sparade grupper. Du kan också importera sparade grupper från andra vyer via **Importera grupper från vyer** — se [Importera grupper från andra vyer](configuring.md#importing-groups-from-other-views).

Eftersom den vyspecifika historiken bara visar signaler som tillhör den aktuella vyn kan du hämta in signaler från andra vyer med hjälp av **Importera signaler**.

![Dialogrutan Importera signaler med Tillgängliga till vänster och Valda till höger](/Images/History/history-import-signals.png){align=center}

**Så här importerar du signaler från andra vyer:**

1. Klicka på **Importera signaler**. En dialogruta öppnas som visar alla signaler från alla andra vyer, ordnade efter system och objekt.
2. Expandera trädet i panelen **Tillgängliga** för att hitta den signal du vill ha.
3. Markera en signal och klicka på **→** för att flytta den till panelen **Valda**.
4. Upprepa för varje signal du vill lägga till.
5. Klicka på **Importera och stäng**. Signalerna läggs till i signallistan och kan markeras och appliceras på diagrammet.

Om du vill ta bort en signal från ditt urval innan import markerar du den i panelen **Valda** och klickar på **←**. Klicka på **Rensa tillagda** för att tömma den högra panelen helt.


## Objektpopup (fliken Historik) { #object-popup-history-tab }

Varje objekt i projektet har en flik [**Historik**](../../reference/Popup/History.md) i sitt popup. Om du öppnar fliken visas de loggade signalerna för det objektet i ett diagram.

![Fliken Historik i ett objektpopup](/Images/History/history-object-popup.png){align=center}

Signaler som tillhör objektet men saknar konfigurerad loggenhet listas på höger sida under **Taggar som inte loggas**.

Signallistan stödjer tangentbordsnavigering med knapparna **▲** och **▼**. Klicka på **Välj** för att markera den markerade signalen.

Signaler med suffixet `_MV` (uppmätt värde) väljs automatiskt när popupen öppnas.

Klicka på **Applicera** för att plotta de valda signalerna. Klicka på **Stäng** för att stänga popupen.

## Nästa steg { #next-steps }

* [Konfigurera](configuring.md) — signalval, spåra signal, sparade grupper och diagraminställningar i detalj
* [Utöka](extending.md) — öppna det vyspecifika popupen från ett skript och felsökning
<!-- --8<-- [end:body] -->
