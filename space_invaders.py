import pygame
import os
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# load sounds
BULLET_HIT_SOUND = pygame.mixer.Sound('space_invaders/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('space_invaders/Gun+Silencer.mp3')
#load fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
#decide frame rate/ velocity etc
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
# loading spaceship images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('space_invaders', 'yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('space_invaders', 'red.png'))
#transforming and scaling to match the window size
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('space_invaders', 'space.png')), (WIDTH, HEIGHT))
#create a border
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# intialize health
red_health=10
yellow_health=10