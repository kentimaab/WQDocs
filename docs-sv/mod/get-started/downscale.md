---
title: Nedskalad version
description: Den minimala WideQuick MOD-mallen och hur du lägger till valfria moduler som resurspaket.
product: mod
page_type: getstarted
status: draft
last_reviewed: 2026-09-22
tags: 
 - MOD
---

# Nedskalad version

Utöver det fullständiga [mallprojektet](download.md#mallprojekt) finns WideQuick MOD även tillgängligt som en **nedskalad version**: ett minimalt projekt som endast innehåller Core-modulen. Alla valfria moduler är helt bortlämnade, vilket ger integratörer en mindre startpunkt än standardmallen.

## Vad den nedskalade versionen innehåller { #what-the-downscale-version-includes }

Det nedskalade projektet levereras endast med [Core](../modules/Core/index.md): navigering, larm, teman, grafiska symboler, projektövergripande inställningar samt användar- och behörighetshantering. Det är samma grund som alla WideQuick MOD-projekt bygger på, utan några av de valfria modulerna lagda ovanpå.

## Vad som lämnas bort { #what-is-left-out }

Ingen av de valfria modulerna ingår i den nedskalade versionen:

* [Spårningslogg](../modules/audit-trail/index.md) — spårar ändringar i Datalager-variabler och underhållsuppgifter.
* [Säkerhetskopiering och återställning](../modules/backup-and-restore/index.md) — sparar och återställer Datalager-variabelvärden med namn.
* [Kalender](../modules/calendar/index.md) — månads-, vecko- och dagsvyer över händelser och underhållsdeadlines.
* [Dashboards](../modules/dashboards/index.md) — konfigurerbara vyer för att övervaka signaler, värden och status.
* [Dokument](../modules/documents/index.md) — hanterar filer och kopplar dem till objekt.
* [Historik](../modules/history/index.md) — grafiska vyer av loggad signaldata.
* [Loggbok](../modules/logbook/index.md) — registrerar och organiserar fritextanteckningar kopplade till delar av systemet.
* [Underhåll](../modules/maintenance/index.md) — schemalägger, spårar och automatiserar underhållsuppgifter.
* [Kartor och indikatorer](../modules/maps/index.md) — planritningsvyer och kartindikatorer.
* [Rapporter](../modules/reports/index.md) — genererar, schemalägger och anpassar rapporter.

Ett projekt som byggs från den nedskalade versionen börjar därför med enbart Core och växer genom att bara lägga till de moduler projektet faktiskt behöver.

## Lägga till en modul { #adding-a-module }

Varje valfri modul distribueras som ett resurspaket, en `.wqrc`-fil som paketerar allt modulen behöver: skript, vyer, objekt och databasschema. För att lägga till en modul i ett nedskalat projekt, ladda ned dess resurspaket och importera det via det inbyggda gränssnittet för resurser. Se [Resurser och resurspaket](../reference/Resources-and-Resource-package.md) för den fullständiga importproceduren.

Eftersom [varje modul är oberoende](../concepts/index.md#module-independence), kan paket importeras i valfri kombination och valfri ordning. Att lägga till Underhåll kräver inte att Kalender också läggs till, även om de två integreras när båda finns på plats.

## Välja startpunkt { #choosing-a-starting-point }

* Börja från den **nedskalade versionen** när projektets modulbehov är begränsat, eller ännu inte är helt klarlagt, och moduler bör läggas till medvetet i takt med att kraven bekräftas.
* Börja från det fullständiga **mallprojektet** (se [Ladda ned](download.md)) när de flesta eller alla moduler förväntas användas redan från start.

Oavsett vilken startpunkt som används är modulerna i sig identiska: att importera en modul i ett nedskalat projekt ger samma resultat som att den redan finns med i det fullständiga mallprojektet. Den enda skillnaden är vad som finns på plats när projektet öppnas för första gången: enbart Core, eller alla moduler redo att användas.
