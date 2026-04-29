# Threat Detection & Response Workflows

## Standard Log Processing Workflow
1. **Generation:** Attack Simulation script writes to `logs/X.log`.
2. **Collection:** `LogCollector` reads new lines from `logs/X.log` and clears it.
3. **Parsing:** `LogParser` converts the string into a Python dictionary.
4. **Correlation:** `ThreatDetector` updates state and flags indicators if rules match.
5. **Scoring:** `ZyronAIEngine` calculates final risk based on indicators and ML heuristics.
6. **Action:** `ResponseEngine` takes automated action based on `ZyronAIEngine` output.

## Automated Response Escalation Path
- **LOW:** No action, logged for reporting.
- **MEDIUM:** IP added to watchlist. Simulated rate-limiting applied.
- **HIGH:** IP temporarily blocked at the firewall level (e.g., 3600 seconds).
- **CRITICAL:** Segment isolated. IP permanently blackholed. Mandatory human review triggered.