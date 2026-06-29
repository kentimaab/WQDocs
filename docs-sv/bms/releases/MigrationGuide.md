---
title: Migreringsguide - BMS
description: Steg-för-steg-guider för uppgradering mellan WideQuick BMS-versioner.
product: bms
page_type: release
status: draft
last_reviewed: 2026-06-26
tags:
 - BMS
---

# Migreringsguide - BMS

Steg-för-steg-guider för uppgradering mellan WideQuick BMS-versioner. Den senaste migreringen visas först och är expanderad; äldre migrationer är hopfällda.

## WideQuick BMS 2026.1.0 → 2026.1.1 { #bms-migration-2026-1-1 }
__Utgiven 2026-06-26__
<details class="release" markdown="1" open>
<summary>Migreringssteg</summary>

## Förutsättningar

* WideQuick BMS 2026.1.0 (Template- eller Demo-projekt)
* WideQuick V14 eller senare installerat

## Migreringssteg

1. Ladda ner resurspaketet **Migration BMS.2026.1.1**.

2. Öppna ditt `WideQuick_BMS_Template_2026_1_0` eller
`WideQuick_BMS_Demo_2026_1_0`-projekt i **WideQuick Designer®** och importera
resurspaketet.

3. I **WideQuick Designer®**, klicka på knappen **Resurser** för att öppna
resurspanelen.

    ![Resursknapp](/docs/sv/Images/Resources/Resources%20.png)

    I resurspanelen, navigera till **Arkiv → Importera from...** och välj
    **Migration BMS.2026.1.1** från det nedladdade paketet.

    När resursen har laddats in, ställ in alla filer på **Ersätt** så att de
    befintliga filerna i projektet skrivs över med de uppdaterade versionerna.
    Gif-filmen nedan visar hur detta görs:

    ![Importera resurs](/docs/sv/Images/Resources/MigrationImport.gif)

    När alla filer är inställda på **Ersätt**, klicka på **Importera** för att
    starta processen.

    !!! warning
        När **Importera** har klickats, rör inte applikationen förrän den är
        klar. Processen tar ungefär 1 minut. Om den kraschar, kör importen igen.

4. Starta projektet i **WideQuick Runtime®**.

5. Stäng applikationen och starta den igen.

6. Efter den andra omstarten är alla ändringar tillämpade. Skriptet `scCheck.js`
kan nu tas bort från projektet.

</details>
