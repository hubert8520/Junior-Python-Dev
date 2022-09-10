import pygame as pg
import random
pg.init()
pg.font.init()


# ------------- COLORS ------------- #
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

# ------------- SCREEN SETTINGS ------------- #
WIDTH = 1200
HEIGHT = 800
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Hubert Grzelka Space Shooter project')
FPS = 60


# ------------- FONTS ------------- #
menu_font = pg.font.SysFont('Comic Sans MS', 50)
main_font = pg.font.SysFont('Comic Sans MS', 30)
lost_font = pg.font.SysFont('Comic Sans MS', 50)


# ------------- CLASSES ------------- #
class Button:
    def __init__(self, button_name: str):
        self.img = pg.image.load(
            'images/menu/' + button_name + ".png").convert_alpha()
        self.img2 = None
        self.rect = self.img.get_rect()
        self.sound = pg.mixer.Sound('sounds/button_sound.wav')

    def hoovered_over(self, mouse_pos_varName):
        return self.rect.collidepoint(mouse_pos_varName)

    def clicked(self, mouse_pos_varName, event):
        if self.rect.collidepoint(mouse_pos_varName):
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    return True


class SinglePlayerButton(Button):
    def __init__(self, button_name: str):
        super().__init__(button_name)
        self.img2 = pg.image.load(
            'images/menu/' + button_name + "_2.png").convert_alpha()
        self.rect.x = WIDTH // 2 - self.img.get_width() // 2
        self.rect.y = 300


class ExitButton(SinglePlayerButton):
    def __init__(self, button_name: str):
        super().__init__(button_name)
        self.rect.y = 400


class Background():
    def __init__(self):
        self.img = pg.image.load('images/backgrounds/background_0.png')
        self.img_scaled = pg.transform.scale(self.img,
                                             (WIDTH, HEIGHT)).convert_alpha()
        self.x = 0
        self.y = 0
        self.score = 0

    def draw_bg(self, screen_var_name):
        screen_var_name.blit(self.img, (self.x, self.y))


class Eny_Laser:
    def __init__(self):
        self.img = None
        self.rect = None
        self.speed = 4
        self.dmg = 1

    def draw(self):
        window.blit(self.img, self.rect)

    def move(self):
        self.rect.y += self.speed


class RedLaser(Eny_Laser):
    def __init__(self):
        super().__init__()
        self.img = pg.image.load(
            'images/enemies/red_alien_bullet.png').convert_alpha()
        self.rect = self.img.get_rect()
        self.dmg = 2


class GreenLaser(Eny_Laser):
    def __init__(self):
        super().__init__()
        self.img = pg.image.load(
            'images/enemies/green_alien_bullet.png').convert_alpha()
        self.rect = self.img.get_rect()


class P_Bullet(Eny_Laser):
    def __init__(self):
        super().__init__()
        self.img = pg.image.load(
            'images/player/player_bullet.png').convert_alpha()
        self.rect = self.img.get_rect()
        self.speed = -10


class Player():
    def __init__(self):
        self.img = pg.image.load('images/player/player_ship.png')
        self.img_scaled = pg.transform.scale(self.img, (self.img.get_width() * 0.5,
                                                        self.img.get_height() * 0.5)).convert_alpha()
        self.rect = self.img_scaled.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2)

        self.bulletList = []
        self.speed = 6
        self.hp = 10

    def draw(self, screen_var_name):
        screen_var_name.blit(self.img_scaled, (self.rect.x, self.rect.y))
        for bullet in self.bulletList:
            bullet.draw()

    def shot(self, bulletObj):
        self.bulletList.append(bulletObj)
        bulletObj.rect.center = (self.rect.centerx,
                                 self.rect.y - bulletObj.rect.height // 2)

    def bullets_move(self):
        for bullet in self.bulletList:
            bullet.move()
            if bullet.rect.y <= 0:
                self.bulletList.remove(bullet)

    def bullet_hit(self, redEnemyList: list, greenEnemyList: list):
        for bullet in self.bulletList:
            for enemy in redEnemyList:
                try:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.hp -= bullet.dmg
                        self.bulletList.remove(bullet)
                except ValueError:
                    print("ValueError has been handled")
                    continue
            for enemy in greenEnemyList:
                try:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.hp -= bullet.dmg
                        self.bulletList.remove(bullet)
                except ValueError:
                    continue

    def check_collision(self, redEnemyList: list, greenEnemyList: list):
        for enemy in redEnemyList:
            if enemy.rect.colliderect(self.rect):
                redEnemyList.remove(enemy)
                self.hp -= 5
        for enemy in greenEnemyList:
            if enemy.rect.colliderect(self.rect):
                greenEnemyList.remove(enemy)
                self.hp -= 5


class RedEnemy(Player):
    def __init__(self):
        self.img = pg.image.load('images/enemies/red_alien.png')
        # magic numbers 0.3 and 0.37 are for scaling
        # thanks to them, enemies will be same size as player
        self.img_scaled = pg.transform.scale(self.img, (self.img.get_width() * 0.3,
                                                        self.img.get_height() * 0.37)).convert_alpha()
        self.img_width = self.img_scaled.get_width()
        self.img_height = self.img_scaled.get_height()

        self.rect = self.img_scaled.get_rect()
        self.rect.x = random.randint(1, WIDTH - self.img_width)
        self.rect.y = random.randint(0, 170)

        self.bulletList = []
        self.speed = random.randint(3, 5)
        self.countdown = 0
        self.hp = 3

    def start_countdown(self):
        self.countdown = random.randint(1, 60 * 2)

    def move(self):
        if self.rect.x > 0 and self.rect.x + self.rect.width < WIDTH:
            self.rect.x += self.speed
        if self.rect.x + self.img_width >= WIDTH or self.rect.x <= 0:
            self.speed = -self.speed
            self.rect.x += self.speed

    def die(self, enemyList: list):
        enemyList.remove(self)

    def shot(self, bulletObj):
        self.bulletList.append(bulletObj)
        bulletObj.rect.center = (
            self.rect.centerx, self.rect.y + self.rect.height)

    def bullets_move(self):
        for bullet in self.bulletList:
            bullet.move()
            if bullet.rect.y >= HEIGHT:
                self.bulletList.remove(bullet)

    def bullet_hit(self, player: object):
        for bullet in self.bulletList:
            if bullet.rect.colliderect(player.rect):
                self.bulletList.remove(bullet)
                player.hp -= bullet.dmg


class GreenEnemy(RedEnemy):
    def __init__(self):
        super().__init__()
        self.img = pg.image.load('images/enemies/green_alien.png')
        self.img_scaled = pg.transform.scale(self.img, (self.img.get_width() * 0.3,
                                                        self.img.get_height() * 0.37)).convert_alpha()
        self.img_width = self.img_scaled.get_width()
        self.img_height = self.img_scaled.get_height()

        self.rect = self.img_scaled.get_rect()
        self.rect.x = random.randint(1, WIDTH - self.img_width)
        self.rect.y = random.randint(270, 370)

        self.hp = 2


# ------------- BACKGROUND AND LVL SETTINGS ------------- #
bg = Background()
lvl = 1
player = Player()

player_hp_font = main_font.render(f'Your health: {player.hp}', True, WHITE)
player_score_font = main_font.render(
    f'Your score: {bg.score}', True, WHITE)
player_lost_font = lost_font.render(f'You lost!', True, WHITE)

# ------------- CREATED FUNCTIONS ------------- #


def draw_whole_window(redEnemyList: list, greenEnemyList: list, player: object):
    window.blit(bg.img_scaled, (bg.x, bg.y))
    window.blit(player_hp_font, (10, 10))
    window.blit(player_score_font,
                (WIDTH - player_score_font.get_rect().width - 10, 10))
    if player.hp > 0:
        for enemy in redEnemyList:
            enemy.draw(window)
        for enemy in greenEnemyList:
            enemy.draw(window)
        player.draw(window)
    else:
        redEnemyList.clear()
        greenEnemyList.clear()
        window.blit(player_lost_font,
                    (WIDTH // 2 - player_lost_font.get_rect().width // 2, HEIGHT // 2))
    pg.display.flip()


def update_score():
    global player_score_font
    global lvl
    player_score_font = main_font.render(
        f'Your score: {bg.score}', True, WHITE)


def update_player_hp_font():
    global player_hp_font
    player_hp_font = main_font.render(f'Your health: {player.hp}', True, WHITE)
