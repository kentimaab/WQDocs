---
title: Loggbok — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Loggbok — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Loggboken och all
    relaterad funktionalitet som täcks av Loggboksguiderna:
    
    * `scDoc`
    * `scLinking`
    * `scSubNav`
    * `scObjectFinder`
    * `scPrototypes`
    * `scSuffix`
    * `scThemes`
    * `scUsers`
    * `scAlert`

Loggboken finns i huvudmenyn under **Dokument & Loggbok → Loggbok**.

## Loggboksvyn { #the-logbook-view }

Loggboksvyn har två paneler. Den vänstra panelen visar ämnesträdet — en hierarkisk lista över alla ämnen som har minst en post. Välj en nod och klicka på **Visa poster** för att läsa in alla poster under det ämnet i postlistan till höger. Om du väljer **Alla ämnen** längst upp i trädet visas alla poster för samtliga ämnen.

Postlistan visar följande kolumner: **Rubrik**, **Meddelande**, **Kontext**, **Användare**, **Skapad** och **Senast ändrad**.

Välj en post och klicka på **Redigera anteckning** för att öppna den för redigering, eller **Ta bort anteckning** för att radera den permanent.

![Loggboksvy med ämnesträd och postlista](/docs/sv/Images/Logbook/logbook-overview.png){align=center}

## Skapa en post { #creating-an-entry }

Klicka på **Lägg till anteckning** för att öppna popup-fönstret **Skapa ny loggbokspost**. Fyll i följande fält:

* **Ämne** — den sökväg som denna post tillhör. Använd `/` för att skapa nivåer, till exempel `MB/AS01/VS10/GT11`. Posten går sedan att hitta genom att välja valfri överordnad nod i ämnesträdet.
* **Kontext** — en valfri grupperingsetikett. Klicka på **...** för att hantera tillgängliga kontexter.
* **Rubrik** — en kort rubrik för posten.
* **Meddelande** — den fullständiga texten i anteckningen.

Klicka på **Spara** för att spara och fortsätta, eller **Spara & Stäng** för att spara och stänga popup-fönstret. Posten visas omedelbart högst upp i postlistan.

![Popup för att skapa post med namngivna fält](/docs/sv/Images/Logbook/create-entry-popup.png){align=center}

## Filtrering { #filtering }

Klicka på filterikonen för att öppna panelen **Filtrera loggbok**. Tillgängliga filter:

* **Tidsperiod** — filtrera efter skapandedatum (Skapad från / Skapad till)
* **Användare** — visa poster från en specifik användare
* **Sök** — sök efter text i rubriken, meddelandet eller båda
* **Sortering** — nyaste först eller äldsta först

Klicka på **Tillämpa** för att använda filtren, **Rensa filter** för att återställa, eller **Avbryt** för att stänga utan att spara ändringar.

![Filterpanel](/docs/sv/Images/Logbook/logbook-filter.png){align=center}

## Nästa steg { #next-steps }

* [Konfigurering](configuring.md) — ämnen, kontexter och åtkomstmönster
* [Utöka](extending.md) — lägga till en loggbok i en anpassad vy eller knapp
<!-- --8<-- [end:body] -->
