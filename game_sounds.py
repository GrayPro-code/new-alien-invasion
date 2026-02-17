import sys
import pygame


class Sounds:
    """ Класс управления звуками."""

    @staticmethod
    def sounds_init():
        """Инициализирует настройки звука"""
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        except pygame.error as e:
            print(f"Ошибка инициализации звука: {e}")
            sys.exit(1)


    @staticmethod
    def play_music(file_path="", volume=1.0, loops=0):
        """
        Воспроизводит музыку.
        file_path: = path to file with sounds
		volume: set volume of sounds from 0.0 to 1.0
		loops: set -1 = replay Ꝏ
        """
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loops)
        except pygame.error as e:
            print(f"Ошибка инициализации звука: {e}")
            sys.exit(1)


    @staticmethod
    def play_sound(file_path="", volume=1.0, loops=0):
        """
        Воспроизводит звук.
        file_path: = path to file with sounds
		volume: set volume of sounds from 0.0 to 1.0
		loops: set -1 = replay Ꝏ
        """
        try:
            sound = pygame.mixer.Sound(file_path)
            sound.set_volume(volume)
            sound.play(loops)
        except pygame.error as e:
            print(f"Не удалось загрузить звук: {e}")
            sys.exit(1)

