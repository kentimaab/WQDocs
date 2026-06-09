<!-- --8<-- [start:body] -->
Alarm Sender
====

The Outgoing Alarm Communication module is a module for scheduling when and what alarms should trigger a mail and/or a text message to persons of interest in your organization. This can be used to monitor your application even when you are not on site. Make sure that you never miss an important alarm.

???+ Note "Requirements"

    The **Outgoing Alarm Communication** module requires the following script libraries:
   
    -  scAlarm
    -  scAlarmSender
    -  scAlert
    -  scModem - For text messages via GSM Modem
   
    As well as the **DatabaseConnection**:

     - Config


## Send E-mail via an SMTP Server { #send-e-mail-via-an-smtp-server }

To send E-Mails from a WideQuick Modular Framework application, or any WideQuick application for that matter you need access to a SMTP Server, this typically also means you need some kind of internet access. 

If you are not entirely sure what an SMTP server is, it is advisable to read up on this. There are many resources available to help you understand it better.

An SMTP (Simple Mail Transfer Protocol) server is a system responsible for sending, receiving, and relaying email messages. In short it is the service that ensures the E-Mail sent from WideQuick application reaches its recipient. 

### Setting up a SMTP configuration { #setting-up-a-smtp-configuration }
To set up a SMTP Server configuration in WideQuick you can go about it in two ways. You can do it directly from **WideQuick Designer®** or you can do it from your **WideQuick Runtime®** application. 

=== "SMTP from **WideQuick Designer**"

    1. **Open the project you are interested in configurating a SMTP connection for in WideQuick Designer.**
    2. **Once loaded you can find the SMTP properties by right-clicking the ***Mail*** node in the Project tree and selecting ++"Properties..."++:**
    
        ![](/Images/Alarm_Sender/Mail_properties.png)   

    3. **Here you can enter all the necessary information for your connection to work.** 
        1. Sender - E-mail address of the sender. For example *user@company.com*
        2. Sender Name - Name of the sender
        3. Server - The address of the SMTP server. For example *smtp.gmail.com* or an ip-address. 
        4. Port - The sever port in use
        5. Domain - The server domain
        6. User - Your username on the server. For example user@company.com
        7. Password - Your password on the server
    4. (**Optional) Setting up Aliases**
        
        The alias system in WideQuick is used to map keywords, an alias, to one or several e-mail addresses. To edit the aliases right click on the **Mail** node in the project tree and click ++"Open"++, or double click the **Mail** node. 

        Aliases can then be added, removed or edited to map an alias to one or more e-mail addresses by separating them with the delimiter (;).

        ![Aliases](/Images/Alarm_Sender/Aliases.png)


=== "SMTP from **WideQuick Runtime**"

    1. **Accessing the SMTP configuration from a WideQuick Runtime**

        To access the SMTP configuration from your WideQuick Runtime application you can use the script:

        ``` javascript title="mailManager"
            System.mailManager.edit()
        ```
        In a WideQuick Modular Framework application this setting can be located on the settings view "Inställningar" / "SMTP Inställningar"
    2. **Here you can enter all the necessary information for your connection to work.** 
        1. Sender - E-mail address of the sender. For example *user@company.com*
        2. Sender Name - Name of the sender
        3. Server - The address of the SMTP server. For example *smtp.gmail.com* or an ip-address. 
        4. Port - The sever port in use
        5. Domain - The server domain
        6. User - Your username on the server. For example user@company.com
        7. Password - Your password on the server
    3. (**Optional) Setting up Aliases**
        
        The alias system in WideQuick is used to map keywords, an alias, to one or several e-mail addresses. 

        Aliases can then be added, removed or edited to map an alias to one or more e-mail addresses by separating them with the delimiter (;).



## Send text messages via GSM Modem { #send-text-messages-via-gsm-modem }

To send alarm text messages from WideQuick a GSM Modem is one way to do so. In this implementation we are going to use a Modem connected to the WideQuick host device via a serial COM-port. 

In developing this a Tosibox 4G modem with a sim card was used as a test device. But any serially connected modem that accepts AT-commands will do.  

All available AT Commands and more information about the GSM module can be found inside the script file.

### Setting up a GSM Modem configuration { #setting-up-a-gsm-modem-configuration }
 
 The GSM Module is configured from your WideQuick Modular Framework application in the **WideQuick Runtime®** application, accessible on the  GSM_Modem workview, which included in the module.
 
 This view can be accessed from the Settings workview "Inställningar" by clicking the GSM settings button.

 To configure the modem connection, please consult the data sheet for your modem and input the correct values. If the configuration is correct press "Verkställ". If the configuration is correct the indicator on the workview should turn green.



 ![GSM Settings](/Images/Alarm_Sender/GSM_Modem_Settings.png) 

## Configure alarm schedules { #configure-alarm-schedules }

To configure alarm schedules in your Modular Framework application the module includes a workview Larm - Schema. from here you can create, activate/inactive, remove and edit your schedules. You also get some monitoring in the workview which gives you an overview of how many mails and/or e-mails that have been sent, if the SMTP is configured (this only works for projects that are not encrypted) and how many alarms that are active as of right now.

![Alarm Schedules](/Images/Alarm_Sender/Alarm_Schedules.png)

### Add a new schedule { #add-a-new-schedule }

To add a new schedule press the "Skapa nytt schema" button. You will now be prompted to enter information on how the schedule should act. 

![Alarm Scheduler](/Images/Alarm_Sender/Allarm_schedule_1.png)

- Should it send both e-mails and text messages?

- When during the day it report on alarms?

- What alarm groups are relevant?

- What severity should trigger the schedule?

- Who is the intended recipient?

- How long should the schedule wait before sending?

### Edit a schedule { #edit-a-schedule }

To edit a schedule, mark it in the list of schedules and press the "Editera schema" button. From here you change and update the schedule with the same dialogs as when you created it with the edition of deactivating/activating the schedule. An deactivated schedule will not trigger any alarms. 

### Remove a schedule { #remove-a-schedule }

To remove a schedule mark it in the list and press "Ta bort valt schema"
<!-- --8<-- [end:body] -->
