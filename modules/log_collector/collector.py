import os
import glob
import logging

class LogCollector:
    def __init__(self, config):
        self.log_dir = config.get('pipeline', {}).get('log_directory', 'logs/')
        self.processed_files = set()
        
    def fetch_new_logs(self):
        """Fetches newly written logs from the simulated log directory."""
        new_logs = []
        if not os.path.exists(self.log_dir):
            return new_logs
            
        log_files = glob.glob(os.path.join(self.log_dir, "*.log"))
        
        for file_path in log_files:
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        new_logs.append(line.strip())
                # For simulation, we just clear the file to act like we processed the stream
                open(file_path, 'w').close() 
            except Exception as e:
                logging.error(f"Failed reading log file {file_path}: {e}")
                
        return new_logs