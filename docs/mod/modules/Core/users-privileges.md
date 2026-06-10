---
title: Users and Privileges
description: Create and manage users and privileges in WideQuick.
product: mod
page_type: howto
status: draft
last_reviewed: 2026-06-08
scripts:
  - scUsers
---
<!-- --8<-- [start:body] -->

# Users and Privileges

WideQuick allows user profiles to be created with specific privileges, enabling
role-based access control across the application. Profiles can be configured to
restrict or grant access to specific views and actions.

## Adding and editing users { #adding-and-editing-users }

Users can be managed in either **WideQuick Designer®** or **WideQuick Runtime®**.

### WideQuick Designer®

In the project tree, double-click **Users and Privileges**. To add a new user,
right-click **Users** and select **Add Users...**. To edit an existing user,
double-click **Users**, right-click the user and select **Properties...**.

### WideQuick Runtime®

Navigate to **Settings** in the main menu and open the **Settings** view. Under
**Users and privileges** click **Change user**. Click **Add...** to create a new
user or select an existing user and click **Edit...** to modify it.

![Users](/Images/User_and_privileges/Users.png)

#### User settings

* **User** — the username for the profile
* **Description** — an optional description of the user
* **Password** / **Verify password** — an optional password for the user
* **Privileges** — grant or deny privileges by double-clicking a privilege, or
selecting it and clicking **Grant** or **Deny**

![Edit Users](/Images/User_and_privileges/Edit_Users.png)

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

![Privilege](/Images/User_and_privileges/Privilege.png)

## Restricting Workviews by privilege { #restricting-workviews-by-privilege }

Access to specific **Workviews** can be restricted based on privileges. Navigate
to **Settings → Workviews → Workviews - Privilege** in the main menu.

![WorkView Privilege](/Images/User_and_privileges/WorkView_privleage.png)

Select the **Workview** where the restriction should be applied. Configuration
options will appear on the right side of the view.

![Workview Settings](/Images/User_and_privileges/Settings.png)

Select the required privilege from the dropdown and click **Save** to apply the
change.

For information on how restricted **Workviews** appear in the navigation menu and
how to configure the two display styles for locked views, see
[Navigation — Configuring](../Core/Navigation/configuring#setting-privilege-requirements-on-views--setting-privilege-requirements-on-views-).
<!-- --8<-- [end:body] -->