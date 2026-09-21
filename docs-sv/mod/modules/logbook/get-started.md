---
title: Loggbok — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Loggbok — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Loggboken och all
    relaterad funktionalitet som täcks av Loggboksguiderna:
    
    * `scLogBook`
    * `scDoc`
    * `scLinking`
    * `scPrototypes`
    * `scThemes`
    * `scAlert`

Loggboken finns i huvudmenyn under **Dokument & Loggbok → Loggbok**.

## Loggboksvyn { #the-logbook-view }

Loggboksvyn har två paneler. Den vänstra panelen visar ämnesträdet, en hierarkisk lista över alla ämnen som har minst en post. Välj en nod och klicka på **Visa inlägg** för att läsa in alla poster under det ämnet i postlistan till höger. Väljs **Alla ämnen** längst upp i trädet visas samtliga poster.

En vald nod omfattar allt som är placerat under den. Väljs en vynod listas anteckningarna på vyn tillsammans med anteckningarna på de objekt som är ritade i den, vilket gör att en hel anläggningsdel kan granskas i ett steg.

Postlistan visar följande kolumner: **Rubrik**, **Placerad på**, **Meddelande**, **Kontext**, **Användare**, **Skapad**, **Senast ändrad** och **Arkiverad**.

**Placerad på** anger vad posten faktiskt är kopplad till, oberoende av hur trädet för tillfället är ordnat. En vy visas med sin sökväg utan filändelsen `.kvie`, ett objekt med sin tagg, och ett eget underämne läggs till efter identifieraren. Detta har betydelse eftersom samma post hamnar under olika noder i de två trädlägena, och den här kolumnen är det enda stället som alltid namnger postens verkliga koppling.

Välj en post och klicka på **Redigera anteckning** för att öppna den för redigering, eller **Arkivera anteckning** för att flytta ut den ur den aktiva listan. En arkiverad post behålls i databasen och döljs i listan i stället för att raderas, och samma knapp återställer den när arkiverade poster visas.

!!! note "Poster arkiveras, de raderas inte"
    Det finns ingen radering av enskilda poster. Den enda åtgärd som permanent tar bort loggboksinnehåll är **ta bort alla arkiverade anteckningar** i inställningsvyn, som rensar samtliga arkiverade poster på en gång. Se [Arkivering](extending.md#archiving).
<!-- --8<-- [end:body-1] -->

![Loggboksvy med ämnesträd och postlista](/docs/sv/Images/Logbook/logbook-overview.png){align=center}

<!-- --8<-- [start:body-2] -->
## Byta hur trädet ordnas { #switching-how-the-tree-is-keyed }

Reglaget **Navigera efter arbetsvyer** ovanför trädet växlar mellan de två sätten att ordna samma poster.

* **På, arbetsvyläge** — trädet följer processvyernas mappstruktur, till exempel **System → Värme → VS11**. Detta läge används när anteckningar söks utifrån en anläggningsdel så som den är ritad i vyerna.
* **Av, signalläge** — trädet följer taggsökvägen, till exempel **MB → AS01 → VS11**. Detta läge används när anteckningar söks utifrån en specifik tagg, oavsett i vilka vyer den förekommer.

Inget döljs av valet. De två lägena är två sätt att ordna samma mängd, så en anteckning som går att nå i det ena går att nå i det andra, oftast under en annan nod. En post som är placerad på ett eget ämne behåller sin egen sökväg i båda lägena.

Inställningen delas med de loggböcker som öppnas från ett objektpopup eller från en processvy, så det valda läget följer med operatören genom projektet. Vid omstart av applikationen återgår trädet till arbetsvyläge.

!!! info "Därför kan en anteckning synas under flera noder"
    En anteckning som är placerad på ett objekt hör till varje vy där objektet är ritat, och en anteckning som är placerad på en vy hör till de objekt som är ritade i den. En pump som förekommer i två vyer visar därför sina anteckningar i båda, och en anteckning skriven på en vy återfinns vid sökning på tagg. Se [Hur de två träden byggs](configuring.md#how-the-two-trees-are-built).

## Skapa en post { #creating-an-entry }

Klicka på **Lägg till anteckning** för att öppna popup-fönstret **Skapa ny loggbokspost**. Fyll i följande fält:

* **Ämne** — vad posten placeras på. Om loggboken öppnats från ett objekt eller från en processvy är fältet redan ifyllt och behöver normalt inte ändras.
* **Kontext** — en valfri grupperingsetikett. Klicka på **...** för att hantera tillgängliga kontexter.
* **Rubrik** — en kort rubrik för posten.
* **Meddelande** — den fullständiga texten i anteckningen.

Klicka på **Spara** för att spara och fortsätta, eller **Spara & Stäng** för att spara och stänga popup-fönstret. Posten visas omedelbart högst upp i postlistan, och under den nod den hör till i båda trädlägena.

En post som skapas från en nod i trädet placeras på det noden står för. Skapas den från en vynod hamnar den på vyn, och skapas den från en objektnod hamnar den på objektet.
<!-- --8<-- [end:body-2] -->

![Popup för att skapa post med namngivna fält](/docs/sv/Images/Logbook/create-entry-popup.png){align=center}

<!-- --8<-- [start:body-3] -->
## Filtrering { #filtering }

Klicka på filterikonen för att öppna panelen **Filtrera loggbok**. Tillgängliga filter:

* **Tidsperiod** — filtrera efter skapandedatum (Skapad från / Skapad till)
* **Användare** — visa poster från en specifik användare
* **Sök** — sök efter text i rubriken, meddelandet eller båda
* **Sortering** — nyaste först eller äldsta först
* **Visa arkiverade** — inkludera arkiverade poster i listan. Arkiverade poster är dolda tills detta aktiveras.

Klicka på **Tillämpa** för att använda filtren, **Rensa filter** för att återställa, eller **Avbryt** för att stänga utan att spara ändringar.
<!-- --8<-- [end:body-3] -->

![Filterpanel](/docs/sv/Images/Logbook/logbook-filter.png){align=center}

<!-- --8<-- [start:body-4] -->
## Nästa steg { #next-steps }

* [Konfigurering](configuring.md) — vad poster placeras på, hur träden byggs, kontexter och åtkomstmönster
* [Utöka](extending.md) — behörigheter, lagring av ämnet och arkivering
<!-- --8<-- [end:body-4] -->
