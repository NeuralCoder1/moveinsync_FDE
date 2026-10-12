"""Extract MoveInSync Google Play reviews and app metadata.

Requires network access and: python -m pip install google-play-scraper

This script paginates explicitly using continuation tokens, pauses between
requests, deduplicates reviews by reviewId, and writes CSV/JSON outputs.
"""
from __future__ import annotations

import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from google_play_scraper import app, reviews, Sort
except ImportError as exc:
    print(
        "ERROR: google-play-scraper is not installed or could not be imported.\n"
        "Install it with: python -m pip install google-play-scraper\n"
        f"Import detail: {exc}",
        file=sys.stderr,
    )
    raise SystemExit(2)

APP_ID = "com.moveinsync.ets"
LANG = "en"
COUNTRY = "in"
BATCH_SIZE = 200  # reasonable page size supported by the library
SLEEP_SECONDS = 1.5
OUTPUT_DIR = Path(__file__).resolve().parent
CSV_PATH = OUTPUT_DIR / "moveinsync_reviews.csv"
JSON_PATH = OUTPUT_DIR / "moveinsync_metadata.json"
CSV_COLUMNS = [
    "review_id", "user_name", "rating", "review_text", "review_date",
    "app_version", "thumbs_up_count",
]


def iso_date(value: Any) -> str:
    """Convert datetime/date-like values to ISO-8601 text safely."""
    if value is None:
        return ""
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def main() -> None:
    print(f"App package: {APP_ID}")
    print(f"Review batch size: {BATCH_SIZE}; pause between requests: {SLEEP_SECONDS}s")

    # App-level metadata is fetched once and kept separate from review data.
    app_info = app(APP_ID, lang=LANG, country=COUNTRY)
    metadata = {
        "package_name": APP_ID,
        "current_rating": app_info.get("score"),
        "total_ratings_count": app_info.get("ratings"),
        "installs": app_info.get("installs"),
        "version": app_info.get("version"),
        "updated_date": app_info.get("updated"),
        "metadata_retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
    }

    # Page through all available review records until no continuation token
    # remains. Deduplication protects against repeated records across pages.
    unique_reviews: dict[str, dict[str, Any]] = {}
    continuation_token = None
    page_number = 0

    while True:
        page_number += 1
        page, continuation_token = reviews(
            APP_ID,
            lang=LANG,
            country=COUNTRY,
            sort=Sort.NEWEST,
            count=BATCH_SIZE,
            continuation_token=continuation_token,
        )
        if not page:
            print(f"Page {page_number}: no records returned; stopping.")
            break

        for item in page:
            review_id = item.get("reviewId")
            if not review_id:
                # Do not silently invent identifiers; skip malformed records.
                continue
            unique_reviews[review_id] = {
                "review_id": review_id,
                "user_name": item.get("userName", ""),
                "rating": item.get("score"),
                "review_text": item.get("content", ""),
                "review_date": iso_date(item.get("at")),
                "app_version": item.get("reviewCreatedVersion") or "",
                "thumbs_up_count": item.get("thumbsUpCount", 0),
            }

        print(
            f"Page {page_number}: received {len(page)}; "
            f"unique reviews so far: {len(unique_reviews)}"
        )
        if not continuation_token:
            break
        time.sleep(SLEEP_SECONDS)

    records = list(unique_reviews.values())
    with CSV_PATH.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)

    with JSON_PATH.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2, default=str)

    dates = [r["review_date"][:10] for r in records if r["review_date"]]
    distribution = {star: 0 for star in range(1, 6)}
    for record in records:
        rating = record["rating"]
        if rating in distribution:
            distribution[rating] += 1

    print("\n=== EXTRACTION SUMMARY ===")
    print(f"Total unique reviews pulled: {len(records):,}")
    print(f"Review date range: {min(dates) if dates else 'N/A'} to {max(dates) if dates else 'N/A'}")
    print("Star distribution:")
    for star in range(1, 6):
        print(f"  {star}★: {distribution[star]:,}")
    print(f"CSV saved: {CSV_PATH}")
    print(f"Metadata JSON saved: {JSON_PATH}")
    print("Note: 'all' means all records exposed by the current Google Play endpoint for this locale at run time.")


if __name__ == "__main__":
    main()
