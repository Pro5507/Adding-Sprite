import pygame
import random

from pygame.sprite import _Group

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT +1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

GREEN= pygame.Color('green')
RED= pygame.Color('red')

LIGHTBLUE = pygame.Color('lightblue')
PINK= pygame.Color('pink')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, hight, width):
        super().__init__()
        self.image= pygame.Surface([width, hight])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity= [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit= False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit= True

            self.rect.move_ip(self.velocity)
        boundary_hit= False
        if self.rect.left <= 0 or self.rect.right >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit= True

            if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))

                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([GREEN, RED]))

    def change_background_color():
        global bg_color
        bg_color = random.choice([LIGHTBLUE, PINK])

    all_sprite_list = pygame.sprite.Group()
    sp1= Sprite(GREEN, 20, 30)
    sp1.rect.x= random.randint(0, 480)
    sp1.rect.y= random.randint(0, 370)
    