"""
Configuration for Prone crypto monitoring
"""

import os

# Telegram settings (already used in notifier)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Cryptocurrencies to track
# Forma: SYMBOL: friendly_name
CRYPTOCURRENCIES = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "solana": "Solana"
}

# Price alert thresholds (optional)
# Format: SYMBOL: {"upper": float, "lower": float}
PRICE_ALERTS = {
    "bitcoin": {"upper": 30000, "lower": 20000},
    "ethereum": {"upper": 2000, "lower": 1000},
    "solana": {"upper": 50, "lower": 20}
}

# API settings
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
