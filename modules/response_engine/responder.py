import logging

class ResponseEngine:
    def __init__(self, config):
        self.auto_block = config.get('response', {}).get('auto_block_enabled', True)
        self.block_duration = config.get('response', {}).get('block_duration_sec', 3600)

    def execute_action(self, event, risk_assessment):
        """Executes defensive actions based on the risk assessment."""
        risk_level = risk_assessment.get('risk_level')
        
        if not self.auto_block:
            logging.info(f"[ACTION] Manual review required for event: {event.get('id')}")
            return
            
        src_ip = event.get('src_ip', 'UNKNOWN_IP')
        
        if risk_level == 'CRITICAL':
            logging.error(f"[ACTION] CRITICAL ALERT! Immediately blackholing IP {src_ip} and isolating segment.")
        elif risk_level == 'HIGH':
            logging.warning(f"[ACTION] HIGH ALERT! Blocking IP {src_ip} at firewall for {self.block_duration} seconds.")
        elif risk_level == 'MEDIUM':
            logging.info(f"[ACTION] MEDIUM ALERT! Adding IP {src_ip} to watchlist and rate-limiting.")
        else:
            logging.debug(f"[ACTION] LOW ALERT. No automated response needed for {src_ip}.")