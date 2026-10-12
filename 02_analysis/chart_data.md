# Chart Data — Underlying Tables

Source: 02_analysis/coded_reviews.csv
Date: 11/10/26

---

## Chart 1 — Theme Pareto (underlying table)

Excludes generic reviews. n = 229 actionable.

| Rank | Theme | Count | % of actionable | Cumulative % |
|------|-------|-------|-----------------|--------------|
| 1 | app functionality error | 41 | 17.9% | 17.9% |
| 2 | booking failure | 23 | 10.0% | 27.9% |
| 3 | feature request | 22 | 9.6% | 37.6% |
| 4 | UI confusing | 16 | 7.0% | 44.5% |
| 5 | login failure | 12 | 5.2% | 49.8% |
| 6 | route planning inaccurate | 12 | 5.2% | 55.0% |
| 7 | app launch failure | 11 | 4.8% | 59.8% |
| 8 | drop location error | 11 | 4.8% | 64.6% |
| 9 | GPS wrong location | 10 | 4.4% | 69.0% |
| 10 | driver could not be contacted | 8 | 3.5% | 72.5% |
| 11 | positive experience | 8 | 3.5% | 76.0% |
| 12 | cancel without confirmation | 7 | 3.1% | 79.0% |
| — | Other (13 themes) | 48 | 21.0% | 100.0% |

**Key insight:** Top 5 themes = 49.8% of actionable. Top 12 themes = 79.0%.

---

## Chart 2 — Severity Distribution (underlying table)

Excludes generic. n = 229.

| Severity | Count |     % |
| -------- | ----: | ----: |
| Blocker  |    47 | 20.5% |
| Friction |   174 | 76.0% |
| Cosmetic |     8 |  3.5% |


## Chart 3 — Journey Stage × Severity Matrix

Excludes generic. Multi-stage reviews counted once per stage they mention.

| Journey stage          | Blocker | Friction | Cosmetic |
| ---------------------- | ------: | -------: | -------: |
| Onboarding             |      12 |       30 |        1 |
| Shift/Roster           |       5 |       24 |        0 |
| Self-Booking           |      12 |       33 |        1 |
| Cab/Shuttle Assignment |      17 |       90 |        5 |
| Route Planning         |       2 |       37 |        2 |
| Pickup Time            |       5 |       23 |        3 |
| Live Tracking          |      15 |       72 |        4 |
| Boarding               |       2 |       12 |        1 |
| Drop                   |       3 |       27 |        2 |
| Issue Escalation       |       7 |       32 |        1 |


**Key insight:** Cab/Shuttle Assignment (112) and Live Tracking (91) dominate.

---

## Cross-Reference

These tables are the source of truth for:
- Findings narrative (02_analysis/findings_narrative.md)
- Rating-lift model (02_analysis/rating_lift_model.md)
- Executive memo (05_submission/executive_memo_draft.md)
- Charts in 02_analysis/*.png

Every claim in the final submission must trace back to a number in these tables.