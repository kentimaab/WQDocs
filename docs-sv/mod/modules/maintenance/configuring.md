---
title: Underhåll — Konfigurering
description: Konfigurera modulen Underhåll med mallar, återkommande scheman och statusreferens.
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-12
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Underhåll — Konfigurering

## Underhållslista { #maintenance-list }

Vyn **Underhåll - Lista** visar alla underhållsuppgifter i projektet i en enda scrollbar lista. Välj en uppgift och klicka på **Öppna** för att öppna uppgiftsinformationen där deadline, beskrivning, status och ansvarig kan uppdateras.

Uppgifter behöver inte vara kopplade till ett taggat objekt. Om **Objekt** lämnas tomt eller ett fritext-namn anges kan underhåll spåras för utrustning som inte är ansluten till HMI:n.

Klicka på **Filtrera** för att öppna filterpanelen:

* **Objekt** — filtrera efter en specifik objekttagg-sökväg.
* **Underhållstyp** — filtrera efter underhållstyp.
* **Underhållsstatus** — filtrera efter en eller flera statusar: Planerat, Klar, Klar - Försenad, Missad, Stoppad.
* **Prioritet** — filtrera efter en eller flera prioritetsnivåer.
* **Ansvarig** — filtrera efter tilldelad arbetstagare.
* **System** — filtrera för att endast visa uppgifter som tillhör ett specifikt system.
* **Tidsinställningar - deadline** — visa alla uppgifter oavsett deadline (**Alla**), eller begränsa till uppgifter med en deadline inom ett valt datumintervall (**Tidsintervall**).

Klicka på **Ta bort filter** för att rensa filtret och visa alla uppgifter igen.

Listan läses inte om av sig själv. När underhållsdata ändras efter att listan lästes in, här eller i en annan klient, visas en blinkande uppdateringsknapp. Klicka på den för att läsa om listan.

### System { #systems }

Varje uppgift hör till det system den skapades på, identifierat med systemets `ApplicationName`. Kolumnen **System** visar vilket system en uppgift hör till, och filtret **System** begränsar listan till ett system.

Om en annan dator redan använder samma `ApplicationName` mot samma underhållsdatabas visar listan varningen *ApplicationName används redan av ett annat system. Byt ApplicationName i inställningarna för att kunna skapa underhåll.* och **Skapa** är inaktiverad tills namnet har bytts.

När `ApplicationName` ändras frågar en dialog om befintliga underhåll ska flyttas till det nya systemnamnet. Om svaret är nej ligger befintliga uppgifter kvar under det gamla namnet.
<!-- --8<-- [end:body-1] -->

![Underhållslista med filterpanel öppen](/docs/sv/Images/Maintenance/maintenance-list-filter.png){align=center}

<!-- --8<-- [start:body-2] -->
## Mallar { #templates }

Mallar gör det möjligt att spara och återanvända ofta förekommande underhållstyper. En mall lagrar underhållstyp, prioritet, standarddeadline-intervall och beskrivning så att samma information inte behöver anges varje gång.
<!-- --8<-- [end:body-2] -->

![Vyn Underhåll - Mallar](/docs/sv/Images/Maintenance/maintenance-templates-view.png){align=center}

<!-- --8<-- [start:body-3] -->
Den vänstra panelen listar alla mallar. Att välja en visar dess fält till höger:

* **Mallnamn för underhåll** — det namn som visas i rullgardinsmenyn **Underhållstyp** när en uppgift skapas.
* **Prioritet** — den standardprioritet som är förifylld när denna mall väljs.
* **Deadline** — ett standarddeadline-intervall (antal + enhet: Dag/Vecka/Månad/År) som föreslås vid skapande av en uppgift.
* **Underhållsbeskrivning** — en standardbeskrivning som är förifylld i uppgiften.
* **Skapa en påminnelse 3 dagar innan** — när rutan är ikryssad får uppgifter som skapas från mallen en påminnelse i kalendern före sin deadline. Nya mallar skapas med rutan avmarkerad. Se [Kalenderintegration](extending.md#calendar-integration).

**Skapa en mall:**

1. Navigera till **Underhåll → Underhåll - Mallar**.
2. Klicka på **Lägg till**. En ny post visas i listan.
3. Välj den nya posten och fyll i fälten till höger.
4. Klicka på **Spara** för att spara mallen.

Mallen är nu tillgänglig i rullgardinsmenyn **Underhållstyp** när en uppgift skapas. Alla förifyllda fält kan fortfarande redigeras innan de sparas. Att redigera mallen påverkar inte uppgifter som redan skapats från den.

För att ta bort en mall, välj den och klicka på **Ta bort**.

## Återkommande underhåll { #recurring-maintenance }

Återkommande underhåll gör det möjligt för systemet att automatiskt generera underhållsuppgifter enligt ett fast schema. I stället för att manuellt skapa samma uppgift varje månad eller kvartal konfigureras det en gång och systemet sköter resten.

Varje konfiguration definierar:

* Vilka objekt underhållet gäller (ett eller flera)
* Underhållstyp och beskrivning
* Hur ofta uppgiften återkommer (upprepningsintervall)
* Hur nästa deadline beräknas (upprepningsregel)
* Om missade uppgifter automatiskt ska generera en uppföljning
<!-- --8<-- [end:body-3] -->

![Konfiguration av återkommande underhåll](/docs/sv/Images/Maintenance/maintenance-recurring.png){align=center}

<!-- --8<-- [start:body-4] -->
Vyn har tre paneler. Den vänstra panelen listar alla konfigurationer. Den mellersta panelen visar inställningarna för den valda konfigurationen. Den högra panelen är ett objektträd där de objekt som konfigurationen gäller väljs. För utrustning som saknar tagg i systemet, använd fritext-fältet **Anpassat objekt** längst ned i objektpanelen för att ange ett namn manuellt.

**Skapa en konfiguration:**

1. Navigera till **Underhåll → Underhåll - Återkommande**.
2. Klicka på **Lägg till**. En ny konfiguration visas i listan.
3. Ange ett namn i fältet **Namn på återkommande underhåll**.
4. Under **Underhållsinformation**, ange **Underhållstyp**, **Ansvarig** och **Prioritet**. Lägg eventuellt till en beskrivning.
5. Under **Schema**, välj en **Upprepningsregel**: **Planerat datum** för att hålla en fast rytm, eller **Utförandedatum** för att starta intervallet från när uppgiften slutfördes.
6. Ange **Upprepningsintervall** som ett antal och en enhet (Dag/Vecka/Månad/År).
7. Ange **Startdatum** för den första uppgiften.
8. I **Objekt**-panelen till höger, markera alla objekt som konfigurationen ska gälla för.
9. **Skapa nästa underhåll automatiskt vid missad deadline** är aktiverat som standard för en ny konfiguration. Inaktivera det om en missad uppgift inte ska generera nästa instans.
10. Bekräfta att **Status (aktiv)** är aktiverad.
11. Klicka på **Spara**. Den första uppgiften skapas omedelbart och visas i **Underhåll - Lista** med statusen **Planerat**.

**Ta bort en konfiguration:** välj den och klicka på **Ta bort**. Alla dess uppgifter med statusen **Planerat** tas bort samtidigt. Uppgifter som är klara, missade eller stoppade ligger kvar i listan.

### Upprepningsintervall { #repeat-interval }

Upprepningsintervallet styr hur ofta en ny uppgift genereras. Tillgängliga enheter är:

| Enhet | Beskrivning |
|---|---|
| Dag | Var N:e dag |
| Vecka | Var N:e vecka |
| Månad | Var N:e månad |
| År | Vart N:e år |

### Upprepningsregel { #repeat-rule }

Upprepningsregeln styr hur deadline för nästa uppgift beräknas när den aktuella är slutförd.

| Regel | Beskrivning |
|---|---|
| Planerat datum | Nästa deadline beräknas utifrån föregående uppgifts deadline, vilket håller en fast rytm oavsett när uppgiften faktiskt slutfördes. Använd detta för lagstadgade krav som måste inträffa med fasta intervall. |
| Utförandedatum | Nästa deadline beräknas från det tillfälle då uppgiften slutfördes, så intervallet startar alltid från det faktiska slutförandedatumet. |

### Skapa automatiskt vid missad deadline { #auto-create-on-missed-deadline }

När **Skapa nästa underhåll automatiskt vid missad deadline** är aktiverat utlöser en missad uppgift automatiskt skapandet av nästa schemalagda instans. Detta säkerställer att schemat fortsätter även om en uppgift inte slutfördes i tid. Den missade uppgiften finns kvar i listan med statusen **Missad** och måste hanteras manuellt.

När det är inaktiverat stannar schemat om en uppgift missas. Ingen ny instans skapas förrän den missade uppgiften har åtgärdats.

### Slutföra en återkommande uppgift { #completing-a-recurring-task }

När en återkommande uppgift markeras som slutförd skapar systemet automatiskt nästa instans baserat på konfigurationen. Den slutförda uppgiften tilldelas statusen **Klar** eller **Klar - Försenad** beroende på om den slutfördes före eller efter sin deadline.

## Status { #status }

| Status | Beskrivning |
|---|---|
| Planerat | Uppgiften är aktiv och har en kommande deadline. |
| Missad | Deadlinen passerade utan att uppgiften slutfördes. Sätts automatiskt av systemet en gång i timmen, via schemat `maintenance_tracker`, så en uppgift kan ligga kvar som **Planerat** i upp till en timme efter sin deadline. |
| Stoppad | Uppgiften har stoppats manuellt och kommer inte att arbetas med. |
| Klar | Uppgiften slutfördes på eller före deadline. |
| Klar - Försenad | Uppgiften slutfördes men efter att deadline hade passerat. |

!!! note
    **Missad** och **Klar - Försenad** sätts av systemet och kan inte väljas manuellt. Vid redigering av en uppgift är **Planerat**, **Klar** och **Stoppad** tillgängliga som användarvalbara statusar. En **Missad** uppgift kan bara behållas som **Missad** eller sättas till **Klar**, och en uppgift som är **Klar** kan inte längre byta status.

Uppgifter som visas i Kalender-modulen är färgkodade efter status. Färgreferensen finns under [Underhållshändelser](../calendar/configuring.md#maintenance-events) i Kalender-modulen.

## Prioritet { #priority }

Uppgifter kan tilldelas en av fyra prioritetsnivåer:

| Prioritet | Beskrivning |
|---|---|
| Kritisk | Högsta prioritet. För uppgifter som inte får försenas. |
| Hög | Hög prioritet. För viktiga men icke-kritiska uppgifter. |
| Normal | Standardnivå för rutinmässigt schemalagt underhåll. |
| Låg | Låg prioritet. För uppgifter som kan skjutas upp vid behov. |

## Behörigheter { #privileges }

| Behörighet | Styr |
|---|---|
| `Maintenance_Add` | **Skapa** i **Underhåll - Lista**, **Nytt underhåll** i objektpopupen och **Lägg till** i **Underhåll - Mallar** |
| `Maintenance_Edit` | Fälten för status och beskrivning vid redigering av en uppgift, samt **Ta bort** i **Underhåll - Mallar** |
| `Maintenance_EditExtended` | Fälten för ansvarig, deadline och prioritet vid redigering av en uppgift, samt att ta bort en uppgift från **Underhåll - Lista** eller objektpopupen |
| `Maintenance_Templates` | **Lägg till** och **Ta bort** i **Underhåll - Återkommande** |

En knapp eller ett fält är inaktiverat för en användare som saknar behörigheten. **Spara** i redigeringsdialogen kräver antingen `Maintenance_Edit` eller `Maintenance_EditExtended`. Alla fyra behörigheterna är nekade som standard. Se [Användare och behörigheter](../Core/users-privileges.md#framework-privileges).

## Nästa steg { #next-steps }

* [Utöka](extending.md) — kalenderintegration och felsökning
<!-- --8<-- [end:body-4] -->
