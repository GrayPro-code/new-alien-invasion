from pygame.sprite import Sprite


class Bullet(Sprite):
	"""Класс для управления снарядами выпущенными кораблем"""

	def __init__(self, ai_game, image):
		"""Создает объект снарядов в текущей позиции корабля"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		# Создание снаряда в позиции (0 0) и назначение правильной позиции
		self.image = image
		self.rect = self.image.get_rect()
		#self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		# Позиция снаряда храниться в вещественном формате
		self.y = self.rect.y

	def update(self, ai_game):
		"""Перемещает снаряд вверх по экрану"""
		# Обновление позиции снаряда в вещественном формате
		self.y -= self.settings.bullet_speed_factor * ai_game.dt
		# Обновление позиции прямоугольника
		self.rect.y = self.y

	def blitme(self):
		"""Рисует корабль в текущей позиции."""
		self.screen.blit(self.image, self.rect)
