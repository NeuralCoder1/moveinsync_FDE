# Engineering Ticket: Release Stability for Booking and Live Tracking

## 1. Title

**P0: Prevent Android launch and runtime crashes across booking and live tracking**

## 2. Owner

**Engineering — Android Mobile / Client Reliability** (proposed team; confirm the internal team name and on-call owner at kickoff).

## 3. Priority

**P0** — addresses a 59-review grouped stability cluster in the prioritized backlog, including 21 Blocker and 38 Friction reviews. The four explicitly scoped themes account for 55 coded reviews: app functionality error (41), app launch failure (11), app crash during booking (2), and app crash during tracking (1). The backlog's 59 total also includes app slow (4).

## 4. Problem statement and evidence

Users report that the app becomes unavailable after updates, hangs during startup, or crashes during core booking and tracking tasks. These failures can leave employees unable to arrange a ride or see and contact their assigned driver.

| Theme | Severity | Source review | Verbatim quote |
| --- | --- | --- | --- |
| app functionality error | Blocker | [row_id 21171](../02_analysis/coded_reviews.csv#L2) | "Not expected out of such time bounded work we do and need to reach on time to work, this causes a lot of issue with missing the cab." |
| app functionality error | Friction | [row_id 16157](../02_analysis/coded_reviews.csv#L18) | "Initially the app was working fine but after the update it's become worst." |
| app launch failure | Friction | [row_id 12020](../02_analysis/coded_reviews.csv#L4) | "It worked for 2 days after installation but now app itself is not opening (shows only opening screen)." |
| app launch failure | Blocker | [row_id 10967](../02_analysis/coded_reviews.csv#L13) | "App stuck on splash screen." |
| app crash during booking | Friction | [row_id 3073](../02_analysis/coded_reviews.csv#L14) | Excerpt: "The app frequently crashes or hangs while booking cabs" |
| app crash during tracking | Blocker | [row_id 15488](../02_analysis/coded_reviews.csv#L9) | Excerpt: "move in sync keeps stopping" |

## 5. Business impact

Stability failures affect core employee workflows and can cause missed rides, loss of live trip visibility, and inability to contact a driver. They also generate new low-star complaints and undermine enterprise confidence in the service.

The rating-lift model places app functionality error (41 coded reviews) inside its top-five portfolio. Starting from the authoritative 4.64 rating, the model's Base case estimates 22.8 negative reviews prevented over six months and 144 additional prompted 5-star reviews, projecting 4.6372 because ordinary incoming reviews are assumed to average 4.3. This is a portfolio-level estimate; the model does **not** isolate the rating impact of this stability fix.

## 6. Root cause hypothesis

**Hypothesis, not confirmed cause:** release changes may be introducing regressions that escape booking, tracking, and cold-start regression coverage. Reports include crashes or startup failure after an update (row_ids 16157, 15488), an app that stops opening after two days (12020), and splash-screen hangs (10967). This is consistent with gaps in release-specific instrumentation, lifecycle/network/error-path coverage, or a crash-free release gate.

The coded reviews do not establish whether a crash-free gate currently exists, identify a responsible code change, or demonstrate an iOS QA gap. Validate those points by reviewing recent release crash telemetry, CI gates, and regression coverage before attributing root cause.

## 7. Proposed fix

1. **Instrument crashes and non-fatal failures.** Integrate Firebase Crashlytics (or the existing approved Sentry deployment). Tag events with app version, Android API level, device model, and flow (`startup`, `booking`, `tracking`); do not include trip, employee, or other sensitive identifiers. Establish pre-change crash-free-session and crash-rate baselines.
2. **Gate staged promotion on stability.** Define crash-free sessions >99.5% over a rolling 14-day window for the eligible cohort. A release cannot advance to the next rollout stage unless the threshold and the no-regression guardrails pass. Set a minimum session count for each cohort before evaluating the rate.
3. **Add device-matrix coverage.** The review data has no structured device/OS columns. The following are anecdotal quote mentions; use them as smoke-test candidates, not verified crash correlations:

	| Device / OS as reported | Review evidence | Test use |
	| --- | --- | --- |
	| vivo V25 Pro; OS not stated | [row_id 105](../02_analysis/coded_reviews.csv#L72), app launch failure | Include in launch/crash smoke testing if available. |
	| OnePlus 12; Android version not stated | [row_id 88](../02_analysis/coded_reviews.csv#L68), generic review | Exploratory current-device smoke test; generic theme, not a confirmed stability-coded report. |
	| Pixel 8; Android 17 as reported | [row_id 89](../02_analysis/coded_reviews.csv#L69), generic review | Exploratory API/device test; verify reported OS and app compatibility before treating as reproducible. |
	| Samsung M51; OS not stated | [row_id 4815](../02_analysis/coded_reviews.csv#L251), generic white-screen report | Include if supported hardware is available; not a stability-coded row. |
	| OnePlus 6; Android 11 | [row_id 12006](../02_analysis/coded_reviews.csv#L126), OTP delivery issue | Optional auth/startup compatibility smoke test; not a crash report. |

	In addition, test the minimum supported Android API, the current Android release, and the prior supported major release on low-, mid-, and high-memory representative devices. Confirm the supported OS policy with product and QA; Play Store evidence does not support an iOS-specific test requirement.
4. **Add automated regression coverage.** Instrument cold start, warm start, upgrade/relaunch, process death/recovery, and offline/poor-network recovery. Exercise booking from trip selection through durable confirmation, including repeated submit/retry behavior. Exercise tracking from an assigned trip through map render, location refresh, app background/foreground, network reconnect, and driver-contact entry point. Add a release smoke suite on the device matrix.
5. **Roll out in stages.** Release internally first, then to 10% of enterprise accounts using a cohort flag, then expand to full rollout only after the crash-free gate and guardrails pass. For the binary release, use Play Console staged rollout; enterprise-account targeting requires a server-side cohort or feature flag. Hold the 10% cohort through the 14-day stability window.

## 8. Acceptance criteria

- Crash-free session rate is **>99.5% for 14 consecutive days** in the 10% pilot cohort, with the agreed minimum session count and no material regression versus control/baseline.
- There are **zero new 1-star reviews mentioning a crash** during the 14 days after pilot release, based on a documented manual or automated review-tagging pass. Treat this as a guardrail; review volume is small and public reviews cannot be reliably assigned to enterprise cohorts.
- Booking submission-to-durable-confirmation API latency is **p95 <3.0 seconds** under the agreed production-like load test; assignment may continue asynchronously after confirmation.
- Automated booking and tracking regression tests pass on the supported device/API matrix in CI and the pre-release smoke run.
- Crash and non-fatal events are visible by app version, device/API, and flow, and the release gate blocks promotion when thresholds fail.

## 9. Success metrics

- Within 90 days, the coded-review rate for **app functionality error** is down **more than 60%** versus a matched pre-release 90-day baseline. Report both count and rate per 1,000 coded actionable reviews because review volume can change. The current 41 mentions are from the broader coded sample window, not a matched 90-day baseline; establish that baseline before rollout.
- **app crash during booking** has zero coded mentions in the 90-day post-release sample (baseline: 2 mentions in the available coded sample).
- Overall 1-star share of new Play Store reviews falls by **5 percentage points** versus the pre-release baseline. Measure at store level; it is not attributable to the treatment cohort unless review-to-cohort linkage is independently available and privacy-approved.
- Monitor crash-free sessions, launch success, booking completion, tracking render/refresh success, and p95 booking confirmation latency by release and device/API throughout rollout.

## 10. A/B test design

- Randomize eligible enterprise accounts into a 10% treatment cohort and 90% holdout, stratified where possible by account size and app-version adoption. Roll out the stability changes only to treatment during the 30-day comparison window; keep the holdout on the current stable behavior/version where Play distribution permits.
- Compare crash-free sessions, launch success, booking completion, tracking success, and internal post-trip 1-star/negative-feedback rate by assigned account cohort. Segment technical outcomes by device model and Android OS/API version.
- Compare public Play Store 1-star review rate as an aggregate 30-day secondary outcome only. Public review data does not identify enterprise account or treatment assignment, so it cannot support a valid treatment-vs-control review-rate comparison without a separately approved linkage method.
- Pre-register the exposure window, minimum eligible sessions/accounts, and decision thresholds before launch; avoid declaring success from a low-volume review-count difference alone.

## 11. Rollback plan

- Use a remotely controlled feature flag to disable the new guarded runtime behavior or cohort exposure. Do not allow a flag to bypass the CI/release crash-free gate.
- If a guardrail fails, stop Play staged rollout immediately. Google Play generally does not force-downgrade installed apps; publish a higher-version rollback build containing the previous stable behavior, then resume only after the gate passes.
- Page the Android on-call if crash rate increases by **>0.5 percentage points above the pre-release baseline in any rolling 24-hour window**, or if a new blocker crash signature appears. Pause expansion pending triage.

## 12. Dependencies

- Approved Crashlytics/Sentry project, SDK integration, retention policy, and privacy review.
- CI/CD support for release metadata, device-matrix smoke tests, and promotion gates.
- QA device matrix refreshed with supported Android API levels and available reported devices above.
- Server-side enterprise cohort/feature-flag capability and a stable holdout mechanism.
- Baseline crash, booking latency, review-theme, and new-review star-share measurements before rollout.

## 13. Estimated effort

**6–8 calendar weeks.** This is larger than 1–2 standard two-week sprints; plan approximately 3–4 two-week sprint equivalents, or adjust if the team uses longer sprint cycles. Estimate includes instrumentation, CI gates, regression coverage, device QA, and the 14-day pilot observation window; it excludes major underlying architecture rewrites if telemetry identifies one.

## 14. Ticket references

- Prioritized backlog: [release-stability P0 row](prioritized_backlog.md).
- Rating-lift model: [base six-month projection](../02_analysis/rating_lift_model.md).
- Coded review evidence: rows [21171](../02_analysis/coded_reviews.csv#L2), [12020](../02_analysis/coded_reviews.csv#L4), [15488](../02_analysis/coded_reviews.csv#L9), [7415](../02_analysis/coded_reviews.csv#L10), [10967](../02_analysis/coded_reviews.csv#L13), [3073](../02_analysis/coded_reviews.csv#L14), and [16157](../02_analysis/coded_reviews.csv#L18).
- Device/OS quote references: rows [105](../02_analysis/coded_reviews.csv#L72), [88](../02_analysis/coded_reviews.csv#L68), [89](../02_analysis/coded_reviews.csv#L69), [4815](../02_analysis/coded_reviews.csv#L251), and [12006](../02_analysis/coded_reviews.csv#L126).
