import sys
import pygame
from pygame.locals import QUIT

from Color import Color

if __name__ == '__main__':
    print('Initialize...')
    pygame.init()

    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    print('Set width and height:', (width, height))

    title = 'Tower-of-Somewhat'
    pygame.display.set_caption(title)
    print('Set window title:', title)

    background_color = Color.BLACK
    window.fill(background_color.value)
    print('Set background color:', background_color)

    title_font = pygame.font.SysFont(None, 60)
    title_text = title_font.render(title, True, Color.WHITE.value)
    title_text_frame = title_text.get_rect(center=(width / 2, 50))
    window.blit(title_text, title_text_frame)
    print('Print title:', title)

    pygame.display.update()

    print('Press X on the top-right of the screen to exit.')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
