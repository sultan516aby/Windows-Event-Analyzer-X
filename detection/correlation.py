from collections import Counter


def correlate_events(events):
    failed_logons = [
        event for event in events
        if str(event.get("event_id")) == "4625"
    ]

    counts = Counter(
        event.get("provider", "Unknown")
        for event in failed_logons
    )

    return [
        {
            "provider": provider,
            "failed_attempts": count,
            "alert": "Repeated Failed Logons" if count >= 3 else "Normal"
        }
        for provider, count in counts.items()
    ]