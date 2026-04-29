import json
import time
import os
import uuid
import random

def simulate():
    print("[SIMULATION] Starting DDoS Attack Scenario...")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"ddos_{int(time.time())}.log")
    
    with open(log_file, "a") as f:
        for i in range(100):
            attacker_ip = f"203.0.113.{random.randint(1, 254)}"
            event = {
                "id": str(uuid.uuid4()),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "event_type": "ddos_traffic",
                "src_ip": attacker_ip,
                "dest_port": 80,
                "payload_size": random.randint(1000, 5000)
            }
            f.write(json.dumps(event) + "\n")
            if i % 10 == 0:
                print(f"[SIMULATION] Generated DDoS traffic burst ({i+10}/100 packets)")
            time.sleep(0.01)

    print(f"[SIMULATION] DDoS Scenario complete. Logs written to {log_file}")

if __name__ == "__main__":
    simulate()