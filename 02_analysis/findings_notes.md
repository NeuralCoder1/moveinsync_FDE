# Findings — Working Notes

This file accumulates sections for the final `findings_narrative.md`. It will be assembled in Phase 2, Step 2.4.

---

## Section A — The Rating Is a Legacy Metric
[to be written in Step 2.4]

---

## Section B — The Rating Cannot Be Fixed by Bug Fixes Alone
[to be written in Step 2.4]

---

## Section C — Fix and Why It's Not What You Expect
[to be written in Step 2.4]

---

## Section D — Three Strategies (A/B/C)
[to be written in Step 2.4]

---

## Section E — Enterprise Channel
[to be written in Step 2.4]

---

## Section F — The Proof
[to be written in Step 2.4]

---

## Scratch notes (from earlier steps)

### Model output — two-lever rating projection
- Base case: 4.64 → 4.6372 in 6 months (ordinary incoming reviews assumed 4.3★)
- Pipeline rebuilt: 4.6425 in 6 months, 4.6492 in 24 months
- Long-run ceiling: 4.418
- Base case falls below 4.5 after about 66.1 years; remains above 4.4 at its 4.418 ceiling

### Key insight
The displayed rating is cumulative and lags current review flow.
Under the model's assumptions, bug fixes protect users and reduce negative reviews but do not lift the displayed rating from its current 4.64.
The rating should be managed while the underlying product improves.

### Strategy summary
- Track A: Stop the bleeding (bug fixes, P0, 2 sprints)
- Track B: Rebuild review pipeline (in-app prompts, P0, parallel)
- Track C: Enterprise channel (nudges through client transport desks, P1)
- Track D: Monitor & iterate (dashboard, ongoing)