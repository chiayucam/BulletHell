import pygame
from Settings import Settings
from Sprite.PlayerMissle import PlayerMissle


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (500,500)
        self.settings = Settings()
        self.Hp = 3
        self.BombCount = 3

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] and self.rect.right <= self.settings.Width:
            self.rect.x += 5
        if key_pressed[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 5
        if key_pressed[pygame.K_DOWN] and self.rect.bottom <= self.settings.Height:
            self.rect.y += 5
        if key_pressed[pygame.K_UP] and self.rect.top >= 0:
            self.rect.y -= 5

    def shoot(self):
        missle = PlayerMissle(self.rect.centerx, self.rect.top)
        return missle