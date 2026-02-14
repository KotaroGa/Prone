from notifier import TelegramNotifier

def main() -> None:
    notifier = TelegramNotifier()
    notifier.send_message("Prone bot initialized successfully")


if __name__=="__main__":
	main()
