
"""
Prone - Crypto Monitoring Bot
Entry point
"""

import time
from notifier import TelegramNotifier
from price_fetcher import fetch_prices
from alert_logic import check_alerts
from config import CHECK_INTERVAL


def main():
    notifier = TelegramNotifier()
    previous_states = {}

    print("[SYSTEM] Prone monitoring started.")

    while True:
        prices = fetch_prices()

        if prices:
            alerts, previous_states = check_alerts(
                prices,
                previous_states
            )

            for alert in alerts:
                print(f"[ALERT] {alert}")
                notifier.send_message(alert)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
