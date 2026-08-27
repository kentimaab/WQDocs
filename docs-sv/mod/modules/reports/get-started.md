---
title: Rapporter — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-08-27
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Rapporter — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Rapporter och all
    relaterad funktionalitet som tas upp i rapportguiderna:
    
    * `scReportScheduler`
    * `scReports`
    * `scAlert`

Det här avsnittet täcker grunderna i rapportmodulen, inklusive hur man lägger till en ny
mall, hur man använder befintliga mallar i **WideQuick® Runtime**, och hur man schemalägger
rapporter att köras automatiskt.

## Konfigurera rapportverktyget { #setting-up-the-reporter }
WideQuick innehåller en uppsättning standardrapportmallar som finns under
**Rapporter** i projektträdet. Anpassade mallar kan också skapas eller importeras
via **WideQuick® Designer**.

För att skapa en ny mall, högerklicka på **Rapporter** i projektträdet och välj
**Lägg till rapport**. Följande fönster öppnas:

<figure markdown="span">
  ![Add report](/docs/sv/Images/Reports/Add_report.png)
  <figcaption>Dialogrutan Lägg till rapport i WideQuick Designer.</figcaption>
</figure>

* **Namn** — Rapportens namn.
* **Källfil** — Importera en färdig mall genom att klicka på mappikonen. För att starta
från en tom mall, se gif-bilden nedan.
* **Utdatakatalog** — Mappen där genererade rapporter sparas. Som standard
placeras rapporter i mappen Rapporter. Klicka på mappikonen för att välja en annan
destination.
* **Generera åtkomst** — Välj mellan **Alla system** (standard) eller
**Endast lokalt system**.
* **Utdatanamn** — Anpassa rapportfilens namn med hjälp av **Byggaren för utdatanamn**.
En förhandsgranskning av namnet visas i fältet **Namnförhandsvisning**.
<figure markdown="span">
  ![Create new report template](/docs/sv/Images/Reports/Create_new_report_template.gif)
  <figcaption>Skapa en ny rapportmall från grunden.</figcaption>
</figure>

Den nya mallen visas under **Rapporter** i projektträdet, där den kan
redigeras för att visa önskad information. Mer information om hur man skapar anpassade
mallar finns [här](extending.md#creating-templates).

!!! note "Lägga till en mall"
    När man lägger till en anpassad mall måste en motsvarande ReportController också
    skapas. Detta förklaras [här](extending.md#creating-the-reportcontroller-view).

## Använda rapportverktyget i **WideQuick® Runtime** { #using-the-reporter-in-widequick-runtime }
För att hantera rapporter i **WideQuick® Runtime**, navigera till
**Historik → Rapporter → Rapporter - Lista**. Den här sidan visar en lista över alla
genererade rapporter med två kolumner:

* **Rapport** — Rapportens namn, som standard Larmrapport \[#\] där \[#\]
anger genereringsnumret.
* **Tidsstämpel** — Datum och tid då inspelningen avslutas.

Från den här sidan kan rapporter skapas, tas bort eller skickas som e-postbilagor. Att skicka
rapporter via e-post kräver att en SMTP-server är konfigurerad, vilket förklaras
[här](../Core/alarms/extending.md#configuring-smtp-in-widequick-designer).

<figure markdown="span">
  ![Report](/docs/sv/Images/Reports/Report.png)
  <figcaption>Listarbetsvyn för rapporter i WideQuick Runtime.</figcaption>
</figure>

För att skapa en ny rapport, klicka på **Skapa rapport**. En konfigurationsmeny visas
till höger. Som standard finns sex rapporttyper tillgängliga: **Larmrapport**,
**Larmrapport ett larm**, **Energirapport**, **Energirapport vecka**,
**Deltarapport vecka** och **Deltarapport år**. Byt mellan dem genom att ändra
rullgardinsmenyn **Rapportmall**.

<div class="figure-row" markdown>

<figure markdown="span">
  ![Alarm Report](/docs/sv/Images/Reports/AlarmReport.png)
  <figcaption>Larmrapport-kontroller.</figcaption>
</figure>

<figure markdown="span">
  ![Alarm Report One Alarm](/docs/sv/Images/Reports/AlarmReportOne.png)
  <figcaption>Larmrapport ett larm-kontroller.</figcaption>
</figure>

<figure markdown="span">
  ![Energy Report](/docs/sv/Images/Reports/EnergyReport.png)
  <figcaption>Energirapport-kontroller.</figcaption>
</figure>

<figure markdown="span">
  ![Delta Report](/docs/sv/Images/Reports/DeltaYear.png)
  <figcaption>Deltarapport-kontroller.</figcaption>
</figure>

</div>

Veckoversionernas kontroller visas inte, eftersom de har samma utformning som sina
motsvarigheter för år.

De sex ReportControllers delar en liknande struktur men skiljer sig åt i vilka alternativ som
är tillgängliga och vilka loggenheter som visas i TreeView. Nedan finns en beskrivning av varje
alternativ:

* **Rapportmall** — Den rapportmall som ska användas. Standardvärde är **Larmrapport**. En guide
till att skapa mallar finns [här](extending.md#creating-templates).
* **Anpassa titel** — Anger rapportens titel, som visas på framsidan.
* **Från** — Startdatum för inspelningsperioden. Det här fältet är låst för energirapporter
och deltarapporter, eftersom de kräver historiska data från den tidpunkten och framåt. Se
[här](configuring.md#changing-year-span) för konfiguration.
* **Till** — Slutdatum för inspelningsperioden.
* **LoggerList** — Visar de signaler som är tillgängliga i den valda loggern. Låst för
larmrapporter, eftersom de inkluderar alla signaler automatiskt. På energi- och
deltakontrollerna är den dessutom låst till dess att en enhet har valts, och listar sedan
endast de signaler som mäts i den enheten. Se [Enheter och prefix](#units-and-prefixes).
* **Antal händelser** — Det maximala antalet händelser att inkludera. För energirapporter
är standardvärdet antalet timhändelser i den valda tidsperioden. I deltarapporter hanteras
detta i onLoad-skriptet.
* **Enhet** och **Prefix** — Den enhet rapporten presenteras i. Finns endast på energi- och
deltakontrollerna. Larmrapporter har ingen enhet. Se
[Enheter och prefix](#units-and-prefixes) nedan.
* **Rapportfilformat** — Rapportens utdataformat: antingen PDF eller PDF och XLSM.
* **Rapportstatus** — Visar rapportens aktuella status, inklusive
slutförande eller eventuella fel.

!!! note "Minst en signal måste vara vald"
    En rapport kan inte skapas förrän minst en signal har valts i **LoggerList**. Detta
    gäller inte larmrapporter, som inkluderar alla signaler automatiskt.

När den väl har genererats läggs rapporten till i rapportlistan där den kan förhandsgranskas.

## Rapporttyper { #report-types }

**Larmrapporten** och **Larmrapport ett larm** samlar larmdata för den valda
tidsperioden. **Energirapporten** visar energidata över en treårsperiod, med
ett individuellt diagram per år och en treårssammanfattning. **Energirapport vecka**
följer samma struktur men visar data på veckobasis och täcker tre veckor
som standard med ett individuellt diagram per vecka och en treveckorssammanfattning.

**Deltarapport år** och **Deltarapport vecka** visar förändringen mellan efterföljande
avläsningar i stället för de loggade värdena i sig, vilket passar mätare som rapporterar
en kontinuerligt ökande totalsumma. Deltarapport år presenterar ett månadsdelta per
kolumn, en kolumn per månad, och täcker tre år som standard. Deltarapport vecka
presenterar ett dagsdelta per kolumn, en kolumn per veckodag, och täcker tre veckor.
Ingen av dem är bunden till ett enda loggningsintervall: Deltarapport år hanterar
intervall från månad till dag, eller ned till timme med den alternativa mallen, och
Deltarapport vecka från timme till dag. För detaljerad konfiguration av varje
rapporttyp, se [Rapporter — Konfigurera](configuring.md).

## Enheter och prefix { #units-and-prefixes }

Energi- och deltarapporterna har en visningsenhet, som väljs med väljarna **Enhet** och
**Prefix** på rapportkontrollen. **Enhet** väljer basenheten, **Prefix** väljer det
SI-prefix som tillämpas på den, och de två kombineras när rapporten skapas, så att `k`
och `Wh` tillsammans ger `kWh`.

Larmrapporter har inga enhetsväljare, och enhetshanteringen hoppas över helt för dem.

Signaler som väljs in i samma rapport har inte nödvändigtvis samma ursprungliga prefix.
En signal kan vara loggad i `Wh` medan en annan redan är loggad i `kWh`. Varje vald
signal får därför en egen skalfaktor, beräknad utifrån signalens eget prefix och den
valda visningsenheten.

Värdena konverteras inte i förväg. Varje signal hämtas i den enhet den loggades i, och
faktorerna skickas till mallen tillsammans med data, där de hamnar på bladet **Meta**
som `Factor1` till `Factor15` tillsammans med den valda enheten. Mallen tillämpar dem,
så skalningen sker i mallen snarare än i skriptet.

Enhetslistan byggs utifrån enheterna hos de signaler som finns i den valda loggern, så
att endast enheter som projektet faktiskt loggar erbjuds.

Den valda enheten filtrerar också signallistan. TreeView är låst till dess att en enhet
har valts, och listar sedan endast de signaler som mäts i den enheten. Om enheten ändras
rensas det aktuella urvalet, eftersom de signaler som valts under den tidigare enheten
inte längre finns i listan.

## Schemalägga en rapport i **WideQuick® Runtime** { #scheduling-a-report-in-widequick-runtime }
För att schemalägga en rapport, navigera till
**Historik → Rapporter → Rapporter - Schema**.

<figure markdown="span">
  ![Report schedule](/docs/sv/Images/Reports/Report_schedule.png)
  <figcaption>Arbetsvyn Rapportschema i WideQuick Runtime.</figcaption>
</figure>

Klicka på **Nytt schema** för att skapa ett nytt schema. En meny med tre sidor visas
till höger. Observera att den andra sidan ändras beroende på den valda
**Rapportmallen**.

<div class="figure-row" markdown>

<figure markdown="span">
  ![Schedule page 1](/docs/sv/Images/Reports/Report_meny.png)
  <figcaption>Sida 1 — schemanamn, mall och frekvens.</figcaption>
</figure>

<figure markdown="span">
  ![Schedule page 2](/docs/sv/Images/Reports/Report_meny2.png)
  <figcaption>Sida 2 — rapportspecifik konfiguration.</figcaption>
</figure>

<figure markdown="span">
  ![Schedule page 3](/docs/sv/Images/Reports/Report_meny3.png)
  <figcaption>Sida 3 — mottagare och utdataformat.</figcaption>
</figure>

</div>

Den andra sidan speglar rapportkonfigurationen som beskrivs i föregående avsnitt,
inklusive väljarna **Enhet** och **Prefix**. En schemalagd rapport lagrar därför samma
visningsenhet och skalfaktorer per signal som en rapport som skapas manuellt, så att en
schemalagd och en manuell körning av samma konfiguration ger samma värden.

Nedan finns beskrivningar av alternativen på den första och tredje sidan:

* Första sidan

    * **Schemanamn** — Schemats namn.
    * **Aktivt schema** — Växlar om den schemalagda rapporten är aktiv och kommer att
    skickas.
    * **Rapportmall** — Den rapportmall som ska användas. Standardvärde är
    **Larmrapport**. Se [här](extending.md#creating-templates) för vägledning om
    att skapa mallar.
    * **Frekvens** — Hur ofta rapporten genereras. De tillgängliga alternativen och
    deras ytterligare inställningar är:

        * **Dagligen** — Välj en specifik tid på dagen. Tider finns tillgängliga i
        30-minutersintervall.
        * **Veckovis** — Välj en veckodag och en specifik tid på dagen.
        * **Månadsvis** — Välj en dag i månaden och en specifik tid på dagen.
        Systemet hanterar automatiskt månader med 30 eller 31 dagar, liksom
        februari och skottår.
        * **Kvartalsvis** — Välj vilken månad i kvartalet (1, 2 eller 3),
        dagen i den månaden och en specifik tid på dagen.
        * **Årsvis** — Välj en månad, dagen i den månaden och en specifik
        tid på dagen.

    * **Schemabeskrivning** — En beskrivning av schemat.
    !!! note
        Schema kontrolleras var 5:e minut. Den konfigurerade tiden är därför
        ungefärlig — rapporter kan skickas upp till 5 minuter efter inställd tid.

* Tredje sidan

    * **Ämnesrad** — Ämnesraden i det e-postmeddelande där rapporten skickas.
    * **Mottagare** — Mottagarna av e-postmeddelandet. Accepterar både e-postadresser
    och alias.
    * **Alias** — Visar tillgängliga alias. Välj ett och klicka på **Lägg till**
    för att lägga till det som mottagare.
    * **Mottagarlista** — Visar den fullständiga listan över mottagare och anger om
    varje post är en e-postadress eller ett alias.
    * **Rapportfilformat** — Formatet i vilket rapporten skickas: PDF eller Excel.

## Nästa steg { #next-steps }

* [Konfigurera](configuring.md) — inbyggda rapportmallar och rapporthistorik
* [Utöka](extending.md) — skapa anpassade mallar och rapportkontroller
<!-- --8<-- [end:body] -->
