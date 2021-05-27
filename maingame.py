import pygame
import random

from pygame.locals import *

pygame.init()

width = 600
height = 600

back = pygame.image.load("space.jpg")

screen = pygame.display.set_mode((width,height))

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

    def update(self):
        pygame.mouse.set_visible(False)

        x,y = pygame.mouse.get_pos()
        self.rect.centerx = x
        self.rect.centery = 500   

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10,500)
        self.vel = 2
    def update(self):
        self.rect.y += self.vel
        if self.rect.top > 600:

            self.rect.x = random.randrange(0,600)
            self.rect.y = random.randrange(0,100)
    def collide(self,pl_group):
        pygame.sprite.spritecollide(self,pl_group,True)

            

def render(pl, pl_group,rock,rock_group):
    screen.blit(back,(0,0))
    pl_group.draw(screen)
    pl.update()
    rock_group.draw(screen)
    rock.update()
    rock.collide(pl_group)
    pygame.display.update()

def main():
    pl = player()
    
    pl_group = pygame.sprite.Group()
    rock_group = pygame.sprite.Group()
    for i in range(1):
        rock = Rock()
        rock_group.add(rock)

    pl_group.add(pl)
    mainloop = True
    while mainloop :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
        render(pl,pl_group,rock,rock_group)        



if __name__ == "__main__":
    main()

