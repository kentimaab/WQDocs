---
title: Loggbok — Felsökning
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Loggbok

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Samma anteckning visas under flera noder | Detta är avsiktligt. En anteckning på ett objekt hör till varje vy där objektet är ritat, och en anteckning på en vy hör till de objekt som är ritade i den. Kolumnen **Placerad på** namnger postens verkliga koppling. Se [Hur de två träden byggs](configuring.md#how-the-two-trees-are-built). |
| En anteckning visas i vyer den inte har med att göra | Den är placerad högre upp i taggsökvägen än avsett, på en enhet eller ett skåp i stället för på ett enskilt objekt eller en vy. Allt under den punkten hör till den, vilket kan omfatta större delen av anläggningen. Ändra postens `topic` till den vy eller det objekt den faktiskt handlar om. |
| En nod finns i trädet i ett läge men inte i det andra | De två lägena ordnar samma poster olika, så en nod i det ena har ingen motsvarighet i det andra. Inget filtreras bort. Växla reglaget och leta under motsvarande vy eller tagg. |
| En post går inte att hitta efter byte av trädläge | Posten har bytt nod, inte försvunnit. Läs dess koppling i kolumnen **Placerad på** och leta sedan efter den vyn eller taggen i det aktuella läget. |
| En anteckning på en vy visas inte under någon tagg i signalläge | Signalläget placerar en vys anteckningar under de taggar som är ritade i vyn. Om inget objekt i vyn ännu är indexerat finns ingenstans att placera den. Öppna vyn en gång så att dess objekt indexeras, och starta sedan om. |
| Två objekt i samma vy har samma lövnamn | Lövets namn utökas med så mycket av taggen som behövs för att skilja dem åt, vilket ger namn som `VS10_GT11` och `VS11_GT11`. Ett objekt vars namn redan är unikt i sin vy behåller sitt enkla namn. |
| En post ligger på en utrustning i stället för på det exakta objektet | Objektet var inte indexerat när kopplingen senast härleddes, så upplösningen föll tillbaka på utrustningen ovanför. Öppna vyn där objektet är ritat och starta sedan om. Kopplingen härleds om vid varje start. |
| `topic_kind` eller `topic_ref` återgår efter omstart | Båda härleds från `topic` vid start. En ändring av enbart den ena ångras. Ändra postens `topic` i stället. Se [Lagring av ämnet](extending.md#topic-storage). |
| Ämnesträdet är tomt | Trädet byggs från poster i databasen. Finns inga poster är trädet tomt. Skapa en post för att verifiera anslutningen, och kontrollera sedan databasanslutningen `Config` om ingenting visas. |
| Loggboken öppnad från menyn visar bara ett ämnes poster | En begränsad loggbok har lämnat kvar sin överlämning. Öppna loggboken igen från **Dokument & Loggbok → Loggbok**, som rensar värdet när det läses. |
| En post har försvunnit ur listan | Den är med största sannolikhet arkiverad, inte raderad. Aktivera **Visa arkiverade** i filtret för att visa arkiverade poster, och återställ den sedan. |
| Ett ämne har försvunnit ur ämnesträdet | Trädet byggs från poster som inte är arkiverade. Ett ämne vars poster alla är arkiverade listas inte förrän arkiverade poster inkluderas. |
| En användare saknas i filtrets användarlista | Användarlistan byggs endast från poster som inte är arkiverade, så en användare vars poster alla är arkiverade visas inte. |
| Arkiverade poster kom tillbaka efter en uppgradering | Poster som tidigare mjukraderats genom den utgångna kolumnen `deleteMark` tas bort vid start, de arkiveras inte. Det som finns kvar var arkiverat snarare än mjukraderat. |

## Kända fel { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
