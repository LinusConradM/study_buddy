#!/usr/bin/env python3
"""
CLI tool to parse syllabus files (PDF/DOCX) and sync deadlines to Google Calendar.
"""

import sys
import argparse

from parsers import extract_text
from deadlines import extract_deadlines
from calendar_sync import get_calendar_service, create_event, list_upcoming_events


def main():
    parser = argparse.ArgumentParser(
        description="Sync syllabus deadlines to Google Calendar"
    )
    parser.add_argument(
        "file", help="Path to syllabus file (PDF or DOCX)"
    )
    parser.add_argument(
        "--calendar-id",
        default="primary",
        help="Google Calendar ID to sync events to (default: primary)",
    )
    parser.add_argument(
        "--dashboard",
        action="store_true",
        help="Display upcoming deadlines from the calendar after syncing",
    )
    args = parser.parse_args()

    try:
        text = extract_text(args.file)
    except Exception as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        sys.exit(1)

    deadlines = extract_deadlines(text)
    if not deadlines:
        print("No deadlines found in syllabus.", file=sys.stderr)
        sys.exit(0)

    service = get_calendar_service()
    for d in deadlines:
        event = create_event(
            service, args.calendar_id, d["title"], d["due"]
        )
        print(
            f"Created event: {event.get('summary')} on "
            f"{event.get('start').get('date')}"
        )

    if args.dashboard:
        events = list_upcoming_events(service, args.calendar_id)
        if not events:
            print("\nNo upcoming deadlines found.")
        else:
            print("\nUpcoming deadlines:")
            for event in events:
                start = event["start"].get("date", event["start"].get("dateTime"))
                print(f"- {start}: {event.get('summary')}")


if __name__ == "__main__":
    main()