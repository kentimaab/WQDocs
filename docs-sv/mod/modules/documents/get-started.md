---
title: Dokument — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

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
    * `scAlert`

Dokumentmodulen finns under **Dokument & Loggbok -> Dokument** i huvudmenyn. Vyn **Dokument - Lista** är den primära ingångspunkten — den visar alla dokument som finns i systemet och låter dig lägga till, förhandsgranska och hantera dem.



## Filvyn { #files-view }

Vyn är uppdelad i två paneler. Den vänstra panelen visar ett filträd med två kategorier: **Lokala filer** och **Onlinefiler**. Lokala filer lagras på servern; onlinefiler är länkar till externa URL:er. Den högra panelen visar förhandsvisning för den valda filen. På **WideQuick Web®** visas en tredje kategori för filer som inte kan öppnas i webbläsaren.

![Documents Files view](/Images/Documents/documents-list.png){align=center}

Följande åtgärder är tillgängliga längst ned i vyn:

* **Förhandsgranska** — öppnar den valda filen i förhandsgranskningspanelen.
* **Lägg till dokument** — öppnar uppladdningsdialogen för att lägga till ett nytt dokument.
* **Ta bort dokument** — tar permanent bort det valda dokumentet.
* **Redigera valt dokument** — byt namn på det valda dokumentet.
* **Synkronisera med lokala filer på server** — söker igenom dokumentmappen på servern och uppdaterar listan för att matcha. Se [Synkronisering med filsystemet](configuring.md#syncing-with-the-filesystem).

## Ladda upp en lokal fil { #uploading-a-local-file }

1. Klicka på **Lägg till dokument**.
2. Välj fliken **Ladda upp fil**.
3. Klicka på släppzonen eller dra filer till den för att lägga till dem i kön.
4. Klicka valfritt på ett filnamn i kön för att byta namn på det innan uppladdning.
5. Klicka på **Ladda upp filer**.

![Upload file tab](/Images/Documents/documents-upload.png){align=center}

Filerna kopieras till servern och läggs till i dokumentlistan under **Lokala filer**.

## Lägga till en onlineresurs { #adding-an-online-resource }

1. Klicka på **Lägg till dokument**.
2. Välj fliken **Onlineresurs**.
3. Ange URL:en i fältet **Dokument-URL**.
4. Ange ett visningsnamn i fältet **Dokumentnamn**.
5. Välj filtyp med hjälp av ikonväljaren.
6. Klicka på **Lägg till**.
7. Klicka på **Ladda upp filer**.

![Online resource tab](/Images/Documents/documents-upload-online.png){align=center}

Resursen läggs till i dokumentlistan under **Onlinefiler**. URL:en lagras — ingen fil laddas ned till servern.

## Förhandsgranska ett dokument { #previewing-a-document }

Välj en fil i den vänstra panelen och klicka på **Förhandsgranska** för att läsa in den i förhandsgranskningspanelen.

De flesta filtyper kan förhandsgranskas direkt — bilder, PDF:er och webbsidor visas inline. På **WideQuick Web®** kan inte Office-filer (Word, Excel, PowerPoint) förhandsgranskas i webbläsaren och grupperas separat i filträdet.

## Nästa steg { #next-steps }

* [Konfigurering](configuring.md) — länka dokument till objekt och hålla filer synkroniserade
* [Utökning](extending.md) — behörighetsreferens
<!-- --8<-- [end:body] -->
