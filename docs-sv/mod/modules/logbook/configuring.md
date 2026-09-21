---
title: Loggbok — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
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

Samma poster ordnas på två sätt, och reglaget ovanför trädet växlar mellan dem. Inget av lägena filtrerar bort något.

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

### Objektpopup { #object-popup }

Varje objekt i projektet har en flik [**Loggbok**](../../reference/Popup/Logbook.md) i sitt popup-fönster. När fliken öppnas markeras objektet i trädet och dess poster listas. Nya poster som skapas härifrån placeras automatiskt på objektet.

Resten av trädet är fortfarande nåbart, så en anteckning på ett angränsande objekt eller på den omgivande vyn kan läsas utan att popup-fönstret lämnas. Poster kan läggas till och redigeras härifrån. Arkivering erbjuds endast i den globala loggboken, eftersom det är där arkiverade poster kan visas igen och återställas. Arkiverade poster listas aldrig i ett objektpopup.
<!-- --8<-- [end:body-2] -->

![Loggboksfliken i objektets popup-fönster](/docs/sv/Images/Logbook/object-popup-logbook.png){align=center}

<!-- --8<-- [start:body-3] -->
### Vybegränsad { #view-scoped }

Menyn **SpeedDial** i processvyer innehåller en knapp som öppnar loggboken med den aktuella vyn markerad i trädet. Vyns poster listas direkt, tillsammans med posterna för de objekt som är ritade i den. Nya poster som skapas härifrån placeras på vyn.

Precis som i objektpopupen är resten av trädet nåbart från en vybegränsad loggbok, så en anteckning som är placerad någon annanstans kan läsas utan att gå tillbaka till huvudvyn.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — behörigheter, lagring av ämnet och arkivering
<!-- --8<-- [end:body-3] -->
