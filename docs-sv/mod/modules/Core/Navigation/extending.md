---
title: Navigation — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Navigation — Utöka

Det här avsnittet beskriver hur du utökar navigationsmodulen med anpassad funktionalitet.
Det inkluderar att skapa genvägar till specifika objekt med GoTo samt att lägga till anpassade
ikoner i navigationsmenyn.

Innan du börjar, se till att du är bekant med grunderna i navigationsmodulen.
Om inte, se [Navigation — Kom igång](get-started.md).

## GoTo { #goto }
GoTo-funktionen gör det möjligt att länka direkt till ett specifikt objekt, vilket möjliggör
skapandet av genvägar som tar användaren till den vy där objektet finns. När
man når ett objekt via GoTo markeras det, vilket gör det enkelt att hitta även i en komplex
vy. Om objektet finns i flera vyer visas ett popup-fönster med alla tillgängliga platser.

För att använda GoTo, tillämpa följande skript på en knapps **onClick**-åtgärd och ersätt
`YOUR_OBJECT.NAME` med namnet på målobjektet:

```javascript title="goTo() function in scLinking script"
scLinking.goTo("YOUR_OBJECT.NAME");
```

I exemplet nedan tillämpas `goTo()`-funktionen på en knapps **onClick**-åtgärd
med målobjektet `MB.AS01.LB02_GT43`:

![goTo](/Images/Navigation/goTO.gif)

### GoTo i Larmgrupper { #goto-in-alarm-groups }
GoTo kan även integreras i **Larmgrupp** och **LarmLista**, vilket gör det möjligt för användare att
omedelbart navigera till det objekt som utlöste ett larm och vidta åtgärder.

Följ dessa steg för att aktivera GoTo för larm:

1. I **WideQuick Designer®**, öppna egenskaperna för **Larmgrupp** och navigera till
**Åtgärder**.
2. Klicka på cirkeln bredvid **Skript** för att aktivera skriptåtgärden och ange
följande:

```javascript title="goToAlarm() function in Alarm Group Measures"
goToAlarm(app.alarmView.Alarm1.nameForCurrentAlarm, app.alarmView.name)
```

3. Lägg till ett **Åtgärd**-tillstånd genom att klicka på **Lägg till** på samma sida. Ange önskad
visningstext och välj en färg.
4. I **Larm**-objektet, navigera till **Larmkolumner** och aktivera
**Använd anpassade larmkolumner**.
5. Välj kategorin **Åtgärd** — om du trycker på den här kolumnen för ett specifikt larm
aktiveras GoTo och navigerar till den **Arbetsvy** där larmet uppstod.

![Alarm_Goto](/Images/Navigation/Alarm_goTo.png)

!!! note 
    För att kunna använda GoTo-funktionen på larm krävs skriptet `scAlarmFinder`


## Anpassade navigationsikoner { #custom-navigation-icons }
Det här avsnittet beskriver hur du implementerar anpassade navigationsikoner kopplade till specifika
vyer. Implementeringsprocessen består av två steg:

1. Importera och konfigurera SVG:n
2. Koppla SVG:n till en **Arbetsvy**-identifierare

### Importera och konfigurera SVG:n { #importing-and-configuring-the-svg }
Importera först din SVG-ikon. Det rekommenderas att ha två versioner — en för mörkt läge
och en för ljust läge. Detta säkerställer att ikonen förblir synlig oavsett användarens
temainställning. Namnge och placera filerna enligt följande:

* `YourSvg-gray.svg` — för det ljusa temat
* `YourSvg-white.svg` — för det mörka temat

Båda filerna ska placeras i `Images/Material_Icons/`.

Om applikationen är avsedd att köras via webbklienten måste SVG:n ha en
definition av `width` och `height`. Utan dessa renderas inte ikonen i webbklienten.
Verifiera detta genom att öppna SVG:n i en textredigerare och bekräfta att de är definierade.
Om inte, lägg till dem i XML-strukturen:

```xml title="SVG width and height definition"
<svg
    width="24"
    height="24"
/>
```

När SVG-filerna är placerade i rätt mapp och deras dimensioner verifierade, gå vidare
till nästa steg.

### Koppla SVG:n { #connecting-the-svg }
För att koppla en SVG till en mapp eller **Arbetsvy**, lägg till ett ytterligare `else if`-block i
funktionen `selectImage()` i skriptet `scSubNav`, som finns under
**Skript → scSubNav** i projektträdet. Hitta funktionen `selectImage()` och lägg till
det nya `else if`-blocket före det sista `else`-blocket, som hanterar reservikonen.
Exemplet nedan visar hur identifieraren `solarcell` kopplas till en solpanelsikon:

```javascript title="selectImage() function in scSubNav script"
else if (type === 'solarcell' || type === 'solar' || type === 'solarpanel' || type === 'solar park') {
    return base + 'solar-power' + s;
}
```

Alla **Arbetsvyer** vars namn innehåller `solarcell`, `solar`, `solarpanel` eller
`solar park` tilldelas motsvarande ikon. Skriptet `scSubNav`
konverterar automatiskt **Arbetsvy**-namn till gemener innan jämförelsen görs, så
skiftläge spelar ingen roll så länge identifierarorden i
funktionen `selectImage()` är gemener. Variabeln `base` innehåller sökvägen till
ikonmappen och `s` innehåller temats suffix, som tillsammans bildar den fullständiga sökvägen till
rätt SVG-fil. Om ingen identifierare matchar tilldelar det sista `else`-blocket en
standardikon.
<!-- --8<-- [end:body] -->
