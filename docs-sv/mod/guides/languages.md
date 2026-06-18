---
title: Språk
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Språk

WideQuick stöder flera språk och byte av språk under körning. MOD-demoprojektet levereras med 20 språk redan konfigurerade. Alla befintliga översättningar kan ändras eller tas bort, och nya översättningar och språk kan läggas till i **WideQuick Designer®**.

Att lägga till ett nytt språk kräver översättning av ett stort antal strängar, men processen är AI-kompatibel.


## Hantera översättningar { #managing-translations }

Öppna översättningsdialogen genom att högerklicka på **ProjectTranslations** i projektträdet och välja **Properties...**

![Translation Dialog showing the list of .ts files and the translations tree](/Images/Languages/translation-dialog.png){align=center}

Den vänstra panelen listar alla `.ts`-filer lagrade i `Regions/ProjectTranslations/`, en per språk. Den högra panelen visar alla översättningsbara strängar i projektet, organiserade efter vy och komponentbibliotek.

### Översättningsfiler { #translation-files }

Knapparna i mitten hanterar `.ts`-filer:

* **Add** — skapa en ny `.ts`-fil för ett språk. Efter att ha lagt till, klicka på **Update** för att fylla den med alla aktuella källsträngar.
* **Edit** — öppna den valda `.ts`-filen för redigering.
* **Remove** — ta bort den valda `.ts`-filen.
* **Rename** — byt namn på den valda `.ts`-filen.
* **Update** — genomsök alla arbetsvyer (`.kvie`) och komponentbibliotek (`.klib`) i projektet efter textegenskaper och lägg till eventuella nya källsträngar i alla `.ts`-filer. Strängar som inte längre förekommer i projektet markeras som föråldrade.

### Redigera enskilda översättningar { #editing-translations }

För att redigera en specifik sträng, bläddra i trädet till höger för att hitta den. Dubbelklicka på översättningsraden (den icke-fetstilta texten) och redigera direkt i den raden.

!!! tip
    `.ts`-filer är vanlig XML och kan även redigeras i en textredigerare. Starta om **WideQuick Designer®** efter att ha gjort ändringar utanför dialogen så att både `.ts`- och `.qm`-filerna uppdateras.

## Översätta strängar som sätts av skript { #translating-script-strings }

Etiketter, texter och knapptexter som placeras direkt på en arbetsvy i Designer plockas upp automatiskt när **Update Translations** körs. Dessa strängar översätts utan någon skriptkod.

Strängar som ett skript skriver eller sätter under körning är annorlunda. Om ett skript tilldelar en etiketts värde, bygger ett meddelande eller returnerar visningstext behöver dessa strängar `Language.translate()` för att följa det aktiva språket.

### Använda Language.translate() { #using-language-translate }

`Language.translate()` tar två argument: namnet på filen som innehåller strängen och källsträngen.

```javascript title="Language.translate()"
var label = Language.translate("Translations.klib", "Larm");
```

Om ingen översättning finns för det aktiva språket returneras källsträngen oförändrad.

### Lägga till strängar i Translations.klib { #adding-to-translations-klib }

För att `Language.translate()` ska fungera måste strängen finnas som en textegenskap i projektet, och i MOD placeras de i `Translations.klib`. Så här lägger du till en ny sträng:

1. Lägg till ett textobjekt i valfri arbetsvy i **WideQuick Designer®** och ange dess text till den sträng som ska översättas.
2. Dra objektet till **Translations** under Object Library.
3. (Valfritt) Byt namn på objektet så att det matchar strängen. Det gör det lättare att hitta senare.

När strängen finns i `Translations.klib`, kör **Tools → Update Translations**. Det lägger till den nya strängen som en källpost i alla `.ts`-filer. Översättningen kan sedan läggas till enligt beskrivningen i [Hantera översättningar](#managing-translations).


## Lägga till och redigera ett språk { #adding-a-language }

För att lägga till ett nytt språk, högerklicka på **Languages** i projektträdet. För att redigera ett befintligt språk, högerklicka på språket i stället och välj **Properties**. Båda öppnar samma dialog.

![Edit Language dialog](/Images/Languages/edit-language.png){align=center}

| Fält | Beskrivning |
|---|---|
| **Language Name** | Det namn som visas i språkväljaren under körning. |
| **Keyboard locale** | Det locale som används för tangentbordsinmatning. |
| **Region** | Den region som är kopplad till det här språket. |
| **Application Translation File** | Den `.ts`-fil som används för WideQuicks inbyggda strängar, till exempel larmstatuseetiketter, filteralternativ och systemdialoger. |
| **Project Translation File** | Den `.ts`-fil som används för projektsträngar. |

!!! tip
    En AI-assistent kan avsevärt påskynda processen att lägga till flera språk, från att fylla i översättningar till att lägga till strängar i `Translations.klib` och uppdatera skript.

## Byta språk under körning { #runtime-switching }

Användare byter språk genom att trycka på knappen **Set lang** i **WideQuick Runtime®**, som finns under **Settings → Settings**. Det öppnar ett popup-fönster med en lista över alla tillgängliga språk.

![The Set lang button](/Images/Languages/set-lang.png){align=center}

!!! note
    Efter att ha bytt språk måste användaren logga in igen.

## Ange startspråk { #starting-language }

Startspråket konfigureras i **WideQuick Designer®**. Högerklicka på projektnamnet i projektträdet och välj **Properties**. I dialogrutan **Project Properties**, ställ in listrutan **Start language** på önskat språk.

![Project Properties dialog with the Start language field](/Images/Languages/project-properties.png){align=center}
<!-- --8<-- [end:body] -->
