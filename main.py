import os
from re import S
import pygame

from Sprite.Boss import Boss
from Sprite.EnemyMissile import EnemyMissile
from Sprite.Player import Player
from Settings import Settings
pygame.init()
Settings = Settings()
FPS = 60
count = 0
pygame.display.set_caption("BulletHell")
screen = pygame.display.set_mode((Settings.Width, Settings.Height))
running = True
clock = pygame.time.Clock()

playerHpImage = pygame.image.load(os.path.join(".\Images", "PlayerHp.jpg")).convert()
playerHpImage_mini = pygame.transform.scale(playerHpImage, (25, 19))
playerHpImage_mini.set_colorkey((255,255,255))
pygame.display.set_icon(playerHpImage_mini)

allSprites = pygame.sprite.Group()
playerMissiles = pygame.sprite.Group()
enemyMissiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
boss = Boss()

allSprites.add(player)
allSprites.add(boss)
enemies.add(boss)


def draw_player_health(surface, hp, img, x, y):
    for i in range(hp):
        img_rect = img.get_rect()
        img_rect.x = x + 30*i
        img_rect.y = y
        surface.blit(img, img_rect)

def draw_boss_health(surf, hp, maxHp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/maxHp)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, (0,255,0), fill_rect)
    pygame.draw.rect(surf, (255,255,255), outline_rect, 2)

while running:
    count += 1
    clock.tick(FPS)
    # Get Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #   if event.key == pygame.K_SPACE:

    boss.shift_shooting_direction(1)
    
    if count % 4 == 0:
        missile = player.shoot()
        allSprites.add(missile)
        playerMissiles.add(missile)

        boss_missiles = boss.shoot()
        allSprites.add(boss_missiles)
        enemyMissiles.add(boss_missiles)

    # Update Info
    allSprites.update()
    hitsOnBoss = pygame.sprite.groupcollide(enemies, playerMissiles, False, True)
    boss.curHp -= len(hitsOnBoss)
    hitOnPlayer = pygame.sprite.spritecollide(player, enemyMissiles, True)
    print(player.Hp)
    player.Hp -= len(hitOnPlayer)
    print(player.Hp)

    #Render Graphics
    screen.fill((255,255,255))
    allSprites.draw(screen)
    draw_player_health(screen, player.Hp, playerHpImage_mini, Settings.Height - 100, 50)
    draw_boss_health(screen, boss.curHp, boss.maxHp, 5, 15)
    pygame.display.update()

    # See if game ends
    if boss.curHp == 0 or player.Hp == 0:
        running = False

