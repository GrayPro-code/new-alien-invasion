import pygame
import sys


# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Интерактивное меню")

# Загрузка фонового изображения
try:
    background = pygame.image.load("images/menu.jpg")  # замените на свой файл
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error:
    print("Ошибка: не удалось загрузить background.jpg")
    pygame.quit()
    sys.exit()

# Цвета
WHITE = (255, 255, 255)
GRAY = (84, 166, 190)
DARK_GRAY = (199, 243, 254)
BLACK = (245, 214, 157)
BORDER_COLOR = (245, 214, 157)

# Шрифт
font = pygame.font.SysFont("Arial", 36)

# Класс кнопки
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.color = GRAY
        self.hover_color = DARK_GRAY
        self.border_radius = 5  # закругление углов
        self.border_width = 2    # толщина рамки

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        # Рисуем рамку
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=self.border_radius)

        # Рисуем внутреннюю часть кнопки (с отступом для рамки)
        inner_rect = self.rect.inflate(-self.border_width*2, -self.border_width*2)
        pygame.draw.rect(surface, current_color, inner_rect, border_radius=self.border_radius - 2)

        # Текст на кнопке
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

# Функции для кнопок
def start_game():
    print("start game...")

def settings():
    print("Открытие настроек...")

def quit_game():
    pygame.quit()
    sys.exit()

# Создание кнопок
buttons = [
    Button("новая игра", WIDTH//2 - 100, 290, 200, 50, start_game),
    Button("Настройки", WIDTH//2 - 100, 360, 200, 50, settings),
    Button("Выход", WIDTH//2 - 100, 430, 200, 50, quit_game)
]

# Главный цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        for btn in buttons:
            btn.check_click(event)

    # Отрисовка
    screen.blit(background, (0, 0))
    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()
    clock.tick(60)
