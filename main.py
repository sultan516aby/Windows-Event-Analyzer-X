from core.parser import parse_log_file
from detection.engine import load_rules, analyze_events
from detection.risk import calculate_risk
from detection.mitre import map_mitre
from detection.correlation import correlate_events
from reports.json_report import export_json
from reports.csv_report import export_csv

events = parse_log_file("samples/sample_logs.csv")
rules = load_rules()

alerts = analyze_events(events, rules)
alerts = calculate_risk(alerts)
alerts = map_mitre(alerts)
correlations = correlate_events(events)
print("Correlations:", correlations)
print(f"Total Events: {len(events)}")
print(f"Total Alerts: {len(alerts)}")

for alert in alerts:
    print(alert)
export_json(events, alerts)    
export_csv(alerts)