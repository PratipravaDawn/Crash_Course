import pygame
import random
import cfg

class ObstacleClass(pygame.sprite.Sprite):

    def __init__(self, img_path, location, attribute):

        pygame.sprite.Sprite.__init__(self)

        self.img_path = img_path
        self.image = pygame.image.load(self.img_path).convert_alpha()

        # Make money 1.5x bigger
        if attribute == "money":

            width = int(self.image.get_width() * 1.5)
            height = int(self.image.get_height() * 1.5)

            self.image = pygame.transform.scale(
                self.image,
                (width, height)
            )

        self.location = location

        self.rect = self.image.get_rect()
        self.rect.center = self.location

        self.attribute = attribute
        self.passed = False

    def move(self, num):
        self.rect.centery = self.location[1] - num


def createObstacles(s, e, num=10):

    obstacles = pygame.sprite.Group()
    locations = []

    for i in range(num):

        row = random.randint(s, e)
        col = random.randint(0, 9)

        location = [
            col * 54 + 20,
            row * 64 + 20
        ]

        if location not in locations:

            locations.append(location)

            attribute = random.choice(
                list(cfg.FREE_PATH.keys())
            )

            img_path = cfg.FREE_PATH[attribute]

            obstacle = ObstacleClass(
                img_path,
                location,
                attribute
            )

            obstacles.add(obstacle)

    return obstacles

def AddObstacles(obstacle0, obstacle1):

    obstacles = pygame.sprite.Group()

    for obs in obstacle0:
        obstacles.add(obs)

    for obs in obstacle1:
        obstacles.add(obs)

    return obstacles