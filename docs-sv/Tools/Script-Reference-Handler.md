---
title: Script Reference Handler
description: Update the script reference handler. For projects in WQ13 which upgrades to WQ14
---

# Script Reference Handler 

Efter **WideQuick®** 14.0 kan fjärrskriptbibliotek nu ha samma namn som skriptbibliotek
i huvudprojektet. Tidigare kunde detta orsaka att systemet körde fel skript. Den här
uppdateringen förbättrar både modulariteten och robustheten hos skriptbibliotek.

För att uppdatera äldre projekt för kompatibilitet med den nya versionen, ladda ner
[Script Reference Migration Handler](https://www.kentima.com/sv-SE/Download/HMI-SCADA-Software/Download_software/WideQuick-HMI-SCADA/Version%20140){target="_blank"}

När nedladdningen är klar, extrahera filerna och följ stegen nedan innan projektet
körs i Runtime.

1. Det rekommenderas starkt att säkerhetskopiera projektet innan WideQuick 14.0
Script Reference Handler används.

2. Kör programmet så visas följande fönster:

![Script Reference](/docs/sv/Images/Script_Refenc_Handler/RefrenceHandler.png)

3. Klicka på ++"Browser"++ i det övre högra hörnet och hitta den aktuella projektmappen.
Detta hittar alla filer i projektet som behöver korrigeras.

4. Avsluta genom att klicka på ++"Correct app. references"++. Ett fönster öppnas —
klicka på ++"Ja"++ och sedan ++"Ok"++ så uppdateras projektet.

5. Det här verktyget bekräftar inte logik, utan ändrar endast referenser. Kontrollera
att projektet fungerar som avsett innan säkerhetskopian tas bort.

![Script Gif](/docs/sv/Images/Script_Refenc_Handler/Script_Handler.gif)