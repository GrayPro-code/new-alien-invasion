import pygame

class Settings:
	"""Класс для хранения всех настроек игры Alien Invasion."""

	def __init__(self):
		"""Инициализирует статические настройки игры."""

		# Параметры экрана
		pygame.init()
		self.screen_width = 1200
		self.screen_height = 700

		# Назначение цвета фона.
		self.bg_image = pygame.image.load("images/bg.jpg")

		# параметры снарядов
		self.bullet_speed = 0.5
		self.bullet_width = 3
		self.bullet_blaster_height = 45
		self.bullet_height = 15
		self.bullet_color = (255, 102, 0)
		self.bullet_blaster_color = (0, 180, 232)
		self.bullets_allowed = 3
		self.bullet_blaster_allowed = 1


		# Загрузка картинок меню оружия

		self.rocket_image = "images/rocket.png"
		self.blaster_image = "images/blaster.png"
		self.default_transparency = 255
		self.weapon_transparency = 100

		self.rocket_position = (50, 650)
		self.blaster_position = (150, 650)

		self.rocket_parameters = [self.bullet_height, self.bullet_color, self.bullets_allowed]
		self.blaster_parameters = [self.bullet_blaster_height, self.bullet_blaster_color, self.bullet_blaster_allowed]

		# Цвет фона счета.
		self.bg_color = (112, 146, 190, 40)    #(135, 206, 250)

		# Настройки корабля
		self.ship_speed = 0.7
		self.ship_limit = 3

		# Настройки пришельцев
		self.alien_speed = 0.1
		self.fleet_drop_speed = 50
		# Темп ускорения игры.
		self.speedup_scale = 1.1
		# Темп роста стоимости пришельца
		self.score_scale= 1.3
		self.initialize_dynamic_settings()



		# Расположение звуков игры
		self.bg_music = "sounds/bg_sound.mp3"
		self.bullet_sound = "sounds/bullet_sound.wav"
		self.alien_sound = "sounds/alien_sound.wav"
		self.freeze_sound = "sounds/freeze_sound.wav"
		self.armageddon_sound = "sounds/armageddon_sound.wav"
		self.weapon_change_sound = "sounds/weapon_change.wav"

		# Громкость звуков игры
		self.bg_volume = 0.3
		self.bullet_volume = 0.4
		self.alien_volume = 0.6
		self.freeze_volume = 0.9
		self.armageddon_volume = 0.9
		self.weapon_volume = 0.8

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






