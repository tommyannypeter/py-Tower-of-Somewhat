import sys
from enum import Enum, auto
import pygame
from pygame.locals import QUIT

from config import CONFIG
from logger import LOGGER
from color import Color

class State(Enum):
    OPENING = auto()
    STAGE = auto()
    EXIT = auto()

class Action(Enum):
    START_GAME = auto()
    GAME_OVER = auto()
    LEAVE = auto()

def opening():
    title = "Tower-of-Somewhat"
    pygame.display.set_caption(title)
    LOGGER.debug(f"Set window title: {title}")

    background_color = Color.BLACK
    window.fill(background_color.value)
    LOGGER.debug(f"Set background color: {background_color}")

    title_font = pygame.font.SysFont(None, 60)
    title_text = title_font.render(title, True, Color.WHITE.value)
    title_text_frame = title_text.get_rect(center=(CONFIG.width / 2, CONFIG.height / 10))
    window.blit(title_text, title_text_frame)
    LOGGER.debug(f"Print title: {title}")

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return Action.LEAVE

def stage():
    return Action.LEAVE

if __name__ == "__main__":
    LOGGER.info("Initialize...")
    pygame.init()

    window = pygame.display.set_mode((CONFIG.width, CONFIG.height))
    LOGGER.debug(f"Set width and height: {(CONFIG.width, CONFIG.height)}")

    current_state = State.OPENING

    while current_state != State.EXIT:
        if current_state == State.OPENING:
            LOGGER.info("Enter Opening")
            action = opening()
            if action == Action.LEAVE:
                current_state = State.EXIT
        elif current_state == State.STAGE:
            LOGGER.info("Enter Stage")
            action = stage()
            if action == Action.LEAVE:
                current_state = State.EXIT

    LOGGER.info("Quit Game")
    pygame.quit()
    sys.exit()
