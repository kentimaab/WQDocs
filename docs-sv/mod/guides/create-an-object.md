---
title: Skapa objekt
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Skapa objekt

Det finns två sätt att skapa objekt i WideQuick. Det första är att bygga ett
processobjekt visuellt i **WideQuick Designer®** genom att kombinera komponenter,
stödobjekt och ett `DynTouch`-objekt. Det andra är att skapa objekt dynamiskt vid
körning med hjälp av funktionen `createObject()`. Det visuella tillvägagångssättet
passar integratörer som bygger processvyer, medan skriptmetoden lämpar sig bättre för
avancerade användningsfall där antalet objekt inte är känt vid designtillfället.

## Skapa ett processobjekt visuellt

Att skapa ett processobjekt i en **Workview** består av tre steg:

1. Välj en komponent som representerar objektet visuellt
2. Lägg till stödobjekt för att visa taggvärden och status
3. Gruppera allt tillsammans med ett `DynTouch`-objekt

När objektet är byggt kan det sparas i biblioteket och återanvändas i projektet.

!!! tip
    Objekt med prefixet `dyn` — till exempel `dynMotorFanR_000` — innehåller redan
    ett förkonfigurerat `DynTouch`-objekt och animationer. För dessa objekt behöver
    bara egenskaperna **Connection**, **Device**, **Sys** och **ObjectName** på
    `DynTouch`-objektet fyllas i för att koppla dem till sina taggar. Ingen manuell
    gruppering krävs.

### Ikon

Det första steget är att välja en komponent som representerar objektet visuellt i
**WideQuick Designer®**. Vilken komponent som helst från objektbiblioteken kan
användas — valet beror på vad objektet representerar i processvyn.

I det här exemplet används **Centrifugal Pumps 01** från biblioteket **PID Pumps**
under **PI&D**. Dra komponenten till **Workview**. Det är möjligt att kombinera
flera komponenter för att representera mer komplexa objekt — till exempel en pump
med en ventil. Gruppera dem inte ännu.

Alla komponenter som är utformade för att representera fysiska objekt — som pumpar,
fläktar och ventiler — är kompatibla med systemet för
[Workview Animation](./workview-animations.md), vilket innebär att de kan byta färg
för att spegla objektets aktuella tillstånd — aktivt, larm, varning eller under service.

### Stödobjekt

Stödobjekt läggs till bredvid komponenten för att visa ytterligare information om
objektet. I det här exemplet läggs ett `ValueDisplay`-objekt till — det finns i
biblioteket **Digital Value Display** under **Workspace Components**.

När `ValueDisplay` konfigureras, ange `analogOutputValue` i egenskapen **SuffixAlias**.
Detta kopplar visningen till den signal som är mappad till det aliaset. Mer
information om suffixalias och hur de fungerar finns i
[Taggstruktur — Suffix Alias](../reference/tag-structure.md#suffix-alias).

Dra de relevanta stödobjekten från biblioteket till **Workview** och placera dem i
förhållande till komponenten. Gruppera ingenting ännu.

### Färdigställ objektet

Det sista steget är att konvertera komponenten och stödobjekten till ett grupperat
objekt med hjälp av ett `DynTouch`-objekt. `DynTouch`-objektet definierar det
klickbara området och binder samman alla visuella element.

Dra `DynTouch`-objektet från biblioteket till **Workview** och ändra storleken så
att det täcker komponenten och alla stödobjekt helt. Ingenting får hamna utanför
`DynTouch`-objektets gräns — ett element utanför gränsen ingår inte i gruppen och
kan orsaka problem med klickning och val.

När `DynTouch`-objektet är på plats, markera alla element — komponenten,
stödobjekten och `DynTouch`-objektet — och gruppera dem med **Ctrl+G**.

### Koppla objektet till taggar

Efter grupperingen måste objektet kopplas till taggar. Öppna egenskaperna för
`DynTouch`-objektet och fyll i fälten **Connection**, **Device**, **Sys** och
**ObjectName**. Dessa fält avgör vilka taggar objektet och dess stödobjekt läser från.

Mer information om hur taggar är strukturerade och hur suffixsystemet fungerar finns i
[Taggstruktur](../reference/tag-structure.md).

![Creating object](/Images/Create_Object/Create-object.gif)

!!! tip
    För att lära dig hur du bygger ett helt anpassat objekt från grunden och applicerar
    animationer, se exemplet [Workview Animations](./workview-animations.md#example-building-a-custom-animated-motor-object).

## Skapa objekt från skript

**WideQuick Runtime®** gör det möjligt att skapa objekt dynamiskt under körning med
hjälp av funktionen `createObject()`. Detta är användbart när antalet objekt inte är
känt vid designtillfället, eller när det varierar — till exempel för att rendera en
post per datasignal istället för att placera ett fast antal tomma objekt i vyn. Till
skillnad från det visuella tillvägagångssättet kräver den här metoden
skriptkunskaper och lämpar sig bättre för avancerade användningsfall.

`createObject()` finns i listan **Functions** under **WorkView** i
**WideQuick Designer®**, tillsammans med konstanterna `ObjectType*`.

### Syntax

`createObject()` stöder två anropssätt.

**Positionsargument:**

```javascript
view.createObject(type, name, x, y, width, height)
```

**Konfigurationsobjekt:**

```javascript
view.createObject(type, { name, x, y, width, height })
```

Konfigurationsobjektformen accepterar även anpassade egenskaper tillsammans med de
standardiserade:

```javascript
view.createObject(type, { name, x, y, width, height, CustomProperty: value })
```

Alla standardargument är obligatoriska. Anpassade egenskaper i konfigurationsobjektformen
är valfria.

| Argument | Beskrivning |
|---|---|
| `type` | Objekttyp — antingen en `ObjectType*`-konstant eller en sträng som matchar ett bibliotekskomponentnamn |
| `name` | Unikt namn för det skapade objektet inom vyn |
| `x` | Horisontell position i pixlar |
| `y` | Vertikal position i pixlar |
| `width` | Bredd i pixlar |
| `height` | Höjd i pixlar |

### Objekttyper

Inbyggda typkonstanter tillgängliga på vyn:

* `view.ObjectTypeBox`
* `view.ObjectTypeEllipse`
* `view.ObjectTypeImage`
* `view.ObjectTypeInstance`
* `view.ObjectTypeLine`
* `view.ObjectTypePolygon`
* `view.ObjectTypeText`
* `view.ObjectTypeTriangle`

Anpassade bibliotekskomponenter kan också instansieras genom att ange komponentens
sökväg som en sträng: `"/Library/ObjectName"`.

### Egenskaper

Efter skapandet kan egenskaper på det returnerade objektet ställas in direkt:

* `obj.brush.color1` — fyllnadsfärg som ett heltalsvärd för färg
* `obj.pen.width` — kantbredd i pixlar
* `obj.font.color` — textfärg
* `obj.value` — visningsvärde för textobjekt
* `obj.onClick` — klickhanterarfunktion

### Exempel

```javascript title="createObject() — positional and config object forms"
// Positional arguments
var ell = view.createObject(view.ObjectTypeEllipse, "myEllipse", 20, 20, 40, 50);
ell.brush.color1 = colors[0];
ell.pen.width    = 0;

// Config object with custom property
var box = view.createObject(view.ObjectTypeBox, { name: "square", x: 20, y: 20, width: 20, height: 40, CustomColor: "#ff0000" });
box.brush.color1 = colors[1];
```

!!! tip
    Objektnamn måste vara unika inom vyn. Att använda ett konsekvent prefix
    tillsammans med ett index undviker namnkonflikter när `createObject()` anropas
    flera gånger i samma vy.

<!-- --8<-- [end:body] -->
