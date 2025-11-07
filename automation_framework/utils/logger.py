import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    """Set up the logger for the framework."""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("api_framework")
    logger.setLevel(logging.INFO)

    # Create a rotating file handler
    handler = RotatingFileHandler(
        os.path.join(log_dir, "framework.log"),
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=2,
    )

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

logger = setup_logger()
