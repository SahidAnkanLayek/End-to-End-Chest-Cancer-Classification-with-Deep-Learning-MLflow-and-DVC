from cnnClassifier.utils.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Logging setup works! This is an info message.")
    logger.debug("This is a debug message (visible in file, not console).")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

if __name__ == "__main__":
    main()
