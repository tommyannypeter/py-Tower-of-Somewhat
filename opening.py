import pygame

from config import CONFIG
from logger import LOGGER
from action import Action
from color import Color
from textprinter import TextPrinter

def opening(window: pygame.Surface) -> Action:
    background_color = Color.BLACK
    LOGGER.debug(f"Set background color: {background_color}")

    title_printer = TextPrinter(
        text="Tower-of-Somewhat",
        font_size=60,
        position=(CONFIG.width / 2, CONFIG.height / 10),
        color=Color.WHITE
    )

    menu_start_printer = TextPrinter(
        text="Start",
        font_size=45,
        position=(CONFIG.width / 2, CONFIG.height / 2),
        color=Color.WHITE
    )

    menu_quit_printer = TextPrinter(
        text="Quit",
        font_size=45,
        position=(CONFIG.width / 2, CONFIG.height / 2 + CONFIG.height / 12),
        color=Color.WHITE
    )

    def print_all() -> None:
        window.fill(background_color.value)
        title_printer.print(window)
        menu_start_printer.print(window)
        menu_quit_printer.print(window)

    print_all()
    LOGGER.debug("Initialize display")
    pygame.display.update()

    while True:
        mouse_position = pygame.mouse.get_pos()
        if menu_start_printer.get_frame().collidepoint(mouse_position[0], mouse_position[1]):
            menu_start_printer.set_color(Color.YELLOW)
        else:
            menu_start_printer.set_color(Color.WHITE)
        if menu_quit_printer.get_frame().collidepoint(mouse_position[0], mouse_position[1]):
            menu_quit_printer.set_color(Color.YELLOW)
        else:
            menu_quit_printer.set_color(Color.WHITE)
        print_all()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Action.QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_quit_printer.get_frame().collidepoint(mouse_position[0], mouse_position[1]):
                    return Action.QUIT
