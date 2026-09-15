---
title: Kalender
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Kalender

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Inga händelser visas i kalendern | Kontrollera att anslutningen till underhållsdatabasen är aktiv. Både kalenderhändelser och underhållsdeadlines läses från samma databas. Om anslutningen ligger nere läses kalendern in men visar inga händelser. |
| Underhållshändelser visas inte | Kontrollera att skriptet `scMaintenance` körs. Kalendern läser underhållsdeadlines genom att anropa funktioner i `scMaintenance` vid inläsning. Om `scMaintenance` inte är tillgängligt hoppas underhållshändelser över. |
| Händelser från en tidigare period visas kvar efter navigering | Kalendern rensar och ritar om alla händelser vid navigering till en ny period. Om inaktuella händelser visas, läs om vyn. Kvarstår problemet, kontrollera om flera instanser av `CalendarManager` har skapats för samma vy, eftersom det kan orsaka dubbel rendering. |
| Kalendern är tom efter att ha öppnats | `CalendarManager` initieras när vyn läses in. Om vyn läses in innan anslutningen till underhållsdatabasen är klar kan inläsningen av händelser misslyckas tyst. Kontrollera `scAlert`-loggen efter fel från `CalendarService` eller `CalendarManager`. |
| Det finns inget alternativ för att prenumerera på en ICS-länk | Direktflöden kräver REST-insticksmodulen, som inte ingår i den här versionen. Importera en lokal `.ics`-fil i stället, och markera helgdagar i kalendern själv. |
| Det finns inget alternativ för att importera röda dagar | Import av röda dagar krävde samma insticksmodul. Markera helgdagar genom att skapa händelser med färgen **HOLIDAY**. Se [Helgdagar och helgdagsaftnar](configuring.md#holidays-and-holiday-eves). |
| En importerad kalender visar inga händelser | Kontrollera att importen är aktiverad i **Kalenderfilter**. En import som inte är synlig lagras fortfarande men ritas inte. Kontrollera sedan `scAlert`-loggen efter fel från `scHoliday`. |
| En redigerad lokal `.ics`-fil visar inte sina ändringar | En fil läses vid importtillfället och kontrolleras inte därefter. Importera filen igen för att hämta in det nya innehållet. |
| En import kan inte läggas till | Tillägg avvisas när namnet eller sökvägen redan tillhör en annan import. Jämförelsen bortser från omgivande blanksteg och ett avslutande snedstreck. |
| En prenumeration hoppas över vid synkronisering med en notering i loggen | Databasen innehåller en rad av typen `url` eller `nager` från en version som hade REST-insticksmodulen. De typerna kan inte hämtas i den här versionen. Ta bort prenumerationen i **Ändra kalendrar** om dess händelser inte längre önskas. |
| `isHoliday` sätts inte på en dag som markerats som helgdag | Kontrollera att händelsen har färgen **HOLIDAY** och inte någon annan färg, eftersom färgen är det som markerar dagen. Kontrollera sedan att dagen ligger inom händelsens tidsspann. |
| `isHoliday` ändras en timme in på dagen | Förväntat. Båda helgdagsvariablerna uppdateras av den timvisa pollningen, som räknar från applikationens start snarare än från midnatt. Se [Helgdagsvariabler](extending.md#holiday-variables). |
| En helgdagsafton sätter inte `isHoliday` | De två är avsiktligt åtskilda, eftersom en helgdagsafton oftast är en förkortad arbetsdag snarare än en stängd dag. Läs `isHolidayEve` för den, eller läs båda där samma beteende önskas. |
| En flerdagshelg markerar bara sin första dag | Klassificeringen använder ett överlappningstest, så varje täckt dag markeras. Om endast den första dagen markeras, kontrollera att händelsens slutdatum är satt som avsett. En helgdagshändelse justeras till hela dygn när den sparas. |
| En helgdag når inte fram till PLC:t | Variablerna bär klassificeringen men skickar den inte. Koppla `isHoliday` och `isHolidayEve` till utgångar på samma sätt som vilket annat värde som helst. |

## Kända fel { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
