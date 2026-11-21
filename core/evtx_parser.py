from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET


def parse_evtx(file_path):
    events = []

    with Evtx(file_path) as log:
        for record in log.records():
            try:
                root = ET.fromstring(record.xml())

                event_id = root.find(".//{*}EventID")
                timestamp = root.find(".//{*}TimeCreated")
                provider = root.find(".//{*}Provider")

                events.append({
                    "event_id": event_id.text if event_id is not None else "",
                    "timestamp": timestamp.get("SystemTime", "") if timestamp is not None else "",
                    "provider": provider.get("Name", "") if provider is not None else "",
                    "message": ""
                })

            except ET.ParseError:
                continue

    return events