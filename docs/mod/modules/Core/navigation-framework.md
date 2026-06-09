<!-- --8<-- [start:body] -->
Navigation
===
???+ Note "Requirements"
    In order for Navigation to work the following scripts are required:
    
    - scNav
	- scAlert

The navigation in WideQuick Modular Framework is automatically generated. This means that the user does not have to manually add buttons for navigation. This automatic menu system allows for an infinite depth. 


## Adding workviews to the navigation { #adding-workviews-to-the-navigation }
The automatic navigation consists of two parts. The workview folder "Main_Menu" and the folder "System". Any workview placed in one of these folders will automatically appear in the menu. However it's STRONGLY recommended that all workviews are placed in the "System" folder and not in the "Main_Menu". This is because future updates to Modular Framework will add additional menu groups to the "Main_Menu" and this could make it more difficult to upgrade to newer versions if the Main_Menu is modified.

In order to create a new view in the menu a new workview has to be placed in the in a workview folder under the "System" folder. As seen in the example below. Clicking on this node in the menu will show the view directly.


![Single depth](/Images/Navigation/Navigation_single.png){ align=top } ![Single depth menu](/Images/Navigation/Navigation_single_menu.png)


If more views are added to the same folder the icon in the menu will change and clicking on the node will instead open up a submenu like seen in the image below. More folders can be added inside this folder to build an even deeper depth.

![Depth](/Images/Navigation/Navigation_depth.png){ align=top }  ![Depth navigation](/Images/Navigation/Navigation_depth_menu.png)

## Setting privilege requirements on views { #setting-privilege-requirements-on-views }
???+ Note "Requirements"
    In order to set privileges the following scripts are required:
    
    * scUsers

    More information about configuring users and privileges can be found [here](users-privileges.md)
    
Since the menu system is automatically generated it is not possible to hide or disable views as done traditionally by hiding/disabling the navigation button using the security tab. Instead this has to been done through the settings in runtime. 

Instead these permissions can be changed in the project under settings. To reach these settings start the project. Under Main Menu select "Inställningar" --> "Arbetsvyer" --> "Arbetsvyer - Privilege".

Here you will see two menu groups: Main_Menu and System. These can be expanded by select a specific view or workview folder. The then selected view/folder which you want to lock to a certain privilege, and select the privilege from the list. The workview will now only be available for users with the correct privilege. It is possible to lock both specific workviews and entire workview folders.

Once a workview is locked to a specific privilege any user that does not have the correct privilege will see a lock-icon on the view/folder as seen on the image below. 


![Locked workview](/Images/Navigation/Locked%20workview.png)

!!! note "Encrypted projects"
	If your project is encrypted WideQuick will not be able to suggest privileges, instead you must type in the name of the privilege manually
<!-- --8<-- [end:body] -->
