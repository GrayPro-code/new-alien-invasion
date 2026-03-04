import pygame


class Weapon:
    """
    Класс отрисовывает значки оружия в заданных координатах и меняет прозрачность
    значков и параметры снарядов в зависимости от выбора оружия
    """
    def __init__(self, image, transparency, position):
        """ Загружаем изображение, устанавливаем его прозрачность и расположение"""
        self.image = pygame.image.load(image).convert_alpha()
        self.image.set_alpha(transparency)
        self.rect = self.image.get_rect(center=position)











