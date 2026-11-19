
import asyncio
import pygame
import cfg

from game_functions import (
    load_best_score,
    save_best_score,
    ShowStartInterface,
    ShowEndInterface,
    create_game,
    createObstacles,
    AddObstacles,
    UpdateFrame
)


async def main():
    pygame.init()

    try:
        pygame.mixer.init()
        audio_enabled = True
    except pygame.error:
        audio_enabled = False

    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("Crash Course")

    clock = pygame.time.Clock()
    best_score = load_best_score()

    # Start screen
    ShowStartInterface(screen, cfg.SCREENSIZE)

    started = False

    while not started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                started = True

        await asyncio.sleep(0)

    car, obstacles0, obstacles1, obstacles = create_game()

    distance = score = money = 0
    paused = False
    crashed = False
    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif crashed:
                    if event.key == pygame.K_RETURN:
                        car, obstacles0, obstacles1, obstacles = create_game()
                        distance = score = money = 0
                        paused = crashed = False

                elif event.key == pygame.K_p:
                    paused = not paused

                    if audio_enabled:
                        if paused:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

                elif not paused:
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        car.turn(-1)

                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        car.turn(1)

        if not running:
            break

        if crashed:
            ShowEndInterface(screen, cfg.SCREENSIZE, score, best_score)
            await asyncio.sleep(0)
            continue

        if paused:
            UpdateFrame(
                screen, obstacles, car,
                score, best_score, paused=True
            )
            clock.tick(cfg.FPS)
            await asyncio.sleep(0)
            continue

        car.move()
        distance += car.speed[1]

        if distance >= 640 and money == 0:
            money = 1
            obstacles0 = createObstacles(20, 20)
            obstacles = AddObstacles(obstacles0, obstacles1)

        if distance >= 1280 and money == 1:
            money = 0
            distance -= 1280

            for obstacle in obstacles0:
                obstacle.location[1] -= 1280

            obstacles1 = createObstacles(10, 15)
            obstacles = AddObstacles(obstacles0, obstacles1)

        for obstacle in obstacles:
            obstacle.move(distance)

        hit_obstacles = pygame.sprite.spritecollide(
            car, obstacles, False
        )

        if hit_obstacles:
            hit = hit_obstacles[0]

            if hit.attribute == "block" and not hit.passed:

                if audio_enabled:
                    pygame.mixer.music.stop()

                    try:
                        crash_sound = pygame.mixer.Sound(
                            cfg.CRASH_SOUND_PATH
                        )
                        crash_sound.set_volume(0.4)
                        crash_sound.play()
                    except pygame.error:
                        pass

                car.setFall()

                UpdateFrame(
                    screen, obstacles, car,
                    score, best_score
                )

                await asyncio.sleep(0.5)

                crashed = True

                continue

            elif hit.attribute == "money" and not hit.passed:

                if audio_enabled:
                    try:
                        money_sound = pygame.mixer.Sound(
                            cfg.MONEY_SOUND_PATH
                        )
                        money_sound.set_volume(0.4)
                        money_sound.play()
                    except pygame.error:
                        pass

                score += 10
                hit.passed = True
                obstacles.remove(hit)

            if score > best_score:
                best_score = score
                save_best_score(best_score)

        UpdateFrame(
            screen, obstacles, car,
            score, best_score
        )

        clock.tick(cfg.FPS)
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
