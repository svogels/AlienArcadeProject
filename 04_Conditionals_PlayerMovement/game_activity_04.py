import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade - Activity 4")

# Colours
BLACK = (0, 0, 0)
PLAYER_COLOR = (66, 135, 245)

# Player properties
player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10
player_speed = 5 # --- NEW

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- NEW: Conditional Logic for Movement ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed

    # Drawing
    screen.fill(BLACK)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.display.flip()

pygame.quit()
