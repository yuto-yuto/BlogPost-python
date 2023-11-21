import logging
import logging.handlers
import os
from datetime import datetime
from path import Path


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


_LEVEL_MAP = {
    logging.CRITICAL: 5,
    logging.FATAL: 5,
    logging.ERROR: 4,
    logging.WARNING: 3,
    logging.WARN: 3,
    logging.INFO: 2,
    logging.DEBUG: 1,
    logging.NOTSET: 0,
}


class LoggingFormatter(logging.Formatter):
    """
    CustomFormatter provides a format that supports TNCanalyzer. The format is same as advanced-touch.
    """

    def __init__(self) -> None:
        formatter = "%(custom_time)s <%(custom_log_level)s>[%(levelname)s] %(name)s %(source_path)s line: %(lineno)d %(message)s"
        super().__init__(formatter)

    def format(self, record: logging.LogRecord) -> str:
        # 21.11.2023 18:00:00.567
        record.custom_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
        record.custom_log_level = _LEVEL_MAP.get(record.levelno, 0)
        record.source_path = self.__get_source_path(record)

        return super().format(record)

    def __get_source_path(self, record: logging.LogRecord):
        try:
            parent_dir_name = os.path.basename(os.path.dirname(record.pathname))
            return os.path.join(parent_dir_name, record.filename)
        except BaseException:  # pylint: disable=:broad-exception-caught
            return ""

def generate_logger_with_custom_formatter(log_path: str):
    logger = logging.getLogger("NICE_APP")
    logger.setLevel(logging.DEBUG)
    
    log_path_dir = Path(log_path).parent
    os.makedirs(log_path_dir, exist_ok=True)

    rotatingHandler = logging.handlers.RotatingFileHandler(
        log_path,
        encoding="utf-8",
        maxBytes=1024,
        backupCount=5,
    )
    rotatingHandler.setFormatter(LoggingFormatter())
    logger.addHandler(rotatingHandler)

    return logger


def generate_logger_without_custom_formatter(log_path: str):
    logger = logging.getLogger("ABC_APP")
    logger.setLevel(logging.DEBUG)
    
    log_path_dir = Path(log_path).parent
    os.makedirs(log_path_dir, exist_ok=True)

    rotatingHandler = logging.handlers.RotatingFileHandler(
        log_path,
        encoding="utf-8",
        maxBytes=1024,
        backupCount=5,
    )
    formatter = "%(asctime)s <%(levelno)d>[%(levelname)s] %(name)s %(filename)s line: %(lineno)d %(message)s"
    rotatingHandler.setFormatter(logging.Formatter(formatter))
    logger.addHandler(rotatingHandler)

    return logger

def write_log(logger: logging.Logger):
    logger.debug("message")
    logger.info("message")
    logger.warning("message")
    logger.error("message")
    logger.critical("message")

log_path_dir = Path(__file__).parent.joinpath("temp")
log_path = Path(log_path_dir).joinpath("test.log")
logger_without = generate_logger_without_custom_formatter(str(log_path))
write_log(logger_without)


log_path2 = Path(log_path_dir).joinpath("test.log")
logger_with = generate_logger_with_custom_formatter(str(log_path2))
write_log(logger_with)