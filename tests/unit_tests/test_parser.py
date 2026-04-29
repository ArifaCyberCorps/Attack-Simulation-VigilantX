import pytest
from modules.log_parser.parser import LogParser

def test_json_parsing():
    parser = LogParser({})
    raw = '{"event_type": "test", "src_ip": "1.1.1.1"}'
    parsed = parser.parse(raw)
    
    assert parsed is not None
    assert parsed['event_type'] == "test"
    assert parsed['src_ip'] == "1.1.1.1"
    assert 'timestamp' in parsed

def test_invalid_json():
    parser = LogParser({})
    raw = 'invalid json { data'
    parsed = parser.parse(raw)
    
    assert parsed is None