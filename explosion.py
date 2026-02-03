import os
import pygame
from pygame.sprite import Sprite





# === Класс взрыва ===
class Explosion(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = []
        self.load_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))
        self.frame_rate = 50  # мс между кадрами
        self.last_update = pygame.time.get_ticks()

    def load_frames(self):
        """
        Загружаем кадры взрыва.
        Здесь предполагается, что у вас есть папка 'explosion'
        с изображениями explosion1.png, explosion2.png, ...
        """
        for i in range(1, 14):  # 5 кадров
            img_path = os.path.join("images/explosion", f"explosion{i}.png")
            image = pygame.image.load(img_path).convert_alpha()
            self.frames.append(image)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index < len(self.frames):
                self.image = self.frames[self.frame_index]
            else:
                self.kill()  # Удаляем спрайт после завершения анимации