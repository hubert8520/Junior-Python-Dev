import pygame as pg
from static2 import *
pg.init()


def main_game():
    pg.init()
    # ------------- ENEMIES SETTINGS ------------- #
    red_enemies_count = 5
    redEnemyList = [RedEnemy()
                    for _ in range(red_enemies_count)]

    green_enemies_count = 5
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
                pg.quit()

            if event.type == pg.KEYDOWN:
                # MAX 3 BULLETS FOR A PLAYER
                if event.key == pg.K_SPACE and len(player.bulletList) < 3:
                    player.shot(P_Bullet())
        player.bullets_move()
        player.bullet_hit(redEnemyList, greenEnemyList)
        player.check_collision(redEnemyList, greenEnemyList)

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

            red_enemy.start_countdown()
            if red_enemy.countdown == 1:
                red_enemy.shot(RedLaser())
            red_enemy.bullets_move()
            red_enemy.bullet_hit(player)
            update_player_hp_font()

            if red_enemy.hp <= 0:
                bg.score += 1
                update_score()
                red_enemy.die(redEnemyList)

        for green_enemy in greenEnemyList:
            green_enemy.move()

            green_enemy.start_countdown()
            if green_enemy.countdown == 1:
                green_enemy.shot(GreenLaser())
            green_enemy.bullets_move()
            green_enemy.bullet_hit(player)
            update_player_hp_font()

            if green_enemy.hp <= 0:
                bg.score += 1
                update_score()
                green_enemy.die(greenEnemyList)

        if len(greenEnemyList) == 0 and len(redEnemyList) == 0:
            red_enemies_count += 2
            green_enemies_count += 2
            redEnemyList = [RedEnemy()
                            for _ in range(red_enemies_count)]
            greenEnemyList = [GreenEnemy()
                              for _ in range(green_enemies_count)]


def menu():
    singlePlayerButt = SinglePlayerButton("single_player")
    exitButt = ExitButton("exit")
    qr_code = pg.image.load('images/menu/QR.png').convert_alpha()
    steering = pg.image.load("images/menu/steering.png").convert_alpha()

    run = True
    while run:
        mouse_pos = pg.mouse.get_pos()

        window.blit(bg.img_scaled, (0, 0))
        menu_label = menu_font.render(
            "Space Shooter Project", True, (WHITE))
        window.blit(menu_label, (WIDTH/2 - menu_label.get_width()/2, 150))

        if not singlePlayerButt.hoovered_over(mouse_pos):
            window.blit(singlePlayerButt.img, (WIDTH // 2 -
                        singlePlayerButt.img.get_width() // 2, 300))
        else:
            window.blit(singlePlayerButt.img2,
                        (WIDTH // 2 - singlePlayerButt.img2.get_width() // 2, 300))

        if not exitButt.hoovered_over(mouse_pos):
            window.blit(exitButt.img, (WIDTH // 2 -
                        exitButt.img.get_width() // 2, 400))
        else:
            window.blit(exitButt.img2,
                        (WIDTH // 2 - exitButt.img2.get_width() // 2, 400))

        window.blit(qr_code, (200, 300))
        window.blit(steering, (WIDTH // 2 + 150, 300))

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if singlePlayerButt.clicked(mouse_pos, event):
                run = False
            if exitButt.clicked(mouse_pos, event):
                pg.quit()

    main_game()


menu()
