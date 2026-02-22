import json


class GameStats:
	""" Отслеживание статистики в игре alien invasion"""

	def __init__(self, ai_game):
		# Инициализирует статистику.
		self.settings = ai_game.settings
		self.reset_stats()
		# Игра запускается в неактивном состоянии
		self.game_active = False
		# Рекорд не должен сбрасываться.
		self.high_score = self.read_high_score()[1]
		self.name = self.read_high_score()[0]

	def reset_stats(self):
		"""Инициализирует статистику изменяющуюся в ходе игры"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1


	def write_high_score(self):
		high_score = {self.name: self.high_score}
		# Запись в файл с отступами и сохранением кириллицы
		with open("high_score.json", "w", encoding="utf-8") as file:
			json.dump(high_score, file, ensure_ascii=False, indent=4)


	@staticmethod
	def read_high_score():
		with open("high_score.json", "r", encoding="utf-8") as file:
			high_score = json.load(file)
			for key, value in high_score.items():
				data = key, value
		return data









