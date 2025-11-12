import logging
import os
import datetime

def setup_logger():
    """Set up the logger for the framework."""
    # Get the absolute path of the project root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Create reports directory if it doesn't exist
    reports_dir = os.path.join(project_root, "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        
    # Create logs directory inside reports
    log_dir = os.path.join(reports_dir, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a unique log file name with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"test_run_{timestamp}.log")

    logger = logging.getLogger("api_framework")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a file handler
    handler = logging.FileHandler(log_file)

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
