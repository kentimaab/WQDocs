---
title: Teman — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Teman — Konfigurering

## Ändra en färg { #changing-a-color }

I **WideQuick Designer®**, öppna grenen **Themes** i projektträdet och dubbelklicka på det tema du vill redigera. Dialogrutan **Edit theme** öppnas med tre flikar: **Components**, **Custom colors** och **Keyboard**.

![Theme editor](/Images/Themes/theme-edit-dialog.png){align=center}

Navigera till fliken **Custom colors** och dubbelklicka på en färgkod för att ändra dess värde.

## Hur färger appliceras på objekt { #how-colors-are-applied-to-objects }

Färger från det aktiva temat appliceras på objekt via skript. Ett `onLoad`-skript eller ett dynamikuttryck anropar `System.themes.color()` med namnet på färgrollen:

```javascript title="Applying a theme color in onLoad"
this.brush.color1 = System.themes.color("surface")
this.pen.color = System.themes.color("onSurface")
```

För att se vilken färgroll ett specifikt objekt använder, kontrollera dess `onLoad`-skript eller dynamik. Namnet som skickas till `System.themes.color()` motsvarar direkt en post i inställningarna för **Edit theme**.

## Anpassade färger { #custom-colors }

Fliken **Custom colors** innehåller projektspecifika färger tillsammans med standardrollerna — till exempel `Symbol_Alarm`, `Symbol_Warning` och `Alarm_Severity_0` till `Alarm_Severity_5`. Dessa följer samma namnkonvention som standardroller och används på samma sätt i skript:

```javascript title="Using a custom color"
System.themes.color("Symbol_Alarm")
```

För att lägga till en ny anpassad färg, klicka på **+** längst ned på fliken **Custom colors** (den läggs till som ColorX), tilldela ett namn och ange ett värde. Använd samma namn i alla teman så att färgen löses korrekt vid byte mellan teman.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — skapa ett anpassat tema som följer en grafisk profil
<!-- --8<-- [end:body] -->
