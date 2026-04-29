import time

class ThreatDetector:
    def __init__(self, config):
        self.config = config
        self.history = {} # In-memory state for tracking (e.g. IP -> timestamps)
        self.bf_threshold = self.config.get('detection', {}).get('brute_force_threshold', 5)
        self.bf_window = self.config.get('detection', {}).get('brute_force_time_window_sec', 60)

    def analyze(self, event):
        """Rule-based detection. Returns a list of threat indicators."""
        indicators = []
        event_type = event.get('event_type')
        src_ip = event.get('src_ip')
        
        if event_type == 'failed_login' and src_ip:
            self._record_event(src_ip, 'failed_login')
            if self._check_rate(src_ip, 'failed_login', self.bf_threshold, self.bf_window):
                indicators.append('BRUTE_FORCE_PATTERN')
                
        if event_type == 'port_scan':
             indicators.append('PORT_SCANNING_BEHAVIOR')
             
        if event_type == 'suspicious_process':
             indicators.append('MALWARE_BEHAVIOR')

        if event_type == 'ddos_traffic':
             indicators.append('DDOS_PATTERN')
             
        if event_type == 'credential_leak':
             indicators.append('LEAKED_CREDENTIAL_USED')

        return indicators

    def _record_event(self, key, event_name):
        if key not in self.history:
            self.history[key] = {}
        if event_name not in self.history[key]:
            self.history[key][event_name] = []
        self.history[key][event_name].append(time.time())

    def _check_rate(self, key, event_name, threshold, window):
        if key in self.history and event_name in self.history[key]:
            current_time = time.time()
            # filter timestamps within the window
            recent = [t for t in self.history[key][event_name] if current_time - t <= window]
            self.history[key][event_name] = recent
            if len(recent) >= threshold:
                return True
        return False