import sys
import pygame

from config import CONFIG
from logger import LOGGER
from state import State
from action import Action
from opening import opening
from stage import stage

def should_continue(state: State) -> bool:
    return state != State.EXIT

def next_action(state: State) -> Action:
    if state == State.OPENING:
        return opening(window)
    if state == State.STAGE:
        return stage()
    LOGGER.error(f"Not implemented state: {state}")
    LOGGER.error("Quit directly")
    return Action.QUIT

if __name__ == "__main__":
    LOGGER.info("Initialize...")
    pygame.init()

    pygame.display.set_caption("Tower-of-Somewhat")
    LOGGER.debug("Set window title")

    window = pygame.display.set_mode((CONFIG.width, CONFIG.height))
    LOGGER.debug(f"Set width and height: {(CONFIG.width, CONFIG.height)}")

    current_state = State.OPENING

    while should_continue(current_state):
        match next_action(current_state):
            case Action.QUIT:
                current_state = State.EXIT

    LOGGER.info("Quit Game")
    pygame.quit()
    sys.exit()
