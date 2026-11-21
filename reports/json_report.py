import json
from datetime import datetime


def export_json(events, alerts, output="reports/report.json"):
    report = {
        "generated_at": datetime.now().isoformat(),
        "total_events": len(events),
        "total_alerts": len(alerts),
        "alerts": alerts
    }

    with open(output, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(f"Report saved: {output}")