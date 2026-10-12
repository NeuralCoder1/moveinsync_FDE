# Claude Conversation — Qualitative Coding Thread

- URL: https://claude.ai/share/d869fcea-aacf-4b40-a8d2-84e289339b6d
- Started: 11/10/2026
- Purpose: Code Play Store reviews against the journey-stage taxonomy from the case study PDF. Identify severity, theme, verbatim quotes, and fixability.

## Coding Protocol (Locked)

For each review:
1. **Row ID** — CSV row index, first column
2. **Journey stage(s)** — one or more from the 10-stage taxonomy
3. **Severity** — Blocker / Friction / Cosmetic
4. **Theme tag** — 2–4 word label
5. **Verbatim quote** — exact text, original script, no paraphrasing
6. **Gloss** — English translation if non-English
7. **Fixability** — App-fix / Vendor-ops / Employer-policy, with "(?)" for ambiguous cases

## Rules
- Multi-stage reviews: list all stages, one severity, one theme, one quote per row
- Non-English: quote verbatim in original, gloss in separate column
- Unclassifiable: mark "Unclassifiable / no stage", Cosmetic severity
- Fixability ambiguity: pick primary owner, flag with "(?)"

## Batch size
40 reviews per message

## Batches sent

| # | Date | # of reviews | Rating filter | Sort | Verified |
|---|------|--------------|---------------|------|----------|
| 1 | 2026-10-11 | 40 (rows 1–40) | None (all ratings) | CSV order as-is, newest first at the top | Quotes checked against the CSV (40/40 exact). Your spot-check is pending. |

Batch 1 is the only batch so far. The CSV has 24,314 reviews, so 24,274 are not yet coded.