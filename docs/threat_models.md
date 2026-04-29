# Threat Models Simulated

This prototype validates defenses against the following threat vectors:

## 1. Brute Force Login
- **Behavior:** Rapid, successive failed login attempts targeting a single account or multiple accounts from a single source IP.
- **Detection:** `ThreatDetector` rule for X failures within Y seconds.
- **AI Assessment:** High risk if threshold exceeded significantly.

## 2. Port Scanning
- **Behavior:** Sequential or randomized connection attempts across a wide range of ports on a target host to identify listening services.
- **Detection:** Identifying multiple distinct `dest_port` connections from the same `src_ip` in a short window.
- **AI Assessment:** Medium-High risk depending on volume.

## 3. Distributed Denial of Service (DDoS)
- **Behavior:** Massive volume of inbound traffic from randomized source IPs targeting a specific service port.
- **Detection:** Sudden spike in traffic volume/payload size directed at a single destination.
- **AI Assessment:** High-Critical risk due to potential service disruption.

## 4. Malware Behavior
- **Behavior:** Suspicious process execution chains (e.g., `cmd.exe` spawning `powershell.exe` with encoded payloads, or registry modifications).
- **Detection:** Rule matching against known malicious process trees and actions.
- **AI Assessment:** Critical risk due to likely system compromise.

## 5. Credential Leaks
- **Behavior:** Successful login from an anomalous geolocation using credentials identified in known breach datasets.
- **Detection:** Matching username and successful login against anomaly criteria (unseen IP).
- **AI Assessment:** Critical risk due to account takeover.