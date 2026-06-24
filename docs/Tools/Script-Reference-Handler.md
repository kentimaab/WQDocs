---
title: Script Reference Handler
description: Update the script reference handler. For projects in WQ13 which upgrades to WQ14
---

# Script Reference Handler 


After **WideQuick®** 14.0, remote script libraries can now have the same names as script libraries in the main project. Previously, this could cause the system to run the wrong script. This update improves both modularity and robustness of script libraries.

To update older projects for compatibility with the new version, download the [Script Reference Migration Handler](https://www.kentima.com/en-GB/Download/HMI-SCADA-Software/Download_software/WideQuick-HMI-SCADA/Version%20140){target="_blank"}

Once downloaded, extract the files and follow the steps below before running the project in Runtime.

1. It's strongly recommended to back up a project prior the use of WideQuick 14.0 Script Reference Handler.

2. Run the program and this window will be displayed:

![Script Reference](/docs/Images/Script_Refenc_Handler/RefrenceHandler.png)

3. Press ++"Browse"++ in the top right corner and find the project folder in question. This will find all files in the project that needs to be corrected.

4. Finish it up by pressing ++"Correct app. references"++. This will open a window, press ++"Ja"++ and then ++"Ok"++ and the projected is updated.

5. This tool does not confirm logic, only changes the references. Ensure the projects works as intended before removing the backup.

![Script Gif](/docs/Images/Script_Refenc_Handler/Script_Handler.gif)