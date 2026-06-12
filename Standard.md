# WideQuick Documentation — Style Guide

## Text Formatting

### Object names
Object names are formatted as inline code. Always refer to them with the word "object"
to distinguish them from script references.

Syntax: `ObjectName` object

Examples: `LoggerList` object, `to_time_Singel` object, `Numbe_of_event` object

---

### UI elements
Buttons, menus, dropdowns, and other UI elements are formatted as bold.

Syntax: `**UI Element**`

Examples: **Skapa Rapport**, **Hide Sheet**, **Edit Expression**

---

### Script and code references
Script names, functions, properties, and code references are formatted as inline code.
Always refer to scripts with the word "script" and functions with the word "function"
to distinguish them from object names.

Syntax: `scriptReference`

Examples: `scReports` script, `view.data`, `variable_ref[#]`, `addReportToQueue()` function

---

### File and path references
File names and paths are formatted as inline code.

Syntax: `FileName`

Examples: `Template_ReportController`, `scReports.js`

---

### Navigation paths
Navigation paths use bold with arrows as separators.

Syntax: `**Step → Step → Step**`

Examples: **Historik → Rapporter → Rapporter - Lista**

---

### Product names
The registered trademark symbol and bold formatting apply only to **WideQuick Designer®** and **WideQuick Runtime®**. These are the two named software products.

The framework itself is referred to as "WideQuick MOD" in prose and "WideQuick Modular Framework" in frontmatter and formal descriptions. Neither form gets the bold + ® treatment.

Syntax: `**Product Name®**`

Examples: **WideQuick Designer®**, **WideQuick Runtime®**

---

## Lists

### Bullet lists
Always use `*` for bullet lists.

### Numbered lists
Use numbered lists when the order of steps matters.

### Nested lists
Nested lists use four spaces of indentation.

---

## Admonitions

Syntax: `!!! type "Title"`

### Note
Use for important information the reader should be aware of but that won't cause
issues if missed.

### Info
Use for contextual background or supplementary details that help the reader understand
but are not required to follow the instructions.

### Tip
Use for helpful suggestions or best practices.

### Warning
Use for information that could cause issues or break functionality if not followed.

---

## Code blocks

### Language identifier
Always specify the language identifier.

| Language | Identifier |
|---|---|
| Scripts | `javascript` |
| Excel formulas | `excel` |
| Markdown examples | `markdown` |
| YAML configuration | `yaml` |
| TOML configuration | `toml` |

### Title
Use a title to reference the script and function where the change should be made,
rather than specific line numbers. Line numbers may change as scripts are updated.

Syntax: ```` ```javascript title="scReports — createReport()" ````

### Before and after
When showing a change, use two code blocks with descriptive titles.

Syntax: ```` ```javascript title="scReports — createReport() — before" ````

Syntax: ```` ```javascript title="scReports — createReport() — after" ````

---

## Images

Images are stored under `docs/assets/` and referenced with a path relative to the current file.

### Single image
Single images are centered using the align attribute.

Syntax: `![Alt text](../assets/images/example.png){align=center}`

### Side by side images
Side by side images use a flex div with a gap of `0.5rem`.

```markdown
<div markdown style="display: flex; justify-content: center; align-items: center; gap: 0.5rem;">

![img1](../assets/images/example-a.png)

![img2](../assets/images/example-b.png)

</div>
```

### Image sizing
Use height in pixels to control image size when images need to match.

Syntax: `![Alt text](../assets/images/example.png){style="height:400px;"}`

---

## Headings

### Page title
H1 is used for the page title only.

### Major sections
H2 is used for major sections.

### Subsections
H3 is used for subsections.

### Object or component descriptions
H3 is used for individual object or component descriptions.

### Anchors
Every H2 and H3 heading must have an explicit anchor tag. This keeps cross-references stable if a heading is renamed or translated — the anchor stays fixed regardless of what the heading text says.

Syntax: `## Heading text { #anchor-id }`

Anchor naming rules — apply in order:
1. Lowercase everything
2. Replace ` — ` (em-dash with spaces) with `-`
3. Replace ` - ` (hyphen with spaces) with `-`
4. Replace spaces with `-`
5. Remove: `®` `(` `)` `[` `]` `.` `:` `,` `'` `"` `!` `?`
6. Collapse multiple consecutive hyphens into one
7. Remove leading and trailing hyphens

Examples:

```markdown
## Remote Alarms { #remote-alarms }
### Alarm - List { #alarm-list }
### Configuring SMTP in WideQuick Designer® { #configuring-smtp-in-widequick-designer }
## Step 1 — Generate the theme { #step-1-generate-the-theme }
```

### Cross-references
When linking to a section in another file, always use the explicit anchor ID.

Syntax: `[Link text](file.md#anchor-id)`

Examples:

```markdown
See [Remote Alarms](../guides/remote-systems.md#remote-alarms) for setup instructions.
See [GoTo in Alarm Groups](../Navigation/extending.md#goto-in-alarm-groups) for setup instructions.
```

---

## Navigation pages

Navigation pages provide a brief introduction to the section and links to all
subsections. They follow this structure:

* A short introduction paragraph explaining what the section covers.
* A horizontal rule `---` between each guide group.
* Each guide group has an H3 heading that links to the guide.
* Each entry under the guide is a bullet point with a bold link and a short description
separated by a dash.

Syntax:
```markdown
### [Guide Title](guide.md)
* [**Section Title**](guide.md#section-anchor) — Short description of what it covers.
```

Example:
```markdown
### [Get started](get-started.md)
* [**Setting up the Reporter**](get-started.md#setting-up-the-reporter) — How to add
and configure report templates in **WideQuick Designer®**.
```

---

## Prose Style

### Voice
Write in the third person or use the imperative for instructions. Avoid second-person "you" and "your".

| Avoid | Prefer |
|---|---|
| You can configure this in Designer. | This is configured in Designer. |
| Select your language from the dropdown. | Select the language from the dropdown. |

---

### Em-dashes in sentences
Do not use em-dashes (—) as parenthetical separators or clause connectors in prose. Restructure the sentence instead.

| Avoid | Prefer |
|---|---|
| Text — labels and headers — is picked up automatically. | Labels and headers are picked up automatically. |
| Rename the object — this makes it easier to find later. | Rename the object. This makes it easier to find later. |

Em-dashes are still correct in list descriptions (`* **Item** — description`) and navigation paths (`**Step → Step**`).

---

## Frontmatter

Every page must have a YAML frontmatter block. Fields and their valid values:

| Field | Required | Values / notes |
|---|---|---|
| `title` | Yes | Plain text. Shown in the browser tab and nav. |
| `description` | Yes | One sentence. Used by search and meta tags. |
| `product` | Yes | `mod`, `bms`, `wwt`, or `wq` |
| `page_type` | Yes | `concept`, `guide`, `reference`, `troubleshooting` |
| `doc_id` | Recommended | Ticket reference, e.g. `DOC-M9`. Used to track coverage. |
| `status` | Yes | `draft` or `published` |
| `last_reviewed` | Yes | ISO date, e.g. `2026-06-11` |

Example:

```yaml
---
title: Calendar
description: Schedule recurring events and maintenance deadlines across the installation.
product: mod
page_type: concept
doc_id: DOC-M13
status: draft
last_reviewed: 2026-06-11
---
```

---

## Transclusion

Content is shared between products using the pymdownx snippets `--8<--` syntax. The source file wraps its shareable content in named markers; consumer files include it by reference.

### Marking content in the source file

```markdown
<!-- --8<-- [start:body] -->

# Page content here

<!-- --8<-- [end:body] -->
```

### Including content in a consumer file

```markdown
---
title: Calendar — Configuring
---

--8<-- "mod/modules/calendar/configuring.md:body"
```

The path is relative to `docs/` (the snippets `base_path`). Always use the `:body` suffix to include only the marked region, not the full file.