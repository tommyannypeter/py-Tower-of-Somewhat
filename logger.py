import logging

class _CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    text = "[%(asctime)s.%(msecs)03d][%(filename)s:%(lineno)d][%(levelname)s]: %(message)s"

    FORMATS = {
        logging.DEBUG   : grey + text + reset,
        logging.INFO    : grey + text + reset,
        logging.WARNING : yellow + text + reset,
        logging.ERROR   : red + text + reset,
        logging.CRITICAL: bold_red + text + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y%m%d_%H:%M:%S")
        return formatter.format(record)

class _Logger:
    stream_logger = None
    file_logger = None
    def __init__(self) -> None:
        self.set_stream_logger()
        self.set_file_logger()

    def set_stream_logger(self) -> None:
        self.stream_logger = logging.getLogger("stream_logger")
        self.stream_logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(_CustomFormatter())
        self.stream_logger.addHandler(stream_handler)

    def set_file_logger(self) -> None:
        self.file_logger = logging.getLogger("file_logger")
        self.file_logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler("tos.log", "w+")
        self.file_logger.addHandler(file_handler)

    def debug(self, string) -> None:
        self.stream_logger.debug(string)
        self.file_logger.debug(string)

    def info(self, string) -> None:
        self.stream_logger.info(string)
        self.file_logger.info(string)

    def warning(self, string) -> None:
        self.stream_logger.warning(string)
        self.file_logger.warning(string)

    def error(self, string) -> None:
        self.stream_logger.error(string)
        self.file_logger.error(string)

    def critical(self, string) -> None:
        self.stream_logger.critical(string)
        self.file_logger.critical(string)

LOGGER = _Logger()
