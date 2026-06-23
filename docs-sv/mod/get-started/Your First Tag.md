---
title: Din första tagg
description: Koppla en tagg från start till slut och verifiera i ett Processpopup.
product: mod
page_type: getstarted
status: draft
last_reviewed: 2026-05-19
tags: 
 - MOD
---

# Din första tagg

Den här guiden visar hur du kopplar en enskild tagg från start till slut — från att skapa en OPC UA-tagg till att verifiera den i ett Processpopup. Det är det snabbaste sättet att bekräfta att ditt projekt är korrekt konfigurerat och redo för implementering.

Innan du börjar, se till att du har mallprojektet öppet i **WideQuick 13.4.1** eller senare. Om inte, se [Ladda ner WideQuick MOD](download.md)

<!-- --8<-- [start:body] -->

## Steg 1 - Konfigurera en anslutning

Det första steget är att konfigurera en anslutning i **WideQuick Designer®**. I det här exemplet används en **OPC UA**-anslutning med namnet `OPC`. En fullständig guide för att konfigurera OPC UA finns i WideQuick-manualen genom att trycka på ++f1++ i WideQuick Designer.

Följande anslutningstyper stöds också:

* MQTT
* BACnet
* Modbus Serial
* Modbus TCP/IP
* OPC Server
* OPC UA

![OPCUA](/docs/sv/Images/First_tag/OPCUA.gif)

## Steg 2 - Skapa taggen

I **WideQuick Designer®**, öppna **Taggeditorn** och skapa en ny boolesk tagg enligt taggstrukturen:

`OPC.AS01_VS10_PV01_IO`

Den här taggen består av:

* **Anslutning** — `OPC`
* **Enhet** — `AS01`
* **System** — `VS10`
* **Objektnamn** — `PV01`
* **Suffix** — `_IO`

![Create](/docs/sv/Images/First_tag/Create.gif)

För mer information om taggstrukturen, se [Taggstruktur](../reference/tag-structure.md).

## Steg 3 - Skapa en Arbetsvy

I **WideQuick Designer®**, skapa en ny **Arbetsvy** inuti **System 1**. Den kommer då att visas automatiskt i navigeringsmenyn. För mer information om hur navigeringen fungerar, se [Navigation — Kom igång](../modules/Core/Navigation/get-started.md).

![arbetsvy](/docs/sv/Images/First_tag/CreateWork.gif)

## Steg 4 - Placera motorobjektet

Öppna den nya **Arbetsvy** och dra objektet `dynMotorPumpR_000` från objektbiblioteket **Motors** in i vyn.

Välj objektet `DynTouch` inuti gruppen och navigera till fliken **Egenskaper**. Ange följande:

* **Anslutning** — `OPC`
* **Enhet** — `AS01`
* **Sys** — `VS10`
* **ObjectName** — `PV01`

![DynTouch properties](/docs/sv/Images/First_tag/Properties.gif)

!!! tip
    Objektet `dynMotorPumpR_000` är ett färdigt objekt från objektbiblioteket **Motors**. För att lära dig hur du skapar egna objekt, se [Skapa ett objekt](../guides/create-an-object.md).

## Steg 5 - Koppla suffixaliaser och verifiera

### Konfigurera animationen

Starta projektet och navigera till **Inställningar → Suffix → Suffix - Larm**. Välj **4 - Aktiv** och klicka på **Lägg till nytt suffixalias i vald kategori**. När du uppmanas att ange ett namn, skriv **On** och klicka på **Ok**. Klicka på **Skriv ändringar till DB** för att spara.

Suffixaliaset **On** är nu en del av gruppen **4 - Aktiv**. Välj sedan **On** i trädvyn och tilldela `_IO` till fältet **Suffix**.

För mer information om hur animationssystemet fungerar, se [Arbetsvy-animationer](../guides/workview-animations.md).

![Suffix Alarm configuration](/docs/sv/Images/First_tag/SuffixAlarm.gif)

### Konfigurera Processpopupen

Nästa steg är att koppla suffixet till **Process**-popupen, så att ett klick på objektet öppnar popupen och gör det möjligt att styra signalen. Navigera till **Inställningar → Suffix → Suffix - Popups**.

Den här vyn visar alla konfigurerade standardpopups. För att skapa en anpassad popup, se [Skapa ett popup](../guides/create-a-popup.md). Välj **Process** och klicka på **Lägg till nytt suffixalias i vald kategori**. Ge det nya suffixaliaset namnet **On** för konsekvensens skull. Välj sedan aliaset **On** och tilldela `_IO` till fältet **Suffix**.

![Suffix Popup configuration](/docs/sv/Images/First_tag/SuffixPopup.gif)

### Verifiera

Navigera till vyn som innehåller motorobjektet och vänsterklicka på det för att öppna popup-fliken. Välj **Process** — reglaget för signalen `_IO` finns tillgängligt här. Växla den till `true` och kontrollera att det gröna ljuset på motorobjektet aktiveras, vilket bekräftar att taggen är korrekt kopplad från start till slut.

![Hello World result](/docs/sv/Images/First_tag/HelloWorld_result.png)

!!! tip
    Om det gröna ljuset inte visas, kontrollera att taggnamnet i **Taggeditorn** exakt matchar egenskaperna som angetts på objektet `DynTouch`, inklusive versalisering.

<!-- --8<-- [end:body] -->
