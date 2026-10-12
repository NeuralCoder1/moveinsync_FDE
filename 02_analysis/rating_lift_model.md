# Rating-Lift Model: Two Levers

## Baseline and assumptions

| Input | Value |
| --- | ---: |
| Starting Play Store reviews | 115,000 |
| Starting displayed rating | 4.64 |
| Starting cumulative star sum (115,000 x 4.64) | 533,600 |
| Monthly new reviews | 228 |
| Six-month organic new reviews (228 x 6) | 1,368 |
| Coded sample | 320 |
| Actionable coded reviews (excluding 91 generic) | 229 |
| Coded-review sampling window | Approximately 18 months |
| Monthly 5-star reviews (228 x 0.53) | Approximately 121 |

The top-five theme counts are from the Pareto table in `chart_data.md`. For the star-sum projection, ordinary incoming reviews are assumed to average 4.3 stars (held constant from the prior model assumption), prevented negative reviews are assumed to be 1-star, and each additional prompted review is assumed to be 5-star. Positive-review gains use the supplied rounded estimate of +24 per month in the base case, scaled proportionally to +12 and +36 per month in the pessimistic and optimistic cases. These are expected-value estimates, so prevented-review counts and projected totals can be fractional. The starting rating and star sum use the authoritative metadata value rounded to 4.64.

## Lever 1: Reduce negative reviews

Monthly complaints = `n_theme / 18`. Monthly reductions apply the scenario's reduction rate to that complaint estimate.

| Pareto rank | Theme | n_theme | Monthly complaints | Pessimistic reduction (30%) | Base reduction (60%) | Optimistic reduction (80%) |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | app functionality error | 41 | 2.2778 | 0.6833 | 1.3667 | 1.8222 |
| 2 | booking failure | 23 | 1.2778 | 0.3833 | 0.7667 | 1.0222 |
| 3 | feature request | 22 | 1.2222 | 0.3667 | 0.7333 | 0.9778 |
| 4 | UI confusing | 16 | 0.8889 | 0.2667 | 0.5333 | 0.7111 |
| 5 | login failure | 12 | 0.6667 | 0.2000 | 0.4000 | 0.5333 |
| **Total** | **Top five** | **114** | **6.3333** | **1.9000** | **3.8000** | **5.0667** |

## Lever 2: Increase positive reviews

| Scenario | 5-star review boost | Additional 5-star reviews per month | Additional 5-star reviews over 6 months |
| --- | ---: | ---: | ---: |
| Pessimistic | 10% | 12 | 72 |
| Base | 20% | 24 | 144 |
| Optimistic | 30% | 36 | 216 |

## Combined six-month projection

Negative reviews prevented = top-five monthly reductions x 6. New review total = `115,000 + 1,368 - prevented + additional positive reviews`. New star sum = `533,600 + (1,368 x 4.3) - prevented + (additional positive reviews x 5)`.

| Scenario | Negative reduction | Positive boost | Negative reviews prevented (6 mo) | Additional 5-star reviews (6 mo) | New total reviews | New cumulative star sum | Projected rating |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Pessimistic | 30% | 10% | 11.4 | 72 | 116,428.6 | 539,831.0 | 4.636584138 |
| Base | 60% | 20% | 22.8 | 144 | 116,489.2 | 540,179.6 | 4.637164647 |
| Optimistic | 80% | 30% | 30.4 | 216 | 116,553.6 | 540,532.0 | 4.637625951 |

## Base scenario: extended projections

The monthly Base rates are held constant: 228 organic new reviews, 3.8 negative reviews prevented, and 24 additional 5-star reviews. For each horizon, new total reviews = `115,000 + organic new reviews - negative reviews prevented + additional positive reviews`. Cumulative star sum = `533,600 + (organic new reviews x 4.3) - negative reviews prevented + (additional positive reviews x 5)`.

| Horizon | Total new organic reviews | Negative reviews prevented | Additional positive reviews | Cumulative new total N | Cumulative star sum | Projected rating |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 12 months | 2,736 | 45.6 | 288 | 117,978.4 | 546,759.2 | 4.634400873 |
| 24 months | 5,472 | 91.2 | 576 | 120,956.8 | 559,918.4 | 4.629077489 |
| 5 years (60 months) | 13,680 | 228.0 | 1,440 | 129,892.0 | 599,396.0 | 4.614572106 |

## Long-run rating thresholds

At constant monthly rates, the rating is `(533,600 + 1,096.6 x months) / (115,000 + 248.2 x months)`, which approaches a ceiling of `1,096.6 / 248.2 = 4.418211` as time increases.

| Threshold | Result under constant Base rates |
| --- | --- |
| 4.4 | Remains above 4.4; the 4.418211 long-run ceiling is higher |
| 4.5 | Falls below 4.5 after approximately 793 months, or 66.1 years |

## Review Pipeline Rebuilt scenario

This scenario assumes 684 gross new reviews per month, with 60% receiving 5 stars. The remaining 40% are modeled at 4.234043 stars, inferred from the current 4.64 average and 53% 5-star share: `(4.64 - 0.53 x 5) / 0.47`. The implied average for all 684 new reviews is 4.693617 stars. The 24 prompt-driven positive reviews per month are already included in the 684 and are not added a second time. The same 3.8 prevented 1-star reviews per month are subtracted from both review count and star sum.

| Scenario | Horizon | Gross new reviews | Negative reviews prevented | 5-star reviews (60% of gross) | Cumulative new total N | Cumulative star sum | Projected rating |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Review Pipeline Rebuilt | 6 months | 4,104 | 22.8 | 2,462.4 | 119,081.2 | 552,839.8 | 4.642544787 |
| Review Pipeline Rebuilt | 12 months | 8,208 | 45.6 | 4,924.8 | 123,162.4 | 572,079.6 | 4.644920922 |
| Review Pipeline Rebuilt | 24 months | 16,416 | 91.2 | 9,849.6 | 131,324.8 | 610,559.2 | 4.649230130 |