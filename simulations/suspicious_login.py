import json
import time
import os
import uuid

def simulate():
    print("[SIMULATION] Starting Suspicious Login Scenario...")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"suspicious_login_{int(time.time())}.log")
    
    event = {
        "id": str(uuid.uuid4()),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "event_type": "credential_leak",
        "username": "ceo_admin",
        "src_ip": "185.15.55.20", # IP not seen before
        "country": "UNKNOWN",
        "login_status": "SUCCESS"
    }
    
    with open(log_file, "a") as f:
        f.write(json.dumps(event) + "\n")
        print(f"[SIMULATION] Logged successful login using leaked credential from suspicious IP.")

    print(f"[SIMULATION] Suspicious Login Scenario complete. Logs written to {log_file}")

if __name__ == "__main__":
    simulate()