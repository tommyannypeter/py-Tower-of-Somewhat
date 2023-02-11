import sys
import pygame

from config import CONFIG
from logger import LOGGER
from state import State
from action import Action
from opening import Opening
from stage import Stage

def should_continue(state: State) -> bool:
    return state != State.EXIT

def next_action(state: State) -> Action:
    match state:
        case State.OPENING:
            scene = Opening(name='Opening', window=window)
        case State.STAGE:
            scene = Stage(name='Stage', window=window)
        case _:
            LOGGER.error("Not implemented state: %s", str(state))
            LOGGER.error("Quit directly")
            return Action.QUIT
    return scene.start()

if __name__ == "__main__":
    LOGGER.info("Initialize...")
    pygame.init()

    pygame.display.set_caption("Tower-of-Somewhat")
    LOGGER.debug("Set window title")

    window = pygame.display.set_mode((CONFIG.width, CONFIG.height))
    LOGGER.debug("Set width and height: (%d, %d)", CONFIG.width, CONFIG.height)

    current_state = State.OPENING

    while should_continue(current_state):
        match next_action(current_state):
            case Action.START:
                current_state = State.STAGE
            case Action.QUIT:
                current_state = State.EXIT

    LOGGER.info("Quit Game")
    pygame.quit()
    sys.exit()
