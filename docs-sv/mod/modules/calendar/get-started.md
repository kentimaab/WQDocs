---
title: Kalender — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Kalender — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Kalender och all
    relaterad funktionalitet som täcks i kalenderguider:
    
    * `scCalendar`
    * `scDayViewManager`
    * `scWeekViewManager`
    * `scMaintenance`
    * `scDatabase`
    * `scThemes`
    * `scAlert`

Kalendern är tillgänglig i huvudmenyn under **Kalender**. Den öppnas i månadsvy och läser automatiskt in händelser och underhållsdeadlines för den aktuella perioden.

## Vyer { #views }

Kalendern har tre vylägen. Byte mellan dem görs direkt i kalendern:

* Klicka på en månadsfliken längst upp för att byta till **månadsvy** för den månaden.
* Klicka på bakgrunden på en dag för att byta till **veckovy** för den veckan.
* Klicka på en händelse för att byta till **dagsvy** för den dagen.
* I veckovy, klicka på dagnamnet för att byta till **dagsvy** för den dagen.

Använd pilknapparna i det övre fältet för att flytta framåt eller bakåt en period åt gången.

### Månad { #month }

Månadsvy visar ett fullständigt kalendernät för den aktuella månaden. Händelser visas som färgade indikatorer på varje dag. Om fler händelser finns på en dag än vad som kan visas, visar ett överflödesmärke hur många som är dolda.

![Månadsvy med händelser](/Images/Calendar/calendar-month-events.png){align=center}

### Vecka { #week }

Veckovy visar den aktuella 7-dagarsperioden som ett tidsnät. Händelser renderas som block med sina start- och sluttider synliga.

![Veckovy](/Images/Calendar/calendar-week.png){align=center}

### Dag { #day }

Dagsvy visar en enskild dag som ett tidsnät. Den fungerar på samma sätt som veckovyn men fokuserad på en dag åt gången.

![Dagsvy](/Images/Calendar/calendar-day.png){align=center}


## Sidopanel { #sidebar }

Sidopanelen visar två saker: en minikalender för den aktuella månaden och en lista med kommande händelser.

Minikalendern markerar den aktuellt valda dagen.

Listan med kommande händelser visar nästa händelser och underhållsdeadlines sorterade efter datum, och slår ihop båda händelsekällorna till en enda lista.

![Sidopanel med kommande händelser](/Images/Calendar/calendar-sidebar.png){align=center}

## Skapa en händelse { #creating-an-event }

Nya händelser kan skapas på två sätt:

* Klicka på **+** i det övre fältet för att öppna popup-rutan **Lägg till/redigera kalenderhändelse** direkt.
* I **Vecka**- eller **Dag**-vy, klicka en gång på tidsnätet för att ange starttid, klicka sedan igen för att ange sluttid. Popup-rutan öppnas med Start och Slut förifyllda.

Fyll i fälten:

* **Titel** — en kort etikett som visas på händelsen.
* **Start** och **Slut** — datum och tid för händelsen. Kan justeras efter att popup-rutan öppnats.
* **Färg** — anger visningsfärgen för händelsen i kalendern.
* **Kategori** — grupperar händelsen under en namngiven kategori.
* **Beskrivning** — valfria ytterligare detaljer.

Klicka på **Spara** för att lägga till händelsen i kalendern.

## Nästa steg { #next-steps }

* [Konfigurera](configuring.md) — redigera händelser, underhållsfärger och påminnelseinställningar
* [Utöka](extending.md) — felsökning
<!-- --8<-- [end:body] -->
