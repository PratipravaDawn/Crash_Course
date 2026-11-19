import pygame
import cfg

class Carclass(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.direction = 0

        # Car images except the falling/crashed image
        self.imgpath = list(cfg.CAR_IMAGE_PATHS.values())[:-1]

        self.img = pygame.image.load(self.imgpath[self.direction]).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.center = [320, 100]

        self.speed = [self.direction, 6 - abs(self.direction) * 2]

    def turn(self, num):

        self.direction += num

        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)

        center = self.rect.center

        self.img = pygame.image.load(self.imgpath[self.direction]).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.center = center

        self.speed = [
            self.direction,
            6 - abs(self.direction) * 2
        ]

        return self.speed

    def move(self):

        self.rect.centerx += self.speed[0]

        # Keep car inside screen
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)

    def setFall(self):
        
        self.img = pygame.image.load(
            list(cfg.CAR_IMAGE_PATHS.values())[-1]
        ).convert_alpha()

    def setFwd(self):

        self.direction = 0
        self.img = pygame.image.load(
            self.imgpath[self.direction]
        ).convert_alpha()