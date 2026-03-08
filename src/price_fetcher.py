
"""
Handles crypto price retrieval from external API
"""

import requests
from config import CRYPTOCURRENCIES, COINGECKO_API_URL


def fetch_prices() -> dict:
    """
    Fetches current USD prices for configured cryptocurrencies.
    Returns:
        dict: {symbol: price}
    """
    ids = ",".join(CRYPTOCURRENCIES.keys())
    params = {
        "ids": ids,
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(
            COINGECKO_API_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        return {
            symbol: data[symbol]["usd"]
            for symbol in CRYPTOCURRENCIES.keys()
            if symbol in data
        }

    except requests.RequestException as error:
        print(f"[ERROR] Price fetch failed: {error}")
        return {}