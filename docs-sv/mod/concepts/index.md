---
title: Koncept
product: mod
page_type: overview
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# WideQuick Modulärt Ramverk

Varje HMI- och SCADA-projekt ställer samma frågor:

- Hur hanterar du larm?
- Hur fungerar navigeringen? Var finns historiken?
- Hur loggar operatörer sina åtgärder?

Svaren förändras sällan, men de flesta integratörer bygger om dem från grunden, projekt efter projekt.

WideQuick MOD är Kentimas svar på det problemet.

Sedan början av 2000-talet har Kentima byggt motorn bakom kraftfulla HMI- och SCADA-system inom flera branscher: fastighetsautomation, vatten- och avloppsrening, process och batch. I WideQuick MOD extraherade Kentima det som är universellt och gjorde det återanvändbart. Resultatet är en strukturerad projektgrund som levereras med produktionsfärdiga moduler för de funktioner varje system behöver, samtidigt som den förblir helt öppen för systemintegratörer att konfigurera, utöka och anpassa efter varje kundkrav.

Ramverket begränsar inte vad du bygger. Det eliminerar arbetet du aldrig borde ha behövt göra två gånger.

## En modulär arkitektur { #architecture }

WideQuick MOD är byggt på en enda idé: varje funktion är en oberoende modul som du bara inkluderar om du behöver den. Kärnapplikationen tillhandahåller körningsmiljön, navigeringen, användarhanteringen och datalagret. Allt annat är valfritt och additativt.

Diagrammet nedan visar hur hela stacken passar ihop: från WideQuick HMI/SCADA-plattformen i botten, genom WideQuick MOD och dess modulbibliotek, upp till konceptapplikationerna som byggs ovanpå.

<div class="arch-wrap" style="margin: 1.5rem 0;">

  <div class="arch-tier">
    <div class="arch-tier__label arch-tier__label--concepts">
      <span>Concepts &amp; Applications</span>
    </div>
    <div class="arch-tier__rows">
      <div class="arch-row">
        <div class="arch-sublabel-col"><span>Concepts</span></div>
        <div class="arch-indent arch-indent--lg"></div>
        <a href="../../bms/" class="arch-concept arch-concept--bms">
          <small>WideQuick</small>
          <strong>BMS</strong>
          <span>Building Management System</span>
        </a>
        <a href="../../wwt/" class="arch-concept arch-concept--wwt">
          <small>WideQuick</small>
          <strong>WWT</strong>
          <span>Water &amp; Wastewater Treatment</span>
        </a>
      </div>
    </div>
  </div>

  <div class="arch-tier">
    <div class="arch-tier__label arch-tier__label--framework">
      <span>Framework &amp; Solutions</span>
    </div>
    <div class="arch-tier__rows">
      <div class="arch-row">
        <div class="arch-sublabel-col"><span>Framework</span></div>
        <div class="arch-indent arch-indent--sm"></div>
        <a href="../" class="arch-concept arch-concept--mod">
          <small>WideQuick</small>
          <strong>MOD</strong>
          <span>Modular Framework</span>
        </a>
      </div>
      <div class="arch-row">
        <div class="arch-sublabel-col"><span>Modules</span></div>
        <div class="arch-indent arch-indent--sm"></div>
        <div class="arch-content arch-content--solutions">
          <div class="arch-mini-chips">
            <span>Alarms</span><span>Maintenance</span><span>Alarm Sending</span><span>Navigation</span><span>Popups</span><span>Reports</span><span>Dashboards</span><span>History</span><span>Calendar</span><span>Maps</span><span>Documents</span><span>Logbook</span><span>Graphical Symbols</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="arch-tier">
    <div class="arch-tier__label arch-tier__label--software">
      <strong>WideQuick</strong>
      <span>HMI / SCADA</span>
    </div>
    <div class="arch-tier__rows">
      <div class="arch-row">
        <div class="arch-sublabel-col arch-sublabel-col--light"><span>Core</span></div>
        <div class="arch-content arch-content--core">
          <div class="arch-mini-chips">
            <span>Arbetsvyer</span><span>Graphical Objects</span><span>Interactive Objects</span><span>Dynamics</span><span>Alarms</span><span>History</span><span>Events</span><span>Users</span><span>Themes</span><span>Language</span><span>Data Store</span>
          </div>
        </div>
      </div>
      <div class="arch-row">
        <div class="arch-sublabel-col arch-sublabel-col--light"><span>Communication</span></div>
        <div class="arch-content arch-content--comms">
          <div class="arch-mini-chips">
            <span>OPC UA</span><span>OPC DA</span><span>Modbus</span><span>BACnet</span><span>MQTT</span><span>Database connectors</span><span>C API</span><span>.NET Plugin</span>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>

Börja nerifrån. **WideQuick HMI/SCADA** är plattformslagret: körningsmiljön, den grafiska motorn, kommunikationsprotokoll och kärnfunktioner som larm, historik och användarhantering. Det är det som alla WideQuick-projekt körs på.

Ett lager upp sitter WideQuick MOD. Det lägger till en strukturerad projektmodell ovanpå WideQuick och ett bibliotek av färdigbyggda moduler: larm, underhåll, dashboards, historik, navigering och mer. Integratörer väljer vad projektet behöver och lämnar bort resten.

Längst upp finns **konceptapplikationerna**, BMS och WWT. Dessa är inte separata produkter. De är förkonfigurerade implementationer av WideQuick MOD, byggda för en specifik bransch, med ett bestämt modulurval och en projektstruktur som redan finns på plats.

**Det översta lagret är valfritt.** Många projekt körs direkt på WideQuick MOD utan att någonsin använda BMS eller WWT. Om din bransch, kund eller projektomfattning inte passar en konceptapplikation, bygg direkt på MOD och sätt ihop exakt de moduler du behöver.

**Du levererar bara vad projektet behöver.** En enkel processöversikt bär ingen vikt av rapportmotorer, underhållsschemaläggare eller konfiguration för larmsändning. En komplex installation med flera anläggningar kan dra in alla tillgängliga moduler utan några strukturella ändringar i projektet.

**Omfattningen är ett medvetet val.** Inte ett resultat av vad som råkade ingå i en startmall.

## Många branscher, ett ramverk { #many-industries }

Samma ramverk används inom fundamentalt olika tillämpningsområden. Fastighetsautomationssystem spårar HVAC, passerkontroll och energi. Vatten- och avloppsanläggningar övervakar reningsprocesser, pumpstationer och larm. Applikationer för batch- och processindustri hanterar recept, produktionsloggning och operatörsarbetsflöden.

Det dessa har gemensamt är att de alla är byggda på samma WideQuick MOD-grund, med samma **WideQuick Designer®**-verktygskedja, samma modulbibliotek och samma driftsättningsmodell. Den domänspecifika logiken finns i konfigurationen och modulvalet, inte i en annan produkt.

Detta är viktigt för integratörer som arbetar inom flera branscher: kunskapen, verktygen och projektstrukturen överförs direkt från ett vertikalt segment till nästa.

## Konceptapplikationer { #concept-applications }

Building Management System (BMS) och Water & Wastewater Treatment (WWT) är konceptapplikationer: kompletta, förstrukturerade implementationer av WideQuick MOD riktade mot specifika branscher. De levereras med ett bestämt modulurval, navigeringsstruktur och systemvyer som speglar de typiska kraven inom det aktuella området.

De är startpunkter, inte begränsningar. En integratör kan ta en konceptapplikation som den är, utöka den med ytterligare moduler, eller använda den som referens när man bygger ett anpassat projekt från basramverket.

Många framgångsrika driftsättningar använder aldrig en konceptapplikation alls. Batch-produktion, livsmedels- och dryckesindustri samt allmänna processindustriprojekt körs rutinmässigt direkt på WideQuick MOD med ett anpassat modulurval som passar projektet exakt.

## Moduloberoende { #module-independence }

Varje modul i ramverket är oberoende. Det finns inga dolda beroenden mellan exempelvis Kalendermodulen och Larmmodulen. Var och en kan inkluderas eller exkluderas utan att påverka de andra.

För en systemintegratör innebär detta att den levererade applikationen kan avgränsas exakt till vad slutkunden behöver. En mindre installation kan köras med Larm, Historik och en dashboard. En större lägger till Underhållsschemaläggning, Rapporter och Kartor. Inget av projekten kräver tillfälliga lösningar eller stub-implementationer för de funktioner som lämnades bort.

Det praktiska arbetsflödet är att börja från mallapplikationen, inkludera de relevanta modulerna och ta bort resten. Det som återstår är en ren, ändamålsenlig applikation utan döda vyer eller oanvänd konfiguration.

<!-- --8<-- [end:body] -->
