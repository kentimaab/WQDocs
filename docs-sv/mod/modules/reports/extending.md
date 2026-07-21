---
title: Rapporter — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Rapporter — Utöka
WideQuick levereras med en uppsättning standardrapportmallar, men det är också möjligt att 
skapa helt anpassade mallar som är skräddarsydda för dina specifika behov. Det här avsnittet 
täcker hela processen för att skapa en anpassad rapportmall och tillhörande 
ReportController-vy, från att designa Excel-layouten till att koppla den till livedata 
från databasen.

Innan du börjar, se till att du är bekant med grunderna i rapportsystemet. 
Om inte, se [Rapporter — Kom igång](get-started.md) & [Rapporter — Konfigurering](configuring.md).

## Skapa mallar { #creating-templates }
Processen för att skapa egna rapportmallar består av tre steg:

1. Designa din mall i Excel
2. Konfigurera datablad, makron och loggenheter
3. Koppla ihop allt

### Designa din mall { #designing-your-template }
Det första steget är att designa din rapportmall i Excel. Detta inkluderar att besluta om 
layout, vilka diagram som ska inkluderas och hur data ska presenteras. WideQuick sätter inga 
begränsningar på designen — mallen kan anpassas fritt för att passa dina behov.

En rapportmall består vanligtvis av tre blad:

* Presentationsblad — Den synliga delen av rapporten. Innehåller diagram, tabeller och 
alla andra visuella element som rapporten ska visa.
* Datablad — Ett dolt blad som innehåller rådata hämtad från databasen. Det här 
bladet matar presentationsbladet med data. Databladet är enklare att konfigurera i 
**WideQuick® Designer**, där dolda blad är synliga, jämfört med direkt i Excel.
* Metablad — Ett dolt blad som innehåller allmän information om rapporten, som 
rapporttitel, aktuellt datum och tid, vald loggenhet och valda signaler. Det här 
bladet är användbart för att visa rapportmetadata på presentationsbladet.

!!! tip "Kom igång"
    En bra startpunkt är att skissa upp hur den slutliga rapporten ska se ut innan du 
    öppnar Excel. Att veta vilken data du behöver och hur den ska presenteras kommer att 
    göra det mycket enklare att konfigurera databladet och makrona.

För att lägga till ett nytt blad i mallen, öppna mallen i **WideQuick® Designer** och 
navigera till botten av bladflikarna. Klicka på **Create New Sheet**, se bilden nedan. 
För att dölja bladet, högerklicka på bladfliken och välj **Hide Sheet**.

<figure markdown="span">
  ![newSheet](/docs/sv/Images/Reports/NewSheet.png)
  <figcaption>Lägger till ett nytt blad i mallen i WideQuick Designer.</figcaption>
</figure>

!!! note
    Dolda blad är bara synliga i **WideQuick® Designer** och syns inte 
    i den slutgenererade rapporten eller när mallen öppnas direkt i Excel. Försök att 
    generera en rapport med bladet synligt när makrokommandot är inställt, för att få 
    en känsla för hur datan är orienterad.

### Konfigurera datablad, makron och loggenheter { #configuring-the-data-sheet-macros-and-loggers }
Databladet är ett dolt blad i rapportmallen som fungerar som behållare 
för rådata hämtad från databasen. När en rapport genereras använder WideQuick 
makrokommandon placerade i databladet för att fråga databasen och fylla den med data.

För att lägga till ett makrokommando, högerklicka på en cell i databladet och välj 
**Edit Expression**. Detta öppnar följande popup:

<figure markdown="span">
  ![MacroConfigure](/docs/sv/Images/Reports/MacroInsertion.png)
  <figcaption>Edit Expression-popup för att infoga ett makrokommando.</figcaption>
</figure>

Nedan beskrivs varje fält:

* **Variable** — Definierar vilken signal som ska frågas. Två alternativ är tillgängliga:
    * `variable_ref[#]` — Frågar en specifik signal, där `#` är signalens index. 
    Ett separat makroanrop krävs för varje signal.
    * `alarms` — En "wildcard" som hämtar alla larm i den valda loggenheten.

* **Values** — Definierar vilka datakolumner som ska inkluderas. Beror på typen av data 
som frågas:
    * Signaldata: `name`, `datetime`, `value` är vanligtvis tillräckligt.
    * Larmdata: `name`, `state`, `severity`, `timestamp`, `text`, `group` — inkludera 
    bara de fält som behövs för rapporten.

* **Logger** — Loggenheten som rapporten hämtar data från. Denna måste anges statiskt 
och kan inte ändras dynamiskt.
* **Fixed/Range timespan** — Rapportören använder **Range timespan** som standard, med 
`Report_Reference.from_time` och `Report_Reference.to_time` som start- och sluttider. 
Dessa anges av tidsobjekten i ReportController.
* **Limit** — Det maximala antalet rader att fylla. Detta anges av användaren i 
ReportController vid generering av rapporten.
* **Datetime format** — Det format som används för datum- och tidsvärden. Standardvärdet är 
`yyyy-MM-dd hh:mm:ss` men kan justeras för att passa rapportens behov.

Placeringen av makrokommandot är viktig — data fylls i med start från cellen där makrot 
placeras och expanderar nedåt. Kolumnerna bestäms av fältet **Values**. Till exempel 
kommer ett signalmakro med `VALUES(name, datetime, value)` att fylla tre kolumner med 
start från makrocellen:

<div class="figure-row" markdown>

<figure markdown="span">
  ![Signal macro](/docs/sv/Images/Reports/MacroExample.png)
  <figcaption>Signalmakro placerat på databladet.</figcaption>
</figure>

<figure markdown="span">
  ![Signal macro result](/docs/sv/Images/Reports/MacroExample2.png)
  <figcaption>Resulterande kolumner ifyllda av makrot.</figcaption>
</figure>

</div>

Och för larmdata med `VALUES(name, state, severity, timestamp, text, group)`:

<div class="figure-row" markdown>

<figure markdown="span">
  ![Alarm macro](/docs/sv/Images/Reports/MacroAExample.png)
  <figcaption>Larmmakro placerat på databladet.</figcaption>
</figure>

<figure markdown="span">
  ![Alarm macro result](/docs/sv/Images/Reports/MacroAExample2.png)
  <figcaption>Resulterande kolumner ifyllda för larmdata.</figcaption>
</figure>

</div>

Antalet ifyllda rader beror på **Limit** och tidsintervallet, som anges av 
användaren i ReportController vid generering av rapporten.

!!! tip "Metablad"
    Metabladet är ett användbart ställe att lagra allmän rapportinformation som inte 
    hämtas från loggenheten. Det använder `$()` -uttryck för att skriva ut interna eller systemvariabler 
    direkt i celler. Till exempel:

    * `$(Report_Reference.title)` — Rapporttiteln angiven av användaren.
    * `$(Report_Reference.logger)` — Loggenheten som används för rapporten.
    * `$(Report_Reference.from_time)` — Rapportens starttid.
    * `$(Report_Reference.to_time)` — Rapportens sluttid.
    * `$(Report_Reference.limit)` — Det maximala antalet händelser.
    * `$(Report_Reference.variable_ref[#])` — Signalen vid index `#`.
    * `$(System.dateTime)` — Aktuellt datum och tid.
    * `$(System.user)` — Den aktuella användaren.

    Metabladet är det enda sättet att föra in rapporttiteln angiven av användaren till 
    presentationsbladet. Integratören är fri att inkludera de fält som är relevanta 
    för sin rapport.

### Koppla ihop allt { #wiring-it-up }
Med presentationsbladet designat och databladet ifyllt med makrokommandon är 
det sista steget att koppla samman de två — länka rådata till diagram, tabeller och 
andra visuella element i presentationsbladet.

Några tips för att koppla ihop mallen effektivt:

* Använd databladet för beräkningar — Eftersom databladet är dolt i den slutliga 
rapporten är det ett bra ställe att utföra mellanliggande beräkningar innan resultaten 
skickas till presentationsbladet. För att redigera det i Excel, gör det tillfälligt synligt.
* Håll beräkningar borta från makrodata — Eftersom makrodata expanderar nedåt rad 
för rad, placera eventuella ytterligare beräkningar i kolumner längre till höger för att 
undvika konflikter.
* Referera till databladet från presentationsbladet — Diagram, staplar och andra 
visuella element i presentationsbladet bör referera till celler i databladet 
snarare än att innehålla logik i sig själva. Detta håller presentationsbladet rent och 
enklare att underhålla.
* Använd fasta intervall som täcker det maximala möjliga antalet rader — Eftersom mängden data 
varierar beroende på **Limit** och tidsintervallet, definiera intervall som täcker det maximala 
antalet rader rapporten kan producera. Använd `IFERROR` för att hantera tomma celler 
på ett smidigt sätt.

!!! note
    Den här guiden täcker inte Excel-formeldesign i detalj — möjligheterna är 
    i stor utsträckning upp till integratören. Tipsen ovan är specifika för att arbeta med 
    WideQuick-makrodata.

## Skapa ReportController-vyn { #creating-the-reportcontroller-view }
Med mallen skapad är nästa steg att bygga ReportController-vyn.
Den här vyn bestämmer vilka signaler och data som skickas till rapporten när den genereras.
Systemet kopplar en ReportController till en rapportmall genom att matcha deras namn, så det 
är viktigt att vyn namnges exakt samma som rapportmallen.

För att komma igång, navigera till **Templates** i projektträdet och duplicera 
**Template_ReportController**-vyn. Flytta duplikatet till mappen **ReportController** 
och döp om det för att matcha rapportmallens namn.

När en ReportController-vy laddas, initierar dess mallskript ett `view.data`-objekt 
med standardvärden såsom rapporttyp, tidsintervall, loggenhet och signalreferenser.
Varje objekt placerat i vyn — som `to_time`, `Report_CustomTitle` och 
`LoggerList` — läser från och skriver till detta delade `view.data`-objekt när användaren 
interagerar med dem.

När `Button_CreateReport`-objektet klickas, samlar det in det fullständiga `view.data`-objektet 
och lägger till det i en rapportkö via funktionen `scReports.addReportToQueue()`. 
Rapporter i kön behandlas en i taget — `scReports`-skriptet fyller ett 
globalt **Report_Reference**-objekt med köad data, som makrokommandona i 
databladet läser från vid förfrågan mot databasen.

Den korrekta mallen identifieras och aktiveras med hjälp av fältet `report_type` i 
`view.data`, som härleds direkt från ReportController-vyns namn. Det är därför 
det är kritiskt att ReportController-vyns namn exakt matchar rapportmallens 
namn — om de skiljer sig åt kommer `scReports`-skriptet inte att kunna hitta och aktivera 
rätt mall.

!!! warning "Namnkonvention"
    ReportController-vyns namn måste exakt matcha rapportmallens namn. Om de 
    skiljer sig åt kommer `scReports`-skriptet inte att kunna hitta och aktivera rätt mall.

För att bygga vyn finns en uppsättning färdiga objekt tillgängliga i objektbiblioteket under 
**Report**. Nedan beskrivs varje objekt och när det ska användas:

| Objekt | Använd när |
|---|---|
| `LoggerList` | Du behöver att användaren väljer signaler från en loggenhet |
| `LarmLogger_list` | Du behöver att användaren väljer larm från en larmloggenhet |
| `Report_CustomTitle` | Du vill att användaren ska ange en anpassad rapporttitel |
| `Button_CreateReport` | Alltid — detta krävs för att generera rapporten |
| `Report_output_type` | Du vill att användaren ska kunna välja mellan PDF- och Excel-utdata |
| `to_time` | Du behöver att användaren anger en sluttid |
| `from_time` | Du behöver att användaren anger en starttid |
| `to_time_Singel` | Rapporten använder ett fast tidsintervall (t.ex. de senaste 3 åren) |
| `Numbe_of_event` | Du behöver begränsa antalet insamlade händelser |

### LoggerList { #loggerlist }
`LoggerList`-objektet är en TreeView konfigurerad för att visa signalerna som loggas av en 
specifik loggenhet. När en signal väljs visas en grön bockmarkering bredvid den i 
TreeView. Objektet inkluderar även två textrutor som visar den aktuellt valda loggenheten 
och antalet valda signaler av det maximalt tillåtna.

Loggenheten som ska visas och det maximala antalet valbara signaler konfigureras båda 
som egenskaper på objektet. Tilldela önskade värden när du placerar objektet i en 
ReportController.

### LarmLogger_list { #larmlogger_list }
`LarmLogger_list`-objektet är en specialiserad version av `LoggerList`, byggd 
för att visa larm loggade av en loggenhet. Till skillnad från `LoggerList` bygger den automatiskt 
sitt träd baserat på larmgrupper och utelämnar redundant information. Om till exempel alla 
larm i loggenheten följer mönstret `AS01.AS01_XXX_XX`, kommer TreeView att visa 
dem enkelt som `XXX_XX`.

Det här objektet har två egenskaper som måste konfigureras:

* **Logger** — Bestämmer vilken loggenhet som TreeView byggs från. Detta bör alltid 
matcha loggenheten som rapporten frågar mot.
* **Signals** — Styr hur många signaler som kan väljas för rapporten. Standardvärdet för 
maximum är 15, men detta kan ändras — se [här](#changing-the-maximum-of-signals-to-be-selected). 
Den här egenskapen bör alltid anges till ett numeriskt värde, om inte TreeView är 
avsiktligt låst.

### Report_CustomTitle { #report_customtitle }
`Report_CustomTitle`-objektet består av en etikett och en textruta. Textrutan anger 
rapportens titel och är konfigurerad för att kommunicera med den aktiva datan i vyn.

### Button_CreateReport { #button_createreport }
`Button_CreateReport`-objektet är en knapp som utlöser rapportgenerering. När 
den klickas samlar den in data från vyn och skickar den till `scReports`-skriptet för att skapa 
rapporten.

### Report_output_type { #report_output_type }
`Report_output_type`-objektet består av en etikett och en ComboBox. Det valda 
ComboBox-värdet bestämmer om rapporten genereras som enbart PDF, eller som både en 
PDF och en Excel-fil.

### to_time { #to_time }
`to_time`-objektet består av en etikett och en DateTime-redigerare. DateTime-redigeraren 
anger rapportens sluttid och är konfigurerad för att rapportera sitt aktuella värde till vyn.

### from_time { #from_time }
`from_time`-objektet fungerar på samma sätt som `to_time`-objektet, men anger 
rapportens starttid istället.

### to_time_Singel { #to_time_singel }
`to_time_Singel`-objektet kombinerar funktionaliteten hos `to_time` och `from_time` 
i ett enda objekt. Det används när rapportmallen kräver ett fast tidsintervall. 
Följande egenskaper kan konfigureras:

* **Years prior** — Anger tidsintervallet i år.
* **Weeks prior** — Anger tidsintervallet i veckor.

Observera att dessa två egenskaper utesluter varandra — veckor och år kan inte 
kombineras.

### Numbe_of_event { #numbe_of_event }
`Numbe_of_event`-objektet består av en etikett och en SpinBox. SpinBox-värdet 
bestämmer hur många händelser som samlas in per makroanrop. Denna distinktion är viktig:

* Om jokertecknet `alarms` används representerar värdet det **totala** antalet händelser.
* Om `variable_ref[#]` används representerar värdet antalet händelser **per signal**.

## Ändra maximalt antal signaler som kan väljas { #changing-the-maximum-of-signals-to-be-selected }
I standardinställningarna för rapportören tillåts 15 signaler att väljas för 
rapportgenerering. Detta kan enkelt ändras om fler signaler krävs. Navigera först i 
**WideQuick® Designer** till **Data Types → Arrays → variable_ref** och välj 
**Properties...**. Detta öppnar följande popup:

<figure markdown="span">
  ![Variable Array](/docs/sv/Images/Reports/Variabel_ref.png)
  <figcaption>Popup för egenskaper för variable_ref-arrayen.</figcaption>
</figure>

Ändra **Max. size** till önskat värde. Klicka på **Apply** och sedan **Ok**. 
**Report_Reference**-arrayen har nu uppdaterats.

Uppdatera sedan `scReports`-skriptet för att hantera den nya storleken. Leta upp 
funktionen `createReport()` och ändra värdet `15` till ditt nya **Max. size**-värde:

``` javascript title="scReports — createReport() — before"

for (var i = 0; i < 15; i++) Report_Reference.variable_ref[i] = "";
var signals = reportObj.variable_ref.split(',');
for (var i = 0; i < signals.length && i < 15; i++) Report_Reference.variable_ref[i] = signals[i];

```

``` javascript title="scReports — createReport() — after"

for (var i = 0; i < YOUR_MAX_VALUE; i++) Report_Reference.variable_ref[i] = "";
var signals = reportObj.variable_ref.split(',');
for (var i = 0; i < signals.length && i < YOUR_MAX_VALUE; i++) Report_Reference.variable_ref[i] = signals[i];

```
<!-- --8<-- [end:body] -->
