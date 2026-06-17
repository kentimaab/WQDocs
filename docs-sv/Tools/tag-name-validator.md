---
title: Taggnamnsvalidator
page_type: overview
status: draft
last_reviewed: 2026-06-16
tags:
---

# Taggnamnsvalidator

Det här verktyget låter dig kontrollera att taggnamnen i ditt WideQuick-projekt har en giltig taggstruktur för Modular Framework. För att ett WideQuick-variabelnamn ska vara giltigt måste det följa strukturen **Connection**.**Device**.**Sys**\_**ObjectName**\_**Suffix**.

Genom att kopiera namnkolumnen från din Data Store i WideQuick Designer och klistra in den i textfältet nedan kan du kontrollera vilka av dina signaler som följer taggstrukturen och vilka som inte gör det.

Eftersom WideQuick-namnet skiljer sig åt mellan Modbus och OPC UA/DA finns det två flikar. Skillnaden mellan de två är att Modbus ärver Connection- och Device-delen av syntaxen från sin Connection och Device i DataStore.

För mer information om hur taggstrukturen är avsedd att fungera, besök [Taggstruktur](../mod/reference/tag-structure.md){target=_blank}

=== "OPC UA and DA"

    <div class="tag-validator" markdown>
    <textarea id="tagTextarea" placeholder="Enter tag/variable names, one per line"></textarea>
    <button id="filterButton">Show Only Invalid Tags</button>
    <div id="tagResults"></div>
    </div>

=== "Modbus Serial and TCP/IP"

    <div class="tag-validator-modbus" markdown>
    <textarea id="tagTextarea-modbus" placeholder="Enter tag/variable, one per line"></textarea>
    <button id="filterButton-modbus">Show Only Invalid Tags</button>
    <div id="tagResults-modbus"></div>
    </div>
