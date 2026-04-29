#!/bin/bash
# Run all attack simulations

echo "================================================="
echo " VigilantX - Running All Attack Simulations"
echo "================================================="

export PYTHONPATH=$(pwd)
mkdir -p logs

echo "1. Running Brute Force Simulation"
python simulations/brute_force_attack.py
sleep 2

echo "2. Running Port Scan Simulation"
python simulations/port_scan_simulation.py
sleep 2

echo "3. Running DDoS Simulation"
python simulations/ddos_simulation.py
sleep 2

echo "4. Running Malware Behavior Simulation"
python simulations/malware_behavior.py
sleep 2

echo "5. Running Suspicious Login Simulation"
python simulations/suspicious_login.py
sleep 2

echo "================================================="
echo " All simulations completed. Check the 'logs' directory."
echo "================================================="
