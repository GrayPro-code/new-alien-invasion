import sys
import pygame


class Sounds:
	""" Класс управления звуками."""

	def __init__(self):

		try:
			pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
		except pygame.error as e:
			print(f"Ошибка инициализации звука: {e}")
			sys.exit(1)

	def bg_sound(self):
		""" Воспроизводит фоновый звук игры."""
		try:
			pygame.mixer.music.load("sounds/bg_sound.mp3")
			pygame.mixer.music.set_volume(0.3)
			pygame.mixer.music.play(-1)
		except pygame.error as e:
			sys.exit(1)


	def bullet_sound(self):
		""" Воспроизводит звук выстрела корабля."""
		try:
			bull_sound = pygame.mixer.Sound("sounds/bullet_sound.wav")
			bull_sound.set_volume(0.4)
			bull_sound.play()
		except pygame.error as e:
			print(f"Не удалось загрузить звук: {e}")
			sys.exit(1)

	def alien_sound(self):
		""" Воспроизводит звук уничтожения пришельца."""
		try:
			ali_sound = pygame.mixer.Sound("sounds/alien_sound.wav")
			ali_sound.play()
		except pygame.error as e:
			print(f"Не удалось загрузить звук: {e}")
			sys.exit(1)

	def armageddon_sound(self):
		""" Воспроизводит звук взрыва armageddon."""
		try:
			ali_sound = pygame.mixer.Sound("sounds/armageddon_sound.wav")
			ali_sound.play()
		except pygame.error as e:
			print(f"Не удалось загрузить звук: {e}")
			sys.exit(1)


	def weapon_change(self):
		""" Воспроизводит звук смены оружия."""
		try:
			ali_sound = pygame.mixer.Sound("sounds/weapon_change.wav")
			ali_sound.play()
		except pygame.error as e:
			print(f"Не удалось загрузить звук: {e}")
			sys.exit(1)


	def freeze_sound(self):
		""" Воспроизводит звук замедления пришельцев."""
		try:
			ali_sound = pygame.mixer.Sound("sounds/freeze_sound.wav")
			ali_sound.play()
		except pygame.error as e:
			print(f"Не удалось загрузить звук: {e}")
			sys.exit(1)

