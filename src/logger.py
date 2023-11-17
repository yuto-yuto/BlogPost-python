import logging
import logging.handlers
import os


class Logger:
    def __init__(self, *, log_path: str, name: str, level=logging.INFO) -> None:
        self._log = logging.getLogger(name)
        self._log.setLevel(level)

        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        rotatingHandler = logging.handlers.RotatingFileHandler(
            log_path,
            encoding="utf-8",
            maxBytes=1024 * 1024,  # 1 MB
            backupCount=10,
        )

        formatter = (
            "%(asctime)s [%(levelname)s] - %(pathname)s line %(lineno)d - %(message)s"
        )
        rotatingHandler.setFormatter(logging.Formatter(formatter))

        self._log.addHandler(rotatingHandler)

    def debug(self, msg: str) -> None:
        """Write DEBUG level log"""
        self._log.debug(msg)

    def info(self, msg: str) -> None:
        """Write INFO level log"""
        self._log.info(msg)

    def warn(self, msg: str) -> None:
        """Write WARNING level log"""
        self._log.warning(msg)

    def error(self, msg: str) -> None:
        """Write ERROR level log"""
        self._log.error(msg)

    def fatal(self, msg: str) -> None:
        """Write FATAL level log"""
        self._log.fatal(msg)
