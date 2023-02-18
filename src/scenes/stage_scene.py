import time
import pygame

from config import CONFIG
from logger import LOGGER
from action import Action
from color import Color
from textprinter import TextPrinter
from scenes.scene import Scene

class StageScene(Scene):
    def __init__(self, name: str, window: pygame.Surface) -> None:
        super().__init__(name, window)
        title_printer = TextPrinter(
            text='Stage 1',
            font_size=60,
            position=(CONFIG.width / 2, CONFIG.height / 10),
            color=Color.WHITE
        )
        self._printers.append(title_printer)

    def _detail(self) -> Action:
        self._print_all()
        LOGGER.debug("Initialize display")

        LOGGER.warning("Not Implemented...Sleep for 5 sec")
        time.sleep(5)
        return Action.QUIT
