---
title: Loggbok — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-12
tags:
 - MOD
---
<!-- --8<-- [start:body-1] -->

# Loggbok — Konfigurering

## Vad en post placeras på { #what-an-entry-is-filed-against }

Varje post kopplas till en av tre saker. Kopplingen avgör var posten hamnar i ämnesträdet, och den bestäms av var posten skapades i stället för av en inskriven sökväg.

| Koppling | Skapas från | Exempel |
|---|---|---|
| En arbetsvy | Loggboksknappen i **SpeedDial** i en processvy, eller en vynod i trädet | `System/MySystem/Station1/Pump1` |
| Ett objekt | Fliken **Loggbok** i ett objektpopup, eller en objektnod i trädet | `Connection.Device.System_ObjectName` |
| Ett eget ämne | En sökväg som inte matchar något av ovanstående | `Optimering/2026-03/Nattdrift` |

Den tredje varianten täcker anteckningar som inte hör till en enskild utrustning. En driftsättningstråd, en säsongsdiskussion om optimering eller en projektlogg placeras under en egen sökväg och visas i trädet precis som den är skriven, i båda trädlägena.

En post som är kopplad till en vy eller ett objekt kan ändå ha en egen sökväg under sig. En anteckning placerad på `Connection.Device.System_ObjectName` med underämnet `Trend` är kopplad till givaren och grupperas under en **Trend**-nod under den, så att flera anteckningar om samma objekt kan hållas isär.

!!! info "Ämnen registreras inte i förväg"
    Ett ämne finns för att en post använder det. Det finns ingen ämneslista att underhålla, och när den sista posten under en nod försvinner försvinner noden.

## Hur de två träden byggs { #how-the-two-trees-are-built }

Samma poster ordnas på två sätt, och reglaget under trädet växlar mellan dem. Inget av lägena filtrerar bort något.

### Arbetsvyläge { #workview-mode }

Trädet följer processvyernas mappstruktur och läses därför som navigeringsmenyn.

```text
System
  MySystem
    Station1
      Pump1
```

En anteckning placerad på en vy ligger på vyns nod. En anteckning placerad på ett objekt ligger under varje vy där objektet är ritat, som ett löv med objektets namn.

### Signalläge { #signal-mode }

Trädet följer taggsökvägen och läses därför som Datalagret.

```text
Connection
  Device
    System
      ObjectName
```

En anteckning placerad på ett objekt ligger på sin tagg. En anteckning placerad på en vy ligger under de taggar som är ritade i vyn, eftersom en vy i den här ordningen bara är meningsfull genom den utrustning den visar.

### Därför syns en anteckning på mer än ett ställe { #why-a-note-appears-in-more-than-one-place }

De två ordningarna är länkade genom objektindexet, som registrerar vilka objekt som är ritade i vilka vyer. Länken följs åt båda hållen:

* En anteckning på ett objekt visas under **varje** vy där objektet är ritat. En pump som visas både i en översikt och i en detaljvy har med sina anteckningar i båda.
* En anteckning på en vy visas under de objekt som är ritade i vyn.
* En anteckning på en utrustning, i stället för på en enskild tagg, visas överallt där något som tillhör utrustningen är ritat.

Detta är avsiktligt. En anteckning om en pump är relevant i varje vy där en operatör kan möta pumpen, och en anteckning om en vy är relevant för den utrustning vyn täcker.

!!! warning "En anteckning på ett skåp eller en enhet når långt"
    Samma regel gäller på varje nivå i taggsökvägen. En anteckning placerad på en enhet som `Connection.Device` hör till varje vy som visar något från den enheten, vilket kan vara större delen av anläggningen. En anteckning om ett fysiskt skåp hamnar rätt om den placeras på den **vy** som representerar skåpet. Placeras den på enhetens tagg sprids den över varje vy som matas av skåpet.

### Objekt med samma namn { #objects-that-share-a-name }

Två objekt som är ritade i samma vy kan ha samma namn, till exempel en `Pump1` som tillhör `System1` och en annan som tillhör `System2`. I arbetsvyläge skulle båda annars göra anspråk på samma löv.

När det inträffar utökas lövets namn med så mycket av taggen som behövs för att skilja dem åt, vilket ger `System1_Pump1` och `System2_Pump1`. Objekt vars namn redan är unika i sin vy behåller sitt enkla namn.

## Kontexter { #contexts }

Kontexter är namngivna grupperingar som kan användas för att kategorisera poster över ämnesgränserna. Exempel: `Operations`, `Commissioning`, `Alarms`. Standardkontexten `General` finns alltid tillgänglig.

Kontexter hanteras från popup-fönstret **Ändra loggbokskontext**, som öppnas genom att klicka på **...** bredvid fältet Kontext när en post skapas eller redigeras. Därifrån kan kontexter läggas till, byta namn och tas bort. Om en kontext tas bort raderas inte de poster som tillhör den. Dessa poster finns kvar i loggboken utan tilldelad kontext.

Vid filtrering i loggboken visas, när en kontext väljs, enbart poster tilldelade den kontexten oavsett ämne.
<!-- --8<-- [end:body-1] -->

![Vy för kontexthantering](/docs/sv/Images/Logbook/context-management.png){align=center}

<!-- --8<-- [start:body-2] -->
## Åtkomstmönster { #access-patterns }

### Globalt { #global }

Den fullständiga loggboken under **Dokument & Loggbok → Loggbok** visar alla poster. Ämnesträdet till vänster begränsar visningen till ett specifikt område i systemet, i den ordning som är vald. Detta är den primära vyn för operatörer som behöver granska eller lägga till anteckningar för hela projektet.

Det är också den enda loggboken som visar anslutna fjärrsystem, vart och ett under en egen toppnod. Se [Fjärrsystemens loggböcker](#logbooks-of-remote-systems).

### Objektpopup { #object-popup }

Varje objekt i projektet har en flik [**Loggbok**](../../reference/Popup/Logbook.md) i sitt popup-fönster, som visas för användare med behörigheten `Logbook_View`. När fliken öppnas markeras objektet i trädet och dess poster listas. Nya poster som skapas härifrån placeras automatiskt på objektet.

Resten av trädet är fortfarande nåbart, så en anteckning på ett angränsande objekt eller på den omgivande vyn kan läsas utan att popup-fönstret lämnas. Poster kan läggas till och redigeras härifrån. Arkivering erbjuds endast i den globala loggboken, eftersom det är där arkiverade poster kan visas igen och återställas. Arkiverade poster listas aldrig i ett objektpopup.
<!-- --8<-- [end:body-2] -->

![Loggboksfliken i objektets popup-fönster](/docs/sv/Images/Logbook/object-popup-logbook.png){align=center}

<!-- --8<-- [start:body-3] -->
### Vybegränsad { #view-scoped }

Menyn **SpeedDial** i processvyer innehåller en knapp som öppnar loggboken med den aktuella vyn markerad i trädet. Vyns poster listas direkt, tillsammans med posterna för de objekt som är ritade i den. Nya poster som skapas härifrån placeras på vyn.

Precis som i objektpopupen är resten av trädet nåbart från en vybegränsad loggbok, så en anteckning som är placerad någon annanstans kan läsas utan att gå tillbaka till huvudvyn.

## Fjärrsystemens loggböcker { #logbooks-of-remote-systems }

Den globala loggboken visar loggboken för varje anslutet fjärrsystem bredvid systemets egen. Varje fjärrsystem visas som en toppnod i ämnesträdet, namngiven efter fjärrsystemet så som det är konfigurerat under **Remote Systems**. Se [Fjärrsystem](../../guides/remote-systems.md#configuring-a-remote-system).

Under noden finns fjärrsystemets eget träd, ordnat i samma läge som det lokala och byggt från fjärrsystemets egna vyer och objekt. Väljs själva noden listas alla poster i det systemet.

Posterna kopieras inte. De ligger kvar i fjärrsystemets databas och läses därifrån varje gång, så noden visar alltid fjärrsystemets aktuella loggbok. I kolumnen **Placerad på** börjar en post från ett fjärrsystem med systemets namn, till exempel `Anläggning2: System/MySystem/Station1`.

### Skriva i ett fjärrsystems loggbok { #writing-to-a-remote-systems-logbook }

En anteckning som skapas under ett fjärrsystems nod skrivs till det systemets loggbok. Den placeras på den vy, det objekt eller det ämne den skapades på, precis som om den hade skrivits i fjärrsystemet, och fjärrsystemets operatörer ser den direkt i sin loggbok. Redigering, arkivering och återställning av en post sker i det system posten tillhör.

* **Kontext** — när en nod under ett fjärrsystem har valts arbetar kontextlistan och popup-fönstret **Ändra loggbokskontext** med det systemets kontexter.
* **Användare** — posten registrerar den användare som är inloggad där anteckningen skrevs. Den registrerar inte vilket system det var.
* **Behörigheter** — den användarens loggboksbehörigheter, i det system där loggboken är öppen, avgör vad som kan göras. Fjärrsystemets egna behörighetsinställningar används inte.

### Uppdatering i realtid { #live-updates }

Varje loggboksvy uppdaterar sitt träd och sin postlista av sig själv när en post ändras. Varje skrivning räknar upp punkten `LogBookSync` i Datalagret i det system den skrevs till, och varje loggboksvy lyssnar på punkten i sitt eget system och i varje fjärrsystem i sitt träd. En post som läggs till i fjärrsystemet, i en webb- eller fjärrklient eller från ett annat system visas därför utan att vyn behöver öppnas igen.

### Krav och begränsningar { #remote-requirements-and-limits }

* Fjärrsystemet är tillagt under **Remote Systems** med **Auto connect on startup** aktiverat. Utan det är anslutningen bara öppen medan något annat använder den, och loggboken håller den inte öppen, så noden och dess uppdateringar kommer och går.
* Fjärrsystemet kör den här versionen av ramverket eller senare. Ett system utan loggbokens tabeller får ingen nod. Ett system utan punkten `LogBookSync` visas, men uppdateras inte i realtid.
* Ett fjärrsystem som inte är anslutet har ingen nod. Den visas nästa gång trädet byggs om efter att anslutningen är uppe, till exempel när loggboken öppnas igen.
* Kontextfiltret ovanför trädet listar det här systemets kontexter. Filtrering av ett fjärrsystems poster fungerar för kontextnamn som finns i båda systemen.
* En anteckning som skrivs härifrån på en vy i fjärrsystemet som aldrig har öppnats där, och som ännu saknar anteckningar, placeras först som ett eget ämne. Fjärrsystemet placerar den på vyn vid sin nästa start. En anteckning på ett objekt kräver dessutom att objektets vy har öppnats där.
* Ett ämne på översta nivån i det här systemet med samma namn som ett fjärrsystem döljs bakom systemets nod. Ge ett sådant ämne ett annat namn.
* Objektpopupen och de vybegränsade loggböckerna visar bara det här systemets loggbok.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — behörigheter, lagring av ämnet och arkivering
<!-- --8<-- [end:body-3] -->
