import pygame


class Weapon:

    def __init__(self, image, transparency, position):
        self.weapon_image = pygame.image.load(image).convert_alpha()
        self.weapon_image.set_alpha(transparency)
        self.weapon_rect = self.weapon_image.get_rect(center=position)


    @staticmethod
    def active(ai_game, parameters):
        ai_game.settings.bullet_height = parameters[0]
        ai_game.settings.bullet_color = parameters[1]
        ai_game.settings.bullets_allowed = parameters[2]










