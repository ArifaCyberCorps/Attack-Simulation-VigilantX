import json
import time
import os
import uuid

def simulate():
    print("[SIMULATION] Starting Port Scan Attack Scenario...")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"portscan_{int(time.time())}.log")
    
    attacker_ip = "10.0.0.55"
    ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]
    
    with open(log_file, "a") as f:
        for port in ports:
            event = {
                "id": str(uuid.uuid4()),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "event_type": "port_scan",
                "src_ip": attacker_ip,
                "dest_port": port,
                "action": "connection_attempt"
            }
            f.write(json.dumps(event) + "\n")
            print(f"[SIMULATION] Scanning port {port} from {attacker_ip}")
            time.sleep(0.1)

    print(f"[SIMULATION] Port Scan Scenario complete. Logs written to {log_file}")

if __name__ == "__main__":
    simulate()