---
title: Kalender — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Kalender — Konfigurering

## Händelser { #events }

Kalenderhändelser skapas, redigeras och tas bort direkt i kalendern. De lagras i underhållsdatabasen tillsammans med underhållsdata.

När en händelse skapas eller redigeras kan en färg väljas från en fast uppsättning alternativ: **ENERGY**, **POWER**, **SYSTEM**, **SAFETY**, **SECURITY**, **HVAC**, **WATER**, **HOLIDAY**, **HOLIDAYEVE** och **DEFAULT**. Dessa färger definieras i temat **CalendarColors** i `Themes.kdat`.

**HOLIDAY** och **HOLIDAYEVE** har betydelse utöver utseendet. Se [Helgdagar och helgdagsaftnar](#holidays-and-holiday-eves).

**Redigera en händelse:**

Klicka på en befintlig händelse för att öppna popup-fönstret **Lägg till/redigera kalenderhändelse**. Alla fält kan uppdateras. Klicka på **Spara** för att tillämpa ändringarna.

**Ta bort en händelse:**

Öppna händelsen och klicka på **Ta bort**. Detta tar bort händelsen permanent.

![Popup-fönstret Lägg till/redigera kalenderhändelse](/docs/sv/Images/Calendar/edit-event-popup.png){align=center}

## Underhållshändelser { #maintenance-events }

Underhållsdeadlines från [underhållsmodulen](../maintenance/index.md) visas automatiskt i kalendern. De är skrivskyddade och kan inte redigeras eller tas bort från kalendern. Ändringar måste göras i **Underhåll - Lista**.

Varje underhållshändelse visas på dagen för sin deadline. Färgen ställs in automatiskt baserat på uppgiftens aktuella status och kan inte väljas manuellt. Dessa färger definieras i temat **MaintenanceColors** i `Themes.kdat` och är separata från de färger som används för kalenderhändelser.

När en underhållshändelse klickas öppnas ett popup-fönster som visar objekt, status, deadline och underhållstyp. Klicka på **Öppna redigering** för att navigera direkt till den uppgiften i **Underhåll - Lista**.

| Status | Färg |
|---|---|
| Planerad | Gul |
| Missad | Mörkröd |
| Stoppad | Grå |
| Påminnelse | Dämpad olivgrön |

![Underhållshändelser med olika statusfärger i månadsvy](/docs/sv/Images/Calendar/maintenance-event-colors.png){align=center}

## Påminnelser { #reminders }

En påminnelsehändelse kan visas i kalendern ett angivet antal dagar före en underhållsdeadline. Påminnelsen visas som en separat post med färgen **Påminnelse**, skild från själva deadlinehändelsen.

Påminnelser är aktiverade som standard för uppgifter som skapas utan en mall. Uppgifter som skapas från en mall använder mallens påminnelseinställning, som är avstängd som standard. Standardvärdet för påminnelseförskjutningen är 3 dagar. Se [Utöka](extending.md#reminder-configuration) för hur dessa inställningar ändras.

## Helgdagar och helgdagsaftnar { #holidays-and-holiday-eves }

En dag markeras som helgdag genom att en vanlig kalenderhändelse skapas på den med färgen **HOLIDAY**. En helgdagsafton markeras på samma sätt med **HOLIDAYEVE**. Ingen separat dialog eller import är inblandad.

Händelsen justeras till hela dygn när den sparas, eftersom en dag antingen är en helgdag eller inte. En start- och sluttid som angetts i tidsnätet vidgas till att täcka de dagar händelsen berör.

De två hålls isär avsiktligt. En helgdagsafton är oftast en förkortad arbetsdag snarare än en stängd dag, så en anläggning behöver ofta ett annat schema för den än för själva helgdagen.

Flerdagshelger fungerar som väntat. En händelse som sträcker sig över flera dagar markerar varje dag den täcker, inte bara den dag den börjar.

### Skicka klassificeringen till ett PLC { #handing-the-classification-to-a-plc }

Kalendern publicerar dagens klassificering till två interna variabler i Datalagret:

| Variabel | Betydelse |
|---|---|
| `isHoliday` | Sann när dagens datum täcks av en **HOLIDAY**-händelse. |
| `isHolidayEve` | Sann när dagens datum täcks av en **HOLIDAYEVE**-händelse. |

Båda är vanliga booleska variabler och kan kopplas till en utgång på samma sätt som vilket annat värde som helst, så att ett PLC eller DUC kan läsa dagtypen och köra sina egna scheman utifrån den. Klassificeringen är en egenskap hos dagen, så ett par variabler räcker för samtliga scheman i stället för att varje tidkanal bär sin egen kopia.

Variablerna skrivs vid uppstart och uppdateras vid varje synkronisering. Att markera en dag i kalendern får därför effekt den dagen utan ytterligare åtgärder.

!!! note "Kalendern klassificerar dagen, PLC:t avgör vad som ska hända"
    Överlämningen rapporterar endast vilken dagtyp som gäller i dag. Vilka utgångar som ändras, och när, ligger kvar hos PLC:ts egen schemalogik.

## Importera en kalender { #importing-a-calendar }

**Importera** öppnar dialogen **Importera kalender**, som lägger till händelser från en lokal `.ics`-fil. Klicka på **Välj fil...** för att välja en fil från disk, och därefter på **Importera fil**.

Varje importerad fil blir en prenumeration. Alla händelser den bidragit med märks med den, så en import kan byta färg eller tas bort som en enhet utan att påverka händelser som skapats direkt i kalendern eller händelser från en annan fil.

En import avvisas om dess namn eller sökväg matchar en som redan finns. Jämförelsen bortser från omgivande blanksteg och ett avslutande snedstreck.
<!-- --8<-- [end:body-1] -->

![Dialogen Importera kalender](/docs/sv/Images/Calendar/import-calendar.png){align=center}

<!-- --8<-- [start:body-2] -->
!!! warning "En importerad fil läses en gång"
    En fil läses vid importtillfället och kontrolleras inte därefter. Att redigera eller byta ut `.ics`-filen på disk uppdaterar inte kalendern. Importera filen igen för att hämta in det nya innehållet.

!!! info "Direktflöden och import av röda dagar ingår inte i den här versionen"
    Att prenumerera på en ICS-länk, och att importera ett lands röda dagar, bygger båda på REST-insticksmodulen som inte ingår i den här versionen. Helgdagar markeras i stället i kalendern själv, enligt beskrivningen ovan.

    En databas som förts över från en version med insticksmodulen kan fortfarande innehålla prenumerationer av de typerna. De hoppas över vid synkronisering och en notering skrivs till loggen. Deras händelser ligger kvar i kalendern tills prenumerationen tas bort.

## Hantera importerade kalendrar { #managing-imported-calendars }

**Ändra** öppnar **Ändra kalendrar**, som listar varje import med namn och typ. Välj en för att byta namn med **Byt namn**, ta bort den med **Ta bort**, eller välj en färg i kombinationsrutan och klicka på **Byt färg**. Att ta bort en import raderar dess händelser ur kalendern. Händelser som skapats direkt i kalendern påverkas inte.

Importer skapas med färgen **DEFAULT**.
<!-- --8<-- [end:body-2] -->

![Dialogen Ändra kalendrar](/docs/sv/Images/Calendar/edit-calendars.png){align=center}

<!-- --8<-- [start:body-3] -->
**Sync** läser om varje import omedelbart. Eftersom en filimport läses vid importtillfället har detta främst betydelse för att städa upp en befintlig databas, inte för att hämta in nytt innehåll.

### Välja vilka kalendrar som visas { #choosing-which-calendars-are-shown }

**Filter** öppnar **Kalenderfilter**, som styr vilka importer som ritas i kalendern. Inställningen gäller för alla klienter snarare än för en enskild användare. Händelser som skapats direkt i kalendern visas alltid och påverkas inte av filtret.
<!-- --8<-- [end:body-3] -->

![Dialogen Kalenderfilter](/docs/sv/Images/Calendar/calendar-filter.png){align=center}

<!-- --8<-- [start:body-4] -->
Kryssa i de kalendrar som ska visas och klicka på **Tillämpa**.

## Exportera en kalender { #exporting-a-calendar }

**Exportera** öppnar **Exportera kalender**. Kryssa i vilka kalendrar som ska ingå, och välj sedan antingen **Generera** för att skriva en `.ics`-fil, eller **Skicka med e-post** för att skicka exporten som en bilaga.

**Egna/interna händelser** listas bredvid importerna, så att händelser som skapats direkt i kalendern kan tas med eller utelämnas separat. Helgdags- och helgdagsaftonshändelser ingår i den gruppen, så ett markerat år kan exporteras och flyttas till en annan installation.
<!-- --8<-- [end:body-4] -->

![Dialogen Exportera kalender](/docs/sv/Images/Calendar/export-calendar.png){align=center}

<!-- --8<-- [start:body-5] -->
## Nästa steg { #next-steps }

* [Utöka](extending.md) — påminnelsekonfiguration, helgdagsvariablerna och prenumerationstabellen
<!-- --8<-- [end:body-5] -->
