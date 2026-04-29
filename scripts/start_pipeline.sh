#!/bin/bash
# Start the VigilantX Core Pipeline

echo "================================================="
echo " Starting VigilantX Autonomous Defense Framework"
echo "================================================="

# Set python path to current directory to allow module imports
export PYTHONPATH=$(pwd)

# Create logs directory if it doesn't exist
mkdir -p logs

echo "[INFO] Launching main pipeline..."
python main.py
