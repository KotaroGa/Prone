"""
Handles price threshold comparison and alert state management
"""

from config import PRICE_ALERTS


def check_alerts(prices: dict, previous_states: dict):
    """
    Compares prices against configured thresholds.

    Returns:
        tuple:
            - list of alert messages
            - update state dict
    """

    alerts = []
    updated_states = previous_states.copy()

    for symbol, price in prices.items():
        threshold = PRICE_ALERTS.get(symbol)
        if not threshold:
            continue

        upper = threshold.get("upper")
        lower = threshold.get("lower")

        # ABOVE threshold
        if upper and price > upper:
            if previous_states.get(symbol) != "above":
                alerts.append(
                    f"🚀 {symbol.upper()} crossed above ${upper} -> ${price}"
                )
                updated_states[symbol] = "above"

        # BELOW threshold
        elif lower and price < lower:
            if previous_states.get(symbol) != "below":
                alerts.append(
                    f"🔻 {symbol.upper()} dropper below ${lower} -> ${price}"
                )
                updated_states[symbol] = "below"

        else:
            updated_states[symbol] = "normal"


    return alerts, updated_states
