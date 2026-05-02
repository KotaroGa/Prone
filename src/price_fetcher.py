
"""
Handles crypto price retrieval from external API
"""

import requests
import logging

logger = logging.getLogger("prone")

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"


def fetch_prices(symbols: list[str]) -> dict:
    """
    Fetches current USD prices for given cryptocurrencies.

    Args:
        symbols: list of crypto ids (e.g. ["bitcoin", "ethereum"])

    Returns:
        dict: {symbol: price}
    """

    if not symbols:
        logger.warning("No symbols provided for price fetch")
        return {}

    ids = ",".join(symbols)

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
            for symbol in symbols
            if symbol in data
        }

    except requests.RequestException as error:
        logger.error(f"Price fetch failed: {error}")
        return {}
