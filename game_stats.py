class GameStats:
	""" Отслеживание статистики в игре alien invasion"""

	def __init__(self, ai_game):
		# Инициализирует статистику.
		self.settings = ai_game.settings
		self.reset_stats()
		# Игра запускается в неактивном состоянии
		self.game_active = False
		# Рекорд не должен сбрасываться.
		self.high_score = self.read_high_score()

	def reset_stats(self):
		"""Инициализирует статистику изменяющуюся в ходе игры"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def write_high_score(self):
		""" Записывает в файл текущий рекордный счет"""
		with open("high_score.txt", "w") as f:
			f.write(str(self.high_score))

	@staticmethod
	def read_high_score():
		""" Загружает из файла рекорд игры"""
		with open("high_score.txt") as f:
			return int(f.read())