import sys
import pygame
from pygame.locals import QUIT

from logger import LOGGER
from color import Color

if __name__ == "__main__":
    LOGGER.info("Initialize...")
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    LOGGER.debug(f"Set width and height: {(WIDTH, HEIGHT)}")

    TITLE = "Tower-of-Somewhat"
    pygame.display.set_caption(TITLE)
    LOGGER.debug(f"Set window title: {TITLE}")

    background_color = Color.BLACK
    window.fill(background_color.value)
    LOGGER.debug(f"Set background color: {background_color}")

    title_font = pygame.font.SysFont(None, 60)
    title_text = title_font.render(TITLE, True, Color.WHITE.value)
    title_text_frame = title_text.get_rect(center=(WIDTH / 2, 50))
    window.blit(title_text, title_text_frame)
    LOGGER.debug(f"Print title: {TITLE}")

    pygame.display.update()

    print("Press X on the top-right of the screen to exit.")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
