import pygame as pg
from static2 import *
pg.init()

# ------------- ENEMIES SETTINGS ------------- #
red_enemies_count = 5
redLaser = RedLaser()
redEnemyList = [RedEnemy()
                for _ in range(red_enemies_count)]

green_enemies_count = 5
greenLaser = GreenLaser()
greenEnemyList = [GreenEnemy()
                  for _ in range(green_enemies_count)]


# ------------- GAME LOOP ------------- #
clock = pg.time.Clock()
run = True

while run:
    # FPS HANDLER
    clock.tick(FPS)

    # DISPLAY HANDLER---------------------------------------
    draw_whole_window(redEnemyList, greenEnemyList, player)

    # EVENT HANDLER-----------------------------------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            # MAX 3 BULLETS FOR A PLAYER
            if event.key == pg.K_SPACE and len(player.bulletList) < 3:
                player.shot(P_Bullet())
    player.bullets_move()
    player.bullet_hit(redEnemyList, greenEnemyList)

    # PLAYER MOVEMENT---------------------------------------
    key_pressed = pg.key.get_pressed()
    if key_pressed[pg.K_UP] and (player.rect.y > 0):
        player.rect.y -= player. speed
    if key_pressed[pg.K_DOWN] and (player.rect.y < HEIGHT - player.rect.height):
        player.rect.y += player.speed
    if key_pressed[pg.K_LEFT] and (player.rect.x > 0):
        player.rect.x -= player.speed
    if key_pressed[pg.K_RIGHT] and (player.rect.x < WIDTH - player.rect.width):
        player.rect.x += player.speed

    # GAME LOGIC---------------------------------------------
    for red_enemy in redEnemyList:
        red_enemy.move()
        red_enemy.bullets_move()

        red_enemy.start_countdown()
        if red_enemy.countdown == 1:
            red_enemy.shot(redLaser)

        if red_enemy.bullet_hit(player):
            update_player_hp_font()

        if red_enemy.hp <= 0:
            bg.score += 1
            update_score()
            red_enemy.die(redEnemyList)

    for green_enemy in greenEnemyList:
        green_enemy.move()
        green_enemy.bullets_move()

        green_enemy.start_countdown()
        if green_enemy.countdown == 1:
            green_enemy.shot(greenLaser)

        if green_enemy.bullet_hit(player):
            update_player_hp_font()

        if green_enemy.hp <= 0:
            bg.score += 1
            update_score()
            green_enemy.die(greenEnemyList)


pg.quit()
