import pygame
import sys
import os


# Инициализация Pygame
# os.environ['SDL_VIDEO_WINDOW_POS'] = "100,50"
#pygame.init()
#
## Размер окна
#
#screen = pygame.display.set_mode((500, 700))
#pygame.display.set_caption("Alien Invasion ARMAGEDDON")
#
## Загрузка фонового изображения
#try:
#    background = pygame.image.load("images/menu.jpg")  # замените на свой файл
#    background = pygame.transform.scale(background, (500, 700))
#except pygame.error:
#    print("Ошибка: не удалось загрузить background.jpg")
#    pygame.quit()
#    sys.exit()
#
## Цвета
#WHITE = (255, 255, 255)
#GRAY = (84, 166, 190)
#DARK_GRAY = (199, 243, 254)
#BLACK = (245, 214, 157)
#BORDER_COLOR = (245, 214, 157)
#
## Шрифт
#font = pygame.font.SysFont("Arial", 36)

# Класс Menu
class Menu:
    def __init__(self, text, x, y, width, height, callback):
        self.font = pygame.font.SysFont("Arial", 36)
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.color = (106, 142, 154)#(84, 166, 190)
        self.hover_color = (46, 64, 79)#(199, 243, 254)
        self.border_radius = 7  # закругление углов
        self.border_width = 1    # толщина рамки

    #def run_menu(self):



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

# Функции для кнопок
#   def start_game(self):
#       ai = AlienInvasion()
#       ai.run_game()

#   def menu_settings(self):
#       print("Открытие настроек...")

#   def quit_game(self):
#       pygame.quit()
#       sys.exit()

# Создание кнопок
#buttons = [
#    Menu("новая игра", 500//2 - 100, 290, 200, 50, Menu.start_game),
#    Menu("Настройки", 500//2 - 100, 360, 200, 50, Menu.menu_settings),
#    Menu("Выход", 500//2 - 100, 430, 200, 50, Menu.quit_game)
#]

# Главный цикл
#clock = pygame.time.Clock()
#while True:
#    for event in pygame.event.get():
#   #     if event.type == pygame.QUIT:
#            Menu.quit_game()
#        for btn in buttons:
#            btn.check_click(event)
#
#    # Отрисовка
#    screen.blit(background, (0, 0))
#    for btn in buttons:
#        btn.draw(screen)
#
#    pygame.display.flip()
#    clock.tick(60)
