import pygame
import os
pygame.font.init()
pygame.mixer.init

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2-player game")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

border = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

#bullet_hit_sound = pygame.mixer.Sound('Assets/Grenade+1.mp3)
#bullet_fire_sound = pygame.mixer.Sound('Assets/Gun+Silencer.mp3)

health_font = pygame.font.SysFont('comicsans',40)
winner_font = pygame.font.SysFont('comicsans'100)

FPS = 60
vel = 5
bullet_vel = 7
max_bullets = 3
spaceship_width, spaceship_height = 55,40

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

yellow_spaceship_image = pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(
    yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

def draw_window():
    



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
            pygame.quit()

