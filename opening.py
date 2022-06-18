import pygame
from pygame.locals import QUIT

from config import CONFIG
from logger import LOGGER
from action import Action
from color import Color

def opening(window):
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
