---
title: Larm — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Larm — Konfigurering

## Skapa larmgrupper { #creating-alarm-groups }

Larm organiseras i grupper i **WideQuick Designer®**. Varje grupp definierar gemensamma standardvärden — färger, ikoner och åtgärder — som dess larm ärver om de inte åsidosätts individuellt.

1. I projektträdet högerklickar du på **Alarms** under **Data Store** och väljer **Add Group...**.
2. Ange ett **Name** för gruppen.
3. Ange **Monitor variable** — en boolesk variabel som är `true` så länge något larm i gruppen är aktivt.
4. Konfigurera valfritt standardfärger under **Colors** för varje larmstatus, standard **Icons** samt ett standard **Measure** för gruppen.
5. Klicka på **OK**.

![Dialogruta för att lägga till larmgrupp](/docs/sv/Images/Create_Alarm/AddAlarm.png){align=center}

## Lägga till larm { #adding-alarms }

När en grupp finns, öppna den (dubbelklicka eller högerklicka → **Open**) och klicka på **Add** för att skapa ett nytt larm.

![Dialogruta för nytt larm](/docs/sv/Images/Create_Alarm/NewAlarm.png){align=center}

| Fält | Beskrivning |
|---|---|
| **Name** | Unikt namn för larmet inom gruppen |
| **Alarm class** | Etikett som används för att rangordna eller kategorisera larm — till exempel `1`, `A` eller `High` |
| **Ack rule** | När larmet kan kvitteras — se nedan |
| **Text** | Kort etikett som visas i larmlistan, t.ex. *Motor överhettning* |
| **Details** | Längre beskrivning som visas när larmet expanderas i loggen |
| **Activation** | Utlösningsvillkor och valfri fördröjning innan larmet aktiveras |
| **Block type** | Om larmet kan undertryckas: **None**, **Manually** (av operatör) eller **Automatic** (av en variabel) |
| **Block variable** | Variabel som används när **Block type** är **Automatic** — larmet undertrycks medan denna variabel är sant |
| **Colors** | Färgåsidosättningar per larm. Om det lämnas tomt används gruppens standardvärden |
| **Activation monitor** | Boolesk variabel som sätts till `true` medan larmet är aktivt |
| **Acknowledge monitor** | Boolesk variabel som sätts till `true` medan larmet är kvitterat |
| **Measure** | Åtgärd tillgänglig i larmlistan — används för att lägga till en GoTo-länk. Se [GoTo i larmgrupper](../Navigation/extending.md#goto-in-alarm-groups) |
| **Description** | Intern notering om larmet. Visas inte vid körning |

### Aktivering { #activation }

Dubbelklicka på fältet **Activation** för att konfigurera utlösaren. Ange variabeln som larmet övervakar och lägg valfritt till en fördröjning — larmet aktiveras bara om villkoret har varit sant under hela fördröjningsperioden.

![Aktiveringsinställningar](/docs/sv/Images/Create_Alarm/Activation.png){align=center}

### Kvitteringsregler { #acknowledgement-rules }

* **Normal** — kan kvitteras när som helst.
* **Strict** — kan bara kvitteras efter att larmet har blivit inaktivt.
* **Auto** — kvitteras automatiskt när larmet blir inaktivt. Kan även kvitteras manuellt medan det fortfarande är aktivt.

### Åtgärd { #measure }

Fältet **Measure** på ett larm aktiverar en åtgärdskolumn i larmlistan. Genom att konfigurera en GoTo-åtgärd kan operatörer navigera direkt till det objekt som utlöste larmet genom att trycka på åtgärden i listan. Se [GoTo i larmgrupper](../Navigation/extending.md#goto-in-alarm-groups) för installationsanvisningar.

![Åtgärdsinställningar](/docs/sv/Images/Create_Alarm/Measure.png){align=center}

## Larmnotifieringsscheman { #alarm-notification-schedules }

Vyn **Alarm - Schedule** styr när och till vem larmnotifieringar skickas via e-post eller SMS. Den visar ett stapeldiagram över skickade och misslyckade e-postmeddelanden och SMS under den senaste månaden, en lista med alla konfigurerade scheman samt en statuspanel med schemantal, aktuellt larmantal och SMTP-status.

!!! note "Krav"
    Notifieringsscheman kräver att `scAlarmSender` körs samt en konfigurerad e-post- eller SMS-kanal. Se [Utöka](extending.md).

![Vyn Alarm - Schedule](/docs/sv/Images/Alarms/alarm-schedule-view.png){align=center}

### Skapa ett schema { #creating-a-schedule }

Klicka på **New schedule** för att öppna skapandeassistenten. Den går igenom tre sidor.

**Steg 1 — När**

![Nytt schema steg 1](/docs/sv/Images/Alarms/alarm-schedule-step-1.png){align=center}

* **Name** — namn för schemat.
* **System** — vilket system det här schemat gäller för: det lokala systemet eller ett anslutet fjärrsystem.
* **Active schedule** — växla för att aktivera eller inaktivera schemat utan att ta bort det.
* **Weekdays** — välj vilka dagar i veckan schemat är aktivt. Endast de valda dagarna visas i avsnittet **Time interval** nedan.
* **Time interval** — konfigurera aktiva tidsfönster för varje vald dag. Varje dag visar en primär **From/To**-tidsperiod. Klicka på **+**-knappen för att lägga till en sekundär tidsperiod för den dagen, vilket möjliggör två separata notifieringsfönster samma dag. Om både **From** och **To** sätts till `00:00` inaktiveras notifieringar för den tidsperioden. För att ta emot notifieringar hela dagen, sätt **From** till `00:00` och **To** till `23:59`.

!!! note
    Att sätta **To** till `23:59` täcker hela dagen inklusive den sista minuten.
**Steg 2 — Vad**

![Nytt schema steg 2](/docs/sv/Images/Alarms/alarm-schedule-step-2.png){align=center}

* **Severity level** — vilka larmklasser som utlöser det här schemat. Lämna tomt för att inkludera alla klasser.
* **Alarm groups** — vilka larmgrupper som övervakas. Använd **Select all** för att inkludera alla grupper.

**Steg 3 — Vem**

![Nytt schema steg 3](/docs/sv/Images/Alarms/alarm-schedule-step-3.png){align=center}

* **Subject line** — ämnesrad som används för utgående e-postnotifieringar.
* **Recipient** — lägg till enskilda e-postadresser eller telefonnummer direkt.
* **Alias** — välj från konfigurerade alias för att lägga till en grupp mottagare på en gång.
* **Collect alarm dispatches** — fördröjning i sekunder innan sändning. Larm som utlöses inom detta fönster samlas in och skickas tillsammans i en enda notifiering.

### Redigera och ta bort scheman { #editing-and-deleting-schedules }

Markera ett schema i listan och klicka på **Edit schedule** för att ändra det. Aktivt och inaktivt läge kan växlas inifrån redigeringsdialogen.

Klicka på **Delete schedule** för att ta bort det valda schemat.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — konfigurera e-post och SMS för larmnotifieringar
<!-- --8<-- [end:body] -->
