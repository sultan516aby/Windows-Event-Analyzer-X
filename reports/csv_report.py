import csv


def export_csv(alerts, output="reports/report.csv"):
    if not alerts:
        print("No alerts to export.")
        return

    with open(output, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=alerts[0].keys())
        writer.writeheader()
        writer.writerows(alerts)

    print(f"CSV Report saved: {output}")