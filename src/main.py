
"""
Prone - Crypto Monitoring Bot
Entry point
"""

import time
from notifier import TelegramNotifier
from price_fetcher import fetch_prices
from alert_logic import check_alerts
from state_manager import load_state, save_state
from config import load_crypto_config, get_check_interval
from logger import setup_logger

config = load_crypto_config()
CHECK_INTERVAL = get_check_interval()


def main():
    notifier = TelegramNotifier()
    previous_states = load_state()
    logger = setup_logger()

    logger.info("Prone monitoring started")

    while True:
        prices = fetch_prices()

        if prices:
            alerts, previous_states = check_alerts(
                prices,
                config,
                previous_states
            )

            for alert in alerts:
                logger.info(alert)
                notifier.send_message(alert)
            
            save_state(previous_states)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
