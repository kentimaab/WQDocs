---
title: Rapporter — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Rapporter — Konfigurering

Det här avsnittet beskriver hur du konfigurerar de fyra rapportmallarna i WideQuick Mod efter dina behov, samt hur du använder den inbyggda Rapporthistoriken för att återskapa eller skicka om misslyckade rapporter.

* **Alarm_Report**
* **Alarm_Report_OneAlarm**
* **Energy_Report**
* **Energy_Report_Week**

## Larmrapport { #alarm-report }
Larmrapporten genererar en fullständig översikt över alla larm i hela systemet. 
Den innehåller ett cirkeldiagram som visar larmfördelning per larmklass (A–F som standard) och 
en fullständig lista över alla larm som utlöstes under den valda tidsperioden. Larmklasserna 
kan anpassas efter dina behov.

Som standard hämtar Larmrapporten data från databasen ansluten till 
**Larmlogg**-loggern. Om du vill lagra data i en annan databas är det bara att ändra 
var Larmloggern lagrar sina data — detta påverkar inte rapporten i sig.

Om du däremot vill konfigurera en separat logger för larm måste rapporten uppdateras 
i enlighet med detta. Följ dessa steg:

* Konfigurera den nya loggern med typen Alarm och välj önskad databas. Se 
[Loggers](../../guides/Loggers.md) för mer information.
* Uppdatera makroanropet i rapportmallen (se bild).
* Uppdatera vyn **Alarm_Report** så att den refererar till den nya loggern.

!!! note "Makro"
    Larmrapportmallen använder makrot `alarms`, som samlar in alla larm som loggats 
    via den valda loggern.

För att ändra loggern som används i makrot, leta upp makrokommandot och ändra 
`FROM Larmlogg` till `FROM <DinLogger>`. Du kan redigera texten direkt, eller högerklicka 
på cellen som innehåller makrokommandot och välja **Edit Expression** för att öppna 
uttrycksredigeraren.

<figure markdown="span">
  ![MacroLogger](/Images/Reports/MacroLogger.png)
  <figcaption>Redigering av larmmakrot så att det pekar på en annan logger.</figcaption>
</figure>

För att ändra vilken logger som visas när rapporten skapas, navigera till 
**Workviews → Partials → ReportController → Alarm_Report** i **WideQuick Designer®**. 
Välj objektet `LarmLogger_list`, gå till **Properties** och uppdatera egenskapen **Logger** 
till önskad logger.

<figure markdown="span">
  ![ObjectLogger](/Images/Reports/ObjectLogger.png)
  <figcaption>Inställning av Logger-egenskapen på objektet LarmLogger_list.</figcaption>
</figure>

!!! warning "Namnkonvention"
    Namnet på ReportController måste stämma överens exakt med namnet på rapportmallen, 
    annars genereras inte rapporten.

## Larmrapport — ett larm { #alarm-report-one-alarm }
Den här mallen används när du behöver en rapport för ett enda specifikt larm. Den fungerar 
på liknande sätt som Larmrapporten, men med två viktiga skillnader:

* Cirkeldiagrammet ingår inte.
* Makrot frågar efter ett specifikt larm i stället för alla larm i loggern.

Processen för att byta logger och databas är densamma som beskrivs för Larmrapporten.

## Energirapport { #energy-report }
Energirapportmallarna är mer komplexa än Larmrapporterna eftersom de bearbetar 
data för presentationsändamål. Det här avsnittet förklarar hur du justerar rapporten för att täcka 
olika tidsperioder och hur du byter logger.

Som standard täcker Energirapporten en treårsperiod. Den innehåller ett individuellt 
diagram för varje år samt en treårssammanfattning. Observera att mallen stöder maximalt 
tre individuella årsdiagram. Till exempel skulle en Energirapport som genereras i 
maj 2026 visa 2026 fram till maj, samt helårsdata för 2025 och 2024. För att säkerställa 
att det första årsdiagrammet är fullständigt ifyllt bör slutdatumet sättas till slutet av 
december.

!!! note
    Energirapporten är konfigurerad för timvärden.

### Byta logger { #changing-logger }
För att byta logger som används av Energirapporten, följ samma steg som för 
Larmrapporten:

* Konfigurera den nya loggern.
* Uppdatera makroanropen i rapportmallen.
* Uppdatera ReportController-vyn.

### Ändra årsintervall { #changing-year-span }
Processen för att ändra årsintervallet för Energirapporten kräver ytterligare bearbetning 
av mallen samt ändringar i ReportController. Här täcker vi följande konfigurationer:

!!! tip "Säkerhetskopia"
    Innan du bearbetar mallen rekommenderas det att spara en kopia som säkerhetskopia.

* Enbart innevarande år
* Ett år från aktuellt datum

#### Enbart innevarande år
Att bearbeta mallen så att den bara visar innevarande år är den enklaste konfigurationen. 
Rapporten innehåller endast data från det år den produceras i. Till exempel kommer en rapport 
som produceras den 31 september 2026 bara att visa data från den 1 januari 2026 
till den 31 september 2026.

Navigera först till `\Your_Project\Reports\Templates` och öppna `EnergyReport.xlsx`. Följ sedan 
GIF-bilden nedan:

<figure markdown="span">
  ![PrintArea](/Images/Reports/PrintArea.gif)
  <figcaption>Inställning av utskriftsområdet för en Energirapport med ett enda år.</figcaption>
</figure>

!!! note
    Mallen får inte vara öppen i **WideQuick Designer®** när ändringar görs i Excel.

Nu visar rapportmallen bara innevarande år. Den hämtar dock fortfarande data från 
tre år bakåt, så ytterligare ändringar krävs. Navigera till 
**Workviews → Partials → ReportController → Energy_Report** i **WideQuick Designer®**. 
Välj objektet `to_time_Singel`, gå till **Properties** och ändra värdet för 
**YearsPrior** till 1. Rapporten är nu konfigurerad för att producera en Energirapport för 
innevarande år.

#### Ett år från aktuellt datum
Den här konfigurationen producerar en fullständig årsrapport oavsett vilket datum den produceras.

Öppna `EnergyReport.xlsx` som finns i `\Your_Project\Reports\Templates`. I stället för att 
välja `A:1` till `Q:31`, välj `A:97` till `Q:127` och ange det som utskriftsområde. 
Välj sedan rad 113 i rubrikbladet och klistra in följande:

```excel title="EnergyReport.xlsx — row 113"
=IFERROR("Totalt -- "&TEXT(Meta!B13/86400000+DATE(1970,1,1),"yyyy-mm-dd")&" - "&TEXT(Meta!B14/86400000+DATE(1970,1,1),"yyyy-mm-dd"),"Totalt -- alla år")
```

Spara Excel-filen och öppna **WideQuick Designer®**. Navigera till 
**Workviews → Partials → ReportController → Energy_Report**. Välj 
objektet `to_time_Singel` och ändra egenskapen **YearsPrior** till 1.

Rapporteraren producerar nu en fullständig årsrapport från det angivna datumet, med ett 
diagram för det året.

## Energirapport vecka { #energy-report-week }
Energirapport vecka följer samma struktur som Energirapporten, men visar 
data på veckobasis i stället för årsbasis. Som standard täcker den en trevekkorsperiod 
med ett individuellt diagram för varje vecka samt en treveckorssammanfattning. Precis som 
Energirapporten är den konfigurerad för timvärden.

### Byta logger { #changing-logger-week }
För att byta logger som används av Energirapport vecka, följ samma steg som för 
Larmrapporten:

* Konfigurera den nya loggern.
* Uppdatera makroanropen i rapportmallen.
* Uppdatera ReportController-vyn.

### Ändra veckointervall { #changing-week-span }
Processen för att ändra veckointervallet följer samma steg som 
[Ändra årsintervall](#changing-year-span), med två skillnader:

* Mallfilen som ska ändras är `WeeklyEnergyReport.xlsx`, som finns i 
`\Your_Project\Reports\Templates`.
* I egenskaperna för objektet `to_time_Singel`, använd värdet **WeeksPrior** i stället för 
**YearsPrior**.

De två tillgängliga konfigurationerna är:

* **Enbart innevarande vecka** — Rapporten innehåller bara data från innevarande vecka.
* **En vecka från aktuellt datum** — Rapporten producerar en fullständig veckosrapport oavsett 
vilket dag den produceras.

!!! tip "Säkerhetskopia"
    Innan du bearbetar mallen rekommenderas det att spara en kopia som säkerhetskopia.

## Rapporthistorik { #report-history }
Rapporthistoriken är tillgänglig från vyn **Reports - Schedule**. Den 
visar ett stapeldiagram med rapportstatistik för de senaste 30 dagarna, inklusive dagliga 
värden som anger om varje rapport genererades framgångsrikt och om den skickades 
framgångsrikt.

Använd navigeringsknapparna för att välja en specifik dag och se detaljerad information. 
Popup-fönstret listar alla rapporter för den dagen tillsammans med deras status. Misslyckade rapporter, 
skickade e-postmeddelanden och misslyckade e-postmeddelanden kan omkonfigureras för att återskapas eller skickas om.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — skapa anpassade mallar och rapportkontroller
<!-- --8<-- [end:body] -->
