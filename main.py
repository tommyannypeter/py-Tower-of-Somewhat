import pygame

from config import CONFIG
from logger import LOGGER
from state import State
from action import Action
from opening import Opening
from stage import Stage

class TowerOfSomewhat():
    def __init__(self) -> None:
        LOGGER.info("Initialize...")
        pygame.init()
        pygame.display.set_caption("Tower-of-Somewhat")
        LOGGER.debug("Set window title")
        self._window = pygame.display.set_mode((CONFIG.width, CONFIG.height))
        LOGGER.debug("Set width and height: (%d, %d)", CONFIG.width, CONFIG.height)

    def start(self) -> None:
        current_state = State.OPENING
        while self._should_continue(current_state):
            current_state = self._next_state(current_state)
        LOGGER.info("Quit Game")
        pygame.quit()

    def _should_continue(self, state: State) -> bool:
        return state != State.EXIT

    def _next_state(self, state: State) -> State:
        match self._next_action(state):
            case Action.START:
                return State.STAGE
            case Action.QUIT:
                return State.EXIT

    def _next_action(self, state: State) -> Action:
        match state:
            case State.OPENING:
                scene = Opening(name='Opening', window=self._window)
                return scene.start()
            case State.STAGE:
                scene = Stage(name='Stage', window=self._window)
                return scene.start()
            case _:
                LOGGER.error("Not implemented state: %s", str(state))
                LOGGER.error("Quit directly")
                return Action.QUIT

if __name__ == "__main__":
    game = TowerOfSomewhat()
    game.start()
