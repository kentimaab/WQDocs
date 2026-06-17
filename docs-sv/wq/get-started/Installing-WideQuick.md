---
title: Installera WideQuick
product: wq
page_type: getstarted
status: draft
last_reviewed: 2026-06-16
tags:
 - WQ
---

# Installera WideQuick

**WideQuick®** består av tre delar — **Designer**, **Runtime** och **Remote**
— som alla installeras från samma installationspaket.

**WideQuick® Designer** är utvecklingsmiljön som används för att bygga
användargränssnittet för ett projekt. Den arbetar med kollaborativa arbetsbilder
som innehåller objekt kopplade till variabler i DataStore och skapar dynamiska
effekter. Objekt och arbetsbilder visas statiska i Designer — dynamiken aktiveras
först i Runtime.

**WideQuick® Runtime** är ett fristående program som installeras på målmaskinen
tillsammans med ett projekt skapat i Designer. När det startas presenterar det
arbetsbilder och objekt i användargränssnittet, hanterar DataStore och sköter
kommunikationen med I/O-moduler och OPC-servrar.

**WideQuick® Remote** gör det möjligt för en eller flera användare att ansluta till
samma målsystem från olika stationer, vilket möjliggör en klient/server-miljö.
Med Designer kan även en översiktsbild skapas för att presentera flera målsystem
samtidigt.

Om mer komplexa lösningar behövs — till exempel anpassad styr- och reglationslogik
— kan ett applikationsprogram kombineras med Runtime via **WideQuick® C API**.
Applikationsprogram har samma åtkomst till DataStore-variabler som Runtime och kan
användas för att skapa skräddarsydd processkontroll. C API:et ingår inte i
standardpaketet.

Installationspaketet kan laddas ned från
<a href="https://www.kentima.com" target="_blank">kentima.com</a>.

## Systemkrav

För att använda **WideQuick® Designer**, **Runtime** eller **Remote** krävs
följande minimala hårdvara:

* En x86-64-processor (Intel 64/AMD64)
* 4 096 MB RAM
* 1 024 MB ledigt diskutrymme

**WideQuick®**-produkterna stöds på följande operativsystem:

* Windows 10 (1809, 64-bit)
* Windows 11 (64-bit)
* Windows Server 2019 eller senare (64-bit)
* Debian GNU/Linux 11.0 (64-bit)

## Installationsprocedur

Kör installationsfilen på den dator där du vill installera **WideQuick®**.
Installationsprogrammet guidar dig genom följande steg.

### Välkommen

![Welcome](/Images/Install/Welcome.png)

Installationsprogrammet öppnas med en välkomstskärm som visar alla steg som
kommer att genomföras under installationen. Klicka på **Next** för att börja.

### Installationskatalog

![Installation Directory](/Images/Install/PathDir.png)

Välj den mapp där **WideQuick®** ska installeras. Standardplatsen är
`C:/Program Files/Kentima AB/WideQuick 14`. Klicka på **...** för att bläddra
till en annan mapp. Klicka på **Next** för att fortsätta.

!!! tip "Tips"
    Standardinstallationsmappen rekommenderas för de flesta installationer.

### Välj komponenter

![Select Components](/Images/Install/Select%20Components.png)

Välj vilka komponenter som ska installeras. Längst ned i dialogen visas det
diskutrymme som krävs för de valda komponenterna. Håll muspekaren över en
komponent för att se en beskrivning i panelen **Details** till höger.

Tillgängliga komponenter är:

| Komponent | Beskrivning |
|---|---|
| **Startup Remote project** | En körbar fil som möjliggör fjärråtkomst till en Runtime-instans. Kräver att **WideQuick Remote** också är installerat. |
| **Startup project** | Ett minimalt WideQuick-projekt placerat i installationsmappen. Används som bas vid överföring av projekt till målmaskinen. |
| **WideQuick C API** | API för integrering av WideQuick med C-baserade applikationer, vilket möjliggör anpassad styr- och reglationslogik tillsammans med Runtime. |
| **WideQuick Designer** | Utvecklingsmiljön för att bygga och konfigurera WideQuick-projekt. Kräver ingen produktkod. |
| **WideQuick LED Driver** | Drivrutin för integration med LED-hårdvara. |
| **WideQuick License Handler** | Verktyg för att visa licensinformation och uppgradera licenser. |
| **WideQuick Manual** | Den inbyggda hjälpmanualen, tillgänglig i **WideQuick® Designer** genom att trycka på **F1**. |
| **WideQuick Remote** | Ansluter till en körande Runtime-instans från en annan maskin och möjliggör en klient/server-miljö. |
| **WideQuick Runtime** | Kör ett WideQuick-projekt på målmaskinen. |

#### Rekommenderade konfigurationer

**Utvecklingsmaskin** — för att bygga och testkör projekt på samma maskin:

* **WideQuick Designer**
* **WideQuick Runtime**
* **WideQuick Manual**
* **WideQuick License Handler**

**Runtime-maskin** — för att köra ett projekt lokalt på målmaskinen:

* **WideQuick Runtime**
* **WideQuick License Handler**
* **Startup project**

**Fjärrtillgänglig Runtime-maskin** — för att köra ett projekt som även kan
nås på distans:

* **WideQuick Runtime**
* **WideQuick Remote**
* **Startup project**
* **Startup Remote project**
* **WideQuick License Handler**

### Licensavtal

![License Agreement](/Images/Install/LicenseAgreement.png)

Läs licensavtalet noggrant. Markera **I accept the license** för att godkänna
villkoren. Klicka på **Next** för att fortsätta.

!!! note "Obs"
    Du måste godkänna licensavtalet för att fortsätta med installationen.

### Startmenymapp

![Start Menu Folder](/Images/Install/StartMenuFolder.png)

Välj den Startmenymapp där genvägar till **WideQuick®** ska skapas. Standard är
**WideQuick 14**. En befintlig mapp kan väljas från listan, eller ett nytt namn
kan anges i fältet längst upp. Klicka på **Next** för att fortsätta.

!!! tip "Tips"
    Standardmappens namn rekommenderas för de flesta installationer.

### Produktkod

![Product Code](/Images/Install/ProductCode.png)

Ange produktnyckeln för **WideQuick® Runtime**. Produktnyckeln finns i
orderbekräftelsen som du fått från Kentima.

Produktnyckeln kan lämnas tom och anges senare med verktyget **WideQuick License
Handler** efter att installationen är klar. Klicka på **Next** för att fortsätta.

!!! note "Obs"
    En produktnyckel krävs endast för **WideQuick® Runtime** och
    **WideQuick® Remote**. **WideQuick® Designer** kräver ingen produktnyckel.

### Klar att installera

![Ready to Install](/Images/Install/Ready%20to%20install.png)

All nödvändig information har samlats in. Dialogen visar det totala diskutrymme
som installationen kommer att använda. Klicka på **Install** för att starta
installationen.

### Installerar

![Installing](/Images/Install/Installing.png)

Installationsprogrammet kopierar och packar nu upp alla valda komponenter.
En förloppsindikator visar aktuell status. Klicka på **Show Details** för att
se en detaljerad logg över installationsprocessen.

### Klar

![Finished](/Images/Install/Finish.png)

**WideQuick 14** har installerats. Dialogen bekräftar installationsplatsen.
Klicka på **Finish** för att stänga installationsprogrammet.

**WideQuick® Designer** kan nu startas från Startmenyn under **WideQuick 14**.

!!! tip "Tips"
    Om du hoppade över att ange produktnyckeln under installationen, öppna
    **WideQuick License Handler** från Startmenyn för att ange den nu.
