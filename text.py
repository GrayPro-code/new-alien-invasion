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


#def main():
#    pygame.init()
#    screen = pygame.display.set_mode((500, 700))
#    pygame.display.set_caption("Плавное появление текста")
#
#    clock = pygame.time.Clock()
#
#    # Загружаем фоновое изображение
#    try:
#        background = pygame.image.load("images/menu.jpg").convert()
#        background = pygame.transform.scale(background, (500, 700))
#    except pygame.error:
#        print("Ошибка: не найден файл background.jpg")
#        pygame.quit()
#        sys.exit()
#
#    # Шрифт
#    font_text = pygame.font.Font(None, 72)  # None = стандартный шрифт
#
#    # Создаём объект текста
#    fade_text = TextFadeIn("ALIEN INVASION", font_text, (255, 255, 255), (50, 500), speed=1)
#    fade_text_2 = TextFadeIn("ARMAGEDDON", font_text, (255, 255, 255), (70, 570), speed=0.1)
#
#    running = True
#    while running:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                running = False
#            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#                running = False
#
#        # Обновляем состояние текста
#        fade_text.update()
#        fade_text_2.update()
#
#        # Рисуем фон и текст
#        screen.blit(background, (0, 0))
#        fade_text.draw(screen)
#        fade_text_2.draw(screen)
#
#        pygame.display.flip()
#        clock.tick(60)
#
#    pygame.quit()
#    sys.exit()
#
#
#if __name__ == "__main__":
#    main()
