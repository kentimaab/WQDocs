---
title: Automatisk skalning
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Automatisk skalning
???+ info "Krav"
    Följande skript krävs för att använda Automatisk skalning och all
    relaterad funktionalitet som täcks i guiderna för Automatisk skalning:
    
    * `scWM`
    * `scAlert`


WideQuick MOD skalar automatiskt användargränssnittet för att passa alla skärmstorlekar eller webbläsarfönster. Det innebär att ett projekt kan köras på olika skärmar utan att layouten behöver ändras.

Skriptet `scWM` hanterar all skalning. Det övervakar huvudfönstret var 500 ms och beräknar en skalningsfaktor baserat på en referensupplösning på 1920×1080. Den aktuella faktorn är alltid tillgänglig som `scWM.scalingFactor`.


## Skalning av huvudvy { #main-view-scaling }

Huvudvyn skalas automatiskt — ingen konfiguration krävs. `scWM` applicerar kontinuerligt rätt zoomnivå när fönstret ändrar storlek. Detta fungerar även på **WideQuick Remote®**-klienter och **WideQuick Web®**-klienter. Webbklienter skalar relativt till webbläsarfönstret snarare än skärmupplösningen.

## Skalning av popup-fönster { #popup-scaling }

Popup-fönster skalas inte automatiskt. För att skala ett popup-fönster proportionellt mot huvudvyn och placera det på skärmen, anropa `scWM.scaleAndPlacePopup()` i popup-arbetsvyns **onLoad**-skript. För att hitta onLoad-skriptet, högerklicka på arbetsvyn i projektträdet i **WideQuick Designer®**, välj **Egenskaper**, öppna fliken **Åtgärd** och dubbelklicka på **load**.

```javascript title="Popup arbetsvy — onLoad"
scWM.scaleAndPlacePopup(this);
```

![Scaled popup centered in the main content area](/Images/Automatic_Scaling/scaling-popup-centered.png){align=center}

Som standard centreras popup-fönstret inom huvudinnehållsområdet, exklusive navigeringsmenyn. Ett valfritt justeringsargument placerar det längs en skärmkant istället:

| Justering | Beskrivning |
|---|---|
| (ingen) | Centrerad på skärmen (standard) |
| `"bottom"` | Förankrad längst ned på skärmen |
| `"top"` | Förankrad längst upp på skärmen |
| `"left"` | Förankrad till vänster på skärmen |
| `"right"` | Förankrad till höger på skärmen |

```javascript title="Popup arbetsvy — onLoad (bottom alignment)"
scWM.scaleAndPlacePopup(this, "bottom");
```

### Aktivera Pannable/Zoomable { #enabling-pannablezoomable }

Skalning av popup-fönster kräver att **Pannable/Zoomable** är aktiverat på popup-arbetsvyn. I **WideQuick Designer®**, högerklicka på arbetsvyn i projektträdet och välj **Egenskaper**. Öppna fliken **Layout** och markera **Pannable/Zoomable**.

![Pannable/Zoomable setting in arbetsvy properties](/Images/Automatic_Scaling/Pannable_zoomable.png){align=center}

## Placering utan skalning { #placement-without-scaling }

För mindre popup-fönster som inte behöver ändra storlek, använd `scWM.placePopup()` för att centrera popup-fönstret utan att skala det:

```javascript title="Popup arbetsvy — onLoad"
scWM.placePopup(this);
```

## Ladda om en vy { #reloading-a-view }

För att tvinga en arbetsvy att återinitialiseras, använd `scWM.reloadPage()`:

```javascript title="Button or script"
scWM.reloadPage("ViewName");
```

Detta växlar kortvarigt till en dummyvy och tillbaka, vilket tvingar målvyn att läsas om. Användbart när en vy behöver återspegla konfigurationsändringar utan att manuellt navigera bort.

## Använda skalningsfaktorn i egna skript { #using-the-scaling-factor-in-custom-scripts }

`scWM.scalingFactor` exponerar den aktuella skalan som ett tal mellan 0 och 1 (eller högre på stora skärmar). Alla egna skript som behöver ta hänsyn till den aktuella zoomnivån kan läsa den direkt:

```javascript title="Custom script"
var factor = scWM.scalingFactor;
var scaledSize = baseSize * factor;
```

Detta används internt av kartskripten för att beräkna om elementpositioner när fönstret ändrar storlek.
<!-- --8<-- [end:body] -->
