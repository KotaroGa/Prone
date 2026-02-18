from notifier import TelegramNotifier
from price_checker import fetch_prices

def main():
    notifier = TelegramNotifier()
    prices = fetch_prices()

    if prices:
        print("[INFO] Prices fetched successfully: ")
        for symbol, price in prices.items():
            print(f"{symbol}: ${price}")
        # Example: send a test message
        notifier.send_message(f"Current prices: {prices}")
    else:
        print("[WARN] No prices fetched.")


if __name__=="__main__":
    main()
