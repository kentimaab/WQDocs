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


## WideQuick BMS 2026.1.0 { #bms-2026-1-0 }
__Utgiven 2026-05-21__
Modular Framework-version: [WideQuick MOD 2026.1.0](../../mod/releases/index.md#mod-2026-1-0) 
<details class="release" markdown="1" open>
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
| **Underhållssystemidentitet** | Vid första start tillskrivs underhållsuppgifter det aktuella systemet baserat på värdnamn, och en migreringsdialog visas om ett namnbyte på applikationen upptäcks. Granska tilldelningen efteråt för att bekräfta att uppgifterna tillhör rätt system. |

</details>
