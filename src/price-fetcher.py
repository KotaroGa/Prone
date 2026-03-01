"""
Crypto Price Checker
Fetches current prices for configured cryptocurrencies
"""

import requests
from config import CRYPTOCURRENCIES, COINGECKO_API_URL


def fetch_prices() -> dict:
	"""
	Fetches the current price for each cryptocurrency in CRYPTOCURRENCIES.

	Returns:
		dict: {symbol: price_usd}
	"""
	ids = ",".join(CRYPTOCURRENCIES.keys())
	params = {
		"ids": ids,
		"vs_currencies": "usd"
	}

	try:
		response = requests.get(COINGECKO_API_URL, params=params, timeout=10)
		response.raise_for_status()
		data = response.json()

		# Extract prices
		prices = {symbol: data[symbol]["usd"] for symbol in CRYPTOCURRENCIES.keys()}
		return prices

	except requests.RequestException as e:
		print(f"[ERROR] Failed to fetch prices. {e}")
		return {}

