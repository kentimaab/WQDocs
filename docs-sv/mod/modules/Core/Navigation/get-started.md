---
title: Navigation — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Navigation — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Navigation och all
    relaterad funktionalitet som täcks i navigationsguiden:
    
    * `scNav`
    * `scSubNavPopup`
    * `scLinking`
    * `scSubNav`
    * `scObjectFinder`
    * `scPrototypes`
    * `scSuffix`
    * `scThemes`
    * `scUsers`
    * `scAlert`

Det här avsnittet täcker grunderna i navigationsmodulen, inklusive hur man lägger till
**Workviews** i navigationsmenyn och hur helskärmsmenyn fungerar. Navigationsmodulen
bygger automatiskt menystrukturen utifrån mappstrukturen i
**WideQuick Designer®**, vilket gör det enkelt att hantera och utöka i takt med att projektet växer.

För åtkomstkontroll och visningsinställningar för begränsade vyer, se
[Navigation — Konfigurering](configuring). För avancerad funktionalitet som GoTo-genvägar
och anpassade ikoner, se [Navigation — Utökning](extending).

## Lägga till Workviews i navigationen { #adding-workviews-to-the-navigation }
Den automatiska navigationen består av två delar: mappen **Main_Menu** och mappen
**System**. Alla **Workviews** som placeras i någon av dessa mappar visas automatiskt
i menyn.

Det rekommenderas starkt att alla **Workviews** placeras i mappen **System** snarare
än i **Main_Menu**. Framtida uppdateringar av Modular Framework kan lägga till
ytterligare menygrupper i **Main_Menu**, vilket kan komplicera uppgraderingar om den
har modifierats.

För att skapa en ny vy i menyn, placera en ny **Workview** inuti en mapp under
**System**-mappen, som visas i exemplet nedan. Att klicka på denna nod i menyn öppnar
vyn direkt.

<div markdown style="display: flex; justify-content: center; align-items: center; gap: 0.5rem;">

![Single Depth](/Images/Navigation/Navigation_depth.png)

![Single Depth Menu](/Images/Navigation/Navigation_single_menu.png)

</div>

Om flera **Workviews** läggs till i samma mapp ändras ikonen i menyn — att klicka på
den öppnar en undermeny istället, som visas nedan. Ytterligare mappar kan nästlas inuti
för att bygga ännu djupare navigationsstrukturer.

<div markdown style="display: flex; justify-content: center; align-items: center; gap: 0.5rem;">

![Depth](/Images/Navigation/Navigation_single.png)

![Depth Navigation](/Images/Navigation/Navigation_depth_menu.png)

</div>

## Helskärmsmeny { #fullscreen-menu }
Helskärmsmenyn ger användarna en omedelbar överblick över katalogstrukturen och
möjliggör snabb navigering till nästlade vyer. Den kan aktiveras eller inaktiveras i **WideQuick Runtime®** via
**Inställningar**, så att användarna kan växla utifrån sina preferenser.

Menyn byggs automatiskt utifrån katalogstrukturen i **WideQuick Designer®**, vilket
innebär att designbeslut som tas där återspeglas direkt i körläget.

![FullScreen_Toggle](/Images/Navigation/ToggleFullNav.png)

Helskärmsmenyn är utformad för att visa så många **Workviews** som möjligt och samtidigt
förbli organiserad. Layouten följer dessa regler:

* Enbart **Workviews** — Om en katalog enbart innehåller **Workviews** utan
underkataloger arrangeras **Workviews** i rader.
* Enbart kataloger — Om en katalog enbart innehåller underkataloger arrangeras
toppnivåkatalogerna i kolumner, med sina underordnade visade i samma kolumn.
* Blandat innehåll — Alla **Workviews** på toppnivå placeras i den första kolumnen,
följt av kataloger arrangerade kolumnvis.

Helskärmsmenyn kan visa upp till 90 kataloger och **Workviews** samtidigt. Om denna
gräns överskrids anpassar menyn sig automatiskt på två sätt:

* **Kolumnspill** — Om en enskild kolumn överskrider det maximala antalet rader visas
en **Mer...**-knapp längst ned i den kolumnen. Att klicka på den roterar navigationen
till mappen längst upp i den kolumnen, vilket låter användaren bläddra igenom dess innehåll.
* **Sidspill** — Om det finns för många toppnivåkataloger för att få plats på en enda
sida visas en navigeringspil i det övre vänstra hörnet för att navigera till nästa sida.

Tillsammans gör dessa två mekanismer att helskärmsmenyn kan skalas till system av
valfri storlek — oavsett hur många vyer eller kataloger ett projekt innehåller kommer
menyn alltid att vara navigerbar.

![FullScreen_Menu](/Images/Navigation/Nav_2Stor.png)

## Nästa steg { #next-steps }

* [Konfigurering](configuring.md) — behörighetskrav på vyer och visningsinställningar för begränsade vyer
* [Utökning](extending.md) — GoTo-funktion och anpassade navigationsikoner
<!-- --8<-- [end:body] -->
