---
title: Migreringsguide - BMS
description: Steg-för-steg-guider för uppgradering mellan WideQuick BMS-versioner.
product: bms
page_type: release
status: draft
last_reviewed: 2026-10-08
tags:
 - BMS
---

# Migreringsguide - BMS

Steg-för-steg-guider för uppgradering mellan WideQuick BMS-versioner. Den senaste migreringen visas först och är expanderad; äldre migrationer är hopfällda.

## WideQuick BMS 2026.1.1 → 2026.1.1.2 { #bms-migration-2026-1-1-2 }
__Utgiven 2026-10-06__
<details class="release" markdown="1" open>
<summary>Migreringssteg</summary>

## Förutsättningar

* WideQuick BMS 2026.1.1 (Template- eller Demo-projekt)
* WideQuick V14 eller senare installerat

## Migreringssteg

1. Ladda ner det resurspaket som passar ditt projekt:

    * **RemoteFixBMS.1.1_Template.wqrc** för Template-projektet
    * **RemoteFixBMS.1.1_Demo.wqrc** för Demo-projektet

2. Öppna ditt `WideQuick_BMS_Template_2026_1_1` eller
`WideQuick_BMS_Demo_2026_1_1`-projekt i **WideQuick® Designer** och importera
resurspaketet.

3. I **WideQuick® Designer**, klicka på knappen **Resurser** för att öppna
resurspanelen.

    ![Resursknapp](/docs/sv/Images/Resources/Resources%20.png)

    I resurspanelen, navigera till **Arkiv → Importera from...** och välj
    resurspaketet bland de nedladdade filerna.

    När resursen har laddats in, ställ in alla filer på **Ersätt** så att de
    befintliga filerna i projektet skrivs över med de uppdaterade versionerna.
    Gif-filmen nedan visar hur detta görs:

    ![Importera resurs](/docs/sv/Images/Resources/RemoteFixImport.gif)

    När alla filer är inställda på **Ersätt** inklusive Datalager variablerna, klicka på **Importera** för att
    starta processen.

    !!! warning
        När **Importera** har klickats, rör inte applikationen förrän den är
        klar. Om den kraschar, kör importen igen.

4. Starta projektet i **WideQuick® Runtime**.

5. Om projektet ansluter till fjärrsystem, öppna **Fjärrsystem** i
**WideQuick® Designer** och aktivera **Auto connect** för varje fjärrsystem vars
larm ska ingå i larmräknarna. Utan det är anslutningen till ett fjärrsystem bara
öppen medan en vy använder den, till exempel larmlistan.

6. Om larmgrupper har lagts till i projektet, öppna var och en i
**WideQuick® Designer** och ersätt dess `Measure`-skript med:

    ```javascript title="Larmgrupp — Measure"
    if (view.goToCurrentAlarm) { view.goToCurrentAlarm(); }
    ```

    Det tidigare skriptet, som anropar `scAlarmFinder.goToAlarm` med `app.alarmView`,
    fungerar inte på webbklienten. Larmgrupperna som levereras med Demo-projektet
    uppdateras av resurspaketet.

7. Om projektet har egna vyer med en larmlista, lägg till följande i varje vys
Load-skript så att **Gå till larm** fungerar från vyn. Ersätt `Alarm1` med namnet
på vyns `Alarm`-objekt:

    ```javascript title="Vy — Load"
    var gotoList = this.view.Alarm1;
    var gotoViewName = this.view.name;
    this.view.goToCurrentAlarm = function () {
        scAlarmFinder.goToAlarm(gotoList.nameForCurrentAlarm, gotoViewName);
    };
    ```

!!! note
    **Gå till larm** på ett larm från ett fjärrsystem öppnar systemet i
    **WideQuick® Remote** och navigerar till larmet där. Det kräver att fjärrsystemet
    också kör WideQuick BMS 2026.1.1.2.

!!! note
    **Ersätt** skriver över projektets versioner av filerna i paketet. Om du har
    gjort egna ändringar i någon av dem behöver de föras in igen efter importen.
    De ändrade filerna listas i [versionsnoteringarna](index.md#bms-2026-1-1).

!!! note
    Skriptfunktioner anropas nu via sitt skriptbibliotek. Egna skript och vyer som
    anropar ramverkets funktioner med deras gamla globala namn måste använda det
    biblioteksprefixade namnet i stället, till exempel `scSmartPopup.smartPopup`,
    `scAlarmFinder.goToAlarm(...)` och `scWorkviewAnimation.AnimationHandler`.

</details>

## WideQuick BMS 2026.1.0 → 2026.1.1 { #bms-migration-2026-1-1 }
__Utgiven 2026-06-26__
<details class="release" markdown="1">
<summary>Migreringssteg</summary>

## Förutsättningar

* WideQuick BMS 2026.1.0 (Template- eller Demo-projekt)
* WideQuick V14 eller senare installerat

## Migreringssteg

1. Ladda ner resurspaketet **Migration BMS.2026.1.1**.

2. Öppna ditt `WideQuick_BMS_Template_2026_1_0` eller
`WideQuick_BMS_Demo_2026_1_0`-projekt i **WideQuick® Designer** och importera
resurspaketet.

3. I **WideQuick® Designer**, klicka på knappen **Resurser** för att öppna
resurspanelen.

    ![Resursknapp](/docs/sv/Images/Resources/Resources%20.png)

    I resurspanelen, navigera till **Arkiv → Importera from...** och välj
    **Migration BMS.2026.1.1** från det nedladdade paketet.

    När resursen har laddats in, ställ in alla filer på **Ersätt** så att de
    befintliga filerna i projektet skrivs över med de uppdaterade versionerna.
    Gif-filmen nedan visar hur detta görs:

    ![Importera resurs](/docs/sv/Images/Resources/MigrationImport.gif)

    När alla filer är inställda på **Ersätt** inklusive Datalager variablerna, klicka på **Importera** för att
    starta processen.

    !!! warning
        När **Importera** har klickats, rör inte applikationen förrän den är
        klar. Processen tar ungefär 1 minut. Om den kraschar, kör importen igen.

4. Starta projektet i **WideQuick® Runtime**.

5. Stäng applikationen och starta den igen.

6. Efter den andra omstarten är alla ändringar tillämpade. Skriptet `scCheck.js`
kan nu tas bort från projektet. Detta skript är ett engångsmigrationsskript som
körs vid uppstart för att lägga till saknade suffixalias, uppdatera
användarprivilegier och korrigera databasanslutningsinställningar från
2026.1.0-versionen. Det behövs inte längre när migreringen är klar.

!!! note
    Template- och Demo-projekten i version 2026.1.0 innehöll ett fel där
    databasanslutningarna **Larm**, **Underhåll** och **Historik** saknade sitt
    databasnamn. `scCheck.js` korrigerar detta automatiskt, men endast om
    anslutningarna fortfarande är i sitt ursprungliga felaktiga skick.
    Databasanslutningar som redan har konfigurerats av integratören påverkas inte.
</details>
