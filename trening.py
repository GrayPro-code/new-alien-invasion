import pygame
import random
import math
import sys

# --- Настройки ---
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_SPARKLES = 50

# Цвет фона
BACKGROUND_COLOR = (10, 10, 30)

# --- Класс блестящей точки ---
class Sparkle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(1, 3)
        self.base_brightness = random.randint(100, 255)
        self.phase = random.uniform(0, math.pi * 2)  # для мерцания
        self.speed_x = random.uniform(-0.5, 0.5)
        self.speed_y = random.uniform(-0.5, 0.5)

    def update(self):
        # Двигаем точку
        self.x += self.speed_x
        self.y += self.speed_y

        # Отражение от краёв
        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

        # Мерцание
        self.phase += 0.05
        if self.phase > math.pi * 2:
            self.phase -= math.pi * 2

    def draw(self, surface):
        # Вычисляем текущую яркость
        brightness = self.base_brightness + int(50 * math.sin(self.phase))
        brightness = max(0, min(255, brightness))
        color = (brightness, brightness, brightness)

        # Рисуем мягкое свечение
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.radius)

# --- Основная программа ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Яркие блестящие точки")
    clock = pygame.time.Clock()

    # Создаём список блесток
    sparkles = [Sparkle() for _ in range(NUM_SPARKLES)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обновляем блестки
        for sparkle in sparkles:
            sparkle.update()

        # Рисуем фон
        screen.fill(BACKGROUND_COLOR)

        # Рисуем блестки
        for sparkle in sparkles:
            sparkle.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
