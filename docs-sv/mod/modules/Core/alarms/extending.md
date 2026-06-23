---
title: Larm — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Larm — Utöka

## E-postnotifieringar { #email-notifications }

För att skicka larmnotifieringar via e-post måste en SMTP-server konfigureras. Det kan göras i **WideQuick Designer®** före driftsättning eller i **WideQuick Runtime®** på ett körande system.

### Konfigurera SMTP i WideQuick Designer® { #configuring-smtp-in-widequick-designer }

1. I projektträdet, högerklicka på noden **Mail** och välj **Egenskaper...**.
2. Ange serveruppgifterna.

![Mail properties dialog](/docs/sv/Images/Alarm_Sender/Mail_properties.png){align=center}

### Konfigurera SMTP vid körning { #configuring-smtp-at-runtime }

Klicka på **Konfigurera** i SMTP-sektionen i statuspanelen **Larm — Schema**, eller anropa `System.mailManager.edit()` från ett skript eller en knappåtgärd.

![Edit mail settings](/docs/sv/Images/Alarms/alarm-smtp-settings.png){align=center}

| Fält | Beskrivning |
|---|---|
| **Avsändare** | Avsändarens e-postadress |
| **Avsändarnamn** | Visningsnamn för avsändaren |
| **Server** | SMTP-serveradress eller IP — till exempel `smtp.gmail.com` |
| **Port** | Serverport |
| **Domän** | Serverdomän |
| **Användare** | Kontots användarnamn |
| **Lösenord** | Kontots lösenord |

### E-postalias { #email-aliases }

Aliassystemet kopplar ett kort nyckelord till en eller flera e-postadresser. Alias kan
väljas när mottagare läggs till i ett notifieringsschema, vilket gör det enklare att hantera
mottagargrupper centralt.

Alias hanteras i dialogen **Redigera e-postinställningar** tillsammans med SMTP-
konfigurationen.

### Anpassa e-post

E-postnotifieringen byggs upp som ett rent textmeddelande. Layouten och innehållet kan
anpassas genom att redigera funktionen `writeMail()` i skriptet `scAlarmSender`.

Standardformatet för e-post ser ut så här:

```
---------------------------------------------------------------------------
| Schedule: My Schedule
| Subject: My Subject
---------------------------------------------------------------------------
| ------------------------------------------------------------------------
| | Name: AS01.VS10_PV01_IO
| |
| | Timestamp: 2026-05-29 12:00:00
| |
| | Alarm class: 1
| |
| | Description: My alarm description
| ------------------------------------------------------------------------
|
---------------------------------------------------------------------------
```

Varje rad i e-posten byggs upp genom att text läggs till en meddelandevariabel med `+=`.
Det innebär att integratören kan ändra etiketter, lägga till nya rader med ren text eller
ta bort rader som inte behövs. För att till exempel ändra etiketten **Larmklass** till
**Prioritet**, lokalisera följande rad i funktionen `writeMail()`:

```javascript title="writeMail() function in scAlarmSender script — before"
msg += "| | Larmklass: " + alarm.severity + "\n"
```

Och ändra den till:

```javascript title="writeMail() function in scAlarmSender script — after"
msg += "| | Priority: " + alarm.severity + "\n"
```

De fyra tillgängliga larmfälten som kan inkluderas i meddelandet är:

| Fält | Beskrivning |
|---|---|
| `alarm.name` | Larmets namn |
| `alarm.timestamp` | Datum och tid då larmet utlöstes |
| `alarm.severity` | Larmklass |
| `alarm.text` | Larmbeskrivning |

Ren text kan också läggas till fritt var som helst i meddelandet. För att till exempel lägga till
en sidfot, lägg till följande rad före den avslutande avgränsaren:

```javascript title="writeMail() function in scAlarmSender script"
msg += "| Sent from WideQuick BMS\n"
```

---

## SMS-notifieringar { #sms-notifications }

SMS-notifieringar skickas via ett modem anslutet till WideQuick-värden via en seriell
COM-port. Det kan vara ett traditionellt GSM-modem eller en 4G-router — vilken enhet som
helst som accepterar AT-kommandon via en seriekoppling är kompatibel.

### Konfigurera modemet { #configuring-the-modem }

Modemet konfigureras i **WideQuick Runtime®**. Navigera till
**Inställningar → GSM-inställningar** för att öppna konfigurationsdialogen.

![GSM modem settings](/docs/sv/Images/Alarms/alarm-gsm-settings.png){align=center}

Ange anslutningsparametrarna från enhetens datablad:

| Fält | Beskrivning |
|---|---|
| **Com port** | Seriell port som modemet är anslutet till |
| **Baudrate** | Kommunikationshastighet |
| **Databitar** | Antal databitar |
| **Stoppbitar** | Antal stoppbitar |
| **Paritet** | Paritetsinställning |
| **Flödeskontroll** | Flödeskontrollmetod |
| **Pin** | SIM-kortets PIN, om det krävs |

Aktivera **GSM Modem Active** och klicka på **Spara**. Om konfigurationen är korrekt
lyser indikatorn grönt.

!!! note "Krav"
    SMS-notifieringar kräver att `scModem` körs utöver `scAlarmSender`.

### Anpassa SMS

SMS-notifieringen följer samma mönster som e-posten och kan anpassas genom att
redigera funktionen `writeSMS()` i skriptet `scAlarmSender`. Samma fyra larmfält är
tillgängliga — `alarm.name`, `alarm.timestamp`, `alarm.severity` och
`alarm.text` — och etiketter kan ändras eller ren text läggas till på samma sätt.

Standardformatet för SMS ser ut så här:

```
Schedule: My Schedule
Subject: My Subject
Name: AS01.VS10_PV01_IO
Timestamp: 2026-05-29 12:00:00
Alarm class: 1
Description: My alarm description
```

För att till exempel ändra etiketten **Namn** till **Signal**, lokalisera följande rad
i funktionen `writeSMS()`:

```javascript title="writeSMS() function in scAlarmSender script — before"
msg += "Namn: " + alarm.name + "\n"
```

Och ändra den till:

```javascript title="writeSMS() function in scAlarmSender script — after"
msg += "Signal: " + alarm.name + "\n"
```

!!! note
    Håll SMS-meddelanden korta. De flesta GSM-modem har en teckengräns per meddelande,
    och långa meddelanden kan delas upp i flera delar eller trunkeras.

---

## Fjärrlarmsammanställning { #remote-alarm-aggregation }

Larm från anslutna fjärrsystem kan sammanställas i den lokala larmlistan. Se
[Fjärrsystem — Fjärrlarm](/mod/guides/remote-systems/#remote-alarms) för
installationsanvisningar.
<!-- --8<-- [end:body] -->
