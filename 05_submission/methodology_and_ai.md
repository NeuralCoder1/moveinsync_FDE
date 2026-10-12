# Methodology and AI Appendix

## 1. How I Got Here (Methodology)

I built this analysis from public review data and source material, not from internal product telemetry or a representative survey. I collected Google Play reviews for package `com.moveinsync.ets` with the Python `google-play-scraper` library. The export contains 24,314 reviews dated 2014-03-14 through 2026-10-09. I used the separate [metadata snapshot](../01_raw_data/moveinsync_metadata.json) for the current store rating: 4.6382785 across 114,872 ratings, retrieved 2026-10-11. These are different denominators: the review-text export is not the full set of store ratings.

The scraper requested English-language reviews from the India storefront in pages of 200, followed continuation tokens, and deduplicated records by review ID. I then selected the coding batches from the saved export rather than treating every retrieved review as coded evidence.

I coded 320 reviews in eight non-overlapping batches of 40. The sample includes one-star reviews sorted by thumbs-up count, one-star recent reviews, and a seeded random one-star sample; high-thumbs-up two-, three-, and four-star samples; one-star reviews grouped by common app versions; and a seeded random five-star sample. This design puts high-signal complaints first while retaining recency, version, and positive-review contrasts. It is a purposive sample, not a population estimate. The collection is limited to the records exposed by the scraper and is about 24,000 reviews, not the store's 114,872 ratings.

I applied the case study brief's 10-stage employee-journey taxonomy. Each row in the [coded review file](../02_analysis/coded_reviews.csv) records one or more journey stages, a severity (Blocker, Friction, Cosmetic, or Unclassifiable), a theme, the verbatim review text, an English gloss where needed, and a fixability label (App-fix, Vendor-ops, or Employer-policy). A review could mention multiple stages, but received one primary theme and severity. I used a shared codebook and reconciled theme counts against the row-level file before using them in the findings and backlog.

I used secondary evidence to add context, not to replace review data. This included MoveInSync's [Mobile App Issues and GPS-loss Help Center articles](../01_raw_data/helpcenter_articles.md), its [historical rating-recovery blog](../01_raw_data/company_blog_rating_recovery.md), and eight recent low-rated [App Store review excerpts](../01_raw_data/appstore_reviews.md). Screenshot checks confirmed AmbitionBox at 3.1/5 from 293 reviews and Glassdoor at 3.0/5 from 223 reviews; these self-selected employee reviews do not establish a cause of app defects. I verified one Mastodon post by @rmathew dated 2025-05-08 against its screenshot. I also checked the proposed competitor set (Safetrax, Quick Ride, and sRide); listings could not be verified, so I use no competitor ratings or complaint comparisons.

The [rating-lift model](../02_analysis/rating_lift_model.md) separates two levers: reduce negative reviews and increase positive reviews. It compares pessimistic, base, and optimistic assumptions and a rebuilt-review-pipeline scenario. These are projections, not measured outcomes; I keep the modeled assumptions separate from observed data.

For verification, I matched every quoted review character-for-character against the source CSV, reviewed screenshots against the source pages, and checked internal file references. I also reconciled the displayed rating to metadata before updating the projections. The main limitations remain material: the scraper's pagination cap limits the text sample; Play Store reviewers are self-selected and skew negative; coding was done by one coder, with no independent second-coder reliability check; and device/OS details are not structured fields in the review export. Review themes therefore describe this sample, not all users, and the findings do not establish causality.

## 2. AI Tools and How They Were Used

AI assisted with both computation and interpretation. I used ChatGPT's Code Interpreter to draft and run Python scraping, pandas analysis, chart generation, and rating-lift calculations. A built-in bot supported the qualitative coding pass, theme-based prioritization, P0 specification drafting, and cross-file consistency checks. Claude helped design the early coding protocol and draft assumptions. I used ChatGPT and the bot for code and structured work; I used Claude for early judgment and prose. These tools produced analyses and drafts, not independent evidence. I reviewed the outputs, checked claims against source files, and made the final decisions about findings and recommendations.

| Tool | Task | Verification method |
| --- | --- | --- |
| ChatGPT (Code Interpreter) | Scraping code, pandas summaries, charts, rating-lift math | Ran code locally; checked row counts and distributions against the CSV; reconciled calculations to metadata and the model formulas |
| Built-in bot | Review coding, prioritization, P0 spec, consistency audit | Checked labels and quotations against source rows; traced claims to project files; recalculated sprint-duration arithmetic |
| Claude | Early coding-protocol design and assumption drafting | Compared the protocol with the case study taxonomy and assumptions with source data; revised or removed unsupported claims |

When AI-generated text or analysis appears in this submission, it has been reviewed as AI-assisted work rather than presented as an unaided human result. Human review does not make a claim true; the cited source and verification method are what support it.

I did not treat agreement between tools, confident wording, or a polished chart as independent confirmation. Where a claim could not be directly checked, including employee-review representativeness and current Play Store reply coverage, I kept the limitation visible instead of extending an AI-generated conclusion.
I retained responsibility for the final analysis and wording.

## 3. Where AI Was Wrong and How I Caught It

AI outputs were useful starting points, not reliable facts. A draft described 4.3 as the current Play Store rating. I compared the drafts with the authoritative metadata and found 4.6382785 across 114,872 ratings, retrieved 2026-10-11. I rebased current-rating references to 4.64 and recalculated dependent comparisons and projections. The separate 4.3 figure remains only as the company's historical rating in its recovery story.

Employee-review material also entered an early draft without adequate support: an AmbitionBox rating of 2.7/5 and a “quick fixes” quote. The bot flagged both as unverified. I opened and checked the saved source screenshots; they show AmbitionBox at 3.1/5 from 293 reviews and Glassdoor at 3.0/5 from 223 reviews. I replaced the ratings and removed the unsupported quote rather than treating it as evidence.

The bot initially declined to include the Mastodon “/dev/null” claim because the draft lacked a source. I located the post by @rmathew, dated 2025-05-08, and verified it against a screenshot. I then included it as one person's report, not as a measure of complaint volume or support performance.

I also treated the “430+ enterprise customers” figure as independently verified. The bot challenged its provenance; I traced it to page 1 of the case study brief and corrected the wording to “per the case study brief.” The figure is attributed, not independently confirmed by this analysis.

Finally, I described a 6–8 week engineering estimate as “1–2 sprints.” The bot checked the estimate against a two-week sprint length: 6–8 weeks is 3–4 two-week sprint equivalents. I corrected the P0 specification. This caught an arithmetic and planning error before submission, not a product estimate validated by an engineering team.

*"AI was used as a leverage tool throughout. Every factual claim in this submission traces to a source file. Where AI output could not be verified, it was removed."*