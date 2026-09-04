---
title: Speed Dial
product: mod
page_type: guide
status: draft
last_reviewed: 2026-09-04
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Speed Dial

Speed Dial är en flytande åtgärdsknapp som placeras i en arbetsvy. Den ligger hopfälld som en enda knapp och fälls ut till en uppsättning ikonalternativ när den klickas, så att en vy kan erbjuda flera åtgärder utan att permanent ta upp skärmyta med ett verktygsfält.

I viloläge visas en enda **+**-knapp.

![Speed Dial hopfälld](/docs/sv/Images/SpeedDial/speeddial-collapsed.png){align=center}

Ett klick fäller ut alternativen och roterar knappen till ett **×**, som fäller ihop den igen.

![Speed Dial utfälld, med de fem standardalternativen](/docs/sv/Images/SpeedDial/speeddial-expanded.png){align=center}

Varje alternativ är en ikon kopplad till en funktion. Eftersom funktionen skrivs i själva vyn kan samma komponent driva helt olika åtgärder från en vy till nästa: växla en visningsinställning, öppna en popup begränsad till den aktuella vyn eller köra vilket annat projektskript som helst.

Objekten finns i `Speed Dial.klib`. En Speed Dial rymmer högst sju alternativ.

???+ info "Krav"
    Speed Dial har inga egna skriptberoenden. Standardalternativen som beskrivs i
    [De fem standardalternativen](#the-five-standard-options) förutsätter:

    * `scObjectFinder` — fyller tabellen `ObjectList` som begränsar både larm- och historikalternativet
    * `scAlarmFinder` — fyller tabellen `AlarmObjects` som larmalternativet ansluter mot
    * `scLogBook` — för loggboksalternativet
    * `scAlert` — för felloggning i loggboksalternativet
    * Variablerna `dynTouchVisible` och `showNamplates` i Data Store
    * Vyerna `VySpecifikAlarm.kvie` och `VySpecifikHistorik.kvie`

## Lägga till en Speed Dial i en vy { #adding-a-speed-dial-to-a-view }

Dra ett av Speed Dial-objekten från `Speed Dial.klib` till arbetsvyn och placera det där knappen ska sitta. Inget annat konfigureras via egenskaper. Alternativen definieras i ett skript på instansen, vilket beskrivs i [Konfigurera alternativen](#configuring-the-options).

### Välja variant { #choosing-a-variant }

Biblioteket innehåller flera varianter. De skiljer sig endast i vilken riktning alternativen fälls ut och om varje alternativ har en etikett.

| Objekt | Alternativen fälls ut | Etiketter |
|---|---|---|
| `SpeedDial` | Vertikalt, ovanför knappen | Nej |
| `SpeedDialBottom` | Vertikalt, ovanför knappen, platser i omvänd ordning | Nej |
| `SpeedDialVerticalRight` | Horisontellt, bredvid knappen | Nej |
| `SpeedDialVerticalLeft` | Horisontellt, bredvid knappen, platser i omvänd ordning | Nej |
| `SpeedDialCaption` | Vertikalt | Under varje ikon |
| `SpeedDialCaptionBottom` | Vertikalt, platser i omvänd ordning | Under varje ikon |
| `SpeedDialCaptionsRight` | Vertikalt | Till höger om varje ikon |
| `SpeedDialCaptionsRightBottom` | Vertikalt, platser i omvänd ordning | Till höger om varje ikon |

Använd en enkel variant där knappen sitter längs vyns över- eller underkant, och en `Vertical`-variant där den sitter längs en sida.

## Konfigurera alternativen { #configuring-the-options }

En Speed Dial konfigureras helt från instansens **Load**-händelse. Två arrayer tilldelas där:

* `ImageArray` — bildsökvägen för varje alternativ, i ordning.
* `Functions` — funktionen som ska köras när alternativet klickas, i samma ordning.

Objektets egen Load-hanterare läser båda arrayerna och kopplar dem till alternativplatserna, som heter `Op0` till `Op6`:

```javascript title="Speed Dial.klib — SpeedDial onLoad()"
for (var img = 0; img < 7; img++) {
    if (img < this.ImageArray.length) {
        this.SpeedDialOptions["Op" + img].imgPath = this.ImageArray[img]
        this.SpeedDialOptions["Op" + img].onClick = this.Functions[img]
    } else {
        this.SpeedDialOptions["Op" + img].visible = false
    }
}
```

Platser bortom längden på `ImageArray` döljs, så en Speed Dial med tre alternativ visar tre ikoner och inget mer. Det går inte att lägga till ett åttonde alternativ utan att utöka biblioteksobjektet.

!!! warning "Båda arrayerna krävs och måste vara lika långa"
    Loopen styrs av längden på `ImageArray` och indexerar `Functions` med samma räknare. En post som finns i `ImageArray` men saknas i `Functions` ger ett alternativ vars `onClick` är `undefined`, så ikonen visas men gör ingenting.

### Lägga till etiketter { #adding-captions }

Etikettvarianterna tar en tredje array, `Captions`, som innehåller etiketten för varje alternativ i samma ordning:

```javascript title="Arbetsvy — SpeedDialCaption onLoad()"
this.ImageArray = new Array("Images/Material_Icons/Alarm_white.svg",
                            "Images/Material_Icons/logs-white.svg");

this.Captions = new Array("Larm",
                          "Loggbok");

this.Functions = new Array(function () { /* ... */ },
                           function () { /* ... */ });
```

Etikettvarianterna kör samma loop som de enkla varianterna med en extra tilldelning, som sätter `Op{n}.Caption.Caption` från arrayen. Skicka etikettexten genom `Language.translate` om projektet är översatt.

### Bildsökvägar { #image-paths }

En bildsökväg anges relativt projektroten, och filen måste finnas i projektets resurser. Ikonerna som standardalternativen använder ligger i `Images/Material_Icons/`.

Ikoner ritas på Speed Dials egen bakgrund, så en vit ikonvariant är normalt rätt val. Biblioteket levereras med ljusa ikonfiler av just det skälet, till exempel `Alarm_white.svg` och `logs-white.svg`.

## De fem standardalternativen { #the-five-standard-options }

Fem alternativ återkommer i processvyerna i projektet. Tillsammans utgör de standarduppsättningen för Speed Dial: två visningsväxlare och tre vybegränsade popup-fönster. `Reningsverk.kvie` använder exakt denna uppsättning på en `SpeedDialVerticalLeft`, och det är den uppsättning som visas utfälld ovan.

De listas här i arrayordning. På en `SpeedDialVerticalLeft` innebär det att den första posten hamnar närmast knappen och den sista längst bort, så ikonerna läses från höger till vänster på skärmen.

| # | Ikon | Åtgärd |
|---|---|---|
| 1 | `dynTouch-white.svg` | Växla DynTouch-fält |
| 2 | `Alarm_white.svg` | Vyspecifika larm |
| 3 | `chart-line-variant.svg` | Vyspecifik historik |
| 4 | `showNamePlate.svg` | Växla namnskyltar |
| 5 | `logs-white.svg` | Vybegränsad loggbok |

### 1. Växla DynTouch-fält { #toggle-dyntouch-fields }

```javascript
function () { dynTouchVisible = !dynTouchVisible }
```

Växlar variabeln `dynTouchVisible` i Data Store. När den är `true` är de klickbara DynTouch-fälten över processobjekten alltid synliga; när den är `false` visas de endast vid mouse-over. Variabeln sparas, så valet består efter omstart.

Detta ger en operatör möjlighet att se vilka objekt i en vy som är klickbara utan att hovra över vart och ett.

### 2. Vyspecifika larm { #view-specific-alarms }

```javascript
function () {
    this.view.link("Common_Popup/VySpecifikAlarm/VySpecifikAlarm.kvie", true, { linkName: this.view.name })
}
```

Öppnar larmlistan filtrerad till den aktuella vyn. Vyns eget namn skickas som `linkName`, vilket är det som begränsar listan, så samma funktion fungerar oförändrad i varje vy den klistras in i.

Filtreringen görs i databasen och inte av popup-fönstret. `linkName` matchas mot kolumnen `View` i `ObjectList`, och objekten som hittas där ansluts till `AlarmObjects` för att få fram larmen som hör till vyn:

```sql
SELECT ao.AlarmName FROM AlarmObjects ao
JOIN ObjectList ol ON ao.DeviceKey = ol.Object
WHERE ol.View = '<linkName>'
```

!!! note "Detta alternativ är beroende av båda finder-skripten"
    `ObjectList` byggs av `scObjectFinder` och `AlarmObjects` av `scAlarmFinder`. Båda måste ha körts för att larmalternativet ska returnera något. Om någon av tabellerna är tom, eller om vyn inte har indexerats, öppnas popup-fönstret utan larm i stället för att rapportera ett fel.

### 3. Vyspecifik historik { #view-specific-history }

```javascript
function () {
    app.popOut.newData = { linkName: this.view.name };
    app.popOutVisible = true;
    app.popOut.setView("Pop_Outs/VySpecifikHistorik.kvie")
}
```

Öppnar historik för signalerna som hör till den aktuella vyn. Till skillnad från larmalternativet används pop-out-mekanismen i stället för en länk: data sätts först, pop-out görs synlig och vyn laddas in i den.

Begränsningen fungerar på samma sätt som för larm, utifrån en enda uppslagning:

```sql
Select `Object` from ObjectList Where View = '<linkName>'
```

!!! note "Detta alternativ är beroende av `scObjectFinder`"
    Endast `ObjectList` används här, så historikalternativet kräver `scObjectFinder` men inte `scAlarmFinder`. En vy som saknas i `ObjectList` öppnar en tom historik i stället för ett fel.

### 4. Växla namnskyltar { #toggle-nameplates }

```javascript
function () { showNamplates = !showNamplates; }
```

Växlar variabeln `showNamplates` i Data Store, som styr om namnskyltar ritas på processobjekt. Den är påslagen som standard och sparas.

Att stänga av namnskyltar är användbart i täta vyer där etiketterna skymmer processbilden.

!!! note "Variabeln stavas `showNamplates`"
    Variabeln stavas utan det andra `e`:et. Det är namnet som är definierat i Data Store, så det måste skrivas så i skript.

### 5. Vybegränsad loggbok { #view-scoped-logbook }

```javascript
function () {
    try {
        app.logbookSelectedTopic = scLogBook.normalizeTopic(this.view.name);
        app.popOut.setView("Pop_Outs/LogBookControls/GetLogBookEntryByTopic.kvie");
        app.popOutVisible = true;
    } catch (e) { scAlert.toFile("SpeedDial logbook: " + e.message); }
}
```

Öppnar loggboken filtrerad till den aktuella vyns ämne, och nya poster som skapas därifrån tilldelas det ämnet automatiskt. Ämnet hämtas från vyns egen sökväg via `scLogBook.normalizeTopic()`, så poster som skrivs från en Speed Dial grupperas under vyn de kom från. Se [Loggbok — Konfigurering](../modules/logbook/configuring.md#topics) för hur ämnen är strukturerade.

Detta är det enda standardalternativet som skyddar sig självt. Loggboken är beroende av en databasanslutning och av att `scLogBook` är laddat, så ett fel skrivs till larmloggen via `scAlert.toFile()` i stället för att avbryta operatören. Se [Loggbok — Konfigurering](../modules/logbook/configuring.md#view-scoped) för hur vybegränsade loggböcker beter sig.

### Det kompletta exemplet { #the-complete-example }

De fem alternativen som de ser ut i `Reningsverk.kvie`:

```javascript title="Reningsverk.kvie — SpeedDialVerticalLeft onLoad()"
try {

this.ImageArray = new Array("Images/Material_Icons/dynTouch-white.svg",
                            "Images/Material_Icons/Alarm_white.svg",
                            "Images/Material_Icons/chart-line-variant.svg",
                            "Images/Material_Icons/showNamePlate.svg",
                            "Images/Material_Icons/logs-white.svg");

this.Functions = new Array(function () { dynTouchVisible = !dynTouchVisible },
                           function () {
    this.view.link("Common_Popup/VySpecifikAlarm/VySpecifikAlarm.kvie", true, { linkName: this.view.name })
},
                           function () {
    app.popOut.newData = { linkName: this.view.name };
    app.popOutVisible = true;
    app.popOut.setView("Pop_Outs/VySpecifikHistorik.kvie")
},
                           function () { showNamplates = !showNamplates; },
                           function () {
    try {
        app.logbookSelectedTopic = scLogBook.normalizeTopic(this.view.name);
        app.popOut.setView("Pop_Outs/LogBookControls/GetLogBookEntryByTopic.kvie");
        app.popOutVisible = true;
    } catch (e) { scAlert.toFile("SpeedDial logbook: " + e.message); }
})

} catch (e) { alert(e.message) }
```

Varje funktion refererar till vyn via `this.view` i stället för att namnge en vy, så blocket kan kopieras till en ny processvy utan redigering. Att lägga till standarduppsättningen i en vy handlar om att placera objektet och klistra in detta skript i dess Load-händelse.

## Lägga till ett eget alternativ { #adding-a-custom-option }

Ett eget alternativ läggs till genom att utöka båda arrayerna med ett matchande par. För att lägga till ett dokumentalternativ i standarduppsättningen:

```javascript title="Arbetsvy — SpeedDial onLoad() — efter"
this.ImageArray = new Array("Images/Material_Icons/dynTouch-white.svg",
                            "Images/Material_Icons/Alarm_white.svg",
                            "Images/Material_Icons/chart-line-variant.svg",
                            "Images/Material_Icons/showNamePlate.svg",
                            "Images/Material_Icons/logs-white.svg",
                            "Images/Material_Icons/file-document-edit-outline-white.svg");

this.Functions = new Array(function () { dynTouchVisible = !dynTouchVisible },
                           /* ... de fyra standardfunktionerna ... */
                           function () {
    app.popOut.setView("Common_Popup/Documents.kvie");
    app.popOutVisible = true;
});
```

Håll de två arrayerna i linje med varandra. En post som läggs till i den ena men inte i den andra är det vanligaste konfigurationsfelet, och det misslyckas tyst i stället för att ge ett fel.

!!! tip "Skripten körs i objektets kontext"
    Inuti dessa funktioner är `this` alternativobjektet, så den aktuella vyn nås via `this.view`. En funktion som behöver själva Speed Dial kan använda `this.parent`.
<!-- --8<-- [end:body] -->
