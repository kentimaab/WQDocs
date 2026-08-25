---
title: Users and Privileges
description: Create and manage users and privileges in WideQuick.
product: mod
page_type: howto
status: draft
last_reviewed: 2026-08-25
scripts:
  - scUsers
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Users and Privileges
???+ info "Requirements"
    The following scripts are required to use Users and Privileges and all
    related functionality covered in the Users and Privileges guides:
    
    * `scUsers`
    * `scAlert`

WideQuick allows user profiles to be created with specific privileges, enabling
role-based access control across the application. Profiles can be configured to
restrict or grant access to specific views and actions.

## Adding and editing users { #adding-and-editing-users }

Users can be managed in either **WideQuick® Designer** or **WideQuick® Runtime**.

### WideQuick® Designer

In the project tree, double-click **Users and Privileges**. To add a new user,
right-click **Users** and select **Add Users...**. To edit an existing user,
double-click **Users**, right-click the user and select **Properties...**.

### WideQuick® Runtime

Navigate to **Settings** in the main menu and open the **Settings** view. Under
**Users and privileges** click **Change user**. Click **Add...** to create a new
user or select an existing user and click **Edit...** to modify it.

![Users](/docs/Images/User_and_privileges/Users.png)

#### User settings

* **User** — the username for the profile
* **Description** — an optional description of the user
* **Password** / **Verify password** — an optional password for the user
* **Privileges** — grant or deny privileges by double-clicking a privilege, or
selecting it and clicking **Grant** or **Deny**

![Edit Users](/docs/Images/User_and_privileges/Edit_Users.png)

## Adding and editing privileges { #adding-and-editing-privileges }

In the project tree, double-click **Users and Privileges**. To add a new privilege,
right-click **Privileges** and select **Add Privilege...**. To edit an existing
privilege, double-click **Privileges**, right-click the privilege and select
**Properties...**.

* **Privilege** — the name of the privilege
* **Description** — an optional description of the privilege
* **Default** — whether the privilege is **Granted** or **Denied** by default
* **Virtual privilege** — if a user is granted this privilege, they will also be
granted all privileges selected here
* **Users** — grant or deny users by double-clicking a user, or selecting it and
clicking **Grant** or **Deny**

![Privilege](/docs/Images/User_and_privileges/Privilege.png)

## Framework privileges { #framework-privileges }

The framework ships with the privileges below, defined in `Privileges.kdat`.

!!! warning "Every framework privilege defaults to denied"
    All of them are defined with `Default="denied"`. A privilege added in a new release is therefore unavailable to every role until it is granted, including to roles that already hold the related privileges. After upgrading, review the assignments for any privilege the release introduced.

| Privilege | Grants |
|---|---|
| `AlarmControl` | Acknowledge and block alarms |
| `Schedules` | Add and edit schedules |
| `TimeChannels` | Control time channels |
| `EditUsers` | Edit users |
| `Config` | Configuration actions, including clearing the maintenance log |
| `editSMTP` | Edit the SMTP configuration |
| `Debug` | Debugging. Not intended for live applications |
| `Logbook_View` | View logbook entries |
| `Logbook_Add` | Add logbook entries |
| `Logbook_Edit` | Edit existing logbook entries |
| `Logbook_Archive` | Archive and restore logbook entries in the global logbook view |
| `Logbook_Delete` | Delete all archived notes from the settings view |
| `Logbook_Context` | Add, remove and edit logbook contexts |
| `Documents_View` | View and open documents |
| `Documents_Upload` | Upload new documents |
| `Documents_Edit` | Edit document name and metadata |
| `Documents_Link` | Link and unlink documents to objects |
| `Documents_Delete` | Delete documents |
| `Documents_Sync` | Synchronise the database with the filesystem |
| `Maintenance_Add` | Add new maintenance tasks |
| `Maintenance_Edit` | Edit the status and description of maintenance tasks |
| `Maintenance_EditExtended` | Edit assignee, priority and deadline |
| `Maintenance_Templates` | Edit maintenance templates, including recurring task templates |
| `ControlCurve_ChangeProfile` | Switch between control curve profiles |
| `ControlCurve_EditProfiles` | Edit control curve profiles |
| `ControlCurve_ManualControl` | Change control curve values directly |
| `Settings_Project` | Change general project settings such as language, units, time, SMTP and application name |
| `Settings_Navigation` | Change navigation settings such as fullscreen mode, direct navigation and login requirements |
| `Settings_Process_Images` | Change process image display settings such as nameplates, font size, decimals and hand symbol |

## Virtual privileges { #virtual-privileges }

A virtual privilege allows a single privilege to automatically grant one or more
additional privileges. When a user is assigned a privilege that contains virtual
privileges, they are also granted all the privileges listed under it — without
needing to assign each one individually.

**Example:** If the privilege `EditUsers` has `EditName` and `EditPassword` as
virtual privileges, any user assigned `EditUsers` will automatically also have
`EditName` and `EditPassword`.

Virtual privileges are configured in the privilege properties in **WideQuick®
Designer**. In the project tree, privileges that contain virtual privileges are
marked with a special icon.

<figure markdown="span">
  ![VirtualPrivilege](/docs/Images/User_and_privileges/Virtual.png)
  <figcaption>Icon in project tree.</figcaption>
</figure>

To add virtual privileges to a privilege, open the privilege properties and click
the **Virtual privilege** button to select which privileges should be included.


## Restricting Workviews by privilege { #restricting-workviews-by-privilege }

Access to specific **Workviews** can be restricted based on privileges. Navigate
to **Settings → Workviews → Workviews - Privilege** in the main menu.

![WorkView Privilege](/docs/Images/User_and_privileges/Workview_privleage.png)

Select the **Workview** where the restriction should be applied. Configuration
options will appear on the right side of the view.

![Workview Settings](/docs/Images/User_and_privileges/Settings.png)

Select the required privilege from the dropdown and click **Save** to apply the
change.

For information on how restricted **Workviews** appear in the navigation menu and
how to configure the two display styles for locked views, see
[Navigation — Configuring](../Core/Navigation/configuring#setting-privilege-requirements-on-views--setting-privilege-requirements-on-views-).
<!-- --8<-- [end:body] -->