import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    """Set up the logger for the framework."""
    # Get the absolute path of the project root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    log_dir = os.path.join(project_root, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("api_framework")
    logger.setLevel(logging.INFO)
    logger.propagate = False

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
