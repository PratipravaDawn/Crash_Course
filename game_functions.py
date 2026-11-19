import os
import pygame
import cfg
import sys
import os
from car import Carclass
from obstacle import createObstacles, AddObstacles


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BEST_SCORE_FILE = os.path.join(BASE_DIR, "best_score.txt")


def load_best_score():
    return 0  # Placeholder for best score loading logic
    # try:
    #     with open(BEST_SCORE_FILE, "r", encoding="utf-8") as file:
    #         return int(file.read().strip())
    # except (FileNotFoundError, ValueError):
    #     return 0


def save_best_score(score):
    pass  # Placeholder for best score saving logic
    # try:
    #     with open(BEST_SCORE_FILE, "w", encoding="utf-8") as file:
    #         file.write(str(score))
    # except OSError as e:
    #     print(f"Could not save high score: {e}")


def ShowStartInterface(screen, screensize):
    bg = pygame.image.load(cfg.START_SCREEN_PATH)
    bg = pygame.transform.scale(bg, screensize)

    screen.blit(bg, (0, 0))
    pygame.display.update()


def ShowEndInterface(screen, screensize, score, best_score):

    screen.fill((173, 216, 230))

    tfont = pygame.font.Font(cfg.FONT_PATH, screensize[0] // 6)
    cfont = pygame.font.Font(cfg.FONT_PATH, screensize[0] // 20)

    title = tfont.render("CRASHED!", True, (255, 255, 255))
    score_text = cfont.render(f"Score: {score}", True, (255, 0, 0))
    best_text = cfont.render(f"Best: {best_score}", True, (0, 0, 255))

    prompt = cfont.render("Press ENTER to restart", True, (255, 255, 255))
    quit_text = cfont.render("Press ESC to quit", True, (255, 255, 255))

    center_x = screensize[0] // 2
    center_y = screensize[1] // 2

    texts = [
        (title, (center_x, screensize[1] // 5)),
        (score_text, (center_x, center_y)),
        (best_text, (center_x, center_y + 40)),
        (prompt, (center_x, center_y + 100)),
        (quit_text, (center_x, center_y + 140))
    ]

    for text, pos in texts:
        rect = text.get_rect(center=pos)
        screen.blit(text, rect)

    pygame.display.update()


def ShowScore(screen, score, best_score):
    font = pygame.font.Font(cfg.FONT_PATH, 20)

    pause_text = font.render("Press P to Pause", True, (0, 0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    best_text = font.render(f"Best: {best_score}", True, (0, 0, 0))

    screen.blit(score_text, (10, 10))
    screen.blit(best_text, (10, 35))
    screen.blit(pause_text, (cfg.SCREENSIZE[0] - pause_text.get_width() - 10, 10))



def ShowPause(screen, screensize):
    
    font = pygame.font.Font(cfg.FONT_PATH, screensize[0] // 12)
    text = font.render("PAUSED", True, (255, 255, 255))
    rect = text.get_rect()
    rect.center = (screensize[0] // 2, screensize[1] // 2)
    screen.blit(text, rect)
    pygame.display.update()



def UpdateFrame(screen, obstacles, car, score, best_score, paused=False):
    screen.fill((128, 128, 128))
    obstacles.draw(screen)
    screen.blit(car.img, car.rect)
    ShowScore(screen, score, best_score)
    
    if paused:
        ShowPause(screen, cfg.SCREENSIZE)
    else:
        pygame.display.update()


def create_game():
    car = Carclass()

    obstacles0 = createObstacles(20, 29)
    obstacles1 = createObstacles(10, 19)
    obstacles = AddObstacles(obstacles0, obstacles1)

    try:
        pygame.mixer.music.load(cfg.MUSIC_PATH)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass

    return car, obstacles0, obstacles1, obstacles
