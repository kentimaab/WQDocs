---
title: Tag Name Validator
description: Validate WideQuick tag names against the required Connection.Device.Sys_ObjectName_Suffix structure.
---
Tag Name Validator
===

This tool is a way to confirm that you tag names in you WideQuick project are of valid tag structure for Modular Framework. To be valid a WideQuick Variable name the name has to conform to a **Connection**.**Device**.**Sys**\_**ObjectName**\_**Suffix** structure.

By coping the name column from your Data Store in WideQuick Designer and pasting it into the textfield below you can check which of you signals conform or not to the tag structure. 

As the WideQuick name differs between Modbus and OPC UA/DA there are two tabs. The difference between the two is that Modbus inherits the Connection and Device part of the syntax from its Connection and Device in the Data Store.  

For more information on how the Tag Structure is intended to work please visit [Tag Structure](../mod/reference/tag-structure.md){target=_blank}

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




