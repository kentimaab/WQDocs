---
title: Kalender — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Kalender — Utöka

## Påminnelsekonfiguration { #reminder-configuration }

Det finns för närvarande inget gränssnitt för påminnelseinställningar. Båda kan ställas in via ett skript.

### Globalt förskjutningsvärde { #global-offset }

Antalet dagar före en deadline som en påminnelsehändelse visas. Standard är 3 dagar. Använd `scMaintenance.setReminderOffset` och ange värdet i millisekunder:

```javascript
var days = 5;
scMaintenance.setReminderOffset(days * 24 * 60 * 60 * 1000);
```

### Aktivering per mall { #per-template-toggle }

Styr om påminnelser genereras för uppgifter som skapas från en specifik mall. Standard är av. Det finns ingen hjälpfunktion för detta — uppdatera tabellen `maintenanceLog_templates` direkt och anropa `updateTemplates()` för att uppdatera minnescachen så att kalendern fångar upp ändringen omedelbart:

```javascript
var templateType = "Filterbyte";
var current = scMaintenance.getAllTemplatesMap()[templateType];
var newVal = (current && current.reminder_enabled === 1) ? 0 : 1;
DatabaseConnections["maintenance"].exec(
    "UPDATE maintenanceLog_templates SET reminder_enabled = " + newVal + " WHERE type = '" + templateType + "'"
);
scMaintenance.updateTemplates();
```

Uppgifter som skapas utan en mall genererar alltid påminnelser oavsett denna inställning.
<!-- --8<-- [end:body] -->
