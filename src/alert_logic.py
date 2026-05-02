"""
Handles price threshold comparison and alert state management
"""

def check_alerts(prices: dict, config: dict, previous_states: dict):
    """
    Compares prices against configured thresholds.

    Args:
        prices: dict of current prices
        config: dict with thresholds per asset
        previous_states: dict with last known states

    Returns:
        tuple:
            - list of alert messages
            - updated state dict
    """

    alerts = []
    updated_states = previous_states.copy()

    for symbol, price in prices.items():
        asset_config = config.get(symbol)
        if not asset_config:
            continue

        upper = asset_config.get("upper")
        lower = asset_config.get("lower")


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
                    f"🔻 {symbol.upper()} dropped below ${lower} -> ${price}"
                )
                updated_states[symbol] = "below"

        else:
            updated_states[symbol] = "normal"
        
    return alerts, updated_states
