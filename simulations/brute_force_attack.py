import json
import time
import os
import uuid

def simulate():
    print("[SIMULATION] Starting Brute Force Attack Scenario...")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"bruteforce_{int(time.time())}.log")
    
    target_user = "admin"
    attacker_ip = "192.168.1.105"
    
    with open(log_file, "a") as f:
        for i in range(7): # Threshold is 5
            event = {
                "id": str(uuid.uuid4()),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "event_type": "failed_login",
                "src_ip": attacker_ip,
                "username": target_user,
                "reason": "invalid_password"
            }
            f.write(json.dumps(event) + "\n")
            print(f"[SIMULATION] Generated failed login {i+1} from {attacker_ip}")
            time.sleep(0.5)

    print(f"[SIMULATION] Brute Force Scenario complete. Logs written to {log_file}")

if __name__ == "__main__":
    simulate()