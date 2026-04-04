
import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%D-%M-%Y %H:%M:%S",
    )

    return logging.getLogger("prone")
