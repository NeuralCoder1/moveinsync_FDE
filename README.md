# MoveInSync Play Store Rating — Case Study Submission

**Author:** Looknath Das | **Submitted:** October 12, 2026 | **Role:** Forward Deployed Engineer, MoveInSync

## Executive summary

MoveInSync's Play Store listing displays a **4.64★** rating. In contrast, the
24,314 most recent reviews collected for this case study average **3.61★**;
approximately **26%** of the sample are 1★ reviews. The evidence points to a
bimodal satisfaction problem obscured by the historical rating.

Coding 320 reviews against the case study's 10-stage journey taxonomy found:

- The five leading themes account for about **50% of actionable complaints**.
- **90.6%** of coded complaints are labeled **App-fix**.
- **20.5%** are **Blockers**: users could not complete their task.
- **Cab/Shuttle Assignment (35%)** and **Live Tracking (28%)** are the most
  frequently mentioned journey stages, together accounting for about 63% of
  coded reviews.

A two-lever rating-lift model suggests the displayed rating is structurally
slow to change. With a denominator of 115,000 reviews, bug fixes alone cannot
move the headline rating materially. Even rebuilding the review pipeline to
generate three times the volume with a 60% 5★ share projects a rating of only
4.649 in 24 months.

**Recommendation:** Run four tracks in parallel: address P0 product failures;
rebuild the review pipeline with in-app prompts and a 100% reply SLA; complete
crash remediation and enterprise outreach this quarter; and replace the
displayed rating as the primary success measure with live leading indicators.

**Live dashboard:** [Open the dashboard](https://neuralcoder1.github.io/moveinsync_FDE/)

**Full submission:** [PDF](05_submission/final_submission.pdf)

## Repository guide

This repository contains the evidence behind the recommendation: source data,
coded reviews, analysis, model, prioritized backlog, engineering specification,
dashboard, and final submission.

```text
00_setup/             Process artifacts, assumptions, and source log
01_raw_data/           Play Store data and secondary sources
02_analysis/           Coded reviews, analysis, charts, and model
03_recommendations/    Prioritized backlog and P0 engineering spec
04_dashboard/          Self-contained dashboard
05_submission/         Final PDF, Markdown source, and methodology appendix
```

### `00_setup/` — Process trail

| File | Purpose |
| --- | --- |
| [assumptions.md](00_setup/assumptions.md) | Ten falsifiable hypotheses written before data collection, with confirmation status |
| [ai_workflow.md](00_setup/ai_workflow.md) | Log of AI tools used, where they helped, and where they were wrong |
| [data_sources.md](00_setup/data_sources.md) | Sources, extraction methods, and verification status |
| [chatgpt_conversation.md](00_setup/chatgpt_conversation.md) | Reference to the data-engineering thread and verified app identity |
| [claude_conversation.md](00_setup/claude_conversation.md) | Reference to the qualitative-coding thread and locked protocol |
| [rating_discrepancy_note.md](00_setup/rating_discrepancy_note.md) | Reconciliation of the 4.3, 4.37, and 4.64 rating snapshots |

### `01_raw_data/` — Raw evidence

| File | Purpose |
| --- | --- |
| [moveinsync_reviews.csv](01_raw_data/moveinsync_reviews.csv) | 24,314 scraped Play Store reviews, dated 2014–2026 |
| [moveinsync_metadata.json](01_raw_data/moveinsync_metadata.json) | Store snapshot: 4.6382785★ across 114,872 ratings, retrieved October 11, 2026 |
| [scraper.py](01_raw_data/scraper.py) | Reproducible Play Store scraping script using `google-play-scraper` |
| [data_summary.md](01_raw_data/data_summary.md) | Star distribution, year breakdown, and average-by-window calculations |
| [helpcenter_articles.md](01_raw_data/helpcenter_articles.md) | Documented failure modes from MoveInSync's Help Center |
| [company_blog_rating_recovery.md](01_raw_data/company_blog_rating_recovery.md) | Company's historical rating-recovery story |
| [appstore_reviews.md](01_raw_data/appstore_reviews.md) | iOS complaints used as a cross-platform signal |
| [employee_reviews.md](01_raw_data/employee_reviews.md) | AmbitionBox and Glassdoor culture signals |
| [social_mentions.md](01_raw_data/social_mentions.md) | Public Mastodon, X, and Reddit mentions |
| [competitor_benchmarks.md](01_raw_data/competitor_benchmarks.md) | Competitor research for Safetrax, Quick Ride, and sRide |
| Screenshots | Source-page verification for the Play Store listing, Glassdoor, Help Center, and other sources |

### `02_analysis/` — Analysis and model

| File | Purpose |
| --- | --- |
| [coded_reviews.csv](02_analysis/coded_reviews.csv) | 320 reviews coded against the 10-stage journey taxonomy |
| [coded_reviews.md](02_analysis/coded_reviews.md) | Human-readable coded dataset, organized into eight batches |
| [summary_statistics.md](02_analysis/summary_statistics.md) | Theme frequency, severity, fixability, and journey-stage counts |
| [chart_data.md](02_analysis/chart_data.md) | Source tables for the analysis charts |
| [theme_pareto.png](02_analysis/theme_pareto.png) | Leading themes in negative reviews |
| [severity_distribution.png](02_analysis/severity_distribution.png) | Blocker, Friction, and Cosmetic distribution |
| [journey_stage_heatmap.png](02_analysis/journey_stage_heatmap.png) | Journey stage by severity |
| [rating_lift_model.md](02_analysis/rating_lift_model.md) · [CSV](02_analysis/rating_lift_model.csv) | Two-lever rating projection with pessimistic, base, and optimistic scenarios |
| [findings_narrative.md](02_analysis/findings_narrative.md) | Sourced diagnosis in six sections |
| [monitoring_playbook.md](02_analysis/monitoring_playbook.md) | Metrics, cadence, owners, alerts, and interpretation |

### `03_recommendations/` — Recommendations

| File | Purpose |
| --- | --- |
| [prioritized_backlog.md](03_recommendations/prioritized_backlog.md) | Prioritized P0/P1/P2 backlog, reconciled to 221 actionable reviews |
| [sprint_spec_p0.md](03_recommendations/sprint_spec_p0.md) | Engineering-ready P0 specification, with evidence, rollback plan, and A/B design |

### `04_dashboard/` — Dashboard

| File | Purpose |
| --- | --- |
| [dashboard.html](04_dashboard/dashboard.html) | Self-contained dashboard |

The dashboard is deployed to GitHub Pages by the workflow in
[deploy-pages.yml](.github/workflows/deploy-pages.yml). See the live-dashboard
link above; replace its username placeholder before publishing.

### `05_submission/` — Final submission

| File | Purpose |
| --- | --- |
| [final_submission.pdf](05_submission/final_submission.pdf) | Complete six-section submission |
| [executive_memo_draft.md](05_submission/executive_memo_draft.md) | Executive memo draft |
| [methodology_and_ai.md](05_submission/methodology_and_ai.md) | Methodology, tools used, and AI limitations |
| [final_submission.md](05_submission/final_submission.md) | Markdown source for the PDF |
| [final_submission.html](05_submission/final_submission.html) | HTML version of the submission |

## Methodology at a glance

### Data collection

- **Primary source:** `google-play-scraper` collected 24,314 reviews for package
  `com.moveinsync.ets`, dated March 14, 2014 to October 9, 2026.
- **Store metadata:** The snapshot in `moveinsync_metadata.json` records a
  4.6382785★ rating across 114,872 ratings, retrieved October 11, 2026.
- **Secondary sources:** MoveInSync's Help Center and rating-recovery blog,
  App Store reviews, AmbitionBox, Glassdoor, and public social mentions.
- **Verification:** Claims trace to source files or saved screenshots.

### Review coding

The 320 coded reviews are organized into eight batches: high-thumbs-up 1★,
recent 1★, random 1★, 2★, 3★, 4★, 1★ by app version, and random 5★. Each review
was tagged with:

1. One or more journey stages from the case study's 10-stage taxonomy.
2. Severity: Blocker, Friction, Cosmetic, or Unclassifiable.
3. A consistent theme tag.
4. The verbatim review quote.
5. An English translation, where needed.
6. Fixability: App-fix, Vendor-ops, or Employer-policy.

### Rating-lift model

The model separates two levers:

- **Reduce incoming negative reviews** through product fixes.
- **Increase incoming positive reviews** through in-app prompts and a reply SLA.

It compares pessimistic, base, and optimistic scenarios, plus a rebuilt-review
pipeline variant with three times the monthly volume and a 60% 5★ share.

At the current review velocity, the model estimates a long-run rating ceiling
of **4.418** and approximately **212 years** to reach 4.4. Even the
pipeline-rebuilt scenario reaches only **4.649 in 24 months**. The displayed
rating is a lagging indicator of past product states, not a live measure.
These are assumption-driven projections, not measured outcomes; assumptions
are documented in the [model](02_analysis/rating_lift_model.md).

## Recommendation at a glance

| Track | Timing | Focus |
| --- | --- | --- |
| **A — P0 product fixes** | Sprints 1–2, four weeks | Booking-state persistence, cancel-confirmation UX, OTP and notification reliability, and the top three feature requests |
| **B — Review pipeline** | In parallel | In-app post-trip rating prompts and a 100% reply SLA for 1★–2★ reviews within seven days |
| **C — P1 improvements** | This quarter | Crash remediation, GPS/ETA improvements, and enterprise transport-desk outreach |
| **D — Leading indicators** | Ongoing | Track rolling 90-day rating, blocker rate, theme mix, review velocity, 5★ share, reply rate, and enterprise retention |

**Bottom line:** The displayed rating cannot be fixed in a quarter. It is a
12–24 month structural project. Product fixes stop the bleeding; rebuilding
the review pipeline is what moves the number over time.

## AI usage

AI tools were used deliberately and transparently. The full account is in the
[methodology and AI appendix](05_submission/methodology_and_ai.md).

- **ChatGPT (Code Interpreter):** Play Store scraping, pandas analysis, chart
  generation, and rating-lift calculations.
- **Built-in coding bot:** Qualitative review coding, prioritization, spec
  drafting, and cross-file consistency checks.
- **Claude:** Early coding-protocol design, assumption drafting, and final
  synthesis.

AI-generated claims were checked against source material. For example, the
rating snapshot was corrected from an earlier 4.3 figure to 4.64; employee
review scores were verified against screenshots; a social-media claim was
verified against its post; enterprise-customer attribution was corrected; and
an engineering estimate was revised from 1–2 sprints to 3–4 two-week sprints.
Unverified claims were removed.

## Limitations

- **Sample size:** Scraper pagination is capped at approximately 24,000
  reviews, compared with about 114,872 store ratings. The sample is not the
  full review population.
- **Self-selection bias:** Play Store reviewers may skew negative; satisfied
  users may be less likely to leave a review.
- **Single-coder reliability:** One coder, assisted by AI, coded the sample;
  there was no independent second-coder check.
- **Device and OS data:** Reviews do not provide structured device-model data;
  device references in the spec are anecdotal.
- **Reply cadence:** Current company reply cadence is not publicly verified.
- **Projection assumptions:** The rating-lift model is a projection, not a
  measurement; its assumptions are stated in the model file.

## Suggested reading order

1. [Executive memo draft](05_submission/executive_memo_draft.md) — concise overview and recommendation
2. [Findings narrative](02_analysis/findings_narrative.md) — the diagnosis
3. [Prioritized backlog](03_recommendations/prioritized_backlog.md) — what to fix, in order
4. [Sprint-ready P0 spec](03_recommendations/sprint_spec_p0.md) — one ticket in depth
5. [Rating-lift model](02_analysis/rating_lift_model.md) — why bug fixes alone do not move the needle
6. [Monitoring playbook](02_analysis/monitoring_playbook.md) — how to monitor rating health
7. [Methodology and AI appendix](05_submission/methodology_and_ai.md) — methods, tools, and verification
8. [Full PDF submission](05_submission/final_submission.pdf) — assembled submission

## License and data

This is a case study submission. The analysis, code, and written work are the
author's own. Data was collected from publicly available sources, including
Google Play, the App Store, MoveInSync's Help Center, AmbitionBox, Glassdoor,
and public social media.