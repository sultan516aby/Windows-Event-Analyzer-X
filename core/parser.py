import csv
import re
from pathlib import Path
from datetime import datetime
from core.evtx_parser import parse_evtx

LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{1,2}/\d{1,2}/\d{4}\s+"
    r"\d{1,2}:\d{2}:\d{2}\s+[AP]M)\s+"
    r"(?P<event_id>\d+)\s+"
    r"(?P<level>\S+)\s+"
    r"(?P<message>.*)",
    re.IGNORECASE
)


def normalize_event(event):
    """Convert different log formats into one standard structure."""

    return {
        "timestamp": event.get("timestamp", "").strip(),
        "event_id": str(event.get("event_id", "")).strip(),
        "level": event.get("level", "").strip().upper(),
        "provider": event.get("provider", "").strip(),
        "message": event.get("message", "").strip()
    }


def parse_txt(file_path):
    events = []

    path = Path(file_path)
    text = path.read_text(encoding="utf-8-sig", errors="replace")

    for line_number, line in enumerate(text.splitlines(), start=1):
        match = LOG_PATTERN.match(line.strip())

        if not match:
            continue

        event = normalize_event(match.groupdict())
        event["line_number"] = line_number
        events.append(event)

    return events


def parse_csv(file_path):
    events = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            normalized_row = {
                str(key).strip().lower(): value or ""
                for key, value in row.items()
                if key is not None
            }

            event = normalize_event({
                "timestamp": normalized_row.get("timestamp", ""),
                "event_id": (
                    normalized_row.get("event id")
                    or normalized_row.get("event_id")
                    or normalized_row.get("id", "")
                ),
                "level": normalized_row.get("level", ""),
                "provider": (
                    normalized_row.get("provider")
                    or normalized_row.get("source", "")
                ),
                "message": (
                    normalized_row.get("message")
                    or normalized_row.get("description", "")
                )
            })

            events.append(event)

    return events


def parse_log_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".txt":
        return parse_txt(path)

    if extension == ".csv":
        return parse_csv(path)
    if extension == ".evtx":
        return parse_evtx(path)
    raise ValueError("Supported formats are CSV and TXT only.")