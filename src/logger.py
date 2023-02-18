import logging

class _CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, with_color=True) -> None:
        text = "[%(asctime)s.%(msecs)03d][%(filename)s:%(lineno)d][%(levelname)s]: %(message)s"
        super().__init__(text, datefmt='%Y%m%d_%H:%M:%S')
        self._with_color = with_color

    def format(self, record):
        # pylint: disable=W0212
        if self._with_color:
            colored_fmt = {
                logging.DEBUG   : self.grey + self._fmt + self.reset,
                logging.INFO    : self.grey + self._fmt + self.reset,
                logging.WARNING : self.yellow + self._fmt + self.reset,
                logging.ERROR   : self.red + self._fmt + self.reset,
                logging.CRITICAL: self.bold_red + self._fmt + self.reset
            }
            self._style._fmt = colored_fmt.get(record.levelno)
        return super().format(record)

_stream_handler = logging.StreamHandler()
_stream_handler.setFormatter(_CustomFormatter())
_stream_handler.setLevel(logging.INFO)

_file_handler = logging.FileHandler('tos.log', 'w+')
_file_handler.setFormatter(_CustomFormatter(with_color=False))
_file_handler.setLevel(logging.DEBUG)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(_stream_handler)
LOGGER.addHandler(_file_handler)
LOGGER.setLevel(logging.DEBUG)
