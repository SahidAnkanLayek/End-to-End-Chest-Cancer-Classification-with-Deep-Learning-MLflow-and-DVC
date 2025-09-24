# src/cnnClassifier/utils/logger.py
import logging
from logging.config import dictConfig
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "level": "DEBUG",
            "filename": os.path.join(LOG_DIR, "app.log"),
            "when": "midnight",
            "backupCount": 7,
            "encoding": "utf-8",
            "utc": False
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG"
    },
}

dictConfig(LOGGING_CONFIG)

def get_logger(name: str):
    return logging.getLogger(name)
