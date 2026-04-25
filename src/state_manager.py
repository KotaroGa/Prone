
"""
Handles persisten state for alert tracking
"""

import json
from pathlib import Path
import logging

logger = logging.getLogger("prone")

STATE_FILE = Path("state.json")



def load_state() -> dict:
    """
    Loads state from disk
    """
    if not STATE_FILE.exists():
        logger.info("No previous state found. Starting fresh.")
        return {}
    
    try:
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
            logger.info("State loaded from disk")
            return state
        
    except Exception as e:
        logger.error(f"Failed to load state: {e}")
        return {}



def save_state(state: dict) -> None:
    """
    Save state to disk.
    """
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)
        logger.info("State saved")

    except Exception as e:
        logger.error(f"Failed to save state: {e}")
