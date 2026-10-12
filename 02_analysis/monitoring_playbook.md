# Play Store Rating Monitoring Playbook

The displayed rating is a lagging average across roughly 115,000 ratings. Track current experience with these measures.

## 1. What to Measure

| Metric | Definition | Source | Why it matters |
| --- | --- | --- | --- |
| Rolling 90-day rating | Average star rating of reviews posted in the last 90 days | Weekly Play Store scrape | Reflects current experience, not the full rating history |
| Blocker review rate | New reviews tagged as preventing task completion, divided by all new reviews | Manual or automated tagging | Surfaces urgent failures early |
| Theme mix trend | Counts and share for the five most-mentioned themes; compare with the previous month | Tags on new reviews | Shows whether fixes reduce target themes or new problems emerge |
| Review velocity | Number of new reviews per week | Weekly Play Store scrape | Shows whether in-app prompts and enterprise outreach are reaching users |
| 5-star share | New 5-star reviews divided by all new reviews | Weekly Play Store scrape | Leading indicator of movement in the displayed rating |
| Reply rate for 1- and 2-star reviews | Reviews at least seven days old with a developer reply within seven days, divided by all 1- and 2-star reviews at least seven days old | Play Store scrape | Checks response speed; the company blog describes personalized replies as part of past recovery |
| Enterprise retention rate | Enterprise accounts that renew annually divided by accounts due to renew | Internal CRM | Measures the business outcome the displayed rating is only a proxy for |

## 2. Cadence

- **Weekly:** Scrape new reviews, tag themes and blockers, and calculate the rolling 90-day rating, review velocity, 5-star share, and reply rate.
- **Monthly:** Report the five leading themes, their share of new reviews, blocker rate, and 5-star share. Compare with the prior month and note relevant releases or outreach changes.
- **Quarterly:** Review whether the product is improving and whether the review pipeline is working. Adjust product and outreach priorities; review enterprise retention alongside the review measures.

## 3. Owners

| Task | Owner |
| --- | --- |
| Weekly scrape and tagging | Support-Ops analyst |
| Reply to 1- and 2-star reviews | Support-Ops lead |
| Monthly theme-mix report | Product Manager |
| Quarterly strategy review | VP Product and Engineering Lead |
| Enterprise retention tracking | Enterprise CS |

## 4. Alerts

| Trigger | Action |
| --- | --- |
| A new theme gets more than five mentions in one week | Investigate and escalate to the Product Manager |
| Blocker rate rises by more than 3 percentage points week over week | Escalate to engineering on-call |
| Reply rate falls below 90% | Alert the Support-Ops lead |
| Rolling 90-day rating is more than 0.05 points below its value three months earlier | Escalate to VP Product |
| A new app release is followed by a spike in 1-star reviews | Pause the staged rollout and investigate |

## 5. Interpretation

- **Displayed rating rises slowly:** Expected; roughly 115,000 historical ratings dilute the effect of new reviews.
- **Rolling 90-day rating rises:** Recent experience may be improving; check blocker rate and themes for supporting evidence.
- **Theme mix shifts away from P0 themes:** Fixes may be working; verify with counts and share month over month.
- **Theme mix shifts toward a new theme:** A new failure mode may be emerging; investigate.
- **Review velocity rises while 5-star share is stable:** Outreach is generating reviews, but may not be well targeted; refine timing and audience.
- **Review velocity is flat:** The review pipeline may not be working; check prompt placement and enterprise outreach.
- **Displayed rating falls:** New ratings are outweighing improvements; investigate promptly and escalate.

The displayed rating is a legacy indicator. The metrics above are leading indicators. Track the leading indicators; the displayed rating will follow.