# AI Workflow

This document describes how I used AI tools in this case study, where they helped, where they got things wrong, and how I checked their work. The brief allowed AI use; I'm documenting it so a reviewer can see exactly what was delegated and what I owned.

---

## 1. Tools Used

| Tool | Role in This Project |
|------|----------------------|
| ChatGPT (Code Interpreter) | Python scripting, web scraping, pandas data cleaning and analysis, charting, and dashboard code |
| Claude | Initial qualitative coding protocol design, taxonomy confirmation, assumption drafting, and early interpretive prose |
| Built-in bot | Executed the qualitative review coding pass using the protocol Claude helped design; supported prioritization, specification drafting, and consistency checks |

---

## 2. Division of Labor

I split the work by task. ChatGPT with Code Interpreter handled computational work: scraping, cleaning, aggregating, and charting. Claude was set up first to design the qualitative coding protocol and confirm it against the case study taxonomy, and to help draft assumptions. The workflow then evolved from Claude-based planning to bot-based execution: a built-in bot applied that protocol to the review batches and supported prioritization, specification drafting, and consistency checks. I treated AI outputs as drafts or coded suggestions to verify against source data, not as findings. I made the final calls on what to include, what to discard, and what to conclude.

---

## 3. Where AI Helped Most

- **Refused to fabricate frequency.** When asked to identify the top three requested features, the bot read all 22 feature-request quotes and found 7 that formed clearly repeated clusters: trip-participant contact (3 mentions), post-trip rating/feedback (2), and employee/boarding-point visibility (2). It cited the source row IDs for each cluster and did not rank the remaining 15 heterogeneous requests as if their frequency were established. That restraint is what I want from an AI collaborator.
- **Enforced evidence discipline.** When draft findings included employee-review, social-media, and Help Center claims that were not yet supported by the project’s source files, the bot declined to present them as established facts and called for verification or removal. I then checked the sources and saved screenshots in `01_raw_data/` before citing the supported material. This follows the brief’s guidance: “Reasonable assumptions, clearly stated, are fine.”

---

## 4. Where AI Was Wrong or Misleading

- **Feature-request volume is not feature-request frequency.** My initial framing treated the 22 reviews labeled `feature request` as if they could be ranked into a 22-item menu. Checking the quotes showed that only 7 reviews form three clearly repeated clusters; the other 15 are heterogeneous. I updated the backlog and findings narrative to name only those supported clusters rather than imply a ranked list the data does not support.
- **Unverified claims propagated through drafts.** An earlier memo included an AmbitionBox 2.7/5 rating and 152-review count, a Mastodon “/dev/null” post, and a GPS Help Center claim before the evidence was traceable. The bot flagged these for verification. My source checks corrected the employee figures: the saved screenshots show AmbitionBox at 3.1/5 from 293 reviews and Glassdoor at 3.0/5 from 223 reviews, not 2.7/5. The Mastodon screenshot supports attributing the “/dev/null” wording to one user, not treating it as measured support performance. I verified the GPS-loss Help Center claim before including it at the level supported by the evidence. The source documents and screenshots were then updated for citation.
- **Rating number inconsistency.** Three current-rating figures appeared in project files: 4.3, 4.37, and 4.64, reflecting sources and capture dates that had been mixed together. I reconciled the current displayed rating to 4.64, rounded from the scraped metadata value 4.6382785 retrieved on 2026-10-11, and recalculated the sample gaps and dependent projections. Earlier 4.3 and 4.37 values remain identified as historical snapshots rather than current ratings.

---

## 5. How I Verified AI Outputs

These are the rules I followed throughout the project:

1. **Every number cited must come from the raw data, not from an AI summary.** If a figure appears in my write-up, I recomputed it myself or traced it back to the source file.
2. **Spot-check bot-coded reviews by hand.** I checked sampled labels and quotes against the source CSV and recorded discrepancies for codebook review. This was a single-coder process; no independent second-coder reliability check was performed.
3. **Re-run AI-generated code before trusting its output.** I read the code, confirmed it did what the prompt asked, and checked that row counts and totals matched the source data at each step.
4. **Sanity-check results against the raw data.** I looked at min/max values, null counts, and duplicates, and checked whether any result looked too clean or too convenient.
5. **Check every quote and example.** Any review quoted in the write-up was located in the original dataset. I did not use quotes that only appeared in an AI response.
6. **Do not accept causal claims without evidence.** Where AI proposed a root cause, I checked whether the data supports it or whether it is only a hypothesis, and labeled it accordingly.
7. **Flag uncertainty in the final write-up.** Where the data is thin, ambiguous, or based on a small sample, I say so instead of smoothing it over.
8. **Log the prompt and whether the output was verified.** Every significant AI interaction is recorded in the usage log below, including those where the output was rejected.

---

## 6. AI Usage Log

| Date        | Tool | Prompt Summary                                              | Output        | Verified? (Y/N) |
|-------------|------|-------------------------------------------------------------|---------------|-----------------|
| 10/10/26 | ChatGPT | Wrote google-play-scraper script for com.moveinsync.ets | `scraper.py` + CSV | Y — ran locally, confirmed row count and star distribution |
| 11/10/26 | Claude | Designed initial coding protocol and confirmed journey-stage taxonomy | Protocol and 40-review batch plan | Y — protocol matches the case study taxonomy |
| 12/10/26 | Built-in bot | Executed eight-batch review coding pass using Claude-designed protocol | `coded_reviews.csv` | Y — quotes checked against source CSV and totals reconciled; no independent second-coder reliability check |
| 12/10/26 | Bot,kimi.ai | Generated `chart_data.md` with underlying tables from `coded_reviews.csv` | `chart_data.md` | Y — verified against `summary_statistics.md` |

