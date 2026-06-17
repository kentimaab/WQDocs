---
title: Konfigurera en loggare
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Konfigurera en loggare

En loggare definierar när data ska lagras och var den ska sparas. Loggare
konfigureras i **WideQuick Designer®** och skriver data till en ansluten databas,
som sedan kan användas av vyn **Historik**, **Rapporter** och andra moduler som
förlitar sig på historisk data.

Flera loggare kan dela samma databasanslutning. För att skapa en loggare
högerklickar du på **Loggare** i projektträdet och väljer **Lägg till loggare**.

![Logger settings](/Images/Loggers/logger_settings.png)

## Loggarinställningar

### Loggartyp

Loggartypen avgör vad som utlöser att data lagras.

| Typ | Beskrivning |
|---|---|
| **Cyklisk** | Loggar alla variabler med ett fast tidsintervall. |
| **Ändring** | Loggar varje gång ett variabelvärde ändras. Ändringar köas för att undvika fördröjningar och töms vid det konfigurerade intervallet. |
| **Utlösare** | Loggar alla variabler när det utlöses av ett skript med `Loggers._LoggerName_.trigger()`. |
| **Larm** | Loggar statusändringar för larm. Endast databaslagring. Stöder jokertecken — till exempel loggar `alarmgroup.*` alla larm i en grupp. |
| **Händelse** | Loggar systemhändelser som utlöses av `System.logEvent()`. Endast databaslagring. Kan filtreras efter kontext med `;`-separerade värden. |
| **Användare** | Loggar alla användarsystemhändelser såsom inloggningar och användarändringar. |

!!! note
    När du använder **Ändring** eller **Utlösare** med lagringstypen **Fil** lagras
    värden med 16-bitars precision. Se till att variabelns min- och maxvärden är
    korrekt konfigurerade och att skillnaden mellan dem inte överstiger 65535.

### Lagringstyp

Välj **Databas** eller **Fil** som lagringsmål.

!!! tip
    **Databas** rekommenderas starkt. Fillagring är mindre tillförlitlig, skalar
    dåligt och har reducerad precision vid användning med loggartypen Ändring eller Utlösare.

### Intervall

Anger hur ofta data loggas, konfigurerbart i sekunder och millisekunder. Det
minsta intervallet är `0s 100ms` och det högsta är `3600s`.

### Aktiveringsvariabel

En valfri boolesk signal som aktiverar eller inaktiverar loggaren. När signalen är
`false` pausas loggaren. Användbart för att begränsa loggningen till specifika tidsperioder
eller villkor.

---

## Databasinställningar

![Database settings](/Images/Loggers/database_settings.png)

### Version

Välj version **1** eller **2**. Version **2** rekommenderas eftersom den är mer
lagringseffektiv och använder binär blob-kodning för att minska databasstorleken.

De viktigaste skillnaderna mellan versionerna är:

* **Version 1** kan inte logga variabler av typen `Int64` eller `UInt64`
* **Version 1** skapar två tabeller namngivna efter loggaren, medan **Version 2**
skapar flera automatiskt genererade tabeller beroende på antalet loggade variabler
* **Version 2** lagrar all data i binärt format (databas-blobbar), medan
**Version 1** lagrar data som motsvarande databastyper

!!! note
    För att hämta data från en Version 2-loggare, använd `Logger.data()` istället för
    att fråga databastabellerna direkt.

### Databasanslutning

Väljer vilken databasanslutning den loggade datan lagras i. Flera loggare
kan dela samma databasanslutning.

### Ta bort data äldre än

Tar automatiskt bort loggad data som är äldre än det konfigurerade tröskelvärdet,
angivet i dagar, timmar och minuter. Detta är den rekommenderade metoden för att
hantera databasstorleken över tid.

### Ta bort data när diskutrymmet är lågt

!!! warning
    Det här alternativet rekommenderas inte. Använd **Ta bort data äldre än** för att
    hantera databasstorleken istället.

---

## Variabler

![Variables](/Images/Loggers/variables.png)

Fliken **Variabler** definierar vilka signaler som loggas. Signaler kan läggas till på
två sätt:

* **Bläddra** — öppnar DataStore-webbläsaren för att välja en specifik signal
* **Lägg till** — lägger till en tom rad där ett signalnamn kan anges manuellt

Jokerteckensuffix stöds. Till exempel loggar `*_kWh` alla signaler som slutar på
`_kWh`, vilket gör det enkelt att fånga en grupp relaterade signaler utan att lista var
och en individuellt.

Kolumnen **Hysteresis** är tillgänglig för numeriska signaler och definierar den
minsta värdeförändringen som krävs innan en ny post loggas. Detta är användbart för
att minska brus i loggad data.
<!-- --8<-- [end:body] -->
