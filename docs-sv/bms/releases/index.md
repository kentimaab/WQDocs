---
title: Versioner — BMS
product: bms
page_type: release
status: draft
last_reviewed: 2026-09-15
tags:
 - BMS
---

# Versioner — BMS

Versionsnoteringar för WideQuick BMS. Den senaste versionen visas först och är expanderad;
äldre versioner är ihopfällda, klicka på en version för att expandera den. Varje version bygger på
en specifik version av WideQuick Modular Framework, länkad under respektive rubrik. För hela
ramverkets ändringslogg, se [MOD-versioner](../../mod/releases/index.md).

## WideQuick BMS 2026.1.2 { #bms-2026-1-2 }

__Utgiven 2026-08-20__
Modular Framework Version: [WideQuick MOD 2026.1.0](../../mod/releases/index.md#mod-2026-1-0)
<details class="release" markdown="1" open>
<summary>Versionsnoteringar</summary>

### Nya funktioner

| Funktion | Beskrivning |
|---|---|
| **Kalenderimport och export** | Händelser kan importeras till kalendern från en lokal `.ics`-fil och exporteras tillbaka till en. Varje import behålls som en egen prenumeration i den nya tabellen `ics_subscriptions`, så den kan byta namn, byta färg, döljas eller tas bort som en enhet utan att händelser skapade direkt i kalendern påverkas. En import läses en gång vid importtillfället. Lägger till vyerna **ImportCalendar**, **ExportCalendar**, **EditCalendars** och **CalendarFilter**. |
| **Helgdagar och helgdagsaftnar** | En dag markeras som helgdag genom att en kalenderhändelse skapas på den med färgen **HOLIDAY**, och som helgdagsafton med **HOLIDAYEVE**. En sådan händelse justeras till hela dygn när den sparas. Den dagliga klassificeringen publiceras till två interna variabler i Datalagret, `isHoliday` och `isHolidayEve`, som kan kopplas till en utgång så att ett PLC eller DUC kör sina egna scheman utifrån dagtypen. Klassificeringen är en egenskap hos dagen snarare än ett värde som skrivs in i varje tidkanals egna register, så ett par variabler räcker för samtliga scheman. Matchningen är ett överlappningstest, så en flerdagshelg markerar varje dag den täcker. |
| **Loggboksarkiv** | Loggboksposter kan arkiveras i stället för att raderas. Tabellen `logbook` får kolumnen `archived`, filtret får reglaget **Visa arkiverade**, och den nya behörigheten `Logbook_Archive` styr vem som får arkivera en post. Behörigheten är nekad som standard och måste därför tilldelas en roll innan någon kan arkivera. Inställningsvyn får en åtgärd som permanent raderar samtliga arkiverade anteckningar. |
| **Rapportenheter och prefix** | Rapporter bär en visningsenhet. Rapportkontrollerna har fått väljare för **Enhet** och **Prefix**, och varje vald signal får sin egen skalfaktor, beräknad utifrån signalens eget prefix och den valda enheten. Värdena hämtas i den enhet de loggats i, och faktorerna följer med till mallen tillsammans med data och hamnar på dess **Meta**-blad som `Factor1` till `Factor15`, där mallen tillämpar skalningen. En signal loggad i `Wh` och en annan redan i `kWh` rapporteras därför i samma skala. Listan **Enhet** är inte en fast uppsättning. Den byggs från enheterna hos signalerna på rapportens logger, reducerade till sin SI-bas, så endast enheter som faktiskt finns i datat erbjuds. Att välja en enhet filtrerar signalträdet till signaler av den dimensionen, och trädet är inaktiverat tills en enhet valts. Filtreringen är valfri per kontroll: en rapportvy utan objektet `Unit` lämnar trädet ofiltrerat och skickar värden i sina egna enheter. Prefix på `m³` gäller metern, så `dm³` är en tusendel av `m³` snarare än en tiondel. `ReportQueue`, `reportStats` och `reportSchedules` får kolumnerna `unit` och `factorArray`, som läggs till automatiskt vid första start så att befintliga databaser migrerar sig själva. |
| **Deltarapporter** | Två nya rapportkontroller, **Delta_Week** och **Delta_Year**, rapporterar förändringen över en period i stället för de loggade värdena i sig. De är avsedda för mätare som rapporterar en kontinuerligt ökande totalsumma. **Delta_Week** visar ett dygnsdelta per kolumn, en kolumn per veckodag, och accepterar loggningsintervall från timme till dygn. **Delta_Year** visar ett månadsdelta per kolumn, en kolumn per månad, med mallen `DeltaYear_H.xlsx` som accepterar intervall från månad ned till timme. Båda accepterar upp till 15 signaler. De levereras med nya Excel-mallar (`DeltaWeek.xlsx`, `DeltaYear_H.xlsx`) tillsammans med omarbetade `EnergyReport.xlsx` och `WeeklyEnergyReport.xlsx`. |
| **Lista över fjärrklienter** | Ett nytt skript `scRemoteClients` räknar de fjärrklienter som är anslutna till applikationen. En fjärrklient kan begära detaljlistan över anslutna klienter, som servern returnerar över RPC enbart till den begärande klienten. Listan lagras aldrig. Lägger till pop-out-vyn `RemoteClients.kvie`. |
| **Kriterier för larmutskick** | Utgående larmutskick kan filtreras på larmtillstånd. Tabellen `mail_schedules` får kolumnen `criteria` som accepterar `all`, `active`, `acknowledged`, `unacknowledged` och `inactive`. Kolumnen läggs till automatiskt vid första start och har `active` som standardvärde, så befintliga scheman fortsätter skicka på samma larmtillstånd som tidigare. Trädvyn för larmschema visar vilka larmklasser och vilka kriterier varje schema bevakar. |
| **Linjer och rör på karta** | Linjer och rör kan ritas på en karta tillsammans med nålar. Linjegeometrin definieras på objekten `MainLine1`, `MediumLine1` och `SmallLine1`, och skriptet `scMap` har omarbetats för att placera dem utifrån geografiska koordinater. |
| **Instrument på dashboard** | Två instrumentwidgetar, `Gauge_1x1` och `Gauge_2x2`, har lagts till i `Dashboard Widgets.klib`. De visar ett enskilt värde som en urtavla, i storlekarna en cell respektive två gånger två celler. |
| **Vy för oanvända suffix** | Knappen **Inte kopplade variabler** i felsökningsvyn öppnar den nya `UnboundDebug.kvie`, som listar varje suffix som inte är kopplat till ett popup eller en vy. |
| **Loggbokens ämnesträd** | Loggboken placerar en post på en arbetsvy, ett objekt, eller en egen ämnessökväg, och visar alla tre i ett gemensamt träd. Ett reglage växlar trädet mellan **arbetsvyordning**, som följer processvyernas mappstruktur, och **signalordning**, som följer taggsökvägen. De två är länkade genom objektindexet, så en anteckning på ett objekt visas även under varje vy där objektet är ritat, och en anteckning på en vy visas även under de objekt som är ritade i den. När två objekt i samma vy har samma namn utökas lövets namn med så mycket av taggen som behövs för att skilja dem åt. Tabellen `logbook` får `topic_kind` och `topic_ref`, härledda från `topic` och omhärledda vid varje start, och postlistan får kolumnen **Placerad på** som namnger vad varje post är kopplad till. De loggböcker som öppnas från ett objektpopup och från en processvy förväljer sitt ämne samtidigt som resten av trädet förblir nåbart. |

---

### Förbättringar

| Område | Beskrivning |
|---|---|
| **Larmutskick — kvitterande användare** | Utskick rapporterar nu vilken användare som kvitterat ett larm. Larmtillstånd och den kvitterande användarens namn hämtas från `wqlogg_larmlogg_alarm_data` i stället för att härledas från det aktiva larmobjektet. |
| **Larmdetaljer i beskrivning** | Varje larms detaljer kopieras till dess egenskap `description`, vilket gör texten åtkomlig utanför larmobjekt. |
| **Status för larmschema** | **Larm - Schema** uppdaterar antalet scheman och deras aktiva tillstånd löpande i stället för enbart vid inläsning. |
| **Underhållslogg** | Knappen **Rensa underhållsloggen** tömmer samtliga poster i underhållsloggen. Åtgärden ligger bakom en bekräftelsedialog och behörigheten `Config`. |
| **Larmfrekvens** | **Larm - Frekvens** har fått knappen **Filtrera** som öppnar larmfiltrets pop-out, så frekvensvyn kan avgränsas på samma sätt som larmlistan. |
| **Datumordning i stapeldiagram** | En ny egenskap ritar datumaxeln från höger till vänster i stället för från vänster till höger. |
| **Färger vid kalenderimport** | Importerade kalendrar skapas med färgen **DEFAULT** och kan byta färg i **EditCalendars**. Färgerna **HOLIDAY** och **HOLIDAYEVE** är det som markerar en dag, så att ändra en kalender till eller från någon av dem visar först en varning. |
| **Helgdagar på fjärrklienter** | Skriptet `scHoliday` är registrerat för fjärrklienter. |
| **Temaanpassade filter** | Larmfiltret och underhållsfiltret följer det aktiva temat. |
| **Rapportschemaläggaren följer rapportsystemet** | En schemalagd rapport lagrar samma visningsenhet och signalfaktorer som en manuellt skapad, valda i `ReportSchedule2.kvie`. |
| **Signalkontroll för rapport** | Att skapa en rapport blockeras tills minst en signal är vald, samma kontroll som MOD och WWT redan hade. |
| **Kalender — överskottsmarkering öppnar dagen** | Månadsvyns markering **Visa fler (N)** öppnar dagvyn för det datumet, där dagens samtliga händelser syns. Överskjutande händelser ritas aldrig i månadscellen i sig. |
| **Kalender — händelsenamn i vecka och dag** | Händelser med identiskt tidsspann ritades som staplade fält med sina namn ovanpå varandra. En kolumn som innehåller mer än en händelse fälls nu ihop till ett enda fält med etiketten **Visa händelser (X)**, som öppnar en väljare med allt fältet står för. |
| **Textlängd i larmöversikt** | Långa larmtexter hålls inom bredden på larmöversiktens widget i stället för att sträcka ut den. |
| **Ikoner i inställningar** | Inställningsikoner levereras i grå och vit variant så att de följer det aktiva temat. |
| **Speed dial** | Objektet `SpeedDialRight` ritades i fel proportioner. Dess elementbredder och förskjutningar har korrigerats. |
| **Beskrivningar av objektegenskaper** | Egenskapsbeskrivningar visas som hjälptext i **WideQuick® Designer**. De beskrivningar som lämnats tomma på ventilobjekten har fyllts i, och exemplet `ObjectName` i `DynTouch` saknade sitt avslutande citattecken och stod som `"FS61` i stället för `"FS61"`. |
| **`scPrototypes`** | Har fått hjälpfunktionen `toUpperCase()` för användning i projektskript. |
| **Larmutskick — kompakt SMS** | Ett larmschema kan skicka ett kompakt meddelande i stället för den fullständiga listan per larm. Ett kompakt meddelande bär rubriken, händelsetypen och en kommaseparerad lista över de larm som matchar den, vilket håller ett utskick som omfattar många larm inom en rimlig längd. |
| **Inmatningsrutan accepterar Enter** | Pop-out-rutan för inmatning behandlar **Enter** som en bekräftelse, så ett värde kan skrivas in och bekräftas utan att knappen behöver användas. |
| **Tystare loggar** | Applikations- och felloggarna har städats upp. Schemamigreringar i `scCalendar`, `scHoliday`, `scMaintenance` och `scSuffix` kontrollerar nu om en kolumn finns innan den läggs till, i stället för att försöka ändringen och låta SQLite-drivrutinen rapportera felet till `Errors.log`. `scUsers.hasPriv()` nekar i stället för att kasta ett fel när den anropas utan behörighet. Flera hundra rader återkommande uppstartsbrus är borta. |

---

### Ändringar

| Område | Förändring |
|---|---|
| **Borttagna vyer och skript** | Den oanvända `CreateEnergyReport.kvie` har raderats och `scMapObjects.js` har tagits bort ur projektet. En kopia finns kvar i resurspaketet om den skulle behövas. |
| **Kalenderflöden** | Händelser kan nu importeras till kalendern från en lokal `.ics`-fil. |

---

### Buggar

| # | Område | Beskrivning |
|---|---|---|
| 1 | Underhåll | En missad återkommande deadline föll bort när ingen användare var inloggad, eftersom insättningen krävde en aktuell användare och kastade ett fel i stället. Skaparen faller nu tillbaka på `System`. |
| 2 | Larmutskick | Larmbeskrivningen kunde skickas som den bokstavliga texten `Undefined`. En kontroll undertrycker nu fältet när ingen beskrivning finns. |
| 3 | Larmlista | `dslAlarms.onDataChanged()` kunde lägga till samma larm två gånger. Listan genomsöks nu före tillägg, så dubbletter avvisas. |
| 4 | Kalender | Händelser täckte inte ett helt dygn. En heldagshändelse skrivs nu på index 0 och index 48, så att den spänner över dygnet. |
| 5 | Dashboard | Övergångar till och från sommartid gjorde stapeldiagrammet felinriktat. Åtgärdat, tillsammans med rendering av rutnät och beskrivning. |
| 6 | Karta | `StatusPin` tillämpade sin dynamiska status utan att kontrollera larmobjekten, så en nål kunde visa ett tillstånd som dess objekt inte hade. Den verifierar nu mot både objektlistan och larmobjekten. |
| 7 | Karta | Linjer och rör ritades aldrig på en karta. Uppdateringsanropen i `scMap` var avstängda, och geometriegenskaperna låg på infopopupen i stället för på linjeobjekten. Anropen är nu aktiva, och egenskaperna ligger på objekten `MainLine1`, `MediumLine1` och `SmallLine1`. Värden som tidigare angetts på infopopupen behöver anges på nytt på linjeobjekten. |
| 8 | Karta | Ett rör som sträckte sig över ett stort geografiskt område beräknade sina pixelförskjutningar från en fast `Line0` som kunde hamna utanför den synliga ramen, vilket placerade röret felaktigt. Förskjutningarna utgår nu från hörnet av den synliga ramen. |
| 9 | Objektbibliotek | Egenskapen `CustomLabel` hade ingen effekt på namnskylten för vissa objekt. Åtgärdat i biblioteken för givare, ventiler, speed dial och kartindikatorer, inklusive deras äldre varianter. |
| 10 | Objektbibliotek | Spjäll rapporterade NO och NC inverterat, både i det aktuella och i det äldre spjällbiblioteket. Åtgärdat. |
| 11 | Navigering | Menyknappar bytte inte färg när temat växlades, och ett undernavigeringsobjekt som överlevde sin vy bröt registreringsloopen. En kontroll och ett avregistreringssteg har lagts till. |
| 12 | Navigering | I den fullständiga menyn ångrade **Tillbaka** på en sidindelad undernavigeringssida endast det senaste steget framåt, eftersom sidindelningen styrdes av ett enda föregående indexvärde i stället för av en sidhistorik. Skriptet `scSubNavPopup` registrerar nu startindex för varje sida, så att **Tillbaka** stegar bakåt genom hela sekvensen. |
| 13 | Skriptbibliotek | `scAlarmFinder` var registrerat två gånger i `ScriptLibraries.kdat`, och felmeddelanden i `scAuditTrail` och `scMaintenance` bar fortfarande det gamla prefixet `scMaintenanceLog`, vilket pekade ut fel skript när något gick fel. Den dubbla registreringen har tagits bort och prefixen korrigerats. |
| 14 | Larmöversikt | Lagret **error** kunde inte täcka vyn eftersom andra objekt låg ovanför det. Objektordningen har korrigerats. |
| 15 | Underhåll | `MaintenanceInfoPanel` var registrerad under ett namn som inte stämde med dess vyfil, och en inaktuell `folder`-post låg kvar i `SuffixConfig.db`. Båda korrigerade. |
| 16 | Suffixinställningar | **Suffixalias - Popuper** nycklar sina kategorier på deras svenska namn medan trädet visar dem översatta, så på något annat språk kunde inställningsfälten inte matchas. Kontrollerna visades men tog tyst inte emot inmatning, och att välja en post fyllde inte längre i kombinationsrutorna och textfälten. Den visade etiketten översätts nu tillbaka till sin kanoniska nyckel före användning. Att lägga till en kategori avvisar dessutom ett namn som matchar en befintlig kategoris översatta etikett, vilket annars skulle skapa två poster som inte går att skilja åt. |
| 17 | Suffixinställningar | Att skapa en kategori rapporterade ett fel och lämnade den nya kategorin omarkerad, eftersom trädet söktes igenom med det råa inskrivna namnet och ett villkor som den översatta modellen aldrig kan matcha. Uppslagningen använder nu den etikett noden faktiskt visas under, och hoppar över markeringen i stället för att kasta ett fel om noden inte kan hittas. |
| 18 | Underhåll | En konfiguration för återkommande underhåll gick inte att skapa från **Underhåll - Återkommande**. Tre av kontrollerna, intervallantalet, prioriteten och ansvarig, är inte direktbundna till konfigurationsobjektet, så de värden som angavs förkastades när konfigurationen sparades. De kopieras nu över före sparningen. `getTemplateFromName()` returnerade dessutom en malls `deadline_value` i millisekunder medan `applyOffset()` förväntar sig ett antal intervallenheter, vilket placerade den första deadlinen långt utanför något användbart intervall. Värdet konverteras nu till ett enhetsantal vid inläsning och `deadline_type` normaliseras på samma ställe. Att spara en konfiguration med tomt namn, tom typ, tom beskrivning eller tomt intervall skriver inte längre en trasig rad. |

---

### Översättningar

| Område | Förändring |
|---|---|
| **Nya översättningssträngar i projektet** | Etiketter för loggboksarkiv och vykontrollpopupen, vyer för rapportschema, vyer för kalenderimport, export och redigering, underhållets infopanel och underhållsfilter, etiketter för larmkriterier, etiketter för dokument och filväljare, inloggningsvyn, samt strängar i rapport- och spjällbibliotek. |
| **Borttaget** | Döda källsträngar rensades bort inför den nya översättningsomgången. |
| **Verifierat** | Översatta strängar jämfördes mot den svenska basuppsättningen för att fånga poster som glidit från sin källa. |
| **Larmkriterier** | Kriterier visas översatta men lagras som kanoniska nycklar. Skriptet `scAlarmSender` översätter tillbaka det valda värdet innan det skrivs till databasen. |
| **Rapportsträngar** | Etiketter för enhet, prefix och deltarapporter lades till, och felstavningen "Excell" är nu "Excel" genomgående. |
| **Strängar för ihopfällda kalenderhändelser** | **Visa fler (N)** och **Visa händelser (X)** lades till för ihopfällda händelser i månad, vecka och dag. |
| **Uppdaterade språk** | Arabiska, bulgariska, kroatiska, tjeckiska, danska, engelska, finska, franska, tyska, ungerska, italienska, mandarin, norska, polska, portugisiska (PT och BR), rumänska, slovenska, spanska, svenska. |

---

### Biblioteks- och vyändringar

| Fil | Förändring |
|---|---|
| `scHoliday.js` | Kalenderimport och export, delad ICS-tolk, klassificering av helgdag och helgdagsafton publicerad till `isHoliday` och `isHolidayEve` |
| `scAlarmSender.js` | Kriteriefiltrering, rapportering av kvitterande användare, larmtillstånd hämtat från larmloggen, kontroll av beskrivning, återöversättning av kriterier |
| `scLogBook.js` | Kolumnen `archived`, utfasning och rensning av `deleteMark`, permanent radering av arkiverade poster |
| `scRemoteClients.js` | Nytt skript — antal anslutna klienter och klientlista levererad över RPC |
| `scMap.js` | Hantering av linjer och rör, förskjutningar utgående från den synliga ramen |
| `scMaintenance.js` | `System` som reserv vid obevakade återkommande insättningar |
| `scDashboard.js` | Egenskap för datumordning i stapeldiagram, korrigering för sommartid, rättningar av rutnät och beskrivning |
| `scSubNavPopup.js`, `scThemes.js` | Temaomfärgning av menyknappar, kontroll och avregistrering av inaktuella undernavigeringsobjekt |
| `scAlarm.js` | Dubblettkontroll i `dslAlarms.onDataChanged()` |
| `Privileges.kdat` | Ny behörighet `Logbook_Archive` |
| `DataStore.kdat` | Larmdetaljer kopierade till `description` |
| `ImportCalendar.kvie`, `ExportCalendar.kvie`, `EditCalendars.kvie`, `CalendarFilter.kvie` | Vyer för kalenderimport, export, redigering och filtrering |
| `UnboundDebug.kvie` | Ny vy som listar suffix som inte är kopplade till ett popup eller en vy |
| `RemoteClients.kvie` | Ny pop-out som listar anslutna fjärrklienter |
| `Logbook.kvie`, `LogBookFilter.kvie`, `LogbookViewControllerPopup.kvie` | Arkivkolumn, reglaget **Visa arkiverade**, översatta etiketter |
| `Larm - Schema.kvie`, `AlarmSchedule_1.kvie`, `AlarmSchedule_2.kvie` | Kriterieval, löpande schemaantal och aktivt tillstånd |
| `Spårningslogg - Underhåll.kvie` | Knappen **Rensa underhållsloggen** |
| `Map Indicators.klib` | Linje- och rörobjekt, verifiering av larmobjekt i `StatusPin`, rättningar av `CustomLabel` |
| `Dashboard Widgets.klib` | Instrumentwidgetar, datumordning i stapeldiagram |
| `COMPONENTS.klib`, `COMPONENTS_Legacy.klib`, `DAMPERS_Legacy.klib` | Korrigering av NO och NC för spjäll |
| `Valves.klib`, `Speed Dial.klib`, `DynTouch.klib` | Ifyllda egenskapsbeskrivningar, proportioner för `SpeedDialRight`, korrigerat exempel för `ObjectName` |
| `scReports.js`, `scReportScheduler.js` | Upplösning av enhet och SI-prefix, skalfaktorer per signal, kolumnerna `unit` och `factorArray` med sina schemamigreringar, loggerkontroll |
| `Report.klib` | Väljare för enhet och prefix, stöd för deltarapporter |
| `Delta_Week.kvie`, `Delta_Year.kvie` | Nya deltarapportkontroller, med kontroll av vald signal innan en rapport kan skapas |
| `ReportSchedule2.kvie` | Val av enhet och prefix för schemalagda rapporter |
| `Reports/Templates/*.xlsx` | Nya mallar `DeltaWeek` och `DeltaYear_H`, omarbetade energirapportmallar |
| `scCalendar.js` | Månadsvyns överskottsmarkering öppnar dagvyn för det datumet |
| `scWeekViewManager.js`, `scDayViewManager.js`, `Calendar.klib` | Ihopfällning av händelser i vecka och dag med **Visa händelser (X)** |
| `Larm - Översikt.kvie` | Objektordning så att felagret täcker vyn |
| `Translations.klib` | Tillagda strängar, borttagning av döda strängar, verifiering mot svensk basuppsättning |

</details>


## WideQuick BMS 2026.1.1 { #bms-2026-1-1 }

__Utgiven 2026-07-08__ — Patch-version BMS 2026.1.1.1
<details class="release" markdown="1">
<summary>Versionsnoteringar</summary>

### Buggar

| # | Område | Beskrivning |
|---|---|---|
| 1 | Spårningslogg | Spårningsloggens filter kunde inte kombinera objekt, användare och tid samtidigt (det var begränsat till två villkor), och radantalsgränsen returnerade inte tillförlitligt de senaste raderna. Åtgärdat med ett enda predikatbaserat filter. |
| 2 | Underhåll | Återkommande uppgifter lagrade intervallenheten på det aktiva gränssnittsspråket, så den återkommande förskjutningen kunde hoppas över eller tillämpas felaktigt när språket skilde sig från när uppgiften skapades. Åtgärdat genom att normalisera enheter till en kanonisk form. |

---

### Biblioteks- och vyändringar

| Fil | Förändring |
|---|---|
| `Spårningslogg.kvie` | Spårningsloggens filter omskrivet — predikatbaserad filtrering på objekt/användare/tid med en gräns för de N senaste raderna |
| `scMaintenance.js` | Intervallenheter för återkommande uppgifter normaliserade till en kanonisk form för språkoberoende schemaläggning |

</details>


__Utgiven 2026-07-02__
Modular Framework Version: <!-- MOD VERSION LINK -->
<details class="release" markdown="1">
<summary>Release notes</summary>

### Nya funktioner

| Funktion | Beskrivning |
|---|---|
| **Tidskanalsprofiler** (`scTimeChannel.js`) | Ett nytt skriptbibliotek som låter användare spara och läsa in namngivna tidskanalscheman. En profil sparar på/av-värdena för alla dagtyper — veckodagar, helger, helgdagar och upp till tre specialdagar — för en given tagg och lagrar dem i Config-databasen för senare återanvändning. |
| **Historik — Importera från alla** | Ny arbetsvy `ImportFromAll.kvie` under `Common_Popup/HistorikPopups/` för att importera historiska signalgrupper från vilken del som helst av projektet. |
| **Historik — Importera sparade signaler** | Ny arbetsvy `ImportSavedSignals.kvie` för att importera från tidigare sparade signalurval. |

---

### Förbättringar

| Område | Förändring |
|---|---|
| **Rapportschemaläggare** | Rapporter kan nu skickas vid en specifik tid på dagen (±5 min noggrannhet). Tre nya databaskolumner har lagts till i `reportSchedules`: `trigger_time`, `trigger_day` och `trigger_month`. `checkTrigger`-logiken har skrivits om och `ReportSchedule1.kvie` har uppdaterats med nya UI-kontroller. |
| **Kart pins** | Kart pins använder inte längre tooltip-objekt. De skapas nu med `createObject`, vilket ger bättre kontroll över visningen och gör dem mer stabila i webbklienten. |
| **Karta — navigeringsdjup för mappar** | Navigering från kart pins till mappar var begränsad till 1 nivå djup. Den kan nu navigera till valfritt djup. |
| **Karta — larmtextöversättning** | Larmtexter som visas i kart pins popup körs nu genom `Language.translate` så att de respekterar det aktiva språket. |
| **Karta — `mapView`-egenskap** | Alla interna `mapViews`-referenser har korrigerats till `mapView`. Kartan (`Karta.kvie`) visas inte längre ovanför navigeringsfältet i webbklienten. |
| **Dashboard — stapeldiagram** | Stapeldiagrammet stöder nu grupperingsvy per dagar, veckor och år. |
| **Dashboard — utökad vy** | Historikens angiven tid gäller nu även i den utökade popup-vyn. Cirkel-, stapel- och historikwidgetar initieras nu vid laddning via `scDashboard`. Den utökade förklaringen visar det aktuella värdet vid linjalens position och andelen i procent där det är tillämpligt. Åtgärdat att kolumnbredder i den utökade listan kunde sträckas ut av långt innehåll. |
| **Kalender** | Månadsnamn och veckodagsnamn körs nu genom `Language.translate` och matchar det valda gränssnittsspråket. |
| **Larmsändare — tidslucka 2** | Lade till kolumnen `slot2_active` i `mail_schedules` så att varje veckodag självständigt kan aktivera eller inaktivera sin andra tidslucka. |
| **Larmsändare — veckodag** | Åtgärdat ett off-by-one-fel där `getDay()` förskjöt alla larmdagar med en dag. Ett måndag-först-index används nu korrekt. |
| **Larmsändare — midnattssändning** | Tidsluckor med `00:00 – 00:00` behandlas nu som inaktiverade i stället för att utlösa en midnattssändning. |
| **Larmsändare — timervakt** | Timerfördröjningen skyddar nu mot ett noll eller negativt `timeToSend`-värde och använder minst 2 sekunder som standard. |
| **Larmschema** | Redigering av ett befintligt schema återställer inte längre `emailActive` till 0 utan att meddela användaren. `00:00 till 00:00` är standardtillståndet för inaktiverade nya scheman. Knappar följer nu det aktiva temat. |
| **Larm-e-post och SMS** | Alla hårdkodade svenska etiketter körs nu genom `Language.translate` så att de visas på användarens aktiva språk. |
| **Historik / VySpecifikHistorik** | Kan nu läsa in signalgrupper från andra delar av projektet. Signallistan har bytts från en platt lista till en trädvy. Maximalt antal signaler har sänkts för att förbättra prestanda. Taggar som inte loggas visas nu tydligt. |
| **Underhåll** | Lade till fältet `reminder_enabled` i underhållsmallar. Gränssnittet visar nu en kryssruta för påminnelse i mallredigeraren. |
| **Dokument och Underhåll** | Båda modulerna hanterar nu taggstrukturen `C_c.D_d.S_o_s` utöver tidigare stödda format. |
| **Dokument — UI-etiketter** | Dokumentlistans grupperingsrubriker körs nu genom `Language.translate`. |
| **Styrkurva** | Popup-fönstret visar nu det aktuella värdet på kurvan. Den kan även placeras direkt i en arbetsvy i stället för enbart som ett popup-fönster. |
| **Styrkurva tid** | Uppdaterad till samma funktionsnivå som den vanliga Styrkurvan och visuellt omarbetad. En vertikal linje spårar aktuell klocktid i realtid på grafen. En horisontell linje spårar det aktuella Y0-procesvärdet. X-axelns etikett visar nu aktuell tid i formatet HH:MM. Datapunktsrutor är arrangerade i två kolumner (tidigare en enda kolumn) med stöd för upp till 24 synliga punkter. Förhandsgranskningskurvan uppdateras nu även när Y-axelns min- och maxvärden ändras, inte bara när datapunkter redigeras. |
| **Styrkurva — oberoende sparande och laddning av begränsningsvärden** | Både Styrkurva och Styrkurva tid sparar och läser nu in övre och nedre begränsningsvärden oberoende av varandra. Tidigare krävdes att båda begränsningshandtagen var synliga för att något av värdena skulle inkluderas i en sparad profil. |
| **Styrkurva — förhindra duplicerade profilnamn** | Det är nu blockerat att byta namn på en profil till ett namn som redan används av en annan profil. |
| **Styrkurva — spårningslogg** | `Spårningslogg.kvie` uppdaterad med stöd för styrkurvans spårningslogg. |
| **Process-popup** | Visuell uppdatering med korrigerad elementplacering och avstånd. |
| **Stäng popout** | Popout-fönster som öppnats via en länk använder nu korrekt stängningsåtgärd i stället för `app.popup.visible`. |
| **SubNav-popup** | Initierar nu subnav-routeträdet vid behov för korrekt beteende i webbklienter. Standardfallback-vy korrigerad till `Dashboard Energi.kvie`. |
| **Inställningar** | Inställningsvyn respekterar nu användarens privilegienivåer. |
| **`scPlatform`** | Alla timers anropar nu `setSingleShot(true)` för att förhindra upprepade aktiveringar efter den initiala detekteringen. |
| **Väder** | En dataändringstriggare har lagts till så att väderwidgeten uppdateras automatiskt när underliggande data ändras. |
| **"E-post"-etikett** | Alla ställen som tidigare visade "Epost" använder nu konsekvent "Email". Textrutor har anpassats för att rymma översatta strängar. |
| **Språk icon** | Språkikonen är nu kvadratisk för konsekvent visning i inställningar. |

---

### Buggar

| # | Område | Beskrivning |
|---|---|---|
| 1 | Larmschema | Redigering av ett schema återställde tyst `emailActive` till 0. Åtgärdat. |
| 2 | Larmsändare | Off-by-one-fel i veckodagsindex gjorde att alla schemalagda larmfönster hamnade på fel dag. Åtgärdat. |
| 3 | Karta | Mappnavigering från kartnålar var begränsad till en katalognivå. Åtgärdat för att stödja obegränsat djup. |
| 4 | Datumkonfiguration | Hantering av översättningssträngar orsakade att datumkonfigurationen misslyckades när locale-formatet producerade en icke-numerisk sträng. Datumjämförelse använder nu numeriska värden direkt. |
| 5 | Dashboard | Kolumnbredder i den utökade listan sträcktes ut av långt innehåll. Åtgärdat. |
| 6 | Rapporter | Kolumnordning i loggerlistan var felaktig. Åtgärdat. |
| 7 | Kalender | Månads- och dagnamn renderades med systemets locale i stället för det aktiva WideQuick-språket. Åtgärdat. |
| 8 | Dokument | Taggstrukturen `C_c.D_d.S_o_s` delades felaktigt, vilket orsakade fel vid uppbyggnad av objektträdet. Åtgärdat med korrekt parsning. |
| 9 | Kalender | Underhållspåminnelser visades på två kalenderdagar i stället för en. Åtgärdat genom att låsa påminnelseblocket till början av dagen. |

---

### Översättningar

| Område | Förändring |
|---|---|
| **Nya projektöversättningssträngar** | Larmkvittering, historikimportetiketter, inställnings- och privilegieetiketter, instrumentpanelens widgetsträngar, rapportschemaläggningens tidskontroller, kalendarns månads- och dagnamn, dokumentgruppsetiketter, kartnålarnas tooltip-texter, e-poststatussträngar ("Skickar…", "Skickat!", "Misslyckades") och rapportstatussträngar ("Skapar rapport…", "Rapport klar!"). |
| **Borttaget** | Överblivna svenska källsträngar. |
| **Verifierat** | Alla svenska källsträngar har nu en motsvarande översättningspost. |
| **Uppdaterade språk** | Arabiska, bulgariska, kroatiska, tjeckiska, danska, engelska, finska, franska, tyska, ungerska, italienska, mandarin, norska, polska, portugisiska (PT + BR), rumänska, slovenska, spanska, svenska. |

---

### Biblioteks- och vyändringar

| Fil | Förändring |
|---|---|
| `Translations.klib` | Stora strängadditioner och rensning för alla språk |
| `Dashboard Widgets.klib` | Widget- och språkuppdateringar |
| `Map Indicators.klib` | Uppdateringar av kart pins, indikatorer och tooltips |
| `Report.klib` | Ändringar av rapportmall och layout |
| `COMPONENTS.klib` | Komponentuppdateringar |
| `COMPONENTS_Legacy.klib` | Uppdateringar av äldre komponenter |
| `Dampers_Legacy.klib` | Uppdateringar av äldre komponenter |
| `COMMON_STATIC.klib` | Uppdateringar av statiska komponenter |
| `Calendar.klib` | Uppdateringar av kalendervisning |
| `CustomPopupObjects.klib` | Uppdateringar av popup-objekt |
| `WorkviewNameDisplay.klib` | Uppdateringar av arbetsvy-namnvisning |
| `Buttons.klib` | Nya knappdefintioner |
| `AlarmSchedule_1.kvie` | Fullständig UI-omarbetning för tidslucka 2 och tema |
| `ReportSchedule1.kvie` | Nya sändningstidskontroller |
| `VySpecifikHistorik.kvie` | Laddning av signalgrupper från andra system |
| `Historik.kvie` | Signalgrupper från andra system, trädvy för signallista, max antal sänkt |
| `Dashboard *.kvie` | Förbättringar av stapeldiagram, förklaring och laddning |
| `Karta.kvie` | Rättning av navigeringsfältets z-ordning för webb |
| `WORKSPACE.kvie` | Uppdateringar av arbetsytelayout |
| `LB01/LB02/LB03.kvie` | Uppdateringar av VVS-vyer, standard och äldre |
| `VS11 / VV10–VS20.kvie` | Uppdateringar av värmesystemsvyer |
| `Larm - Logg.kvie` | Uppdateringar av larmloggsvy |
| `Inställningar.kvie` | Inställningsvy med privilegiestöd |

</details>


## WideQuick BMS 2026.1.0 { #bms-2026-1-0 }
__Utgiven 2026-05-21__
Modular Framework-version: [WideQuick MOD 2026.1.0](../../mod/releases/index.md#mod-2026-1-0) 
<details class="release" markdown="1" close>
<summary>Versionsnoteringar</summary>

Detta är den första versionen av WideQuick BMS i Modular Framework-familjen — byggnadsstyrningskonceptet ombyggt på Modular Framework-grunden. Den samlar det fullständiga ramverkets funktionsuppsättning (flerspråksstöd, en systemintegrerad loggbok, en underhållskalender, dokumenthantering samt brett stöd för webb- och fjärrklienter) tillsammans med de byggnadsstyrningsverktyg som definierar BMS-konceptet, såsom tidskanaler, ändamålsenliga suffix, styrkurvor och färdiga byggnadsöversikter.

### Nya funktioner

| Funktion | Beskrivning |
| --- | --- |
| **Flerspråksstöd** | Vyer, skript, objektbiblioteket, dynamik och datalager är nu fullt översättningsbara, med en inbyggd språkväljare och flaggikoner för att byta språk vid körning. |
| **Verktygstipsystem** | En ny verktygstipsmekanism (`scToolTip`) lägger till kontextuella hjälprutor i hela systemet, inklusive historik- och kartobjekt. |
| **Omskrivet arbetsvy-animationssystem** | Animationssystemet har byggts om från grunden för att vara mer mångsidigt och enklare att konfigurera, med en tillhörande inställningsvy och hjälpfunktioner för att läsa användardefinierade temafärger. |
| **ObjectFinder & goTo** | Varje objekt indexeras automatiskt med sin vysökväg och sitt namn, och den nya funktionen `goTo` låter dig hoppa direkt till vilket objekt som helst från var som helst i projektet. |
| **Konfigurerbart körningsbeteende** | Uppdateringsfrekvensen för värdevisning kan nu justeras vid körning, och valt tema (ljust/mörkt) sparas och återställs vid nästa uppstart. |
| **Automatisk datalagring** | Loggrar och historik rensar nu automatiskt data som är äldre än en angiven ålder (t.ex. två år), vilket hindrar databaser från att växa obegränsat över tid. |
| **Webb- och fjärrklientstöd** | Stor utökning av klientstödet: rapportskapande, redigering av larmscheman och loggvisaren fungerar alla på WideQuick Web och fjärrklienter, och suffix, vybehörigheter samt underhållsstatus synkroniseras mellan alla klienter. |
| **Import av äldre vyer** | Vyer byggda i WideQuick BMS 8.0 eller tidigare kan lyftas direkt in i ramverket, där symbolerna omedelbart målas om till de nya, omdesignade objekten men behåller sina kopplingar. |

### Nya och uppdaterade moduler

| Modul | Beskrivning |
| --- | --- |
| **Objektbibliotek** | En omdesignad uppsättning processsymboler (ventiler, sensorer, spjäll med mera) med ett renare och moderniserat utseende, plus de äldre BMS-symbolerna (inklusive luftbehandling) integrerade för att fungera i ramverket med bibehållet välkänt utseende. Objekten standardiserades avseende teckenstorlek, decimaler, bildtexter och beskrivningar, och digitala värdevyer lades till. Det är dessa symboler som äldre BMS 8.0-vyer målas om till vid import. |
| **Tidskanaler** | Tidskanalslfunktionalitet portad från det äldre BMS och integrerad i det gemensamma popupsystemet. Tidskanalskonfigurationer kan sparas och tillämpas, med ett användartilldelat namn och en beskrivning, samt en behörighetskontroll på tidskanalspopupen. |
| **Styrkurvor** | Styrkurveobjekt med konfigurerbara X/Y-börvärden, värdebegränsning och axellåsning, plus en tidsbaserad styrkurva. Kurvsignaler har egna behörigheter och vyerna skalas korrekt över upplösningar. |
| **Manövreringsläge** | En popup för manuell manövrering av objekt, inklusive byte av handikon och avstängningsalternativet, med bildtextförsedda specialknappar. |
| **Översiktsbild** | En ny konfigurerbar översiktsbild byggd från ett bibliotek av återanvändbara widgetobjekt (`Dashboard Widgets.klib`), med färdiga BMS-översiktsbilder och ett dynamiskt larmdiagram. Widgets fungerar på skrivbord, webb och fjärr, den startöversiktsbild som visas efter inloggning är konfigurerbar, och exempelöversiktsbilder finns med att bygga vidare från. |
| **Loggbok** | En ny modul för att skapa, bläddra i och filtrera tidsstämplade loggposter i hela projektet. Filtrera efter ämne, datumintervall och användare; öppna den förfiltrerad till ett specifikt ämne; och bädda in mallen `LogBookEntryButton` i valfri vy. |
| **Kalender** | En ny kalendermodul med månadsnavigering, minikalender och ett sidofält för kommande händelser. Underhållsuppgifter visas som kalenderhändelser med statusbaserade färger och automatiska påminnelser inför planerat arbete. |
| **Dokument** | En ny dokumenthanteringsmodul med en filväljare för att ladda upp dokument och en hanterare (`scDoc`) för att länka dokument till objekt, validerad på skrivbord, fjärr och webb. |
| **Karthanterare** | En ny kartmodul med en exempelvy och webbkompatibelt kartstöd, plus en ny uppsättning kartnavigeringsindikatorobjekt för att placera och länka objekt på en karta. |
| **Historik** | Historik kan nu visas för hela projektet, inte bara ett enskilt objekt, med automatisk decimalskalning och en bredare färgspridning för lättlästa flerkurvstrender. |
| **Underhåll** | Väsentligt utökad: återkommande underhållsuppgifter med ett trädvyobjektväljare, realtidssynkronisering över alla anslutna klienter, uppdateringsknappar, en per-användare underhållsräknare på översiktsbilden, samt status- och prioritetsfärger genomgående. En ny **systemidentitets**-mekanism registrerar varje system, märker uppgifter efter system och lägger till en Systemkolumn och ett filter så att en enda underhållsdatabas kan betjäna flera installationer. |
| **Rapporter** | Rapportschemaläggaren stöder nu två tidsintervall per dag och schemaläggning med alias, visar tydliga statusmeddelanden och kan skapas och köras från fjärrklienter. Rapporter från en befintlig WideQuick-installation kan också migreras till ett Modular Framework-projekt. |
| **Larm** | En ny larmfrekvensvy visar hur ofta larm uppstår, fjärrlarm kan schemaläggas i larmscheman med larmklass och grupp, larmscheman fick knappar för att markera/avmarkera alla larmgrupper, knappen "Visa information" stöder visningsskript, och larmlognhändelser registreras inte längre dubbelt. Larmlistans statusfärger följer den standardiserade BMS-larmfärgkonfigurationen. |

### Ändringar

| Område | Ändring |
| --- | --- |
| **Navigation** | "Loggar" har flyttats till "Rapporter & loggar", "Underhåll & loggar" har döpts om till "Underhåll", enskilda menyalternativ kan döljas vid körning, och en återvisningsknapp har lagts till för dold undernavigering. |
| **Inloggning och användare** | Inloggning är nu möjlig via en kombinationsruta istället för att skriva ett användarnamn, och inloggningskravet kan inaktiveras från inställningsvyn. |
| **Användare och behörigheter** | Nya demoanvändare lades till, var och en med en lämplig rollbaserad behörighetsnivå, och behörighetssystemet omarbetades: behörigheter döptes om från det gamla schemat till ett nytt, dedikerade behörigheter lades till för underhålls- och loggboksåtgärder, och användare får nu ett tydligt meddelande när de saknar behörighet för en åtgärd. Rollen `Servicetekniker` döptes om till `service`. |
| **Processvärdesobjekt** | Värdeuppdateringar drivs nu av en datalagerlyssnare istället för dynamik, vilket ger lättare rendering för inaktuella eller långsamt föränderliga variabler eftersom objektet bara ritar om sig när värdet faktiskt ändras. |
| **Larmterminologi** | Larmterminologin standardiserades: "Allvarlighetsgrad" är nu "Larmklass" och "Bekräfta/Bekräftbara" är nu "Kvittera/Kvitterbara" genomgående i vyer och översättningar. |
| **Signalsimulering** | Demo-Modbus-signaler konverterades till OPC UA, med en simulator (`scSimMB`) som genererar realistiska värden för de nya OPC UA-signalerna. |
| **Inställningar** | Inställningar som inte är tillgängliga på fjärr-/webbklienter är nu tydligt inaktiverade. |
| **Kartindikatorer** | En ny uppsättning kartnavigeringsindikatorobjekt har introducerats och används nu som standard. De tidigare kartindikatorerna används inte längre i ramverkets vyer men är fortfarande fullt funktionella och beter sig precis som förut, så befintliga projekt som använder dem påverkas inte. |
| **Licensiering** | Projektet levereras nu under BSD 3-klausuls-licensen, tillsammans med tredjepartslicenstexter och tillskrivningar. |

### Migrering från ett äldre WideQuick BMS

Som den första BMS-versionen i Modular Framework-familjen finns det ingen tidigare version i denna familj att uppgradera från. När ett befintligt, äldre WideQuick BMS-projekt förs över, notera följande:

| Ämne | Notering |
| --- | --- |
| **Import av äldre vyer** | Vyer byggda i WideQuick BMS 8.0 eller tidigare kan lyftas direkt in i detta projekt, där symbolerna målas om till de nya, omdesignade objekten men behåller sina kopplingar. |
| **Objekt använder SuffixAlias** | Ramverksobjekt refererar sina värden via en `SuffixAlias` snarare än suffixet direkt. Ett suffixalias måste definieras för varje objekt; objekt med ett okonfigurerat alias markeras visuellt i vyerna. |
| **Identitet för underhållssystem** | Vid första start tillskrivs underhållsuppgifter det aktuella systemet baserat på värdnamn, och en migreringsdialog visas om ett namnbyte på applikationen upptäcks. Granska tilldelningen efteråt för att bekräfta att uppgifterna tillhör rätt system. |

</details>
