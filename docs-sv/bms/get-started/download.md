---
title: Ladda ned WideQuick BMS
product: bms
page_type: getstarted
status: draft
last_reviewed: 2026-06-16
tags:
 - BMS
---

# Ladda ned WideQuick BMS

WideQuick BMS är kostnadsfritt för Kentimas partners. Om du ännu inte är partner, besök [kentima.com](https://www.kentima.com){target="_blank"} för att läsa mer och komma i kontakt.

Nedladdningen innehåller allt som behövs för att komma igång:
- ett komplett mallprojekt med alla skript
- objektbibliotek
- systemlogik förkonfigurerad
- ett fullt implementerat demoprojekt för referens.

Projektet kan öppnas och utforskas fritt i WideQuick Designer, men driftsättning av ett levande system kräver licensen **WideQuick Advanced** eller högre.

Om du behöver en WideQuick-licens, vänligen kontakta Kentimas [säljavdelning](https://www.kentima.com/en-GB/Kontakt){target="_blank"}

## Mall- kontra demoapplication

WideQuick BMS 2026.1.0 finns i två versioner att ladda ned på Kentimas webbplats:

!!! note "Krav"
    **WideQuick version 14.0** eller senare måste vara installerat innan du laddar ned och öppnar projektfilerna. Se [Installera WideQuick](/wq/get-started/Installing-WideQuick) för mer information.

[**Ladda ned WideQuick BMS 2026.1.0**](https://www.kentima.com/en-GB/Download/HMI-SCADA%20CONCEPTS/Fastighetsautomation/Download%20application){target="_blank"}

### Mallprojekt
Mallprojektet är ett nytt, implementeringsklart projekt som innehåller den fulla
funktionaliteten i WideQuick BMS 2026.1.0. Alla skript, objektbibliotek och systemlogik
är förkonfigurerade och på plats — integratören börjar helt enkelt bygga sina
systemvyer. Det finns inga implementerade system eller externa anslutningar som
**OPC UA** eller **Modbus**. Det är den rekommenderade utgångspunkten för integratörer som
vill bygga ett nytt projekt från grunden.

![Template project](/Images/BMS_Intro/Template.png)

### Demoprojekt
Demoprojektet är ett fullt implementerat exempel som visar all funktionalitet i
WideQuick BMS 2026.1.0 i användning. Det är användbart både för att förstå hur systemet
fungerar och för att hämta inspiration till implementeringen.

Demoprojektet innehåller tre implementerade system:

* **Värme** — vyer `VS11`, `VV10`, `VS10` och `VS20`
* **Luftbehandling** — vyer `LB01`, `LB02` och `LB03`
* **Tavla** — vyer `AS01` och `AS02`

![Demo project](/Images/BMS_Intro/Demo.png)

!!! note
    Luftbehandlingssystemet innehåller även kopior av vyerna med äldre ikoner,
    som kan användas som referens för projekt som ännu inte har migrerat till det
    nuvarande ikonuppsättningen.

### Starta applikationen

När nedladdningen är klar, extrahera zip-filen till önskad mapp. Den extraherade mappen
innehåller:

* En projektmapp — som innehåller alla projektfiler
* `WideQuick_Mod.kpro` — dubbelklicka på den här filen för att starta projektet i WideQuick Designer.
* För att köra förhandsgranskningen trycker du på ++f5++ på tangentbordet.
