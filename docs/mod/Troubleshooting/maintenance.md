---
title: Maintenance
description: Common issues and solutions for the Maintenance module.
product: mod
page_type: troubleshooting
doc_id: DOC-M6
status: draft
last_reviewed: 2026-06-08
---
<!-- --8<-- [start:body] -->

# Maintenance

## Common Issues { #common-issues }

| Problem | Solution |
|---|---|
| Maintenance widget on the dashboard always shows zero for active tasks | Confirm that the maintenance database connection is active and that the maintenance table contains records with the expected status values. |
| A recurring task was not created after completing the previous one | Check that the configuration is still set to active. If the object was removed from the configuration's object list between completions, no new task is generated for that object. |
| Tasks show the status Ongoing | **Ongoing** is a legacy status from an earlier version of the module. The `scMaintenance` script includes a migration that automatically converts these to **Planned** on startup. If tasks still show **Ongoing** after the system has been restarted, check that the `scMaintenance` script is running and that the migration completed without errors. |
| A missed task did not generate a follow-up | Verify that **Auto-create next maintenance on missed deadline** is enabled on the recurring configuration. |

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
