import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade - Activity 7")

# Colours
BLACK = (0, 0, 0)
PLAYER_COLOR = (66, 135, 245)
ALIEN_COLOR = (239, 68, 68)
BULLET_COLOR = (255, 255, 0) # --- NEW

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

# --- NEW: Bullet properties ---
bullet_width = 5
bullet_height = 10
bullet_speed = 10
bullets = [] # An empty list to hold all bullet Rects

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
            # --- NEW: Fire a bullet ---
            elif event.key == pygame.K_SPACE:
                # Create a new bullet rectangle at the player's current position
                bullet_x = player_x + (player_width / 2) - (bullet_width / 2) # Center it
                bullet_y = player_y
                new_bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
                # Add the new bullet to our list
                bullets.append(new_bullet)

    # Alien Movement Logic
    alien_x += alien_speed
    if alien_x <= 0 or alien_x >= screen_width - alien_width:
        alien_speed *= -1

    # Drawing
    screen.fill(BLACK)
    
    # Draw Player
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    # Draw Alien
    alien_rect = pygame.Rect(alien_x, alien_y, alien_width, alien_height)
    pygame.draw.rect(screen, ALIEN_COLOR, alien_rect)

    # --- NEW: Draw all bullets in the list ---
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)

    pygame.display.flip()

pygame.quit()
