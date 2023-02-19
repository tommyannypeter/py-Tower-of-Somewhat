from typing import List
from typing import Union
import pygame

from config import CONFIG
from logger import LOGGER
from action import Action
from color import Color
from textprinter import TextPrinter
from scenes.scene import Scene

class OpeningScene(Scene):
    def __init__(self, name: str, window: pygame.Surface) -> None:
        super().__init__(name, window)
        title_printer = TextPrinter(
            text='Tower-of-Somewhat',
            font_size=60,
            position=(CONFIG.width / 2, CONFIG.height / 10),
            color=Color.WHITE
        )
        self._printers.append(title_printer)
        menu_start_printer = TextPrinter(
            text='Start',
            font_size=45,
            position=(CONFIG.width / 2, CONFIG.height / 2),
            color=Color.WHITE
        )
        self._printers.append(menu_start_printer)
        menu_quit_printer = TextPrinter(
            text='Quit',
            font_size=45,
            position=(CONFIG.width / 2, CONFIG.height / 2 + CONFIG.height / 12),
            color=Color.WHITE
        )
        self._printers.append(menu_quit_printer)
        self._options: List[TextPrinter]
        self._options = []
        self._options.append(menu_start_printer)
        self._options.append(menu_quit_printer)

    def _detail(self) -> Action:
        self._print_all()
        LOGGER.debug("Initialize display")

        while True:
            self._highlight_touched_options()
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        return Action.QUIT
                    case pygame.MOUSEBUTTONDOWN:
                        action = self._get_click_action()
                        if action:
                            return action

    def _highlight_touched_options(self) -> None:
        for option in self._options:
            if option.is_touch_mouse():
                option.set_color(Color.YELLOW)
            else:
                option.set_color(Color.WHITE)
        self._print_all()

    def _get_click_action(self) -> Union[Action, None]:
        for option in self._options:
            if option.is_touch_mouse():
                match option.get_text():
                    case 'Start':
                        return Action.START
                    case 'Quit':
                        return Action.QUIT
        return None
