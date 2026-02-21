import pygame


class Weapon:
    """
    Класс отрисовывает значки оружия в заданных координатах и меняет прозрачность
    значков и параметры снарядов в зависимости от выбора оружия
    """
    def __init__(self, image, transparency, position):
        """ Загружаем изображение, устанавливаем его прозрачность и расположение"""
        self.weapon_image = pygame.image.load(image).convert_alpha()
        self.weapon_image.set_alpha(transparency)
        self.weapon_rect = self.weapon_image.get_rect(center=position)


    @staticmethod
    def change_bullet(ai_game, parameters):
        """ меняет параметры снаряда"""
        ai_game.settings.bullet_height = parameters[0]
        ai_game.settings.bullet_color = parameters[1]
        ai_game.settings.bullets_allowed = parameters[2]










