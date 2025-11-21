import pygame


class Alien:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение пришельца и получает треугольник.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        # Каждый новый пришелец появляется у нижнего края экрана.
        self.rect.topleft = self.screen_rect.topleft = (560, 40)

    def blitme(self):
        """Рисует пришельца в текущей позиции."""
        self.screen.blit(self.image, self.rect)
