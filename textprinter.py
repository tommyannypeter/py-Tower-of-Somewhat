import pygame

from color import Color

class TextPrinter:
    def __init__(self, text: str, font_size: int, position: tuple, color: Color) -> None:
        self._text = text
        self._font_size = font_size
        self._position = position
        self._color = color
        self._font = pygame.font.SysFont(None, self._font_size)
        self._text_surface = self._font.render(self._text, True, self._color.value)

    def set_text(self, text: str) -> None:
        self._text = text
        self._text_surface = self._font.render(self._text, True, self._color.value)

    def get_text(self) -> str:
        return self._text

    def set_font_size(self, font_size: int) -> None:
        self._font_size = font_size
        self._font = pygame.font.SysFont(None, self._font_size)
        self._text_surface = self._font.render(self._text, True, self._color.value)

    def set_position(self, position: tuple) -> None:
        self._position = position

    def set_color(self, color: Color) -> None:
        self._color = color
        self._text_surface = self._font.render(self._text, True, self._color.value)

    def get_frame(self) -> pygame.Rect:
        return self._text_surface.get_rect(center=self._position)

    def print(self, window: pygame.Surface) -> None:
        window.blit(self._text_surface, self.get_frame())

    def is_touch_mouse(self) -> bool:
        mouse_position = pygame.mouse.get_pos()
        return self.get_frame().collidepoint(mouse_position[0], mouse_position[1])
