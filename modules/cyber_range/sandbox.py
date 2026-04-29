import logging

class CyberRangeSandbox:
    """
    Simulates a controlled environment where attacks can be injected
    and monitored without affecting real infrastructure.
    """
    def __init__(self):
        self.state = "CLEAN"
        self.vulnerabilities = []

    def inject_vulnerability(self, vuln_name):
        self.vulnerabilities.append(vuln_name)
        logging.info(f"[CYBER RANGE] Injected vulnerability: {vuln_name}")
        
    def run_attack_scenario(self, scenario_function):
        logging.info(f"[CYBER RANGE] Starting scenario execution...")
        self.state = "UNDER_ATTACK"
        
        # Execute the simulated attack behavior
        scenario_function()
        
        # Monitor behavior
        logging.info(f"[CYBER RANGE] Scenario execution complete. State analysis pending.")
        self.state = "COMPROMISED" if self.vulnerabilities else "DEFENDED"
        
    def generate_remediation(self):
        remediations = []
        for vuln in self.vulnerabilities:
            remediations.append(f"Patch {vuln} immediately.")
        return remediations