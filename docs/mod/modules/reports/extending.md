---
title: Report - Extending
description: Extend the Reports module with scripts and hooks.
product: mod
page_type: howto
doc_id: DOC-M17
status: draft
last_reviewed: 2026-05-19
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Reports - Extending
WideQuick comes with a set of default report templates, but it is also 
possible to create fully custom templates tailored to your specific needs. This section 
covers the complete process of creating a custom report template and its corresponding 
ReportController view, from designing the Excel layout to wiring it up with live data 
from the database.

Before getting started, make sure you are familiar with the basics of the report system. 
If not, see [Reports — Getting Started](get-started.md) & [Reports — Configuring](configuring.md).

## Creating templates { #creating-templates }
The process of creating your own report templates consists of three steps:

1. Design your template in Excel
2. Configure the data sheet, macros and loggers
3. Wiring it up

### Designing your template { #designing-your-template }
The first step is to design your report template in Excel. This includes deciding the 
layout, what graphs to include, and how data should be presented. WideQuick places no 
restrictions on the design — the template can be tailored freely to fit your needs.

A report template typically consists of three sheets:

* Presentation sheet — The visible part of the report. Contains graphs, tables, and 
any other visual elements the report should display.
* Data sheet — A hidden sheet containing the raw data pulled from the database. This 
sheet feeds the presentation sheet with data. The data sheet is easier to configure in 
**WideQuick Designer®**, where hidden sheets are visible, rather than directly in Excel.
* Meta sheet — A hidden sheet containing general information about the report, such as 
the report title, current date and time, selected logger, and selected signals. This 
sheet is useful for displaying report metadata on the presentation sheet.

!!! tip "Getting started"
    A good starting point is to sketch out what the final report should look like before 
    opening Excel. Knowing what data you need and how it should be presented will make 
    configuring the data sheet and macros much easier.

To add a new sheet to the template, open the template in **WideQuick Designer®** and 
navigate to the bottom of the sheet tabs. Click **Create New Sheet**, see image below. 
To hide the sheet, right-click the sheet tab and select **Hide Sheet**.

<figure markdown="span">
  ![newSheet](/Images/Reports/newSheet.png)
  <figcaption>Adding a new sheet to the template in WideQuick Designer.</figcaption>
</figure>

!!! note
    Hidden sheets are only visible in **WideQuick Designer®** and will not be visible
    in the final generated report or when opening the template directly in Excel. Try
    generating a report with the sheet visible once the macro command is set, to get a
    feel for how the data is oriented.

### Configuring the data sheet, macros and loggers { #configuring-the-data-sheet-macros-and-loggers }
The data sheet is a hidden sheet within the report template that acts as a container 
for the raw data pulled from the database. When a report is generated, WideQuick uses 
macro commands placed in the data sheet to query the database and populate it with data.

To add a macro command, right-click a cell in the data sheet and select 
**Edit Expression**. This will open the following popup:

<figure markdown="span">
  ![MacroConfigure](/Images/Reports/MacroInsertion.png)
  <figcaption>The Edit Expression popup for inserting a macro command.</figcaption>
</figure>

Below is a description of each field:

* **Variable** — Defines which signal to query. Two options are available:
    * `variable_ref[#]` — Queries a specific signal, where `#` is the index of the 
    signal. A separate macro call is required for each signal.
    * `alarms` — A wildcard that pulls all alarms in the selected logger.

* **Values** — Defines which data columns to include. Depends on the type of data 
being queried:
    * Signal data: `name`, `datetime`, `value` is typically sufficient.
    * Alarm data: `name`, `state`, `severity`, `timestamp`, `text`, `group` — include 
    only the fields needed for the report.

* **Logger** — The logger the report queries data from. This must be set statically 
and cannot be changed dynamically.
* **Fixed/Range timespan** — The reporter uses **Range timespan** by default, with 
`Report_Reference.from_time` and `Report_Reference.to_time` as the start and end times. 
These are set by the time objects in the ReportController.
* **Limit** — The maximum number of rows to populate. This is set by the user in the 
ReportController when generating the report.
* **Datetime format** — The format used for datetime values. Defaults to 
`yyyy-MM-dd hh:mm:ss` but can be adjusted to fit the needs of the report.

The placement of the macro command is important — data is populated starting from the 
cell the macro is placed in, expanding downward. The columns are determined by the 
**Values** field. For example, a signal macro with `VALUES(name, datetime, value)` will 
populate three columns starting from the macro cell:

<div class="figure-row" markdown>

<figure markdown="span">
  ![Signal macro](/Images/Reports/MacroExample.png)
  <figcaption>Signal macro placed on the data sheet.</figcaption>
</figure>

<figure markdown="span">
  ![Signal macro result](/Images/Reports/MacroExample2.png)
  <figcaption>Resulting columns populated by the macro.</figcaption>
</figure>

</div>

And for alarm data with `VALUES(name, state, severity, timestamp, text, group)`:

<div class="figure-row" markdown>

<figure markdown="span">
  ![Alarm macro](/Images/Reports/MacroAExample.png)
  <figcaption>Alarm macro placed on the data sheet.</figcaption>
</figure>

<figure markdown="span">
  ![Alarm macro result](/Images/Reports/MacroAExample2.png)
  <figcaption>Resulting columns populated for alarm data.</figcaption>
</figure>

</div>

The number of rows populated depends on the **Limit** and timespan, which are set by 
the user in the ReportController when generating the report.

!!! tip "Meta sheet"
    The Meta sheet is a useful place to store general report information that is not 
    pulled from the logger. It uses `$()` expressions to print internal or system 
    variables directly into cells. For example:

    * `$(Report_Reference.title)` — The report title set by the user.
    * `$(Report_Reference.logger)` — The logger used for the report.
    * `$(Report_Reference.from_time)` — The start time of the report.
    * `$(Report_Reference.to_time)` — The end time of the report.
    * `$(Report_Reference.limit)` — The maximum number of events.
    * `$(Report_Reference.variable_ref[#])` — The signal at index `#`.
    * `$(System.dateTime)` — The current date and time.
    * `$(System.user)` — The current user.

    The Meta sheet is the only way to pass the report title set by the user into the 
    presentation sheet. The integrator is free to include whichever fields are relevant 
    to their report.

### Wiring it up { #wiring-it-up }
With the presentation sheet designed and the data sheet populated with macro commands, 
the final step is to connect the two — linking the raw data to the graphs, tables, and 
other visual elements in the presentation sheet.

A few tips for wiring up the template effectively:

* Use the data sheet for calculations — Since the data sheet is hidden in the final 
report, it is a good place to perform intermediate calculations before passing the 
results to the presentation sheet. To edit it in Excel, temporarily unhide it.
* Keep calculations away from the macro data — Since macro data expands downward row 
by row, place any additional calculations in columns further to the right to avoid 
conflicts.
* Reference the data sheet from the presentation sheet — Graphs, bars, and other 
visual elements in the presentation sheet should reference cells in the data sheet 
rather than containing logic themselves. This keeps the presentation sheet clean and 
easier to maintain.
* Use fixed ranges that cover the maximum possible rows — Since the amount of data 
varies depending on the **Limit** and timespan, define ranges that cover the maximum 
number of rows your report could produce. Use `IFERROR` to handle empty cells 
gracefully.

!!! note
    This guide does not cover Excel formula design in depth — the possibilities are 
    largely up to the integrator. The tips above are specific to working with WideQuick 
    macro data.

## Creating the ReportController view { #creating-the-reportcontroller-view }
With the template created, the next step is to build the ReportController view.
This view determines which signals and data are sent to the report when it is generated.
The system links a ReportController to a report template by matching their names, so it
is important that the view is named exactly the same as the report template.

To get started, navigate to **Templates** in the project tree and duplicate the
**Template_ReportController** view. Move the duplicate to the **ReportController** 
folder and rename it to match the report template name.

When a ReportController view is loaded, its template script initializes a `view.data`
object with default values such as report type, time span, logger, and signal references.
Each object placed in the view — such as `to_time`, `Report_CustomTitle`, and 
`LoggerList` — reads from and writes to this shared `view.data` object as the user 
interacts with them.

When `Button_CreateReport` object is clicked, it collects the complete `view.data` 
object and adds it to a report queue via `scReports.addReportToQueue()` function. 
Reports in the queue are processed one at a time — `scReports` script populates a 
global **Report_Reference** object with the queued data, which the macro commands in 
the data sheet read from when querying the database.

The correct template is identified and triggered using the `report_type` field in
`view.data`, which is derived directly from the ReportController view name. This is why
it is critical that the ReportController view name exactly matches the report template
name — if they differ, `scReports` script will not be able to locate and trigger the 
correct template.

!!! warning "Naming convention"
    The ReportController view name must exactly match the report template name. If they
    differ, `scReports` script will not be able to locate and trigger the correct template.

To build the view, a set of premade objects is available in the object library under
**Report**. Below is a description of each object and when to use it:

| Object | Use when |
|---|---|
| `LoggerList` | You need the user to select signals from a logger |
| `LarmLogger_list` | You need the user to select alarms from an alarm logger |
| `Report_CustomTitle` | You want the user to set a custom report title |
| `Button_CreateReport` | Always — this is required to generate the report |
| `Report_output_type` | You want the user to choose between PDF and Excel output |
| `to_time` | You need the user to set an end time |
| `from_time` | You need the user to set a start time |
| `to_time_Singel` | The report uses a fixed time span (e.g. last 3 years) |
| `Numbe_of_event` | You need to limit the number of collected events |

### LoggerList { #loggerlist }
The `LoggerList` object is a TreeView configured to display the signals logged by a 
specific logger. When a signal is selected, a green checkmark appears next to it in the 
TreeView. The object also includes two text boxes showing the currently selected logger 
and the number of signals selected out of the maximum allowed.

The logger to display and the maximum number of selectable signals are both configured 
as properties on the object. Assign the desired values when placing the object in a 
ReportController.

### LarmLogger_list { #larmlogger_list }
The `LarmLogger_list` object is a specialized version of `LoggerList`, purpose-built 
for displaying alarms logged by a logger. Unlike `LoggerList`, it automatically builds 
its tree based on alarm groups and omits redundant information. For example, if all 
alarms in the logger follow the pattern `AS01.AS01_XXX_XX`, the TreeView will display 
them simply as `XXX_XX`.

This object has two properties that must be configured:

* **Logger** — Determines which logger the TreeView is built from. This should always 
match the logger that the report queries.
* **Signals** — Controls how many signals can be selected for the report. The default 
maximum is 15, but this can be changed — see [here](#changing-the-maximum-of-signals-to-be-selected). 
This property should always be set to a numerical value, unless the TreeView is 
intentionally locked.

### Report_CustomTitle { #report_customtitle }
The `Report_CustomTitle` object consists of a label and a text box. The text box sets 
the title of the report and is configured to communicate with the active data on the 
view.

### Button_CreateReport { #button_createreport }
The `Button_CreateReport` object is a button that triggers report generation. When 
clicked, it gathers data from the view and sends it to the `scReports` script to create 
the report.

### Report_output_type { #report_output_type }
The `Report_output_type` object consists of a label and a ComboBox. The selected 
ComboBox value determines whether the report is generated as a PDF only, or as both a 
PDF and an Excel file.

### to_time { #to_time }
The `to_time` object consists of a label and a DateTime editor. The DateTime editor 
sets the end time of the report and is configured to report its current value to the 
view.

### from_time { #from_time }
The `from_time` object works the same way as the `to_time` object, but sets the start 
time of the report instead.

### to_time_Singel { #to_time_singel }
The `to_time_Singel` object combines the functionality of `to_time` and `from_time` 
into a single object. It is used when the report template requires a fixed time span. 
The following properties can be configured:

* **Years prior** — Sets the time span in years.
* **Weeks prior** — Sets the time span in weeks.

Note that these two properties are mutually exclusive — weeks and years cannot be 
combined.

### Numbe_of_event { #numbe_of_event }
The `Numbe_of_event` object consists of a label and a SpinBox. The SpinBox value 
determines how many events are collected per macro call. This distinction is important:

* If the `alarms` wildcard is used, the value represents the **total** number of events.
* If `variable_ref[#]` is used, the value represents the number of events **per signal**.

## Changing the maximum of signals to be selected { #changing-the-maximum-of-signals-to-be-selected }
In the default reporter settings 15 signals are allowed to be selected for report 
generations. This can easily be changed if more signals are required. First, in 
**WideQuick Designer®** navigate to **Data Types → Arrays → variable_ref** and select 
**Properties...**. This will bring up the following popup:

<figure markdown="span">
  ![Variable Array](/Images/Reports/Variabel_ref.png)
  <figcaption>The variable_ref array properties popup.</figcaption>
</figure>

Change the **Max. size** to the desired value. Click **Apply** then **Ok**. The 
**Report_Reference** array has now been updated.

Next, update the `scReports` script to handle the new size. Locate the 
`createReport()` function and change the value `15` to your new **Max. size** value:

``` javascript title="scReports — createReport() — before"

for (var i = 0; i < 15; i++) Report_Reference.variable_ref[i] = "";
var signals = reportObj.variable_ref.split(',');
for (var i = 0; i < signals.length && i < 15; i++) Report_Reference.variable_ref[i] = signals[i];

```

``` javascript title="scReports — createReport() — after"

for (var i = 0; i < YOUR_MAX_VALUE; i++) Report_Reference.variable_ref[i] = "";
var signals = reportObj.variable_ref.split(',');
for (var i = 0; i < signals.length && i < YOUR_MAX_VALUE; i++) Report_Reference.variable_ref[i] = signals[i];

```
<!-- --8<-- [end:body] -->
