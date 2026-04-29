import pytest
from modules.log_parser.parser import LogParser
from modules.threat_detector.detector import ThreatDetector
from modules.zyron_ai.engine import ZyronAIEngine

def test_full_pipeline_mock():
    # Integration test for the core analysis path
    config = {
        'detection': {'brute_force_threshold': 1, 'brute_force_time_window_sec': 10},
        'zyron_ai': {'risk_levels': ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']}
    }
    
    parser = LogParser(config)
    detector = ThreatDetector(config)
    ai = ZyronAIEngine(config)
    
    raw_log = '{"event_type": "failed_login", "src_ip": "10.0.0.1"}'
    
    parsed = parser.parse(raw_log)
    assert parsed is not None
    
    indicators = detector.analyze(parsed)
    assert 'BRUTE_FORCE_PATTERN' in indicators
    
    assessment = ai.evaluate(parsed, indicators)
    assert assessment['risk_level'] in ['MEDIUM', 'HIGH', 'CRITICAL'] # Because of the high base score
    assert assessment['score'] > 50