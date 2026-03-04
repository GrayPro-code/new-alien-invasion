import json
import pygame
import sys


class NameInputScreen:
    def __init__(self):
        pygame.init()
        self.Flag = True


        # Настройки окна
        self.WIDTH, self.HEIGHT = 500, 700
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("🫡🚀🛸 -= Введи свое имя пилот =- 🫡🚀🛸")

        # Шрифты
        self.FONT = pygame.font.Font(None, 48)
        self.FONT_BTN = pygame.font.Font(None, 40)

        # Цвета
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (46, 64, 79)
        self.GREEN = (106, 142, 154)

        # Поле ввода
        self.input_box = pygame.Rect(100, 300, 300, 50)
        self.color_inactive = self.BLUE
        self.color_active = self.WHITE
        self.color = self.color_inactive

        # Кнопка OK
        self.button_box = pygame.Rect(190, 400, 100, 40)

        # Состояния
        self.active = False
        self.text = "имя игрока"
        self.cursor_visible = True
        self.cursor_timer = 0
        self.cursor_interval = 500
        self.name_confirmed = False
        self.player_name = ""

        # Фон
        self.background = pygame.image.load("images/menu.jpg")
        self.clock = pygame.time.Clock()

    def handle_events(self):
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = True
                    self.color = self.color_active
                else:
                    self.active = False
                    self.color = self.color_inactive

                if self.button_box.collidepoint(event.pos):
                    if self.text.strip():
                        self.player_name = self.text.strip()
                        self.name_confirmed = True
                        self.active = False
                        self.color = self.color_inactive

            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    if self.text.strip():
                        self.player_name = self.text.strip()
                        self.name_confirmed = True
                        self.active = False
                        self.color = self.color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isprintable():
                        self.text += event.unicode

    def update_cursor(self):
        """Мигание курсора"""
        self.cursor_timer += self.clock.get_time()
        if self.cursor_timer >= self.cursor_interval:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0

    def draw(self):
        """Отрисовка экрана"""
        self.screen.blit(self.background, (0, 0))

        if not self.name_confirmed:
            txt_surface = self.FONT.render(self.text, True, self.WHITE)
            width = max(300, txt_surface.get_width() + 10)
            self.input_box.w = width

            pygame.draw.rect(self.screen, self.color, self.input_box, 2)
            self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 10))

            if self.active and self.cursor_visible:
                cursor_x = self.input_box.x + 5 + txt_surface.get_width() + 2
                cursor_y = self.input_box.y + 10
                pygame.draw.line(self.screen, self.WHITE,
                                 (cursor_x, cursor_y),
                                 (cursor_x, cursor_y + self.FONT.get_height() - 10), 2)

            pygame.draw.rect(self.screen, self.GREEN, self.button_box)
            btn_text = self.FONT_BTN.render("OK", True, self.WHITE)
            self.screen.blit(btn_text, (
                self.button_box.x + (self.button_box.width - btn_text.get_width()) // 2,
                self.button_box.y + (self.button_box.height - btn_text.get_height()) // 2
            ))
        else:

            name = self.player_name
            # Запись в файл с отступами и сохранением кириллицы
            with open("name.json", "w", encoding="utf-8") as file:
                json.dump(name, file, ensure_ascii=False, indent=4)
            self.Flag = False

        pygame.display.flip()

    def run(self):
        """Главный цикл"""
        while self.Flag:
            self.handle_events()
            self.update_cursor()
            self.draw()
            self.clock.tick(60)

