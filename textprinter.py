import pygame

from color import Color

class TextPrinter:
    def __init__(self, text: str, font_size: int, position: tuple, color: Color) -> None:
        self.text = text
        self.font_size = font_size
        self.position = position
        self.color = color
        self.font = pygame.font.SysFont(None, self.font_size)
        self.text_surface = self.font.render(self.text, True, self.color.value)

    def set_text(self, text: str) -> None:
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color.value)

    def set_font_size(self, font_size: int) -> None:
        self.font_size = font_size
        self.font = pygame.font.SysFont(None, self.font_size)
        self.text_surface = self.font.render(self.text, True, self.color.value)

    def set_position(self, position: tuple) -> None:
        self.position = position

    def set_color(self, color: Color) -> None:
        self.color = color
        self.text_surface = self.font.render(self.text, True, self.color.value)

    def get_frame(self) -> pygame.Rect:
        return self.text_surface.get_rect(center=self.position)

    def print(self, window: pygame.Surface) -> None:
        window.blit(self.text_surface, self.get_frame())

    def is_touch_mouse(self) -> bool:
        mouse_position = pygame.mouse.get_pos()
        return self.get_frame().collidepoint(mouse_position[0], mouse_position[1])
