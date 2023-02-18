from typing import List
from abc import ABC, abstractmethod
import pygame

from logger import LOGGER
from action import Action
from color import Color
from textprinter import TextPrinter

class Scene(ABC):
    def __init__(self, name: str, window: pygame.Surface) -> None:
        self._name = name
        self._window = window
        self._background_color = Color.BLACK
        self._printers: List[TextPrinter]
        self._printers = []
        LOGGER.debug("Create Scene: %s", self._name)

    def start(self) -> Action:
        LOGGER.info("Enter %s", self._name)
        return self._detail()

    def _print_all(self) -> None:
        self._window.fill(self._background_color.value)
        for printer in self._printers:
            printer.print(self._window)
        pygame.display.update()

    @abstractmethod
    def _detail(self) -> Action:
        ...
