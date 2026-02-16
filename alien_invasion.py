import sys
from time import sleep
import pygame
from game_sounds import Sounds
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from animation import Animation
from random import randint


class AlienInvasion:
    """класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """инициализирует игру и создает игровые ресурсы """
        pygame.init()
        # self.clock = pygame.time.Clock()
        self.sounds = Sounds()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion Armageddon")
        # создание экземпляра для хранения игровой статистики и хранения результатов.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._create_fleet()
        # Создание кнопки Play
        self.play_button = Button(self, "Play")
        # Создание музыки на заднем фоне.
        self.sounds.bg_sound()
        self.switch = True



        # добавляю rocket
        self.rocket_image = pygame.image.load("images/rocket.png")
        self.rocket_rect = self.rocket_image.get_rect(center=(50, 650))
        # добавляем blaster
        self.blaster_image = pygame.image.load("images/blaster.png")
        self.blaster_rect = self.blaster_image.get_rect(center=(150, 650))



        

    def run_game(self):
        """запуск основного цикла игры."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


    def _check_events(self):
        # отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.write_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Сброс игровых настроек.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()
            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()
            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()
            # Указатель мыши скрывается.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """ Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.stats.write_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


        elif event.key == pygame.K_1:
            self.sounds.weapon_change()
            self.switch = True
            self.settings.bullet_height = 15
            self.settings.bullet_color = (255, 102, 0)
            self.settings.bullets_allowed = 3


        elif event.key == pygame.K_2:
            self.sounds.weapon_change()
            self.switch = False
            self.settings.bullet_height = 45
            self.settings.bullet_color = (0, 180, 232)
            self.settings.bullets_allowed = 1







    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу Bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sounds.bullet_sound()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        # Обновление позиции снарядов
        # проверка попаданий в пришельца
        # при обнаружении попаданий удалить снаряд и пришельца
        self.bullets.update()     
        # удаление снарядов вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)    
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """обработка коллизий снарядов с пришельцами"""
        # удаление снарядов и пришельцев участвующих в коллизиях
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, self.switch, True)
        if collisions:
            # Генерирует случайное число
            self.random_integer = randint(0, 100)

            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)


            # получаем координаты сбитых пришельцев
            for alien in aliens:
                self.explosion = Animation(alien.rect.x, alien.rect.y, name_dir="explosion", name_files="explosion")
                self.all_sprites.add(self.explosion)


            #if 5 == self.random_integer and self.settings.bullets_allowed != 3 and self.switch == True:
            #    self.boom = Animation(600, 350, name_dir="boom", name_files="boom")
            #    self.all_sprites.add(self.boom)
            #    self.sounds.triple_shot_sound()
            #    self.settings.bullets_allowed = 3

               

            if 3 == self.random_integer:
                self.freeze = Animation(600, 350, name_dir="freeze", name_files="freeze")
                self.all_sprites.add(self.freeze)
                self.sounds.freeze_sound()
                self.settings.alien_speed_factor /= self.settings.speedup_scale
                self.settings.ship_speed_factor  /= self.settings.speedup_scale
                self.settings.bullet_speed_factor /= self.settings.speedup_scale
                


                # ARMAGEDDON
            elif 2 == self.random_integer:
                self.armageddon = Animation(600, 250, name_dir="armageddon", name_files="armageddon")
                self.all_sprites.add(self.armageddon)
                self.sounds.armageddon_sound()
                self.stats.score += self.settings.alien_points * len(self.aliens)
                self.aliens.empty()
                

            self.sb.prep_score()
            self.sb.check_high_score()
            self.sounds.alien_sound()
        if not self.aliens:
            # уничтожение существующих снарядов повышение скорости и создание нового флота.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Увеличение уровня.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.aliens.update()
        # проверка коллизий пришелец - корабль
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # проверить добрались ли пришельцы до нижнего края экрана
        self._check_aliens_bottom()

    def _ship_hit(self):
        """обрабатывает столкновения корабля с пришельцем"""
        # уменьшение ships left
        if self.stats.ships_left > 0:
            # Уменьшение ships_left и обновление панели счета.
            self.stats.ships_left -= 1
            self.sb.prep_ship()
            # очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()
            # создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()
            # пауза
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит тоже что и при столкновении с кораблем
                self._ship_hit()
                break

    def _create_fleet(self):
        """Создает флот пришельцев"""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов помещающихся на экране"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 1.5 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 1.25 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран."""
        self.screen.blit(self.settings.bg_image, (0, 0))
        self.screen.blit(self.rocket_image, self.rocket_rect)
        self.screen.blit(self.blaster_image, self.blaster_rect)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        #Вывод информации о счете.
        self.sb.show_score()
        # Кнопка Play Отображается в том случае если игра не активна.
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
        
        # self.clock.tick(3000)
        


if __name__ == "__main__":
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
