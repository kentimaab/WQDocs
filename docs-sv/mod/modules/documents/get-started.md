---
title: Dokument — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-12
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Dokument — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Dokument och all
    relaterad funktionalitet som täcks av Dokument-guiderna:
    
    * `scDoc`
    * `scLinking`
    * `scSubNav`
    * `scObjectFinder`
    * `scPrototypes`
    * `scSuffix`
    * `scThemes`
    * `scUsers`
    * `scFilePicker`
    * `scWM`
    * `scButtons`
    * `scNav`
    * `scToolTip`
    * `scSmartPopup`
    * `scAlert`

Dokumentmodulen finns under **Dokument & Loggbok → Dokument** i huvudmenyn. Vyn **Dokument - Lista** är den primära ingångspunkten. Den visar alla dokument i systemet, och där kan de läggas till, förhandsgranskas och hanteras.



## Filvyn { #files-view }

Vyn är uppdelad i två paneler. Den vänstra panelen visar ett filträd med två kategorier: **Lokala filer** och **Onlinefiler**. Lokala filer lagras på servern; onlinefiler är länkar till externa URL:er. Den högra panelen visar förhandsvisning för den valda filen. På **WideQuick® Web** visas en tredje kategori för filer som inte kan öppnas i webbläsaren.
<!-- --8<-- [end:body-1] -->

![Documents Files view](/docs/sv/Images/Documents/documents-list.png){align=center}

<!-- --8<-- [start:body-2] -->
Följande åtgärder är tillgängliga längst ned i vyn:

* **Förhandsgranska** — öppnar den valda filen i förhandsgranskningspanelen.
* **Lägg till dokument** — öppnar uppladdningsdialogen för att lägga till ett nytt dokument.
* **Ta bort dokument** — tar permanent bort det valda dokumentet.
* **Redigera valt dokument** — byt namn på det valda dokumentet, eller ändra URL:en för en onlineresurs. Sökvägen till en lokal fil kan inte redigeras.
* **Synkronisera med lokala filer på server** — söker igenom dokumentmappen på servern och uppdaterar listan för att matcha. Se [Synkronisering med filsystemet](configuring.md#syncing-with-the-filesystem).

## Ladda upp en lokal fil { #uploading-a-local-file }

Lokala filer kan bara laddas upp på servern. På fjärr- och webbklienter är fliken **Ladda upp fil** inaktiverad och visar "Uppladdning av fil är inte möjligt på fjärrsystem".

1. Klicka på **Lägg till dokument**.
2. Välj fliken **Ladda upp fil**.
3. Klicka på **Klicka för att bläddra bland lokala filer** och dubbelklicka på filer i filbläddraren för att lägga till dem i kön.
4. Klicka valfritt på ett filnamn i kön för att byta namn på det innan uppladdning.
5. Klicka på **Ladda upp filer**.
<!-- --8<-- [end:body-2] -->

![Upload file tab](/docs/sv/Images/Documents/documents-upload.png){align=center}

<!-- --8<-- [start:body-3] -->
Filerna kopieras till servern och läggs till i dokumentlistan under **Lokala filer**.

## Lägga till en onlineresurs { #adding-an-online-resource }

1. Klicka på **Lägg till dokument**.
2. Välj fliken **Onlineresurs**.
3. Ange URL:en i fältet **Dokument-URL**.
4. Ange ett visningsnamn i fältet **Dokumentnamn**.
5. Välj filtyp med hjälp av ikonväljaren.
6. Klicka på **Lägg till**.
7. Klicka på **Ladda upp filer**.
<!-- --8<-- [end:body-3] -->

![Online resource tab](/docs/sv/Images/Documents/documents-upload-online.png){align=center}

<!-- --8<-- [start:body-4] -->
Resursen läggs till i dokumentlistan under **Onlinefiler**. Endast URL:en lagras. Ingen fil laddas ned till servern.

## Förhandsgranska ett dokument { #previewing-a-document }

Välj en fil i den vänstra panelen och klicka på **Förhandsgranska** för att läsa in den i förhandsgranskningspanelen.

Bilder, PDF:er och webbsidor visas direkt i förhandsgranskningspanelen. Office- och OpenDocument-filer (Word, Excel, PowerPoint, `.odt`, `.ods`, `.odp`) förhandsgranskas aldrig inline. På skrivbordsklienter öppnas de i det externa program som är kopplat till filtypen. På **WideQuick® Web** grupperas de separat i filträdet, och ett meddelande talar om att de inte kan visas i webbläsaren.

## Nästa steg { #next-steps }

* [Konfigurering](configuring.md) — länka dokument till objekt och hålla filer synkroniserade
* [Utöka](extending.md) — behörighetsreferens
<!-- --8<-- [end:body-4] -->
