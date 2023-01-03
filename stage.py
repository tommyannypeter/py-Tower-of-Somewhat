import time
import pygame

from config import CONFIG
from logger import LOGGER
from action import Action
from color import Color
from textprinter import TextPrinter

def stage(window: pygame.Surface) -> Action:
    LOGGER.info("Enter Stage")

    background_color = Color.BLACK
    LOGGER.debug(f"Set background color: {background_color}")

    title_printer = TextPrinter(
        text="Stage 1",
        font_size=60,
        position=(CONFIG.width / 2, CONFIG.height / 10),
        color=Color.WHITE
    )

    def print_all() -> None:
        window.fill(background_color.value)
        title_printer.print(window)

    print_all()
    LOGGER.debug("Initialize display")
    pygame.display.update()

    time.sleep(5)
    return Action.QUIT
