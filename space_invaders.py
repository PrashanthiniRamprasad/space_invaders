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

class Spaceschip(pygame.sprite.Sprite):
    def __init__(self,image,angle, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), angle)
        self.rect = self.image.get_rect()
    def move_horizontal(self, VEL):
        self.x += VEL
        if player==1:
            if self.rect.left<=0 or self.rect.right>=BORDER.left:
                self.rect.move_ip(-VEL,0)
        if player==2:
            if self.rect.left<=BORDER.right or self.rect.right>=WIDTH:
                self.rect.move_ip(-VEL,0)
    def move_vertical(self, VEL):
        self.rect.move_ip(0,VEL)
        if self.rect.top<=0 or self.rect.bottom>=HEIGHT:
            self.rect.move_ip(0,-VEL)
red = Spaceschip(RED_SPACESHIP_IMAGE, 0, 100, 200)
yellow = Spaceschip(YELLOW_SPACESHIP_IMAGE, 180, 700, 200) 
sprites = pygame.sprite.Group()
sprites.add(red)
sprites.add(yellow)
def draw_window():
        WIN.blit(SPACE, (0, 0))
        pygame.draw.rect(WIN, "black", BORDER)
        red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, "white")
        yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, "white")
        WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        WIN.blit(yellow_health_text, (10, 10))
def draw_bullets():
        for bullet in red_bullets:
            pygame.draw.rect(WIN, "red", bullet)
            bullet.x -= BULLET_VEL
            
        for bullet in yellow_bullets:
            pygame.draw.rect(WIN, "yellow", bullet)
            bullet.x += BULLET_VEL
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

red_bullets = []
yellow_bullets = []

def handle_bullets():
     


    

