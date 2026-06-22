---
title: Arbetsvy-animationer
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Arbetsvy-animationer

???+ info "Krav"
    Följande skript krävs för att använda Arbetsvy-animationer:

    * `scWorkviewAnimation`
    * `scAlert`
    * `scSuffix`
    * `scPrototypes`

WideQuick Modular Framework innehåller ett inbyggt animationssystem som visar
statusindikatorer på objekt för att indikera deras aktuella tillstånd — från larm och varningar
till aktiv och manuell styrning. Systemet styrs av taggsuffix, vilket innebär att
färgen ett objekt visar bestäms av vilka signaler som är aktiva på det objektet.

För mer information om taggsuffix, se [Taggstruktur](../reference/tag-structure.md).

![Animationstillstånd](/Images/Workview_Animations/AllActive.gif)

## Hur det fungerar { #how-it-works }

När ett `DynTouch`-objekt placeras på ett objekt i **WideQuick Designer®** anropas
`AnimationHandler()`-funktionen i `scWorkviewAnimation`-skriptet automatiskt.
Detta skapar en hanterare som bevakar alla DataStore-signaler som matchar
objektets taggnamn kombinerat med de konfigurerade suffixen. Hanteraren exponerar ett
booleskt värde för varje kategori — till exempel `animation.alarm` eller `animation.warning`,
där `animation` är referensen till hanteraren — som är `true` när någon signal
i den kategorin är aktiv.

Det här animationstillståndet delas automatiskt med alla underobjekt i gruppen,
så att varje visuellt element kan reagera självständigt på sin tilldelade kategori.

Alla vanliga komponenter i standardobjektbiblioteken levereras med färdigbyggda animerade
objekt som fungerar direkt, och täcker kategorierna larm, varning, aktiv och ManAuto.
Serviceanimation ingår inte i standardobjekten som standard — exemplet i
[Bygga ett eget animerat motorobjekt](#example-building-a-custom-animated-motor-object)
visar hur man lägger till det i ett eget objekt.

För de flesta integratörer räcker det med att konfigurera suffix i driftsättningen. Att skapa
egna animerade objekt beskrivs i
[Skapa egna animerade objekt](#creating-custom-animated-objects).

## Konfigurera kategorier och suffix { #configuring-categories-and-suffixes }

Animationskategorierna och deras suffixalias konfigureras i **WideQuick
Runtime®** genom att navigera till **Inställningar → Suffix → Suffix - Larm**.

![Lista med Arbetsvy-animationer](/Images/Workview_Animations/Workview_animations_list.png)

Inställningarna är organiserade i två nivåer:

* **Grupper** — definierar animationskategorin och dess färg. Fem grupper finns
tillgängliga som standard: **1 - Larm**, **2 - Varningar**, **3 - Service**,
**4 - Aktiv** och **5 - ManAuto**.
* **Suffixalias** — definieras inom varje grupp. Varje alias har ett läsbart
namn, till exempel `Fellarm`, och är kopplat till ett faktiskt taggsuffix, till exempel
`_LF`. När en signal som slutar med det suffixet blir aktiv animeras objektet i
gruppens färg.

Grupper prioriteras efter nummer — lägre nummer har högre prioritet. Om ett objekt
har både ett aktivt larm och en varning ges larmet prioritet eftersom det är grupp 1.

Att välja en grupp visar två inställningspaneler till höger:

**Inställningar för kategori** — konfigurerar gruppens beteende:

* **Referensnamn** — det namn som används i animationsuttryck, till exempel `alarm`
eller `warning`. Används vid byggande av egna animerade objekt, se
[Skapa egna animerade objekt](#creating-custom-animated-objects).
* **Temafärg** — den färg som visas när något suffixalias i gruppen är
aktivt. En färgförhandsvisning visas till höger.
* **Färgreferens (automatisk)** — genereras automatiskt från referensnamnet.
Behöver inte konfigureras manuellt.
* **Vektornamn (automatiskt)** — genereras automatiskt från referensnamnet.
Behöver inte konfigureras manuellt.

Att välja ett suffixalias inom en grupp visar:

**Inställningar för suffix** — konfigurerar det valda suffixaliaset:

* **Suffix** — det faktiska taggsuffixet kopplat till detta alias, till exempel `_LF`
eller `_LG`.
* **Beskrivning** — en läsbar beskrivning av vad suffixet representerar,
till exempel `Fellarm`.

Standardtemafärgerna för varje grupp är:

| Grupp | Temafärg |
|---|---|
| 1 - Larm | `error` |
| 2 - Varningar | `Symbol_Warning` |
| 3 - Service | `Symbol_Service` |
| 4 - Aktiv | `Symbol_Active` |
| 5 - ManAuto | `Symbol_ManAuto` |

Om inga suffixalias i någon grupp är aktiva får objektet färgen
`Symbol_Default`.

### Lägga till suffixalias i en grupp { #adding-suffix-aliases-to-a-group }

För att lägga till ett suffixalias i en grupp, välj gruppen och klicka på **Lägg till nytt suffixalias
i vald kategori**. Ge aliaset ett läsbart namn som `Fellarm`,
ange det faktiska taggsuffixet som `_LF` och lägg till en beskrivning. Klicka
på **Skriv ändringar till DB** för att spara.

Alla objekt med en signal som matchar det konfigurerade suffixet och som aktiveras kommer att
animeras i gruppens färg.

### Lägga till egna grupper { #adding-custom-groups }

Ytterligare grupper kan läggas till utöver de fem standardgrupperna genom att klicka på **Lägg till ny
kategori**. Ge gruppen ett **Referensnamn**, välj en **Temafärg** och lägg till
relevanta suffixalias. Den nya gruppen blir tillgänglig som ett animationstillstånd
på alla objekt som använder `AnimationHandler()`-funktionen i
`scWorkviewAnimation`-skriptet.

!!! note
    **Referensnamnet** för en egen grupp är det du använder i animationsuttryck
    när du bygger egna objekt. Välj ett kort namn med gemener
    utan mellanslag, till exempel `pressure` eller `fault`.

## Skapa egna animerade objekt { #creating-custom-animated-objects }

För integratörer som vill bygga egna animerade objekt förklaras nedan
hur man kopplar ett underobjekt till en animationskategori.

Varje underobjekt som ska reagera på en animationskategori behöver tre saker:

**onLoad-skript** — sparar objektets ursprungliga färger så att de kan återställas när
ingen kategori är aktiv:

```javascript title="Underobjekt — onLoad"
this.defaultColor = System.themes.color("background");
this.defaultpColor = this.pen.color;
```

**Synlighetsuttryck** — visar objektet bara när kategorin är aktiv:

```javascript title="Underobjekt — synlighet"
this.animation.alarm
```

**Färguttryck** — ställer in färgen baserat på den aktiva kategorin, och återgår till
standardfärgen när den är inaktiv:

```javascript title="Underobjekt — färg"
if (this.animation.alarm) {
    return scWorkviewAnimation.alarmColor;
} else {
    return this.defaultColor
}
```

Ersätt `alarm` med det relevanta kategorinamnet. De tillgängliga kategorinamnen är:

| Kategori | Namn |
|---|---|
| Larm | `alarm` |
| Varningar | `warning` |
| Service | `service` |
| Aktiv | `active` |
| ManAuto | `manauto` |

!!! note
    Egna kategorier som lagts till i driftsättningen är också tillgängliga här. Använd kategorinamnet
    som det definierades i **Inställningar → Suffix → Suffix - Larm**.

!!! tip
    Det enklaste sättet att skapa ett eget animerat objekt är att kopiera ett befintligt
    animerat objekt från standardobjektbiblioteken och anpassa det. Det säkerställer
    att alla uttryck och skript redan finns på plats.

## Exempel - Bygga ett eget animerat motorobjekt { #example-building-a-custom-animated-motor-object }

Det här exemplet visar hur man bygger ett enkelt eget motorobjekt som reagerar på
fyra animationskategorier — larm, varning, service och aktiv. Det visar också
hur man lägger till serviceanimation, som inte ingår i standardobjektbiblioteken
som standard.

### Steg 1 - Verifiera suffixkonfigurationen { #step-1-verify-the-suffix-configuration }

Innan du bygger objektet, kontrollera att alla fyra animationskategorier som används i det här
exemplet är konfigurerade i **Inställningar → Suffix → Suffix - Larm**. Kategorierna 1, 2
och 4 bör redan vara konfigurerade som standard — expandera varje och bekräfta att suffixalias kopplade till de relevanta suffixen finns
under **suffix**:

* **1 - Larm** — bör innehålla suffixalias kopplade till larmsuffix som `_LD` eller `_LG`
* **2 - Varningar** — bör innehålla suffixalias kopplade till varningssuffix som `_LM`
* **4 - Aktiv** — bör innehålla suffixalias kopplade till aktivsuffix som `_IT`

Kategori 3 kräver manuell konfiguration eftersom suffixet `_SERVICE` inte ingår som
standard. Expandera **3 - Service** och kontrollera om `_SERVICE` visas under
**suffix**. Om det inte finns där, klicka på **Lägg till nytt suffixalias i vald kategori**,
ange `_SERVICE` som suffix och ge det en beskrivning som passar dina behov.

![Servicesuffix](/Images/Workview_Animations/Service_suffix.png)

### Steg 2 - Skapa de visuella elementen { #step-2-create-the-visual-elements }

I **WideQuick Designer®**, skapa följande objekt:

* En **cirkel** — den blinkar i larm-, varnings- eller servicefärgen när någon
av dessa kategorier är aktiv.
* En **triangel** — dess kontur ändrar färg när kategorin aktiv är aktiv.
* Ett `DynTouch`-objekt — detta kopplar animationen till taggen.

![Skapa objekt](/Images/Workview_Animations/Create_object.png)

### Steg 3 - Lägg till onLoad-skripten { #step-3-add-the-onload-scripts }

Lägg till följande onLoad-skript på cirkeln:

```javascript title="Cirkel — onLoad"
this.defaultColor = System.themes.color("background");
```

Lägg till följande onLoad-skript på triangeln:

```javascript title="Triangel — onLoad"
this.brush.color1 = System.themes.color("background");
this.defaultpColor = this.pen.color;
```

Dessa skript sparar de ursprungliga färgerna för varje objekt så att de kan återställas när
ingen animationskategori är aktiv.

![onLoad-skript](/Images/Workview_Animations/LoadScripts.gif)

!!! note
    Eftersom triangelns **penselgfärg** inte styrs av något animationsuttryck
    ställs den in till temats bakgrundsfärg vid inläsning. Det säkerställer att fyllningen följer
    det aktiva temat istället för att vara hårdkodad till en specifik färg.

### Steg 4 - Lägg till färguttrycken { #step-4-add-the-color-expressions }

**Cirkel — penselgfärg:**

Lägg till följande uttryck i **penselgfärg**-dynamiken på cirkeln. Cirkeln
blinkar i den färg som hör till den aktiva kategorin med högst prioritet:

```javascript title="Cirkel — penselgfärg"
if (this.animation.alarm && _sys_pulse_1_Hz) {
    return scWorkviewAnimation.alarmColor;
} else if (this.animation.warning && _sys_pulse_1_Hz) {
    return scWorkviewAnimation.warningColor;
} else if (this.animation.service && _sys_pulse_1_Hz) {
    return scWorkviewAnimation.serviceColor;
} else {
    return this.defaultColor
}
```

GIF:en nedan visar var detta uttryck ska läggas till:

![Penselgfärg-dynamik för cirkel](/Images/Workview_Animations/DynCircel.gif)

**Triangel — pennfärg:**

Lägg till följande uttryck i **pennfärg**-dynamiken på triangeln. Triangelns
kontur ändrar färg när kategorin aktiv är aktiv:

```javascript title="Triangel — pennfärg"
if (this.animation.active) {
    return scWorkviewAnimation.activeColor;
} else {
    return this.defaultpColor
}
```

GIF:en nedan visar var detta uttryck ska läggas till:

![Pennfärg-dynamik för triangel](/Images/Workview_Animations/DynTriangel.gif)

### Steg 5 - Gruppera objekten { #step-5-group-the-objects }

Konfigurera `DynTouch`-objektets egenskaper innan grupperingen för att koppla det till
rätt tagg. Under fliken **Egenskaper**, ange följande:

* **Connection** — anslutningsnamnet, till exempel `MB`
* **Device** — enhetsnamnet, till exempel `AS01`
* **Sys** — systemnamnet, till exempel `VS10`
* **ObjectName** — objektnamnet, till exempel `PV01`

Dessa fyra egenskaper kombineras till taggnamnet `MB.AS01_VS10_PV01`, som `AnimationHandler()`-funktionen i `scWorkviewAnimation`-skriptet använder
för att hitta alla signaler som matchar de konfigurerade suffixen.

När egenskaperna är ifyllda, markera cirkeln, triangeln och `DynTouch`-objektet
och tryck **Ctrl+G** för att gruppera dem. Animationstillståndet delas automatiskt
med alla underobjekt i gruppen.

!!! note
    Egenskaperna **Connection**, **Device** och **Sys** kan också ställas in på
    **Arbetsvy**-egenskaperna istället för på varje `DynTouch`-objekt individuellt. Se
    [Taggstruktur](../reference/tag-structure.md) för mer information.

### Steg 6 - Testa i driftsättning { #step-6-test-in-runtime }

Starta projektet och kontrollera att:

* Cirkeln blinkar rött när en signal som slutar med ett larmsuffix är aktiv.
* Cirkeln blinkar gult när en signal som slutar med ett varningssuffix är aktiv.
* Cirkeln blinkar lila när en signal som slutar med `_SERVICE` är aktiv.
* Triangelns kontur ändras till aktivfärgen när en signal som slutar med ett
aktivsuffix är aktiv.

![Demonstration](/Images/Workview_Animations/Demonstration.gif)

!!! tip
    För att testa utan en PLC ansluten, högerklicka på objektet i **WideQuick Runtime®**
    för att öppna felsökningspopupen. Härifrån kan DataStore-variablerna växlas mellan
    `true` och `false` för att verifiera att animationerna fungerar som förväntat.

<!-- --8<-- [end:body] -->
