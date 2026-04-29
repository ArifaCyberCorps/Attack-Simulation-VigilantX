import pytest
from modules.threat_detector.detector import ThreatDetector

def test_brute_force_detection():
    config = {'detection': {'brute_force_threshold': 3, 'brute_force_time_window_sec': 10}}
    detector = ThreatDetector(config)
    
    event = {'event_type': 'failed_login', 'src_ip': '10.0.0.1'}
    
    # 1st attempt
    ind = detector.analyze(event)
    assert 'BRUTE_FORCE_PATTERN' not in ind
    
    # 2nd attempt
    ind = detector.analyze(event)
    assert 'BRUTE_FORCE_PATTERN' not in ind
    
    # 3rd attempt - should trigger
    ind = detector.analyze(event)
    assert 'BRUTE_FORCE_PATTERN' in ind