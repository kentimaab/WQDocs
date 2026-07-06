---
title: Inloggningskonfiguration
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Inloggningskonfigurationer

Den här guiden beskriver hur du konfigurerar inloggningsskärmen i WideQuick Modular Framework och dess vertikaler. Det inkluderar att konfigurera inloggningskravet, ändra hur användare identifierar sig, anpassa bakgrundsbilden och ange den initiala vyn efter inloggning.

## Kräv inloggning { #require-login }

!!! info "En inloggningsskärm ger säkerhet"
    Att använda en inloggningsskärm är en säkerhetsåtgärd som hindrar icke-behöriga användare från att orsaka skada

Som standard krävs inloggning innan användare får tillgång till systemet.

Detta kan inaktiveras genom att stänga av **Kräv inloggning**.
Gör så här: navigera till **Inställningar** i huvudmenyn och öppna vyn **Inställningar**.

![Require login setting](/docs/sv/Images/Login/require-login.png)

När inloggning är inaktiverat hoppas inloggningsskärmen över helt och systemet navigerar
direkt till den konfigurerade startvyn.

Användaren loggas in som oautentiserad, vilket innebär att vyer eller åtgärder som kräver behörighet fortfarande är begränsade.

!!! note
    Att inaktivera **Kräv inloggning** tar inte bort behörighetsbegränsningar. Användare
    kan fortfarande inte komma åt vyer eller utföra åtgärder som kräver en specifik
    behörighet om de inte loggar in manuellt.

    **Däremot** skyddar det inte mot felaktig behörighetshantering. Om kunden inte uttryckligen kräver att inloggningsskärmen saknas, bör du överväga att behålla den.

## Kräv användarnamn { #require-username }

Som standard måste användare ange sitt fullständiga användarnamn vid inloggning. Detta kan konfigureras
till en kombinationsruta genom att stänga av **Kräv användarnamn**.

Navigera till **Inställningar** i huvudmenyn och öppna vyn **Inställningar**.

![Require username setting](/docs/sv/Images/Login/require-username.png)

När detta är inaktiverat visar inloggningsskärmen en kombinationsruta med alla tillgängliga användare i
systemet. Användaren väljer sitt namn i listan och anger sedan sitt lösenord som vanligt.

!!! tip
    Att inaktivera **Kräv användarnamn** är särskilt användbart när WideQuick körs på
    operatörspaneler, där det kan vara besvärligt att skriva ett fullständigt användarnamn. Kombinationsrutan
    gör inloggningen snabbare och enklare på pekskärmar.

!!! note
    Att visa alla tillgängliga användarnamn i en kombinationsruta är mindre säkert än att kräva att
    användarnamnet anges manuellt, eftersom det exponerar listan över systemanvändare.

## Bakgrundsbild

Bakgrundsbilden på inloggningsskärmen konfigureras i **WideQuick® Designer**. I
projektträdet under **Arbetsvyer**, navigera till **Login** **Arbetsvy**. Välj
objektet `Image1` och öppna egenskapen **Image**. Ta bort standardbilderna och lägg till
önskad/önskade bild(er).

Bildfilen/bildfilerna ska placeras i `Images/Login/` i projektmappen innan
den läggs till i WideQuick Designer. Vanliga format som stöds är `PNG`, `SVG` och `JPG`.

!!! tip "En bild eller flera?"
    Om du har lagt till mer än en bild i karusellen är du klar!

    Om du har en bild, ta bort onLoad-skriptet från objektet `Image1`. Det
    skriptet roterar genom de åtta standardbilderna — att ta bort det säkerställer att din anpassade
    bild visas istället.

![Background image configuration](/docs/sv/Images/Login/background-image.gif)

Den rekommenderade bildupplösningen är `1085x1080` pixlar. Objektet `Image1` stöder
även följande visningsalternativ, som kan ställas in i dess egenskaper:

* **Keep aspect ratio** — bibehåller bildens proportioner oavsett objektets storlek
* **Tiled** — upprepar bilden för att fylla objektområdet
* **Stretch** — sträcker ut bilden för att fylla objektområdet oavsett proportioner

!!! tip
    För bästa resultat, använd en bild med den rekommenderade upplösningen `1085x1080`
    med **Keep aspect ratio** aktiverat.

## Start-Arbetsvy

**Start-Arbetsvy** är den vy som öppnas efter inloggning. Den konfigureras i
**WideQuick® Designer** genom att navigera till **WORKSPACE** **Arbetsvy** i
projektträdet under **Arbetsvyer**.

Högerklicka var som helst i vyn och välj **Object** och sedan **MultiviewerPage** från
snabbmenyn. På fliken **Properties**, lokalisera egenskapen **Multiviewer** och
välj önskad **Arbetsvy** från rullgardinsmenyn. Den fullständiga sökvägen behöver inte anges manuellt.

![Start arbetsvy configuration](/docs/sv/Images/Login/start-workview.gif)

Standard-**Start-Arbetsvy** i mallprojektet är **Dashboard Energi**. **Start-Arbetsvy**
bör vara en **Arbetsvy** som finns i antingen mappen **Main_Menu** eller
**System**.

!!! tip
    **Start-Arbetsvy** är systemövergripande som standard. Det är dock möjligt att
    konfigurera olika landningsvyer per användare genom att lägga till flera vyer på
    fliken **Multiviewer** och använda ett laddningsskript för att välja rätt vy baserat på
    den inloggade användaren.
<!-- --8<-- [end:body] -->
