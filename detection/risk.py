SEVERITY_SCORES = {
    "LOW": 10,
    "MEDIUM": 30,
    "HIGH": 70,
    "CRITICAL": 100
}


def calculate_risk(alerts):
    for alert in alerts:
        alert["risk_score"] = SEVERITY_SCORES.get(
            alert["severity"], 0
        )

    return alerts