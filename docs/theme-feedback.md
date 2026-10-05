# Theme feedback workflow

Open `theme-feedback.html` from a local HTTP server or the project gallery.
Choose a theme and example, draw a box around the issue, select its type and
severity, and describe the expected result. Download the JSON report and add
it to the next theme review or agent task.

The report format is:

```json
{
  "format": "theme-feedback",
  "version": 1,
  "reports": [{
    "schemaVersion": 1,
    "createdAt": "ISO-8601 timestamp",
    "theme": "theme slug",
    "page": "example HTML file",
    "viewport": {"width": 0, "height": 0},
    "selection": {"x": 0, "y": 0, "width": 0, "height": 0},
    "element": {"selector": "best-effort selector", "text": "sample"},
    "issue": "issue category",
    "severity": "Minor | Needs attention | Blocking",
    "comment": "expected result or observed problem"
  }]
}
```

Selection geometry is normalized to the preview stage so it remains useful
when the report is opened at another window size. Element selector and text
are hints, not stable locators. Reports contain no screenshots or user data
beyond the selected element's short visible text and the comment.

## Agent review

For each report, inspect the named theme and page, reproduce the issue, check
the same component in a contrasting theme family, and fix the shared CSS rule
when the issue is shared. Prefer CSS and native browser behavior over JS for
style, state, interaction, and animation. Record unverified visual judgments
for human review; do not claim the report alone proves a fix.
