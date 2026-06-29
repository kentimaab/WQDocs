---
title: Versioner — BMS
product: bms
page_type: release
status: draft
last_reviewed: 2026-06-16
tags:
 - BMS
---

# Versioner — BMS

Versionsnoteringar för WideQuick BMS. Den senaste versionen visas först och är expanderad;
äldre versioner är ihopfällda, klicka på en version för att expandera den. Varje version bygger på
en specifik version av WideQuick Modular Framework, länkad under respektive rubrik. För hela
ramverkets ändringslogg, se [MOD-versioner](../../mod/releases/index.md).

## WideQuick BMS 2026.1.1 { #bms-2026-1-1 }
__Released <!-- DATE -->__
Modular Framework Version: <!-- MOD VERSION LINK -->
<details class="release" markdown="1" open>
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

---

### Översättningar

| Område | Förändring |
|---|---|
| **Nya projektöversättningssträngar** | Larmkvittering, historikimportetiketter, inställnings- och privilegieetiketter, instrumentpanelens widgetsträngar, rapportschemaläggningens tidskontroller, kalendarns månads- och dagnamn, dokumentgruppsetiketter och kartnålarnas tooltip-texter. |
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
