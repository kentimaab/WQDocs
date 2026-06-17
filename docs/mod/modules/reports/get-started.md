---
title: Reports - Get started
description: Get up and running with the Reports module.
product: mod
page_type: getstarted
doc_id: DOC-M17
status: draft
last_reviewed: 2026-05-21
scripts:
  - scReportScheduler
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Reports - Get started
???+ info "Requirements"
    The following scripts are required to use Reports and all
    related functionality covered in the Reports guides:
    
    * `scReportScheduler`
    * `scReports`
    * `scAlert`

This section covers the basics of the Report module, including how to add a new 
template, how to use existing templates in **WideQuick Runtime®**, and how to schedule 
reports to run automatically.

## Setting up the Reporter { #setting-up-the-reporter }
WideQuick includes a set of default report templates, found under 
**Reports** in the project tree. Custom templates can also be created or imported 
through **WideQuick Designer®**.

To create a new template, right-click **Reports** in the project tree and select 
**Add Report**. This will open the following window:

<figure markdown="span">
  ![Add report](/Images/Reports/Add_report.png)
  <figcaption>The Add Report dialog in WideQuick Designer.</figcaption>
</figure>

* **Name** — The name of the report.
* **Source file** — Import a premade template by clicking the folder icon. To start 
from a blank template, see the gif below.
* **Output directory** — The folder where generated reports will be saved. By default, 
reports are placed in the Reports folder. Click the folder icon to select a different 
destination.
* **Generate access** — Choose between **All Systems** (default) or 
**Local System Only**.
* **Output name** — Customize the report file name using the **Output Name Builder**. 
A preview of the name is shown in the **Name Preview** field.
<figure markdown="span">
  ![Create new report template](/Images/Reports/Create_new_report_template.gif)
  <figcaption>Creating a new report template from scratch.</figcaption>
</figure>

The new template will appear under **Reports** in the project tree, where it can be 
edited to display the desired information. For more information on creating custom 
templates, see [here](extending.md#creating-templates).

!!! note "Adding a template"
    When adding a custom template, a corresponding ReportController must also be 
    created. This is explained [here](extending.md#creating-the-reportcontroller-view).

## Using the Reporter in **WideQuick Runtime®** { #using-the-reporter-in-widequick-runtime }
To manage reports in **WideQuick Runtime®**, navigate to 
**History → Reports → Reports - List**. This page displays a list of all 
generated reports with two columns:

* **Report** — The name of the report, defaulting to Alarm Report \[#\] where \[#\] 
indicates the generation number.
* **Timestamp** — The date and time at which the recording ends.

From this page, reports can be created, removed, or sent as email attachments. Sending 
reports by email requires an SMTP server to be configured, which is explained [here](../Core/alarms/extending.md#configuring-smtp-in-widequick-designer).

<figure markdown="span">
  ![Report](/Images/Reports/Report.png)
  <figcaption>The Reports list workview in WideQuick Runtime.</figcaption>
</figure>

To create a new report, click **Create Report**. A configuration menu will appear on 
the right. By default, four report types are available: **Alarm Report**, 
**Alarm Report One Alarm**, **Energy Report**, and **Energy Report Week**. Switch 
between them by changing the **Report template** dropdown.

<div class="figure-row" markdown>

<figure markdown="span">
  ![Alarm Report](/Images/Reports/AlarmReport.png)
  <figcaption>Alarm Report controller.</figcaption>
</figure>

<figure markdown="span">
  ![Alarm Report One Alarm](/Images/Reports/AlarmReportOne.png)
  <figcaption>Alarm Report One Alarm controller.</figcaption>
</figure>

<figure markdown="span">
  ![Energy Report](/Images/Reports/EnergyReport.png)
  <figcaption>Energy Report controller.</figcaption>
</figure>

<figure markdown="span">
  ![Energy Report Week](/Images/Reports/EnergyReportWeek.png)
  <figcaption>Energy Report Week controller.</figcaption>
</figure>

</div>

The four ReportControllers share a similar structure but differ in which options are 
available and which loggers are shown in the TreeView. Below is a description of each 
option:

* **Report template** — The report template to use. Defaults to **Alarm_Report**. A guide 
to creating templates can be found [here](extending.md#creating-templates).
* **Customize title** — Sets the title of the report, which appears on the front page.
* **From** — The start time of the recording period. This field is locked for Energy 
Reports, as they require historical data from that point onwards. See 
[here](configuring.md#changing-year-span) for configuration.
* **To** — The end time of the recording period.
* **LoggerList** — Displays the signals available in the selected logger. Locked for 
Alarm Reports, as they include all signals automatically.
* **Number of events** — The maximum number of events to include. For Energy 
Reports, this defaults to the number of hourly events in the selected time period.
* **Report file format** — The output format of the report: either PDF or PDF and XLSM.
* **Report status** — Displays the current status of the report, including 
completion or any errors.

The **Alarm Report** and **Alarm Report One Alarm** collect alarm data for the selected 
time period. The **Energy Report** displays energy data over a three year period, with 
an individual graph per year and a three year summary. The **Energy Report Week** 
follows the same structure but displays data on a weekly basis, covering three weeks 
by default with an individual graph per week and a three week summary. For detailed 
configuration of each report type, see [Reports — Configuring](configuring.md).

Once generated, the report is added to the report list where it can be previewed.

## Scheduling a report in **WideQuick Runtime®** { #scheduling-a-report-in-widequick-runtime }
To schedule a report, navigate to 
**History → Reports → Reports - Schedule**.

<figure markdown="span">
  ![Report schedule](/Images/Reports/Report_schedule.png)
  <figcaption>The Report Schedule workview in WideQuick Runtime.</figcaption>
</figure>

Click **New schedule** to create a new schedule. A menu with three pages will 
appear on the right. Note that the second page changes depending on the selected 
**Report template**.

<div class="figure-row" markdown>

<figure markdown="span">
  ![Schedule page 1](/Images/Reports/Report_meny.png)
  <figcaption>Page 1 — schedule name, template, and frequency.</figcaption>
</figure>

<figure markdown="span">
  ![Schedule page 2](/Images/Reports/Report_meny2.png)
  <figcaption>Page 2 — report-specific configuration.</figcaption>
</figure>

<figure markdown="span">
  ![Schedule page 3](/Images/Reports/Report_meny3.png)
  <figcaption>Page 3 — recipients and output format.</figcaption>
</figure>

</div>

The second page mirrors the report configuration described in the previous section. 
Below are descriptions of the options on the first and third pages:

* First page

    * **Name of schedule** — The name of the schedule.
    * **Active schedule** — Toggles whether the scheduled report is active and will
    be sent.
    * **Report template** — The report template to use. Defaults to
    **Alarm_Report**. See [here](extending.md#creating-templates) for guidance on
    creating templates.
    * **Frequency** — How often the report is generated. The available options and
    their additional settings are:

        * **Daily** — Select a specific time of day. Times are available in
        30-minute intervals.
        * **Weekly** — Select a day of the week and a specific time of day.
        * **Monthly** — Select a day of the month and a specific time of day.
        The system automatically handles months with 30 or 31 days, as well as
        February and leap years.
        * **Quarterly** — Select which month of the quarter (1, 2, or 3), the
        day of that month, and a specific time of day.
        * **Yearly** — Select a month, the day of that month, and a specific
        time of day.

    * **Description of schedule** — A description of the schedule.
    !!! note
        Schedules are checked every 5 minutes. The configured time is therefore
        approximate — reports may be sent up to 5 minutes after the set time.

* Third page

    * **Subject line** — The subject line of the email in which the report is sent.
    * **Recipient** — The recipients of the email. Accepts both email addresses 
    and aliases.
    * **Alias** — Displays available aliases. Select one and click **Add** 
    to add it as a recipient.
    * **List of Recipients** — Shows the full list of recipients, indicating whether 
    each entry is an email address or an alias.
    * **Report file format** — The format in which the report is sent: PDF or Excel.

## Next Steps { #next-steps }

* [Configuring](configuring.md) — built-in report templates and report history
* [Extending](extending.md) — creating custom templates and report controllers
<!-- --8<-- [end:body] -->
