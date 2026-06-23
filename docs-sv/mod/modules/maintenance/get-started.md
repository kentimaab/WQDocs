---
title: Underhåll — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Underhåll — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Underhåll och all
    relaterad funktionalitet som beskrivs i underhållsguiderna:
    
    * `scMaintenance`
    * `scDatabase`
    * `scAlert`

Underhållsmodulen nås via huvudmenyn under **Underhåll**. Härifrån finns tre vyer för att arbeta med underhållsuppgifter.

## Vyer { #views }

### Underhåll - Lista { #maint-list }

Listvyn visar alla underhållsuppgifter för samtliga objekt i projektet. Det är den primära vyn för det dagliga underhållsarbetet.

* Välj en uppgift och klicka på **Öppna** för att visa och uppdatera dess detaljer — deadline, beskrivning, status och tilldelad person.
* Välj en uppgift och klicka på **Ta bort underhåll** för att ta bort den permanent.
* Klicka på **Skapa** för att skapa en ny uppgift.

![Underhåll - Listvy](/docs/sv/Images/Maintenance/maintenance-list.png){align=center}

### Underhåll - Mallar { #maint-templates }

Mallvyn används för att skapa och hantera underhållsmallar. En mall definierar en återanvändbar uppgiftstyp med förinställd typ, prioritet, intervall och beskrivning. När en ny uppgift skapas kan en mall väljas för att fylla i uppgiftsfälten i förväg.

![Underhåll - Mallvy](/docs/sv/Images/Maintenance/maintenance-templates-view.png){align=center}

### Underhåll - Återkommande { #maintenance-recurring }

Vyn för återkommande underhåll hanterar automatiserade underhållskonfigurationer. Varje konfiguration definierar ett schema för ett eller flera objekt. Systemet genererar och spårar uppgifter automatiskt baserat på det konfigurerade intervallet.

![Underhåll - Återkommande vy](/docs/sv/Images/Maintenance/maintenance-recurring.png){align=center}

## Objektpopup { #object-popup }

Varje objekt i projektet har en underhållsflik tillgänglig via dess popup. Öppna popupen genom att klicka på ett objekt och välja fliken [**Underhåll**](../../reference/Popup/Maintenance.md). Här visas alla underhållsuppgifter kopplade till det specifika objektet. Använd **Nytt underhåll**, **Redigera underhåll** eller **Ta bort underhåll** för att hantera uppgifter utan att lämna processvyn.

Kolumnen **Återkommande** visar om varje uppgift har genererats av en återkommande underhållskonfiguration. Värdet **Ja** innebär att uppgiften ingår i ett automatiserat schema — när den slutförs skapas nästa instans automatiskt. Värdet **Nej** innebär att uppgiften skapades manuellt som en engångsåtgärd.

![Underhållsfliken i objektpopupen](/docs/sv/Images/Maintenance/object-popup-maintenance.png){align=center}

## Skapa en uppgift { #creating-a-task }

Nya underhållsuppgifter kan skapas både från vyn **Underhåll - Lista** och från objektpopupen.

Från **Underhåll - Lista**, klicka på **Skapa**. Från objektpopupen, klicka på **Nytt underhåll**.

![Formulär för nytt underhåll](/docs/sv/Images/Maintenance/create-multiple.png){align=center}

Fyll i följande fält:

* **Objekt** — välj det objekt uppgiften tillhör i rullgardinsmenyn. Förifyllt när formuläret öppnas från en objektpopup.
* **Typ av underhåll** — välj en mall för att fylla i prioritet, deadline och beskrivning i förväg. Alla fält kan ändras efter valet.
* **Prioritet** — Kritisk, Hög, Normal eller Låg.
* **Underhållsdeadline** — antingen ett specifikt datum eller ett antal dagar från nu.
* **Skapa flera** — aktivera för att skapa en serie uppgifter på en gång, med ett angivet intervall mellan varje. När alternativet är aktiverat visas två ytterligare fält:
    * **Upprepa var** — intervallet mellan uppgifter (antal + enhet: Dag/Vecka/Månad/År).
    * **Antal gånger** / **Slutdatum** — ange antingen hur många uppgifter som ska skapas, eller ett slutdatum.
* **Tilldelad person** — tilldela uppgiften till en ansvarig användare (valfritt).
* **Beskrivning** — förifyllt från den valda mallen. Kan redigeras fritt innan sparande.

Klicka på **Spara** för att spara. Uppgiften skapas med statusen **Planerad**. Om Skapa flera är aktiverat skapas alla uppgifter i serien på en gång.

## Slutföra en uppgift { #completing-a-task }

1. Navigera till **Underhåll → Underhåll - Lista**.
2. Välj uppgiften i listan och klicka på **Öppna**.
3. Ändra fältet **Status** till **Klar**.
4. Uppdatera eventuellt beskrivningen eller lägg till en notering innan sparande.
5. Klicka på **Spara**. Uppgiftens status uppdateras omedelbart. Om uppgiften ingick i en återkommande konfiguration skapas nästa schemalagda uppgift automatiskt.

!!! note
    Om uppgiften slutfördes efter sin deadline sätter systemet automatiskt statusen till **Klar - Försenad**. Detta kan inte anges manuellt.

## Nästa steg { #next-steps }

* [Konfigurera](configuring.md) — mallar, återkommande scheman och statusreferens
* [Utöka](extending.md) — kalenderintegration och felsökning
<!-- --8<-- [end:body] -->
