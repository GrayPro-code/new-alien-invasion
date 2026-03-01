import os
import sys
import pygame
from text_fade_in import TextFadeIn
from name_input_screen import NameInputScreen
from alien_invasion import AlienInvasion
from settings import Settings
from weapon import Weapon as DrawImage


class MainMenu:
    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "450,50"
        pygame.init()
        self.settings = Settings()


        self.clock = pygame.time.Clock()
        self.screen_width = 500
        self.screen_height = 700

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("🫡🚀🛸-= ALIEN INVASION ARMAGEDDON =-🫡🚀🛸")

        self.background = pygame.image.load("images/menu.jpg")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))

        # Шрифт текста названия игры
        font_text = pygame.font.Font(None, 72)

        # Тексты с плавным появлением
        self.fade_text = TextFadeIn("ALIEN INVASION", font_text, (255, 255, 255), (50, 510), speed=1)
        self.fade_text_2 = TextFadeIn("ARMAGEDDON", font_text, (255, 255, 255), (70, 580), speed=0.3)

        # Кнопки
        self.buttons = [
            ButtonMenu("новая игра", self.screen_width // 2 - 100, 290, 200, 50, start_game),
            ButtonMenu("настройки", self.screen_width // 2 - 100, 360, 200, 50, menu_settings),
            ButtonMenu("выход", self.screen_width // 2 - 100, 430, 200, 50, quit_game)
            ]



    # --------- Основной цикл меню ---------

    def run(self):
        while True:
            # Обновляем состояние текста
            self.fade_text.update()
            self.fade_text_2.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    btn.check_click(event)

            # Отрисовка
            self.screen.blit(self.background, (0, 0))
            self.fade_text.draw(self.screen)
            self.fade_text_2.draw(self.screen)

            for btn in self.buttons:
                btn.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


    def open_menu_settings(self):
        while True:
            # Обновляем состояние текста


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                btn = ButtonMenu("назад", self.screen_width // 2 - 100, 600, 200, 50, menu.run)
                btn.check_click(event)

            # Отрисовка
            self.screen.blit(self.background, (0, 0))
            # добавляю rocket
            rocket = DrawImage(self.settings.rocket_image, self.settings.default_transparency,
                                 self.settings.rocket_position)
            # добавляем blaster
            blaster = DrawImage(self.settings.blaster_image, self.settings.weapon_transparency,
                                  self.settings.blaster_position)

            self.screen.blit(rocket.image, rocket.rect)
            self.screen.blit(blaster.image, blaster.rect)
            ButtonMenu("назад", self.screen_width // 2 - 100, 600, 200, 50, menu.run).draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


class ButtonMenu:
    def __init__(self, text, x, y, width, height, callback):
        self.font = pygame.font.SysFont("Arial", 36)
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.color = (106, 142, 154)#(84, 166, 190)
        self.hover_color = (46, 64, 79)#(199, 243, 254)
        self.border_radius = 7  # закругление углов
        self.border_width = 1    # толщина рамки


    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        # Рисуем рамку
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=self.border_radius)#245, 214, 157

        # Рисуем внутреннюю часть кнопки (с отступом для рамки)
        inner_rect = self.rect.inflate(-self.border_width*2, -self.border_width*2)
        pygame.draw.rect(surface, current_color, inner_rect, border_radius=self.border_radius - 2)

        # Текст на кнопке
        text_surf = self.font.render(self.text, True, (255, 255, 255))#245, 214, 157
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()


  # --------- Методы-действия для кнопок ---------
def start_game():
    pygame.quit()
    NameInputScreen().run()
    pygame.quit()
    AlienInvasion().run_game()

def menu_settings():
    menu.open_menu_settings()

def quit_game():
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()