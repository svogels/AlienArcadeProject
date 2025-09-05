import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade - Activity 8")

# Colours
BLACK = (0, 0, 0)
PLAYER_COLOR = (66, 135, 245)
ALIEN_COLOR = (239, 68, 68)
BULLET_COLOR = (255, 255, 0)

# Player properties
player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10
player_speed = 5

# Alien properties
alien_width = 40
alien_height = 40
alien_x = 100
alien_y = 50
alien_speed = 3

# Bullet properties
bullet_width = 5
bullet_height = 10
bullet_speed = 10
bullets = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_SPACE:
                bullet_x = player_x + (player_width / 2) - (bullet_width / 2)
                bullet_y = player_y
                new_bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
                bullets.append(new_bullet)

    # Alien Movement
    alien_x += alien_speed
    if alien_x <= 0 or alien_x >= screen_width - alien_width:
        alien_speed *= -1

    # --- NEW: Bullet Movement ---
    # Move each bullet up the screen
    for bullet in bullets:
        bullet.y -= bullet_speed
    
    # Remove bullets that have gone off-screen
    # We loop through a copy of the list to safely remove items
    for bullet in bullets[:]:
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Drawing
    screen.fill(BLACK)
    
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    alien_rect = pygame.Rect(alien_x, alien_y, alien_width, alien_height)
    pygame.draw.rect(screen, ALIEN_COLOR, alien_rect)

    # Draw all bullets
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)

    pygame.display.flip()

pygame.quit()
