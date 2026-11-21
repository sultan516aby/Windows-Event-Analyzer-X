from core.evtx_parser import parse_evtx

events = parse_evtx("samples/security.evtx")

print("Total Events:", len(events))

for event in events[:5]:
    print(event)