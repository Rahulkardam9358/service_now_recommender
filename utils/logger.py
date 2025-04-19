import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(
        self,
        name: str = "app_logger",
        log_level: int = logging.INFO,
        log_file: str = "logs/app.log",
        max_bytes: int = 1_000_000,
        backup_count: int = 3
    ):
        self.name = name
        self.log_level = log_level
        self.log_file = log_file
        self.max_bytes = max_bytes
        self.backup_count = backup_count

        self._logger = None
        self._initialize_logger()

    def _initialize_logger(self):
        log_path = Path(self.log_file).parent
        log_path.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger(self.name)
        logger.setLevel(self.log_level)

        # Avoid duplicate handlers
        if not logger.handlers:
            formatter = logging.Formatter(
                "[%(levelname)s] %(asctime)s - %(name)s - %(message)s"
            )

            # Console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)

            # File handler
            file_handler = RotatingFileHandler(
                self.log_file, maxBytes=self.max_bytes, backupCount=self.backup_count
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        self._logger = logger

    def get_logger(self) -> logging.Logger:
        return self._logger
