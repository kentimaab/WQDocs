---
title: Installera WideQuick
product: wq
page_type: getstarted
status: draft
last_reviewed: 2026-11-24
tags:
 - WQ
---

# Installera WideQuick

**WideQuick®** består av tre delar — **Designer**, **Runtime** och **Remote**
— som alla installeras från samma installationspaket.

**WideQuick® Designer** är utvecklingsmiljön som används för att bygga
användargränssnittet för ett projekt. Den arbetar med kollaborativa arbetsbilder
som innehåller objekt kopplade till variabler i Datalager och skapar dynamiska
effekter. Objekt och arbetsbilder visas statiska i Designer — dynamiken aktiveras
först i Runtime.

**WideQuick® Runtime** är ett fristående program som installeras på målmaskinen
tillsammans med ett projekt skapat i Designer. När det startas presenterar det
arbetsbilder och objekt i användargränssnittet, hanterar Datalager och sköter
kommunikationen med I/O-moduler och OPC-servrar.

**WideQuick® Remote** gör det möjligt för en eller flera användare att ansluta till
samma målsystem från olika stationer, vilket möjliggör en klient/server-miljö.
Med Designer kan även en översiktsbild skapas för att presentera flera målsystem
samtidigt.

Om mer komplexa lösningar behövs — till exempel anpassad styr- och reglationslogik
— kan ett applikationsprogram kombineras med Runtime via **WideQuick® C API**.
Applikationsprogram har samma åtkomst till Datalager-variabler som Runtime och kan
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

!!! tip "Tips"
    För att installera utan dialogrutor, till exempel via skript eller Intune,
    se [Installation från kommandoraden](#installation-fran-kommandoraden).

### Välkommen

![Welcome](/docs/sv/Images/Install/Welcome.png)

Installationsprogrammet öppnas med en välkomstskärm som visar alla steg som
kommer att genomföras under installationen. Klicka på **Next** för att börja.

### Installationskatalog

![Installation Directory](/docs/sv/Images/Install/PathDir.png)

Välj den mapp där **WideQuick®** ska installeras. Standardplatsen är
`C:/Program Files/Kentima AB/WideQuick 14`. Klicka på **...** för att bläddra
till en annan mapp. Klicka på **Next** för att fortsätta.

!!! tip "Tips"
    Standardinstallationsmappen rekommenderas för de flesta installationer.

### Välj komponenter

![Select Components](/docs/sv/Images/Install/Select%20Components.png)

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

**Runtime-maskin** — för att köra ett projekt lokalt på målmaskinen:

* **WideQuick Runtime**
* **WideQuick License Handler**
* **Startup project**

**WideQuick Remote-maskin** — för att köra ett projekt som även kan
nås på distans:

* **WideQuick Runtime**
* **WideQuick Remote**
* **Startup project**
* **Startup Remote project**

### Licensavtal

![License Agreement](/docs/sv/Images/Install/LicenseAgreement.png)

Läs licensavtalet noggrant. Markera **I accept the license** för att godkänna
villkoren. Klicka på **Next** för att fortsätta.

!!! note "Obs"
    Du måste godkänna licensavtalet för att fortsätta med installationen.

### Startmenymapp

![Start Menu Folder](/docs/sv/Images/Install/StartMenuFolder.png)

Välj den Startmenymapp där genvägar till **WideQuick®** ska skapas. Standard är
**WideQuick 14**. En befintlig mapp kan väljas från listan, eller ett nytt namn
kan anges i fältet längst upp. Klicka på **Next** för att fortsätta.

!!! tip "Tips"
    Standardmappens namn rekommenderas för de flesta installationer.

### Produktkod

![Product Code](/docs/sv/Images/Install/ProductCode.png)

Ange produktnyckeln för **WideQuick® Runtime**. Produktnyckeln finns i
orderbekräftelsen som du fått från Kentima.

Produktnyckeln kan lämnas tom och anges senare med verktyget **WideQuick License
Handler** efter att installationen är klar. Klicka på **Next** för att fortsätta.

!!! note "Obs"
    En produktnyckel krävs endast för **WideQuick® Runtime** och
    **WideQuick® Remote**. **WideQuick® Designer** kräver ingen produktnyckel.

### Klar att installera

![Ready to Install](/docs/sv/Images/Install/Ready%20to%20install.png)

All nödvändig information har samlats in. Dialogen visar det totala diskutrymme
som installationen kommer att använda. Klicka på **Install** för att starta
installationen.

### Installerar

![Installing](/docs/sv/Images/Install/Installing.png)

Installationsprogrammet kopierar och packar nu upp alla valda komponenter.
En förloppsindikator visar aktuell status. Klicka på **Show Details** för att
se en detaljerad logg över installationsprocessen.

### Klar

![Finished](/docs/sv/Images/Install/Finish.png)

**WideQuick 14** har installerats. Dialogen bekräftar installationsplatsen.
Klicka på **Finish** för att stänga installationsprogrammet.

**WideQuick® Designer** kan nu startas från Startmenyn under **WideQuick 14**.

!!! tip "Tips"
    Om du hoppade över att ange produktnyckeln under installationen, öppna
    **WideQuick License Handler** från Startmenyn för att ange den nu.

## Installation från kommandoraden

WideQuick® kan installeras helt utan dialogrutor (så kallad *silent install*), till exempel när installationen ska skriptas eller distribueras med Intune, SCCM eller GPO. Installationsprogrammet körs då från kommandoraden, och de val som annars görs i dialogrutorna anges i förväg.

Hur valen anges beror på version:

- **WideQuick 13.4 och tidigare** använder InstallShield. Valen spelas först in i en svarsfil, som sedan spelas upp vid den tysta installationen.
- **WideQuick 14** använder Qt Installer Framework. Valen anges direkt som kommandon och flaggor, och ingen svarsfil behövs.

!!! warning "Kräver administratörsrättigheter"
    Kör installationen från en kommandotolk eller PowerShell som är startad som administratör, eller som SYSTEM i ett distributionsverktyg.

### WideQuick 13.4 och tidigare

I WideQuick 13.4 och tidigare installeras WideQuick-produkterna med InstallShield. En tyst installation görs då i två steg:

1. Installationen görs först manuellt och "spelas in". Valen sparas i en svarsfil (`.iss`).
2. Svarsfilen används sedan för att göra samma installation tyst från kommandotolken på andra datorer.

!!! note "Obs"
    De val som görs under inspelningen gäller även för den tysta installationen. Om till exempel bara Designer installeras under inspelningen, är det bara Designer som installeras när svarsfilen används.

#### Spela in installationen

```
setup.exe /r /f1"C:\Temp\my-answer-file.iss"
```

- Byt ut `setup.exe` mot installationsfilen, till exempel `"WideQuick 13.4.1.exe"`.
- Byt ut `C:\Temp\my-answer-file.iss` mot sökvägen där svarsfilen ska sparas.

Det vanliga grafiska installationsprogrammet startar. Gör de val som ska gälla och slutför installationen.

#### Installera från inspelningen

```
setup.exe /s /f1"C:\Temp\my-answer-file.iss" /f2"C:\Temp\my-install.log"
```

- Byt ut `setup.exe` mot installationsfilen.
- Byt ut `C:\Temp\my-answer-file.iss` mot sökvägen till den inspelade svarsfilen.
- Byt ut `C:\Temp\my-install.log` mot sökvägen där loggfilen ska sparas. `/f2` är valfri, men behövs för att kunna [kontrollera resultatet](#kontrollera-resultatet).

| Flagga | Beskrivning |
|---|---|
| `/r` | Spelar in installationen till en svarsfil. |
| `/s` | Installerar tyst med en svarsfil. |
| `/f1"<sökväg>"` | Sökväg till svarsfilen. |
| `/f2"<sökväg>"` | *(Valfri)* Sökväg till loggfilen för den tysta installationen. |

!!! note "Obs"
    Ange hela sökvägen till filerna och skriv inget mellanslag mellan `/f1` eller `/f2` och citattecknet.

#### Kontrollera resultatet

Resultatet skrivs i loggfilen som anges med `/f2`, under `[ResponseResult]`:

| ResultCode | Betydelse |
|---|---|
| `0` | Installationen lyckades. |
| `-3` | Svarsfilen matchar inte installationsprogrammet, till exempel om den spelades in med en annan version eller i ett annat läge. |

Andra negativa värden betyder att installationen misslyckades.

### WideQuick 14

```
"WideQuick 14.0.3.exe" <kommando> [komponenter ...] [flaggor]
```

- **Kommando** – *vad* som ska göras, till exempel `install`. Anges utan bindestreck och bara ett per körning.
- **Komponenter** – *vilka* delar som ska installeras, till exempel `wqruntime wqdesigner`.
- **Flaggor** – *hur* det ska göras, till exempel `--al`. Börjar alltid med `-` eller `--`.

Ersätt filnamnet med det installationspaket du har laddat ned.

!!! note "Obs"
    I kommandoradsläge visas ingen UAC-dialog. Utan administratörsrättigheter avbryts installationen med felet *Cannot elevate access rights while running from command line*.

#### Snabbstart

Installera standardkomponenterna (Runtime, Designer, Manual, Startup project och License Handler) till standardkatalogen:

```
"WideQuick 14.0.3.exe" install --al --da -c
```

Samma sak, men även med Remote och Startup Remote project:

```
"WideQuick 14.0.3.exe" install startupremote --al --da -c
```

#### Rekommenderade konfigurationer från kommandoraden

Kommandona nedan motsvarar [Rekommenderade konfigurationer](#rekommenderade-konfigurationer) ovan. Med `--nd` installeras bara de komponenter som anges. För en utvecklingsmaskin räcker kommandona under [Snabbstart](#snabbstart).

**Runtime-maskin:**

```
"WideQuick 14.0.3.exe" install startup com.kentima.licensehandler --nd --al --da -c
```

**WideQuick Remote-maskin:**

```
"WideQuick 14.0.3.exe" install startup startupremote --nd --al --da -c
```

#### Flaggor

Både långa och korta namn fungerar, till exempel är `--accept-licenses` samma sak som `--al`. För en helt tyst installation behövs `--al`, `--da` och `-c`.

| Flagga | Kort | Beskrivning |
|---|---|---|
| `--accept-licenses` | `--al` | Godkänner licensavtalet. |
| `--default-answer` | `--da` | Besvarar alla frågor med standardsvaret. |
| `--confirm-command` | `-c` | Startar installationen utan att fråga om bekräftelse. |
| `--no-default-installations` | `--nd` | Installerar bara de komponenter som anges. Se [Vad gör --nd?](#vad-gor-nd) |
| `--root <katalog>` | `-t` | Installerar till en annan katalog än standardkatalogen. Använd citattecken om sökvägen innehåller mellanslag. |
| `--accept-messages` | `--am` | Svarar *Ja/OK* på alla frågor i stället för standardsvaret. |
| `--reject-messages` | `--rm` | Svarar *Nej/Avbryt* på alla frågor. |
| `--auto-answer <id=värde,...>` | `--aa` | Besvarar specifika frågor, till exempel `--aa TargetDirectoryInUse=Ok`. Frågans id står först på raden i utskriften. |
| `--no-size-checking` | `--ns` | Hoppar över kontrollen av ledigt diskutrymme. |
| `--verbose` | `-d` | Utförligare utskrift, användbart vid felsökning. |
| `--help` | `-h` | Visar alla tillgängliga kommandon och flaggor. |

!!! note "Obs"
    Använd bara en av `--da`, `--am` och `--rm`.

##### Vad gör --nd?

Standardkomponenterna (Runtime, Designer, Manual, Startup project och License Handler) är förvalda, precis som de förbockade rutorna i steget [Välj komponenter](#valj-komponenter). Komponenter som anges efter `install` **läggs till** de förvalda. `--nd` bockar ur de förvalda först, så att bara det som anges installeras.

| Kommando | Installerar |
|---|---|
| `install` | Standardkomponenterna |
| `install wqremote` | Standardkomponenterna **och** Remote |
| `install wqremote --nd` | **Endast** Remote |

Komponenter som en vald komponent är beroende av installeras alltid automatiskt, även med `--nd`.

!!! note "Obs"
    WideQuick License Handler kommer inte med automatiskt när `--nd` används. Lägg till `com.kentima.licensehandler` om den behövs.

!!! tip "Tips"
    Använd `--nd` och ange komponenterna uttryckligen i skript. Då påverkas installationen inte om standardurvalet ändras i en framtida version.

#### Komponenter

Komponenter anges efter `install`, separerade med mellanslag. De flesta har ett kort alias. License Handler och C API saknar alias och anges med paketnamn.

| Komponent | Alias | Paketnamn | Standard |
|---|---|---|---|
| WideQuick Runtime | `wqruntime` | `com.kentima.wqruntime` | Ja |
| WideQuick Designer | `wqdesigner` | `com.kentima.wqdesigner` | Ja |
| WideQuick Manual | `wqmanual` | `com.kentima.wqmanual` | Ja |
| Startup project (inkl. Runtime) | `startup` | `com.kentima.startup` | Ja |
| WideQuick License Handler | – | `com.kentima.licensehandler` | Ja |
| WideQuick Remote | `wqremote` | `com.kentima.wqremote` | Nej |
| Startup Remote project (inkl. Remote) | `startupremote` | `com.kentima.startup_remote` | Nej |
| WideQuick LED Driver | `wqleddriver` | `com.kentima.wqleddriver` | Nej |
| WideQuick C API | – | `com.kentima.wqcapi` | Nej |

Lista komponenterna i installationspaketet:

```
"WideQuick 14.0.3.exe" search
"WideQuick 14.0.3.exe" search --type package
```

!!! note "Obs"
    Skriv `search`, inte `install se`. `install se` avbryts med felet *2 commands provided, only one can be used at a time*.

#### Ändra eller avinstallera en befintlig installation

Installationspaketet kan inte installera i en katalog som redan innehåller en installation. Använd i stället underhållsverktyget `maintenancetool.exe` i installationskatalogen. Det tar samma kommandon och flaggor och måste också köras som administratör.

**Lista installerade komponenter:**

```
"C:\Program Files\Kentima AB\WideQuick 14\maintenancetool.exe" list
```

**Lägga till en komponent:**

```
"C:\Program Files\Kentima AB\WideQuick 14\maintenancetool.exe" install wqremote --al --da -c
```

**Ta bort en komponent** (ange paketnamn, inte alias):

```
"C:\Program Files\Kentima AB\WideQuick 14\maintenancetool.exe" remove com.kentima.wqremote -c --da
```

**Avinstallera allt:**

```
"C:\Program Files\Kentima AB\WideQuick 14\maintenancetool.exe" purge -c --da
```

!!! warning "Varning"
    `purge` tar bort hela installationskatalogen, även filer som har skapats efter installationen, till exempel `wqservice.ini`. Säkerhetskopiera sådana filer först.

#### Uppgradera inom samma huvudversion

För att uppgradera till en nyare version inom samma huvudversion, till exempel från 14.0.2 till 14.0.3, måste den gamla versionen avinstalleras först:

1. Säkerhetskopiera egna filer i installationskatalogen, till exempel `wqservice.ini`.
2. Avinstallera den gamla versionen med `maintenancetool.exe purge -c --da`.
3. Installera den nya versionen med önskade komponenter.
4. Lägg tillbaka de säkerhetskopierade filerna.

!!! note "Obs"
    En ny huvudversion, till exempel WideQuick 15, installeras i en egen katalog. Den gamla versionen behöver då inte avinstalleras.

#### Distribution med Intune, SCCM eller GPO

- Installationen fungerar när den körs som SYSTEM. Programmet registreras då för alla användare och genvägarna hamnar i den gemensamma Startmenyn.
- Använd `--nd --al --da -c` och ange komponenterna uttryckligen.
- Runtime-installationen skapar Windows-tjänsten **WideQuick Runtime** med starttypen Manuell.
- Kontrollera returkoden:

    | Returkod | Betydelse |
    |---|---|
    | `0` | Installationen lyckades. |
    | `1` | Fel eller avbruten installation. |
    | `3` | Okänd komponent, till exempel ett felstavat alias. |

Exempel i PowerShell:

```powershell
$p = Start-Process "C:\Install\WideQuick 14.0.3.exe" -ArgumentList 'install startup com.kentima.licensehandler --nd --al --da -c' -Wait -PassThru
$p.ExitCode
```

!!! tip "Tips"
    Vid fel, kör om med `-d` och spara utskriften till en fil, till exempel `> C:\Temp\wq_install.log 2>&1`. Installationen skriver även loggen `InstallationLog.txt` i installationskatalogen.
