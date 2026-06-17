---
title: Instrumentpaneler — Utökning
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Instrumentpaneler — Utökning

## Anpassade widgetar — Bygga nya widgetar från befintliga mallar { #custom-widgets-building-new-widgets-from-existing-templates }

För att basera en ny widget på en befintlig drar du den från biblioteket `Dashboard Widgets` till en workview i **WideQuick Designer®**. Högerklicka på den placerade widgeten och välj **Disconnect from template**. Widgeten kan nu redigeras fritt. Justera layouten, lägg till eller ta bort objekt, och ändra skriptlogiken.

När ändringarna är klara drar du widgeten från workview-en tillbaka till bibliotekslistan. Den lagras där som ett nytt objekt. För att byta namn på den högerklickar du på den i bibliotekslistan och anger ett nytt namn.

Samma sista steg gäller när man bygger en widget från grunden: när den är klar drar du den till biblioteket och byter namn på den där.

Det är även möjligt att redigera befintliga widgetar genom att dubbelklicka på en i biblioteket. Detta öppnar en ny workview som endast innehåller en redigerbar version av widgeten.

### Rutnätsdimensioner { #grid-dimensions }

Använd dessa dimensioner för att säkerställa att nya widgetar anpassas till instrumentpanelens rutnät. Kombinera bredd och höjd för önskat spann — en 2×1-widget använder bredd 2 och höjd 1.

| Enheter | Bredd   | Höjd    |
|---------|---------|---------|
| 1       | 385 px  | 240 px  |
| 2       | 780 px  | 490 px  |
| 3       | 1175 px | 740 px  |
| 4       | 1570 px | 990 px  |

### Granska befintliga widgetar { #inspecting-existing-widgets }

För att förstå hur en widget hanterar signaler, egenskaper eller layout dubbelklickar du på den i bibliotekslistan. Detta öppnar en redigerbar version av widgeten där skriptet och dynamiken för varje del kan granskas och användas som referens.

!!! tip
    Högerklicka på en placerad widget i en workview och välj **Show template** för att öppna biblioteket och markera källobjektet — praktiskt för att hitta vilken mall en widget på instrumentpanelen kommer från.

---

## Rollbaserade instrumentpaneler — Styra åtkomst och standardvyer { #role-based-dashboards-controlling-access-and-default-views }

### Ange visningsbehörigheter { #setting-view-privileges }

Visningsbehörigheter begränsar vilka användare som har åtkomst till en given instrumentpanel. Ange dem vid körning genom att navigera till **Huvudmeny → Inställningar → Workview Privileges**. Välj workview-en från trädet till vänster och ange sedan den nödvändiga behörighetsnivån i listrutan **Privilege** till höger.

![Workview privileges](/Images/Dashboard/WVPriv.png){align=center}

### Ange standardvy per roll { #setting-default-view-per-role }

För att ange en annan standardinstrumentpanel per roll lägger du till logiken i `onLoad`-skriptet för workview-en `Workspace.kvie` i **WideQuick Designer®**. Använd `_sys_user_name` för att matcha en specifik användare eller `System.currentUser().hasPrivilege()` för att matcha en behörighetsnivå.

```javascript title="Workspace.kvie — onLoad"
app.MultiViewer = this.MultiviewerPage;
if (_sys_user_name == "Admin"){
    app.MultiViewer.setView("Main_Menu/Dashboards & Kartor/Dashboard/Dashboard Larm.kvie");
}
if (System.currentUser().hasPrivilege("Config")){
    app.MultiViewer.setView("Main_Menu/Dashboards & Kartor/Dashboard/Dashboard Ventilation.kvie");
}
```

---
<!-- --8<-- [end:body] -->
