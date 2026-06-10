---
title: Legacy symbols
description: Overview of the legacy WideQuick symbol libraries from BMS 8.0.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-10
---
<!-- --8<-- [start:body] -->

# Legacy symbols {#legacy-symbols}

WideQuick BMS 8.0 included an earlier generation of symbols which are still
available in the following object libraries:

* **COMPONENTS_Legacy**
* **DAMPERS_Legacy**
* **MOTORS_Legacy**
* **SENSORS_Legacy**
* **VALVES_Legacy**
* **OTHERS_Legacy**

Legacy symbols function the same way as the current symbols and are fully compatible
with WideQuick Modular Framework. However they use the older single-layer animation
system and do not provide the same level of visual feedback as the new symbols.

When importing a view from an older BMS project, all legacy symbols are automatically
upgraded to the new symbol versions. This means migration is seamless — no manual
replacement is needed.

!!! tip "Recommendation"
    It is recommended to migrate away from legacy symbols when building new projects
    or updating existing ones. The new symbols provide richer visual feedback and are
    the actively maintained standard going forward.
<!-- --8<-- [end:body] -->
