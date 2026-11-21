import yaml


def load_rules(file_path="config/rules.yaml"):
    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
        return data["rules"]


def analyze_events(events, rules):
    alerts = []

    for event in events:
        for rule in rules:
            if str(event.get("event_id")) == str(rule["event_id"]):
                alerts.append({
                    "event_id": event["event_id"],
                    "rule_name": rule["name"],
                    "severity": rule["severity"],
                    "message": event.get("message", "")
                })

    return alerts