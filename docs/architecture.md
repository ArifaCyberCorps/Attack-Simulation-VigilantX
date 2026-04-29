# VigilantX System Architecture

## Overview
VigilantX is designed as a modular, high-throughput log processing and autonomous cyber defense pipeline. The architecture emphasizes separation of concerns, allowing components to be upgraded or swapped independently.

## Core Modules

### 1. Log Collector (`modules/log_collector/`)
Ingests raw security event logs from various simulated sources. In this prototype, it monitors a local `logs/` directory for incoming JSON log entries representing network and system events.

### 2. Log Parser (`modules/log_parser/`)
Transforms raw text/JSON logs into structured, standardized dictionary formats that the detection engines can process uniformly. Ensures missing fields (like timestamps) are injected.

### 3. Threat Detector (`modules/threat_detector/`)
A deterministic, rule-based correlation engine. It maintains in-memory state to identify patterns over time (e.g., threshold-based Brute Force detection or Port Scan sequences). It outputs preliminary Threat Indicators.

### 4. Zyron AI Engine (`modules/zyron_ai/`)
The cognitive core of the framework. It acts as a heuristic and anomaly detection overlay. It receives parsed events and indicators from the Threat Detector and calculates a dynamic Risk Score (0-100) and categorizes the threat level (LOW, MEDIUM, HIGH, CRITICAL).

### 5. Response Engine (`modules/response_engine/`)
An automated orchestration module. Based on the Risk Assessment provided by Zyron AI, it simulates active defense measures, such as blackholing IP addresses or rate-limiting suspicious actors.

### 6. Cyber Range Sandbox (`modules/cyber_range/`)
A virtualized environment manager. It allows for the controlled injection of vulnerabilities and the execution of simulated attack scenarios to observe how the defense pipeline reacts.