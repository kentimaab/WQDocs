---
title: Nedskalad version
description: Den minimala WideQuick MOD-mallen och hur du lägger till de valfria modulerna igen som resurspaket.
product: mod
page_type: getstarted
status: draft
last_reviewed: 2026-11-03
tags: 
 - MOD
---

# Nedskalad version

Utöver det fullständiga [mallprojektet](../get-started/download.md#mallprojekt) finns WideQuick MOD även som en **nedskalad version**: mallprojektet med alla valfria moduler borttagna. Varje borttagen modul finns som ett eget paket, så att ett projekt kan börja litet och bara lägga till de moduler det behöver.

## Vad den nedskalade versionen innehåller { #what-the-downscale-version-includes }

Det nedskalade projektet innehåller:

* [Kärna](../modules/Core/index.md): navigering, larm, teman, grafiska symboler, projektövergripande inställningar samt användar- och behörighetshantering. Det är grunden som alla WideQuick MOD-projekt bygger på.
* [Historik](../modules/history/index.md): historikvyn och flikarna Historik och Trend i objektpopupen.

Objektpopupen behåller de flikar som hör till Kärna och Historik. Flikarna för modulerna nedan visas när modulen har importerats.

## Vad som lämnas bort { #what-is-left-out }

Elva moduler är borttagna, och var och en finns som ett eget paket:

* [Spårningslogg](../modules/audit-trail/index.md): loggar ändringar av variabler, vad som ändrades, av vem och när.
* [Säkerhetskopiering och återställning](../modules/backup-and-restore/index.md): sparar värdena på valda variabler under ett namn och återställer dem vid behov.
* [Kalender](../modules/calendar/index.md): månads-, vecko- och dagsvyer över händelser, med import av helgdagar. Visar underhållsdeadlines när Underhåll också är installerat.
* [Styrkurva](../reference/Popup/Control curve.md): popuperna Styrkurva och [Styrkurva Tid](../reference/Popup/Control curveTime.md), för att justera styrkurvor och växla mellan deras profiler.
* [Dashboards](../modules/dashboards/index.md): widgetar och en vymall för att bygga dashboards med signaler, nyckeltal, historik och larm.
* [Dokument](../modules/documents/index.md): lagrar filer i projektet och kopplar dem till objekt.
* [Loggbok](../modules/logbook/index.md): fritextanteckningar kopplade till objekt, vyer och andra delar av systemet.
* [Underhåll](../modules/maintenance/index.md): planerar, följer upp och automatiserar underhåll av objekt, med mallar och återkommande uppgifter.
* [Kartor och väder](../modules/maps/index.md): kartindikatorer kopplade till larm och en väderwidget med prognoser från SMHI.
* [Rapporter](../modules/reports/index.md): larm-, energi- och deltarapporter i Excel, manuellt eller schemalagt, med utskick via e-post.
* [Tidkanal](../reference/Popup/Time-channel.md): popupen för att visa och ändra ett objekts tidkanal och spara den som profil.

## Lägga till en modul { #adding-a-module }

Varje modul laddas ner som en zip-fil från samma sida som mallprojektet, se [Ladda ner](../get-started/download.md). Zip-filen innehåller:

* `<Modul>.wqrc`: resurspaketet, med modulens skript, vyer, objektbibliotek, variabler, behörigheter och, för en modul som har en, dess databas.
* `README.md`: vad modulen innehåller, hur den importeras, vilka behörigheter den för med sig och vad som kräver extra omsorg.

Paketet för Rapporter innehåller dessutom `Reports.kdat`, se [Rapporter](#reports).

Så här lägger du till en modul:

1. Packa upp zip-filen.
2. Importera `.wqrc`-filen i **WideQuick® Designer** via gränssnittet för resurser och välj **Replace all**. Se [Resurser och resurspaket](../reference/Resources-and-Resource-package.md#importing-resources) för importfönstret.
3. Tilldela modulens behörigheter. Paketet lägger till dem men ger dem inte till någon, så tilldela dem till de användare som behöver dem. Paketen innehåller inga användarkonton, så projektets befintliga användare och deras behörigheter lämnas orörda.

Moduler kan importeras i valfri kombination och valfri ordning, eftersom [varje modul är oberoende](../concepts/index.md#module-independence). Kalender fungerar utan Underhåll och börjar visa underhållsdeadlines när Underhåll läggs till.

Objektpopupen kräver ingen inställning. Popuperna för Dokument, Loggbok, Underhåll, Styrkurva och Tidkanal visas i den, och i inställningsvyn **Suffixalias - Popuper**, så snart modulen finns i projektet.

### Kalender och Underhåll { #calendar-and-maintenance }

Kalender och Underhåll lagrar sina data i samma databas, `Data/maintenance.db`, via databasanslutningen `maintenance`. Båda paketen innehåller filen och anslutningen, så att båda modulerna kan importeras var för sig.

!!! warning "När den andra av de två importeras"
    Om en av de två modulerna redan finns i projektet, ändra `maintenance.db` och anslutningen `maintenance` till **Skip** i stället för **Replace** innan du trycker på ++"Import"++. Om filen ersätts raderas alla underhållsuppgifter, mallar, kalenderhändelser och prenumerationer som redan finns i projektet.

Varje modul skapar de tabeller den behöver när Runtime startar.

### Rapporter { #reports }

Rapportdefinitionerna finns i `Reports.kdat`, som ett resurspaket inte kan föra med sig. Filen ligger i zip-filen bredvid `Reports.wqrc`. När paketet har importerats:

1. Stäng projektet i **WideQuick® Designer**.
2. Kopiera `Reports.kdat` till projektmappen, bredvid projektets övriga `.kdat`-filer, och ersätt den befintliga.
3. Öppna projektet igen.

### Kartor och väder { #maps-and-weather }

Inga färdiga kartor ingår. Bygg en kartvy med kartindikatorerna enligt [Kartor och indikatorer](../modules/maps/index.md).

SMHI-anslutningen för väder importeras inaktiv. Väderwidgeten aktiverar den när den hämtar en prognos, så lämna den som den är.

## Välja startpunkt { #choosing-a-starting-point }

* Börja från den **nedskalade versionen** när projektets modulbehov är begränsat, eller ännu inte är helt klarlagt, och moduler bör läggas till medvetet i takt med att kraven bekräftas.
* Börja från det fullständiga **mallprojektet** (se [Ladda ner](../get-started/download.md)) när de flesta eller alla moduler förväntas användas redan från start.

Oavsett vilken startpunkt som används är modulerna i sig identiska: en modul som importeras i ett nedskalat projekt är densamma som den som redan finns i det fullständiga mallprojektet. Det som skiljer är vad som finns på plats när projektet öppnas första gången, och behörigheterna. I det fullständiga mallprojektet har de förkonfigurerade användarna redan modulernas behörigheter, medan en importerad moduls behörigheter inte är tilldelade någon förrän du tilldelar dem.
