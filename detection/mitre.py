MITRE_MAPPING = {
    "4625": {
        "technique": "T1110",
        "name": "Brute Force"
    },
    "4648": {
        "technique": "T1078",
        "name": "Valid Accounts"
    },
    "4688": {
        "technique": "T1059",
        "name": "Command and Scripting Interpreter"
    }
}


def map_mitre(alerts):
    for alert in alerts:
        mapping = MITRE_MAPPING.get(str(alert["event_id"]))

        if mapping:
            alert["mitre_id"] = mapping["technique"]
            alert["mitre_name"] = mapping["name"]
        else:
            alert["mitre_id"] = "Unmapped"
            alert["mitre_name"] = "Unknown"

    return alerts