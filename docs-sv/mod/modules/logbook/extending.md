---
title: Loggbok — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Loggbok — Utöka

## Behörigheter { #privileges }

Dessa behörigheter styr åtkomsten till loggboksoperationer:

| Behörighet | Beskrivning |
|---|---|
| `Logbook_Add` | Krävs för att skapa nya poster |
| `Logbook_Edit` | Krävs för att redigera befintliga poster |
| `Logbook_Archive` | Krävs för att arkivera och återställa poster |
| `Logbook_Delete` | Krävs för **ta bort alla arkiverade anteckningar** i inställningsvyn |
| `Logbook_Context` | Krävs för att lägga till, ta bort eller redigera kontexter |
| `Logbook_View` | Krävs för att se poster |

Användare utan `Logbook_Add` ser knappområdet **Lägg till** inaktiverat och nedtonat, med ett rött överlager som visar ett meddelande om vilken behörighet som krävs. Egenskapen `Enabled` på knappen är bunden till `scUsers.hasPriv("Logbook_Add")`. Samma mönster gäller för övriga loggboksbehörigheter.

!!! warning "Alla loggboksbehörigheter är nekade som standard"
    Samtliga loggboksbehörigheter är definierade med `Default="denied"` i `Privileges.kdat`. Efter en uppgradering måste `Logbook_Archive` tilldelas en roll innan någon kan arkivera en post. Se [Användare och behörigheter](../Core/users-privileges.md).

## Lagring av ämnet { #topic-storage }

En posts placering hålls i tre kolumner i tabellen `logbook`. `topic_kind` och `topic_ref` läggs till vid start om tabellen är äldre än dem, så ett befintligt projekt uppgraderar sig självt.

| Kolumn | Syfte |
|---|---|
| `topic` | Den visningssökväg posten placerades under. Detta är den gällande uppgiften. |
| `topic_kind` | Vad posten är kopplad till: `view`, `signal`, `signal-node` eller `free`. |
| `topic_ref` | Den råa identifieraren för kopplingen: en vysökväg inklusive `.kvie`, eller en tagg. Tom för `free`. |

!!! warning "Endast `topic` ska redigeras direkt"
    `topic_kind` och `topic_ref` är härledda värden. `reconcileTopicRefs()` härleder båda från `topic` vid varje start, så en ändring som skrivs till enbart den ena skrivs över vid nästa omstart. För att flytta en post ändras dess `topic`.

Härledningen tar den längsta del av sökvägen som motsvarar en känd vy eller tagg, och behåller resten som postens egen undersökväg. `MB/AS02/Station2/GT44/Trend` kopplas därför till givaren `MB.AS02.Station2_GT44` och behåller `Trend` som en nod under den.

### Självläkning vid start { #self-healing-on-start }

`reconcileTopicRefs()` körs en gång vid start och härleder om kopplingen för varje distinkt ämne. Det håller placeringarna korrekta efter att vyer bytt namn eller flyttats, och efter att objektindexet byggts om.

!!! note "Objektindexet fylls på när vyer öppnas"
    Kopplingar löses mot indexet över vilka objekt som är ritade i vilka vyer, och det indexet växer allteftersom vyer besöks. En tagg som ännu inte indexerats kopplas i stället till utrustningen ovanför, och landar på den exakta taggen efter att vyn öppnats en gång och applikationen startats om. Posten går att nå oavsett. Det är bara noden den ligger på som skiljer.

## Arkivering { #archiving }

Arkivering har ersatt radering av enskilda poster. Det finns ingen funktion som raderar en enskild post, och ingen vy erbjuder det. En post arkiveras i stället, vilket döljer den i listan men behåller den i databasen. Detta lagras i kolumnen `archived` i tabellen `logbook`, som läggs till vid start om tabellen är äldre än den.

!!! note "Arkivering finns endast i den globala loggboken"
    Arkivering och återställning erbjuds i den fullständiga loggboksvyn under **Dokument & Loggbok → Loggbok**. Objektpopupen och de vybegränsade loggböckerna erbjuder endast att lägga till och redigera.

    Det håller åtgärden där den går att ångra. Att visa arkiverade poster och att återställa dem bygger båda på filtret **Visa arkiverade**, som bara finns i den globala vyn. Att arkivera från en begränsad loggbok skulle dölja posten utan möjlighet att hämta tillbaka den därifrån.

| Tillstånd | `archived` | Beteende |
|---|---|---|
| Aktiv | `0` | Listas normalt. |
| Arkiverad | `1` | Dold om inte vyn uttryckligen inkluderar den. |

Arkiverade poster utesluts från ämnesträdet och från användarlistan i filtret, så ett ämne vars poster alla är arkiverade försvinner ur trädet tills arkiverade poster visas.

| Funktion | Syfte |
|---|---|
| `markEntryAsArchived(entryObj)` | Sätter postens `archived`-flagga till `1` och laddar om vyn. |
| `unarchiveEntry(entryObj)` | Nollställer flaggan och laddar om vyn. |
| `deleteAllArchived()` | Raderar permanent varje arkiverad post och returnerar hur många som togs bort. |
| `getLogBookTopics(contextFilter, showArchived, mode)` | Bygger ämnesträdet i angivet läge. Ämnen för arkiverade poster tas med endast när `showArchived` är `true`. |

En hanterare exponerar `showArchived`, som är `false` som standard. Sätts den till `true` före anropet till `load()` inkluderas arkiverade poster i listan.

!!! warning "Radering av arkiverade poster kan inte ångras"
    `deleteAllArchived()` tar bort varje arkiverad post ur databasen helt. Funktionen ligger bakom raderingsåtgärden i inställningsvyn och är den enda operationen i modulen som förstör arkiverat innehåll.

### Utgången mjukradering { #retired-soft-delete }

En tidigare kolumn `deleteMark` implementerade en separat livscykel för mjukradering. Den har utgått till förmån för `archived`. Vid start raderas rader som fortfarande är märkta `deleteMark=1` och kolumnen tas bort. Ingen manuell migrering behövs.

## Skriptreferens { #script-reference }

Skriptet `scLogBook` löser placeringar och bygger trädet. En vy håller en hanterarinstans, skapad med `new logBookHandler(topic, view)`, som äger postlistan och trädet för den vyn.

### Trädets ordning { #tree-keying }

| Medlem | Syfte |
|---|---|
| `scLogBook.MODE_DIR` | Träd ordnat efter arbetsvyernas katalogstruktur. |
| `scLogBook.MODE_SIGNAL` | Träd ordnat efter signalsökväg. |
| `handler.treeMode` | Det läge hanteraren bygger i. Sätts före `setTreeView()`, annars byggs det första trädet utan ordning. |
| `handler.setTreeMode(mode)` | Byter läge och bygger om. Rensar korsreferenscachen, eftersom objektindexet växer allteftersom vyer öppnas. |

Operatörens val hålls i punkten `LogBookTreeDirMode` i Datalagret, som varje loggboksvy bevakar med en `DataStoreListener`. Punkten sparas inte mellan körningar, så trädet återgår till arbetsvyläge när applikationen startas om.

### Upplösning { #resolution }

| Funktion | Syfte |
|---|---|
| `resolveTopic(topic)` | Löser en visningssökväg till `{kind, ref, tail}`, med det längsta matchande prefixet. |
| `displayPathsFor(kind, ref, tail, topic, mode, preferView)` | De sökvägar en post visas under i angivet läge. Returnerar fler än en när ett objekt är ritat i flera vyer. |
| `viewsForRef(ref)` | De vyer en tagg förekommer i, genom att klättra uppåt i taggsökvägen tills något matchar. |
| `topicsUnderPath(displayPath, mode, withDescendants)` | De lagrade ämnen som är placerade under en vald trädnod. |
| `placementLabel(kind, ref, topic)` | Texten som visas i kolumnen **Placerad på**. |
| `leafLabelFor(view, signal)` | Lövets namn för ett objekt i en vy, utökat med så mycket av taggen som behövs när två objekt har samma namn. |

### Öppna en loggbok begränsad till något { #opening-a-logbook-scoped-to-something }

En vy eller en knapp öppnar en begränsad loggbok genom att ange vilket ämne som ska markeras och sedan länka till loggbokens pop-out. Ämnet skickas i `app.logbookSelectedTopic` och konsumeras av pop-outen:

```javascript title="Öppna loggboken på den aktuella vyn"
app.logbookSelectedTopic = scLogBook.normalizeTopic(this.view.name);
app.popOut.setView("Pop_Outs/LogBookControls/GetLogBookEntryByTopic.kvie");
app.popOutVisible = true;
```

Pop-outen löser sökvägen tillbaka till sin koppling med `resolveTopic()`, registrerar den med `setScope(kind, ref)` och anropar `applyScope()` för att översätta kopplingen till en sökväg för det läge som är aktivt. Att hålla begränsningen som en koppling i stället för som en sökväg är det som gör att markeringen överlever ett lägesbyte.

!!! note "Överlämningen rensas när den konsumeras"
    Huvudvyn för loggboken rensar `app.logbookSelectedTopic` när den läser värdet. Ett kvarlämnat värde skulle annars tillämpas nästa gång loggboken öppnas från menyn, och filtrera listan till ett ämne operatören inte bett om.

<!-- --8<-- [end:body] -->
