---
title: MultiView
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# MultiView

I WideQuick Modular Framework är det möjligt att ha objekt som innehåller länkar till andra Workviews. Detta gör det möjligt att låta systemet byta till en annan Workview baserat på en viss åtgärd. Den här guiden går igenom hur man ställer in detta. Gå först till en Workview där detta ska implementeras och markera objektet. Härifrån trycker du på fliken ++"Action"++, vilket visar följande.

![Action menu](../Images/MultiView/Action_menu.png)

I det här fönstret kan användaren, bredvid händelsefältet, bestämma vilken åtgärd som ska byta Workview. I detta exempel används "Click". Byt sedan från "No action" till "Script" och klicka på textikonen till höger. Detta öppnar skriptfönstret.

![Script menu](../Images/MultiView/Script_window.png)

I det här fönstret kan användaren skapa sitt skript för vad som ska hända när händelsen inträffar. Skriptet för att byta till en annan Workview visas nedan.

``` 
app.MultiViewer.setView("/Path/to/workView/myworkview.kvie")
```
Sökvägen inom parenteserna är inställd på den Workview som man byter till. För att illustrera hur detta ska anges visas en bild av ett projektträd nedan, följt av skriptet med korrekt sökväg.

![Project Tree](../Images/MultiView/Project_tree.png)

```
app.MultiViewer.setView("/System/Test/Link.kvie")
```
<!-- --8<-- [end:body] -->
