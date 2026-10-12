# Data Sources and Collection Methodology

**Case study:** MoveInSync Play Store rating analysis (current rating: 4.64, per scraped metadata retrieved 2026-10-11; exact value 4.6382785, 114,872 ratings)
**Goal:** Identify what to fix first to move the rating, backed by traceable evidence.
**Collection date range:** _fill in_
**App package ID(s) in scope:** `com.moveinsync.ets` (package in scraped metadata; rider/employee vs. driver/admin role is not verified here)

---

## 1. Primary Sources

Raw, first-party evidence about the app itself. These drive the analysis.

| Source | What I'll Extract | How | Status |
|---|---|---|---|
| Google Play Store reviews | Review text, star rating, review date, app version, device model, Android version, thumbs-up count, developer reply (if any) | `google-play-scraper` (Python). Pull twice: sorted by *newest* and by *most relevant*, India storefront, English plus Hindi. Export to CSV/JSON with a retrieval timestamp. | |
| AndroidRank | Star distribution (1 to 5), rating trend over time, installs estimate, rank history | Manual capture of charts and tables, with screenshots and URL. Use the Wayback Machine for historical snapshots where available. | |
| App Store reviews | Review text, stars, date, app version, country | iTunes customer-reviews RSS/JSON feed for the India storefront (returns only the most recent ~500). Manual spot check on the web listing. | Collected (partial): eight recent low-rated excerpts; response coverage not measurable. See `01_raw_data/appstore_reviews.md`. |
| MoveInSync Help Center articles | Article title, category, last-updated date, listed known issues, workarounds, feature descriptions | Manual crawl of the help center index. Save each article as a `.md` file with its URL and access date. | Collected (partial): “Mobile App Issues” and a GPS-loss/device-health article verified 2026-10-12; the full index remains unavailable. See `01_raw_data/helpcenter_articles.md`. |
| APKPure / APKCombo | Version numbers, release dates, changelog text, APK size, min Android version | Copy the version history table into a CSV. Cross-check the latest versions against Play Store "What's new". | |

---

## 2. Secondary Sources

Context and triangulation. These do not drive conclusions alone; they confirm or challenge what the primary data shows.

| Source | What I'll Extract | How | Status |
|---|---|---|---|
| Mastodon / X / Reddit mentions | Posts mentioning MoveInSync (app complaints, praise, outages), date, platform, link | Keyword search ("MoveInSync", "MoveInSync app", "movinsync" and common misspellings). Reddit via search or PRAW; Mastodon search; X manual search. Log URL and date. | One Mastodon post verified by screenshot; X/LinkedIn login-limited and Reddit results unavailable. See `01_raw_data/social_mentions.md`. |
| AmbitionBox / Glassdoor employee reviews | Themes about product quality, engineering culture, support load, tech debt | Manual read of recent reviews. Record themes and short paraphrases only, not raw dumps. | Screenshot-verified ratings and selected text; no representative sample or causal culture analysis. See `01_raw_data/employee_reviews.md`. |
| MoveInSync blog posts | Product announcements, stated priorities, roadmap hints, customer case studies | Manual collection from the company blog. Log title, date, URL, and the claim made. | Collected: rating-recovery post reachable; short excerpts recorded. See `01_raw_data/company_blog_rating_recovery.md`. |
| Competitor apps (Safetrax, Quick Ride, sRide) | Play rating, review count, star distribution, recurring complaint themes, update cadence | Same `google-play-scraper` pipeline as the primary Play data, smaller sample. Same India storefront and date window. | Collected (listing searches attempted; target listings/ratings not verified). See `01_raw_data/competitor_benchmarks.md`. |

---

## 3. Collection Rules

1. **Never edit raw data.** Raw exports are saved once, read-only, in `/data/raw/`. All cleaning, deduplication, translation, and tagging happens in separate files in `/data/clean/`.
2. **Log every pull.** For each collection run, record the source, URL or query, date and time, tool and version, filters used, and row count in the project’s source notes.
3. **Fix the scope and window up front.** Same app ID, same country (India), same date range across all sources, so numbers are comparable. Note any deviation.
4. **Keep evidence traceable.** Every claim in the final analysis must point to a row ID, URL, or screenshot. If I can't trace it, it doesn't go in.
5. **Record what I did not find.** If a source is empty, blocked, or capped (e.g., the App Store feed limit), I write that down instead of silently dropping it. I also respect each site's terms of service and rate limits, and paraphrase rather than republish third-party text.

---

## 4. Sample Size Targets

| Source | Target | Notes |
|---|---|---|
| Google Play reviews | All retrievable, minimum 3,000. Last 12 months fully covered. | Pull the full 1-star and 2-star set so the problem categories are exhaustive; sample 5-star for contrast. Hand-tag at least 500 reviews to build the issue taxonomy. |
| AndroidRank | 1 snapshot of the current distribution plus the full available trend | Screenshot each chart. |
| App Store reviews | Up to 500 (feed cap) | Used for cross-platform comparison only. |
| Help Center articles | 30 to 50 articles, or the full help center if smaller | Prioritize troubleshooting and known-issue articles. |
| APKPure / APKCombo versions | Last 24 months of releases, minimum 15 versions | Needed to line up rating dips with specific releases. |
| Mastodon / X / Reddit | 30 to 50 relevant mentions | Expect low volume; quality over count. |
| AmbitionBox / Glassdoor | 20 to 30 recent reviews | Themes only. |
| MoveInSync blog posts | 10 to 15 posts | Focus on product and engineering posts. |
| Competitor apps | 300 to 500 recent Play reviews per competitor (3 competitors) | Plus ratings and distributions for each. |

If a target can't be met, I record the actual number and why in the collection log.

---

## 5. Known Limitations

- **Negativity skew in reviews.** People with problems are more motivated to write a review, so Play reviews overstate dissatisfaction relative to the full user base. Users who are happy rarely review.
- **Prompted-review bias.** If the app asks for a rating after a successful action, the 4.64 may be inflated compared to organic reviews. I can't see how prompts are triggered from outside.
- **Enterprise user context.** Employees often use the app because their company mandates it. Their frustration may be about their employer's setup or routes, not the app. Some complaints will be misattributed to the app.
- **Scraper limits.** Play Store sorting and caps mean I may not retrieve every review. Developer-deleted or Google-removed reviews are invisible.
- **Rating vs. text mismatch.** Many reviews are star-only with no text, so the star distribution covers more users than the text I can analyze.
- **Language and translation noise.** Hindi, Hinglish, and regional-language reviews lose nuance in translation and may be tagged inconsistently.
- **Fake or low-effort reviews.** Short generic reviews ("good", "nice app") carry little diagnostic value and may include incentivized or bot content.
- **Third-party estimates.** AndroidRank install counts and trends are estimates, and APKPure/APKCombo dates may lag the real Play release date.
- **No internal data.** I don't have crash logs, funnel analytics, support tickets, or the server-side picture. Priorities I recommend are hypotheses based on public signals and should be validated internally.
- **Small and unrepresentative secondary samples.** Social mentions and employee reviews are sparse and self-selected; they support, but cannot prove, a conclusion.
- **Competitor comparability.** Competitors differ in user base, geography, and product scope, so their ratings are context rather than a benchmark.
- **Correlation, not causation.** Lining up a rating dip with a version release suggests a cause but does not confirm it.