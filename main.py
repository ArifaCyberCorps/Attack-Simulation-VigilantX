import sys
import time
import logging
from configs.config_loader import load_config
from modules.log_collector.collector import LogCollector
from modules.log_parser.parser import LogParser
from modules.threat_detector.detector import ThreatDetector
from modules.zyron_ai.engine import ZyronAIEngine
from modules.response_engine.responder import ResponseEngine

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("VigilantX-Main")

def main():
    logger.info("Initializing VigilantX Autonomous Cyber Defense Framework...")
    
    # Load configuration
    config = load_config("configs/system_config.yaml")
    
    # Initialize Modules
    collector = LogCollector(config)
    parser = LogParser(config)
    detector = ThreatDetector(config)
    ai_engine = ZyronAIEngine(config)
    responder = ResponseEngine(config)
    
    logger.info("Pipeline modules loaded successfully. Awaiting logs...")
    
    try:
        while True:
            # 1. Log Generation/Collection
            raw_logs = collector.fetch_new_logs()
            
            for raw_log in raw_logs:
                # 2. Log Parsing
                parsed_event = parser.parse(raw_log)
                if not parsed_event:
                    continue
                
                # 3 & 4. Threat Detection & Correlation
                threat_indicators = detector.analyze(parsed_event)
                
                # 5. Risk Scoring (Zyron AI)
                risk_assessment = ai_engine.evaluate(parsed_event, threat_indicators)
                
                # 6. Alert Generation & Response Simulation
                if risk_assessment['risk_level'] in ['MEDIUM', 'HIGH', 'CRITICAL']:
                    logger.warning(f"ALERT: {risk_assessment['risk_level']} Threat Detected! Confidence: {risk_assessment['confidence']:.2f}%")
                    responder.execute_action(parsed_event, risk_assessment)
                    
            time.sleep(config.get('pipeline', {}).get('poll_interval_sec', 5))
            
    except KeyboardInterrupt:
        logger.info("VigilantX shutting down gracefully.")
        sys.exit(0)

if __name__ == "__main__":
    main()