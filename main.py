import sys
import pygame

from config import CONFIG
from logger import LOGGER
from state import State
from action import Action
from opening import opening
from stage import stage

if __name__ == "__main__":
    LOGGER.info("Initialize...")
    pygame.init()

    window = pygame.display.set_mode((CONFIG.width, CONFIG.height))
    LOGGER.debug(f"Set width and height: {(CONFIG.width, CONFIG.height)}")

    current_state = State.OPENING

    while current_state != State.EXIT:
        if current_state == State.OPENING:
            LOGGER.info("Enter Opening")
            action = opening(window)
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
