# Play Store Data Summary

- Source: google-play-scraper (Python library)
- Package: com.moveinsync.ets
- Scraped on: [today's date]
- Total reviews in sample: 24,314
- Date range: 2014-03-14 to 2026-10-09

## Star Distribution (sample)
| Stars | Count | % |
|-------|-------|---|
| 1★ | 6,352 | 26.1% |
| 2★ | 1,165 | 4.8% |
| 3★ | 1,089 | 4.5% |
| 4★ | 2,794 | 11.5% |
| 5★ | 12,914 | 53.1% |

## Sample average rating
3.61★ (vs. 4.64★ displayed on Play Store; metadata retrieved 2026-10-11)

## Key finding
The sample skews negative. 26% of sampled reviews are 1★. The authoritative Play Store metadata snapshot reports 4.6382785 from 114,872 ratings, displayed here as 4.64★. The full-sample mean is 1.03★ below that displayed rating; the 2024–2026 mean of 3.71★ is 0.93★ below it. The displayed rating is a cumulative metric and is materially higher than the review-sample means.

## Limitation
google-play-scraper caps at ~24K reviews due to internal pagination. This is a representative sample, not the full population.

## Average Rating by Window

| Window | Average |
|--------|---------|
| Full sample (2014–2026) | 3.61★ |
| Recent (2024–2026) | 3.71★ |
| Play Store displayed (metadata retrieved 2026-10-11) | 4.64★ |

## Interpretation
The full sample and recent window are close (3.61 vs 3.71), which means the rating problem is chronic, not a recent crisis. The full-sample mean is 1.03★ below the displayed 4.64★; the recent 3.71★ mean is 0.93★ below it. These gaps are consistent with a cumulative rating reflecting a more positive historical mix; the available data does not decompose the rating by review vintage. The 1★ pattern is stable across years — structural, not episodic.

## Corroborating Evidence

- **Help Center:** two articles are directly verified, including “Mobile App Issues” and a GPS-loss/device-health troubleshooting workflow. The index was inaccessible, so category completeness and the requested article-count threshold remain unverified. See `helpcenter_articles.md`.
- **Company blog:** MoveInSync describes a historical rating decline from 4.6 to 4.3, a production-server bug, and a recovery effort that included personalized review responses. See `company_blog_rating_recovery.md`.
- **App Store:** eight recent low-rated review excerpts include OTP/login, crashes, and other app/commute complaints; the small RSS sample and one visible developer response cannot establish cross-store severity or response rates. See `appstore_reviews.md`.
- **Employee reviews:** screenshots verify AmbitionBox (3.1/5, 293 reviews) and Glassdoor (3.0/5, 223 reviews) ratings and selected review text; these small self-selected sources do not establish a causal link to app quality. See `employee_reviews.md`.
- **Social mentions:** one dated Mastodon complaint was verified by screenshot; X/Reddit/LinkedIn searches remain unavailable or login-limited. The single post cannot establish prevalence or virality. See `social_mentions.md`.
- **Competitor benchmarks:** target Play Store listings and ratings could not be verified, so no category median or relative review-volume conclusion is available. See `competitor_benchmarks.md`.