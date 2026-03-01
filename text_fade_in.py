import pygame
import sys

class TextFadeIn:
    def __init__(self, text, font, color, pos, speed=1):
        """
        text - строка текста
        font - объект pygame.font.Font
        color - цвет текста (R, G, B)
        pos - позиция (x, y)
        speed - скорость появления (1-10, больше = быстрее)
        """
        self.text = text
        self.font = font
        self.color = color
        self.pos = pos
        self.speed = speed
        self.alpha = 0  # Прозрачность (0 - невидимо, 255 - полностью видно)

        # Рендерим текст в Surface
        self.surface = self.font.render(self.text, True, self.color).convert_alpha()

    def update(self):
        """Увеличивает прозрачность до 255"""
        if self.alpha < 255:
            self.alpha += self.speed
            if self.alpha > 255:
                self.alpha = 255
        self.surface.set_alpha(self.alpha)

    def draw(self, screen):
        """Отображает текст на экране"""
        screen.blit(self.surface, self.pos)
