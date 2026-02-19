import os
import pygame
from pygame.sprite import Sprite





# === Класс анимации ===
class Animation(Sprite):
    def __init__(self, x, y, name_dir, name_files):
        super().__init__()
        self.frames = []
        self.load_frames(name_dir, name_files)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))
        self.frame_rate = 50  # мс между кадрами
        self.last_update = pygame.time.get_ticks()


    @staticmethod
    def count_images_in_folder(folder_path):
        """
        Считает количество файлов-изображений в указанной папке.
        Поддерживаемые форматы: jpg, jpeg, png, gif, bmp, tiff, webp.
        """
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Папка '{folder_path}' не найдена.")
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"'{folder_path}' не является папкой.")

    # Допустимые расширения
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

        count = 0
        for file_name in os.listdir(folder_path):
        # Проверяем, что это файл, а не папка
            full_path = os.path.join(folder_path, file_name)
            if os.path.isfile(full_path):
            # Проверяем расширение файла
                _, ext = os.path.splitext(file_name)
                if ext.lower() in image_extensions:
                    count += 1
        return count + 1



    def load_frames(self, name_d, name_f):
        """
        Загружаем кадры анимации.
        Здесь предполагается, что у вас есть папка 'explosion'
        с изображениями explosion1.png, explosion2.png, ...

        """
        for i in range(1, self.count_images_in_folder(f"images/{name_d}")):  
            img_path = os.path.join(f"images/{name_d}", f"{name_f}{i}.png")
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