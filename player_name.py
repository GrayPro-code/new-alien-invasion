

import pygame
import sys

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🫡🚀🛸🫡🚀🛸🫡🚀🛸-= Введи свое имя пилот =-🫡🚀🛸🫡🚀🛸🫡🚀🛸")

# Шрифт
FONT = pygame.font.Font(None, 48)
FONT_BTN = pygame.font.Font(None, 40)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (255, 255, 255)
BLUE = (46, 64, 79)
GREEN = (106, 142, 154)

# Поле ввода
input_box = pygame.Rect(100, 300, 300, 50)
color_inactive = BLUE
color_active = WHITE
color = color_inactive

# Кнопка OK
button_box = pygame.Rect(190, 400, 100, 50)

active = False
text = "имя игрока"
cursor_visible = True
cursor_timer = 0
cursor_interval = 500  # мигание курсора каждые 500 мс
name_confirmed = False
player_name = ""
background = pygame.image.load("images/menu.jpg")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Клик по полю — активируем ввод
            if input_box.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_inactive

            # Клик по кнопке OK
            if button_box.collidepoint(event.pos):
                if text.strip():
                    player_name = text.strip()
                    name_confirmed = True
                    active = False
                    color = color_inactive

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:
                if text.strip():
                    player_name = text.strip()
                    name_confirmed = True
                    active = False
                    color = color_inactive
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                if event.unicode.isprintable():
                    text += event.unicode

    # Мигание курсора
    cursor_timer += clock.get_time()
    if cursor_timer >= cursor_interval:
        cursor_visible = not cursor_visible
        cursor_timer = 0

    # Отрисовка
    screen.blit(background, (0, 0))

    if not name_confirmed:
        # Рендер текста в поле
        txt_surface = FONT.render(text, True, WHITE)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width

        # Поле ввода
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))

        # Курсор
        if active and cursor_visible:
            cursor_x = input_box.x + 5 + txt_surface.get_width() + 2
            cursor_y = input_box.y + 10
            pygame.draw.line(screen, WHITE, (cursor_x, cursor_y),
                             (cursor_x, cursor_y + FONT.get_height() - 10), 2)

        # Кнопка OK
        pygame.draw.rect(screen, GREEN, button_box)
        btn_text = FONT_BTN.render("OK", True, WHITE)
        screen.blit(btn_text, (button_box.x + (button_box.width - btn_text.get_width()) // 2,
                               button_box.y + (button_box.height - btn_text.get_height()) // 2))
    else:
        # Приветствие
        greet_surface = FONT.render(f"Привет, {player_name}!", True, WHITE)
        screen.blit(greet_surface, (WIDTH // 2 - greet_surface.get_width() // 2,
                                    HEIGHT // 2 - greet_surface.get_height() // 2))



    pygame.display.flip()
    clock.tick(60)





#import pygame
#import sys
#
## Инициализация Pygame
#pygame.init()
#
## Настройки окна
#WIDTH, HEIGHT = 600, 200
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Ввод имени игрока")
#
## Шрифт
#FONT = pygame.font.Font(None, 48)
#
## Цвета
#WHITE = (255, 255, 255)
#BLACK = (0, 0, 0)
#
## Переменная для хранения имени
#player_name = ""
#input_active = True  # Пока True — ждём ввода
#
#clock = pygame.time.Clock()
#
#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            sys.exit()
#
#        if input_active and event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_RETURN:  # Enter — завершить ввод
#                input_active = False
#                print(f"Имя игрока: {player_name}")  # Можно сохранить или использовать
#            elif event.key == pygame.K_BACKSPACE:  # Удалить символ
#                player_name = player_name[:-1]
#            else:
#                # Добавляем только печатные символы
#                if event.unicode.isprintable():
#                    player_name += event.unicode
#
#    # Отрисовка
#    screen.fill(WHITE)
#
#    if input_active:
#        text_surface = FONT.render(f"Введите имя: {player_name}", True, BLACK)
#    else:
#        text_surface = FONT.render(f"Привет, {player_name}!", True, BLACK)
#
#    screen.blit(text_surface, (50, HEIGHT // 2 - 20))
#    pygame.display.flip()
#    clock.tick(30)
#