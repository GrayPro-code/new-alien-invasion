import pygame

class Settings:
	"""Класс для хранения всех настроек игры Alien Invasion."""

	def __init__(self):
		"""Инициализирует статические  настройки игры."""

		# Параметры экрана
		self.screen_width = 1200
		self.screen_height = 700

		# Назначение цвета фона.
		self.bg_image = pygame.image.load("images/bg.jpg")

		# Цвет фона счета.
		self.bg_color = (112, 146, 190, 40)    #(135, 206, 250)

		# Настройки корабля
		self.ship_speed = 0.7
		self.ship_limit = 3

		# Настройки пришельцев
		self.alien_speed = 0.1
		self.fleet_drop_speed = 50
		# Темп ускорения игры.
		self.speedup_scale = 1.2
		# Темп роста стоимости пришельца
		self.score_scale= 1.3
		self.initialize_dynamic_settings()

		# параметры снаряда
		self.bullet_speed = 0.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 102, 0) # (0, 0, 255) 
		self.bullets_allowed = 1

	def initialize_dynamic_settings(self):
		"""Инициализирует настройки изменяющиеся в ходе игры"""
		self.ship_speed_factor = 0.7
		self.bullet_speed_factor = 0.5
		self.alien_speed_factor = 0.1
		# fleet_direction = 1 обозначает движение вправо; а - 1 - влево
		self.fleet_direction = 1
		# Подсчет очков.
		self.alien_points = 16

	def increase_speed(self):
		""" Увеличивает настройки скорости."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)






