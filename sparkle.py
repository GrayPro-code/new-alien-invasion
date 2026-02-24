import pygame
import random
import math




# --- Класс блестящей точки ---
class Sparkle:
    def __init__(self):
        self.x = random.randint(0, 1200)
        self.y = random.randint(0, 700)
        self.radius = random.randint(1, 3)
        self.base_brightness = random.randint(1, 255)
        self.phase = random.uniform(0, math.pi * 2)  # для мерцания
        self.speed_x = random.uniform(-0.1, 0.1)
        self.speed_y = random.uniform(-0.1, 0.1)

    def update(self):
        # Двигаем точку
        self.x += self.speed_x
        self.y += self.speed_y

        # Отражение от краёв
        if self.x < 0 or self.x > 1200:
            self.speed_x *= -1
        if self.y < 0 or self.y > 700:
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


