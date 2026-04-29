class RiskScorer:
    """Static standalone risk scorer, superseded dynamically by Zyron AI engine but useful as fallback."""
    def __init__(self):
        pass
        
    def calculate_base_risk(self, event_type):
        risks = {
            'failed_login': 20,
            'port_scan': 30,
            'ddos_traffic': 60,
            'suspicious_process': 70,
            'credential_leak': 90
        }
        return risks.get(event_type, 10)