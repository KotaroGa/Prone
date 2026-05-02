"""
Configuration loader for Prone
"""

import os
import logging

logger = logging.getLogger("prone")



def load_crypto_config() -> dict:
    """
    Loads crypto config from env.

    Format:
        CRYPTO_ASSETS=bitcoin:30000:20000,ethereum:2000:1000
    """
    raw_config = os.getenv("CRYPTO_ASSETS")

    if not raw_config:
        raise ValueError("CRYPTO_ASSETS not defined")
    
    assets = {}

    try:
        pairs = raw_config.split(",")

        for pair in pairs:
            symbol, upper, lower = pair.split(":")

            assets[symbol.strip()] = {
                "upper": float(upper),
                "lower": float(lower)
            }

        logger.info(f"Loaded {len(assets)} assets from config")
        return assets
    
    except Exception as e:
        logger.error(f"Invalid CRYPTO_ASSETS format: {e}")
        raise



def get_check_interval() -> int:
    return int(os.getenv("CHECK_INTERVAL", 60))
