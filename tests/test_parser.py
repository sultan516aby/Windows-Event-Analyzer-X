from core.parser import parse_log_file

def test_csv_parser():
    events = parse_log_file("samples/sample_logs.csv")
    assert len(events) == 4

def test_txt_parser():
    events = parse_log_file("samples/sample_logs.txt")
    assert len(events) == 3

    print("All tests passed!")