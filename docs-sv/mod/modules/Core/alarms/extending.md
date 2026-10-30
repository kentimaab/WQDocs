---
title: Larm — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-12
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Larm — Utöka

## E-postnotifieringar { #email-notifications }

För att skicka larmnotifieringar via e-post måste en SMTP-server konfigureras. Det kan göras i **WideQuick® Designer** före driftsättning eller i **WideQuick® Runtime** på ett körande system.

### Konfigurera SMTP i WideQuick® Designer { #configuring-smtp-in-widequick-designer }

1. I projektträdet, högerklicka på noden **Mail** och välj **Egenskaper...**.
2. Ange serveruppgifterna.

![Mail properties dialog](/docs/sv/Images/Alarm_Sender/Mail_properties.png){align=center}

### Konfigurera SMTP vid körning { #configuring-smtp-at-runtime }

Klicka på **Konfigurera** i SMTP-sektionen i statuspanelen **Larm - Schema**, eller anropa `System.mailManager.edit()` från ett skript eller en knappåtgärd.

![Edit mail settings](/docs/sv/Images/Alarms/alarm-smtp-settings.png){align=center}

| Fält | Beskrivning |
|---|---|
| **Avsändare** | Avsändarens e-postadress |
| **Avsändarnamn** | Visningsnamn för avsändaren |
| **Server** | SMTP-serveradress eller IP, till exempel `smtp.gmail.com` |
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
| Event: Alarm acknowledged (active)
---------------------------------------------------------------------------
| ------------------------------------------------------------------------
| | Name: AS01.Station1_PV01_IO
| |
| | Timestamp: 2026-05-29 12:00:00
| |
| | Alarm class: 1
| |
| | Alarm text: My alarm text
| |
| | Description: My alarm description
| |
| | Acknowledged by: Operator
| ------------------------------------------------------------------------
|
---------------------------------------------------------------------------
```

**Beskrivning** tas bara med när larmet har en beskrivning, och **Kvitterad av** bara när
en användare är känd. När schemat reagerar på alla händelser skrivs raden **Händelse**
för varje larm i stället för i huvudet.

Varje rad i e-posten byggs upp genom att text läggs till en meddelandevariabel med `+=`.
Det innebär att integratören kan ändra etiketter, lägga till nya rader med ren text eller
ta bort rader som inte behövs. För att till exempel ändra etiketten **Larmklass** till
**Prioritet**, lokalisera följande rad i funktionen `writeMail()`:

```javascript title="writeMail() function in scAlarmSender script — before"
msg += "| | " + Language.translate("Translations.klib", "Larmklass") + ": " + alarm.severity + "\n"
```

Och ändra den till:

```javascript title="writeMail() function in scAlarmSender script — after"
msg += "| | Priority: " + alarm.severity + "\n"
```

Etiketterna går genom `Language.translate()`, så en etikett kan också ändras utan att
skriptet redigeras, genom att dess översättning ändras. Se
[Redigera enskilda översättningar](../../../guides/languages.md#editing-translations).
En översättning gäller överallt där samma källtext används.

De tillgängliga larmfälten som kan inkluderas i meddelandet är:

| Fält | Beskrivning |
|---|---|
| `alarm.name` | Larmets namn |
| `alarm.timestamp` | Datum och tid då larmet utlöstes |
| `alarm.severity` | Larmklass |
| `alarm.text` | Larmtext |
| `alarm.description` | Larmbeskrivning. Tom om larmet saknar beskrivning |
| `alarm.eventType` | Händelsen: `active`, `acknowledged`, `unacknowledged` eller `inactive` |
| `alarm.username` | Användaren bakom händelsen, om den är känd |
| `alarm.active` | `true` om larmet är aktivt |

Ren text kan också läggas till fritt var som helst i meddelandet. För att till exempel lägga till
en sidfot, lägg till följande rad före den avslutande avgränsaren:

```javascript title="writeMail() function in scAlarmSender script"
msg += "| Sent from WideQuick\n"
```

---

## SMS-notifieringar { #sms-notifications }

SMS-notifieringar skickas via ett modem anslutet till WideQuick-värden via en seriell
COM-port. Det kan vara ett traditionellt GSM-modem eller en 4G-router. Alla enheter som
accepterar AT-kommandon via en seriekoppling är kompatibla.

Alternativt kan SMS skickas via en Teltonika-router med Teltonika-pluginet. Pluginet
kommunicerar med routerns REST API över nätverket i stället för via en seriell anslutning,
och skickar SMS för samma larmnotifieringsscheman. Det fungerar endast i Windows och
kräver licensen **WideQuick Advanced** med optionen .NET-plugin, eller en Premium-licens.
Se [Skicka SMS med Teltonika](../../../../plug-in/teltonika/oversikt.md).

### Konfigurera modemet { #configuring-the-modem }

Modemet konfigureras i **WideQuick® Runtime**. Navigera till
**Inställningar → Avancerade inställningar → GSM Modem** och klicka på **Ändra GSM inställningar**
för att öppna konfigurationsdialogen. De avancerade inställningarna kräver privilegiet `Debug`.
När GSM är påslaget kan dialogen även öppnas med **Konfigurera** i avsnittet **SMTP och GSM**
i **Larm - Schema**.

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

Klicka på **Spara**. Om konfigurationen är korrekt lyser indikatorn **GSM-modem aktivt**
grönt. Själva GSM slås på och av med reglaget **GSM Modem** på samma ruta i
**Inställningar**.

!!! note "Krav"
    SMS-notifieringar kräver att `scModem` körs utöver `scAlarmSender`.

### Anpassa SMS

SMS-notifieringen följer samma mönster som e-posten och kan anpassas genom att
redigera funktionen `writeSMS()` i skriptet `scAlarmSender`. Samma larmfält är
tillgängliga. Etiketter kan ändras eller ren text läggas till på samma sätt.

Standardformatet för SMS ser ut så här:

```
Schedule: My Schedule
Title: My Subject
Event: Alarm acknowledged (active)
Name: AS01.Station1_PV01_IO
Timestamp: 2026-05-29 12:00:00
Alarm class: 1
Alarm text: My alarm text
Description: My alarm description
Acknowledged by: Operator
```

Med **Kompakt läge** påslaget för schemat innehåller SMS:et bara rubriken och, för varje
händelse, namnen på de larm som matchar. Ett schema vars kolumn `sms_truncated` är satt
till `1` skickar bara antalet nya larm. Det alternativet har ingen inställning i vyerna.

För att till exempel ändra etiketten **Namn** till **Signal**, lokalisera följande rad
i funktionen `writeSMS()`:

```javascript title="writeSMS() function in scAlarmSender script — before"
msg += Language.translate("Translations.klib", "Namn") + ": " + Language.translate("Translations.klib", alarm.name) + "\n"
```

Och ändra den till:

```javascript title="writeSMS() function in scAlarmSender script — after"
msg += "Signal: " + Language.translate("Translations.klib", alarm.name) + "\n"
```

!!! note
    Håll SMS-meddelanden korta. De flesta GSM-modem har en teckengräns per meddelande,
    och långa meddelanden kan delas upp i flera delar eller trunkeras.

---

## Fjärrlarmsammanställning { #remote-alarm-aggregation }

Larm från anslutna fjärrsystem kan sammanställas i den lokala larmlistan. Se
[Fjärrlarm](/mod/guides/remote-systems/#remote-alarms) i guiden Fjärrsystem för
installationsanvisningar.
<!-- --8<-- [end:body] -->
