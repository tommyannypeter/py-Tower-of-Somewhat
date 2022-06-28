from action import Action

from logger import LOGGER

def stage() -> Action:
    LOGGER.info("Enter Stage")
    return Action.QUIT
