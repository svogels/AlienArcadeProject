import pygame
import random

# Initialize mixer and pygame
pygame.mixer.init()
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load Sounds (with error handling)
try:
    shoot_sound = pygame.mixer.Sound('laser.wav')
    explosion_sound = pygame.mixer.Sound('explosion.wav')
except pygame.error:
    print("Warning: Sound files 'laser.wav' or 'explosion.wav' not found. Game will have no sound.")
    class DummySound:
        def play(self): pass
    shoot_sound = DummySound()
    explosion_sound = DummySound()

# Player
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10
player_speed = 5
player_x_change = 0

# Alien
alien_width = 50
alien_height = 50
alien_x = 0
alien_y = 50
alien_speed = 3
alien_rect = pygame.Rect(alien_x, alien_y, alien_width, alien_height)

# Bullet
bullet_width = 5
bullet_height = 15
bullet_speed = 10
bullets = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            elif event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            elif event.key == pygame.K_SPACE:
                bullet_x = player_x + (player_width / 2) - (bullet_width / 2)
                bullet_y = player_y
                bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
                bullets.append(bullet)
                shoot_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update positions
    player_x += player_x_change
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    alien_x += alien_speed
    if alien_x > screen_width - alien_width or alien_x < 0:
        alien_speed = -alien_speed
    
    alien_rect.x = alien_x
    alien_rect.y = alien_y

    # Move bullets and check for collision
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
        elif bullet.colliderect(alien_rect):
            explosion_sound.play()
            bullets.remove(bullet)
            alien_x = random.randint(0, screen_width - alien_width)
            alien_y = 50

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, GREEN, alien_rect)
    
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    
    pygame.display.update()

pygame.quit()
