---
title: Suffixsystem
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Suffixsystem

Suffixsystemet är hur WideQuick MOD kopplar ett klickbart objekt i en arbetsvy till rätt popup-kontroller och Datalager-taggar. När en operatör klickar på en pump, ventil eller sensor slår suffixsystemet upp vilka parametrar som finns för det objektet och renderar bara de kontroller som är tillämpliga.

Länken mellan objekt och parameter är en namnkonvention: en kort sträng (suffixet) som läggs till bastaggnamnet. För ett objekt med namnet `MB.AS01.SYS_PUMP1` resulterar suffixet `_BV` i Datalager-taggen `MB.AS01.SYS_PUMP1_BV`. Om den taggen finns visas motsvarande kontroll.

Konfigurationen lagras i `SuffixConfig.db` som en JSON-struktur kallad `SuffixObj`. Strukturen laddas av `scSuffix` vid uppstart och läses av `scSmartPopup` varje gång en popup öppnas.

## SuffixObj-struktur { #suffixobj-structure }

`SuffixObj` har två aktiva avsnitt på toppnivå.

| Avsnitt | Syfte |
|---|---|
| `Popups` | Definierar popup-grupper — varje grupp mappas till en vyfil och deklarerar vilka suffixkontroller den innehåller. |
| `Views` | Definierar taggkategorier som används för larm-, varnings-, service- och aktivstatusindikationer. |

## Popups { #popups }

Varje post i `Popups` representerar en popup-grupp — en flik eller panel som visas när ett objekt klickas.

```json
"Kontroll": {
  "name": "Kontroll",
  "viewPath": "Control.kvie",
  "Always visible": false,
  "privilage": "",
  "suffixes": {
    "analogOutputValue": {
      "suffix": "_R",
      "desc": "Analog signal ut",
      "decimals": 1,
      "writeable": 1,
      "write_priv": "",
      "unit": ""
    }
  }
}
```

### Popup-gruppens attribut { #popup-group-attributes }

| Attribut | Typ | Beskrivning |
|---|---|---|
| `name` | sträng | Visningsnamn som visas som fliketikett. |
| `viewPath` | sträng | Den `.kvie`-arbetsvy som laddas för denna popup-grupp. |
| `Always visible` | booleskt | Om `true` visas fliken även om inga suffix finns för det klickade objektet. Om `false` döljs fliken om inte minst en suffixtagg hittas i Datalager. |
| `privilage` | sträng | Behörighetsnyckel som krävs för att se denna flik. Tom sträng innebär alla användare. |
| `suffixes` | objekt | Karta av suffix-aliasnamn till suffixdefinitioner (se nedan). |

### Suffixdefinitionens attribut { #suffix-definition-attributes }

| Attribut | Typ | Beskrivning |
|---|---|---|
| `suffix` | sträng | Strängen som läggs till objektets bastaggnamn för att bilda Datalager-nyckeln. |
| `desc` | sträng | Läsbar etikett som visas i popup-kontrollen. |
| `decimals` | nummer | Antal decimaler för numerisk visning. |
| `writeable` | nummer | `1` om kontrollen tillåter operatörsinmatning, `0` för skrivskyddad visning. |
| `write_priv` | sträng | Behörighetsnyckel som krävs för skrivning. Tom sträng faller tillbaka på objektets egna behörighet. |
| `unit` | sträng | Enhetsetikett. Kan lämnas tom om enheten är definierad i Datalager-taggens beskrivning. |

## Views { #views }

Varje post i `Views` definierar en taggkategori som används av statusindikatorsystemet.

```json
"1 - Alarms": {
  "vector": "alarmTags",
  "blink": "true",
  "suffixes": {
    "Givarfel": {
      "suffix": "_LG",
      "desc": "Givarfel"
    }
  }
}
```

| Attribut | Typ | Beskrivning |
|---|---|---|
| `vector` | sträng | Namnet på den körningsarray som ska hålla matchande taggnamn för denna kategori. |
| `blink` | sträng | Anger om indikatorn blinkar när taggar i denna kategori är aktiva. `"true"` eller `"false"`. |
| `suffixes` | objekt | Suffixdefinitioner som skannas för att bygga kategorins tagglista. Endast `suffix` och `desc` används här. |

## Taggupplösning vid körning { #tag-resolution }

När ett DynTouch-objekt klickas sätts bastaggnamnet samman från objektets egenskaper:

```
tagName = Connection + Device + Sys + "_" + ObjectName
```

Till exempel: `MB` + `.AS01.` + `SYS` + `_` + `PUMP1` → `MB.AS01.SYS_PUMP1`

`scSmartPopup` itererar sedan över varje popup-grupp i `SuffixObj.Popups` och kontrollerar om gruppen ska visas:

1. Om `Always visible` är `true` inkluderas fliken villkorslöst.
2. Annars kontrolleras varje suffix i gruppen. Om `Datalager[tagName + suffix.suffix]` finns inkluderas fliken.

Endast flikar som klarar denna kontroll renderas. Det innebär att popup-fönstret automatiskt anpassar sig till de signaler som faktiskt finns för det klickade objektet — ingen manuell konfiguration per objekt behövs.

## Komponentbindning { #component-binding }

Popup-UI-komponenter använder egenskapen `SuffixAlias` för att deklarera vilket suffix de binder till. När en popup öppnas anropar `scSmartPopup` `activate(suffixObj)` på varje registrerad komponent och skickar den lösta suffixdefinitionen. Komponenten binder sedan sin visning och inmatning till `Datalager[tagName + suffixObj.suffix]`.

Komponenter som har `always_visible` satt till `true` förblir synliga även om suffixtaggen inte finns för det aktuella objektet.

## CustomPopupFirstOpen { #custompopupfirstopen }

När en popup öppnas direkt via en DynTouch-länk (utan att gå via flikbehållaren) aktiverar komponenter sina Load-händelser innan föräldravyn har slutfört sin initiering. Det innebär att `registerObject()`-anrop från komponenter sker innan `view.popup` existerar, och suffixbindningen missas.

`scSmartPopup.bootstrapDirect()` löser detta. Den rekonstruerar popup-kontexten från det klickade objektet och återaktiverar Load-händelserna för alla underordnade komponenter, vilket säkerställer att de registrerar sig och tar emot `activate()` efter att vyn är fullt redo.

Denna bootstrap körs automatiskt. Ingen manuell hantering behövs i popup-arbetsytor.

## Redigera konfigurationen { #editing }

Suffixkonfigurationen lagras som JSON i `SuffixConfig.db` och laddas in i minnet av `scSuffix` vid uppstart. Ändringar träder i kraft efter att körningen startas om eller skriptet laddas om.

`scSuffix` hanterar migrering automatiskt: om den hittar det äldre enkolumns-`JSON`-formatet i `SuffixObj` delar den upp innehållet i de tre separata kolumnerna (`Popups`, `ProcessViews`, `Views`) vid första läsningen.

<!-- --8<-- [end:body] -->
