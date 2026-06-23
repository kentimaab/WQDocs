---
title: Inställningar
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Inställningar

Vyn **Inställningar** i **WideQuick Runtime®** ger tillgång till alla
systemkonfigurationsalternativ. Navigera till **Inställningar** i huvudmenyn och
öppna vyn **Inställningar**.

![Settings](/Images/Settings/Settings.png)

---

## Allmänna inställningar

**Applikationsnamn** — namnet på applikationen som visas i namnlisten.
Klicka på **Ändra applikationsnamn** för att uppdatera det.

**WideQuick-version** — visar den för tillfället installerade versionen av **WideQuick®**.
Skrivskyddat.

**Systeminformation** — visar anslutningsinformation för det aktuella systemet. Klicka
på **Visa systeminformation** för att öppna dialogen, som visar server- och klient-Runtime-namn,
IP-adress och port.

**XXX-version** — visar den för tillfället installerade ramverket av **WideQuick®**.
Skrivskyddat.

**Språk** — applikationens visningsspråk. Klicka på **Ange språk** för att byta
språk. Se [här](../../../mod/guides/languages.md) för mer information.

**Enheter** — det enhetssystem som används för visning av värden, till exempel SI. Klicka
på **Ändra enhetssystem** för att växla mellan enhetssystem.

**Tid** — visar aktuellt systemdatum och -tid. Klicka på **Redigera tid** för att
justera den.

**Tema** — växlar mellan de tillgängliga applikationsteman, till exempel ljust
och mörkt läge.

**SMTP-inställningar** — konfigurerar den SMTP-server som används för att skicka e-postaviseringar.
Klicka på **Redigera** för att öppna konfigurationsdialogen. Se
[Larm — Utöka](../Core/alarms/extending.md#email-notifications) för mer
information.

**Fjärrsystem** — hanterar anslutningar till fjärranslutna WideQuick Runtime-instanser. Klicka
på **Hantera fjärrsystem** för att lägga till eller konfigurera fjärrsystem. Se [här](../../../mod/guides/remote-systems.md) för mer
information.

**Anslutna klienter** — visar antalet för tillfället anslutna fjärrklienter.
Klicka på **Visa anslutna klienter** för att se en lista över aktiva anslutningar.

**Schema** — WideQuick:s inbyggda schemaläggningssystem, som kontrolleras var 5:e minut för att
starta konfigurerade schemalagda uppgifter såsom rapportgenerering. Klicka på **Redigera
schema** för att konfigurera scheman.

---

## Processbilder

**Visa namnplåtar** — växlar huruvida objektnamnplåtar är synliga i processvyn.

**Visa dynTouch** — växlar huruvida `DynTouch`-objektgränser är synliga,
användbart för felsökning av objektplacering i **WideQuick Designer®**.

**Teckenstorlek för stödobjekt** — anger teckenstorleken för stödobjekt såsom värdevisningar.
Ange ett värde eller använd pilarna för att justera.

**Global decimalinställning** — anger antalet decimaler som visas för numeriska
värden i hela applikationen. Ange ett värde eller använd pilarna för att justera.

**Uppdateringsfrekvens värdevisning (ms)** — styr hur ofta värdevisningar
uppdateras, i millisekunder. Lägre värden uppdaterar oftare men kräver mer
bearbetning. Ange ett värde eller använd pilarna för att justera.

**Handsymbol** — den symbol som visas när ett objekt är i manuellt läge. Klicka
på **Redigera handsymbol** för att ändra den.

---

## Användare och behörigheter

**Användare** — visar den för tillfället inloggade användaren. Klicka på **Byt användare** för att
växla till ett annat användarkonto. Se [här](users-privileges.md) för mer information.

**Lösenord** — klicka på **Ändra lösenord** för att ändra lösenordet för den aktuella
användaren.

**Kräv inloggning** — när aktiverat måste användare logga in innan de får tillgång till systemet.
När inaktiverat kringgås inloggningsskärmen och användaren går in som oautentiserad.
Se [Inloggningskonfigurationer](../../guides/Login%20Config/#require-login) för mer
information.

**Kräv användarnamn** — när aktiverat måste användare skriva sitt fullständiga användarnamn när
de loggar in. När inaktiverat visas istället en kombinationsruta med alla tillgängliga användare.
Se [Inloggningskonfigurationer](../../guides/Login%20Config/#require-username)
för mer information.

---

## Navigering

**Visa låsta menyer** — växlar huruvida menyalternativ som kräver en behörighet är
synliga för oautentiserade användare. Se
[Navigering — Konfigurering](Navigation/configuring.md#setting-privilege-requirements-on-views)
för mer information.

**Visa låsta undermenyer** — växlar huruvida undermenyalternativ som kräver en behörighet
är synliga för oautentiserade användare. Se
[Navigering — Konfigurering](Navigation/configuring.md#setting-privilege-requirements-on-views)
för mer information.

**Helskärm** — växlar huruvida navigationen körs i helskärmsläge.

**Direktnavigering (karta)** — när aktiverat navigerar ett klick på ett nålobjekt på en karta
direkt till dess länkade **Arbetsvy**. När inaktiverat visas först en informationspanel
som låter användaren välja om denne vill navigera. Se
[Kartor — Konfigurering](../maps/configuring.md) för mer information.

---

## Avancerade inställningar

**Felsökningsträd** — klicka på **DebugTree** för att öppna felsökningsträdet, som visar
hela Datalager-variabelhierarkin. Användbart för felsökning av taggkopplingar.

**Konsol** — klicka på **Öppna konsol** för att öppna skriptkonsolen, som visar
skriptutdata och fel under körning.

**Aktivera felsökningslogg** — när aktiverat skrivs en detaljerad felsökningslogg till disk.
Användbart för att diagnostisera problem i produktionsmiljöer.

**GSM-modem** — konfigurerar det GSM-modem som används för SMS-larmaviseringar. Klicka
på **Ändra GSM-inställningar** för att öppna konfigurationsdialogen. Se
[Larm — Utöka](alarms/extending.md#sms-notifications) för mer
information.
<!-- --8<-- [end:body] -->
