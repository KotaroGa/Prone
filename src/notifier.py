from pathlib import Path
import os
import requests
import logging
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR /".env")

logger = logging.getLogger("prone")

class TelegramNotifier:
    def __init__(self) -> None:
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

        if not self.token or not self.chat_id:
            logger.error("Missing Telegram configuration in enviroment variables")
            raise ValueError("Missing Telegram configuration in enviroment variables")

        self.base_url = f"https://api.telegram.org/bot{self.token}/sendMessage"


    def send_message(self, message: str) -> None:
        payload = {
            "chat_id": self.chat_id,
            "text": message,
        }

        try:
            logger.info("Sending Telegram message")

            response = requests.post(
                self.base_url,
                json=payload,
                timeout=10
            )

            if response.status_code != 200:
                logger.error(
                    f"Telegram API error: {response.status_code} | {response.text}"
                )
                raise RuntimeError(
                    f"Failed to send Telegram message: {response.text}"
                )

        except requests.RequestException as error:
            logger.error(f"Telegram request failed: {error}")
            raise
