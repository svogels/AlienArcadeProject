import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade - Activity 2")

# --- NEW: Define Variables ---
# Colours (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_COLOR = (66, 135, 245) # A nice blue

# Player properties
player_width = 50
player_height = 50
# Start the player in the bottom-middle of the screen
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10 # 10 pixels from the bottom

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- NEW: Drawing ---
    # 1. Fill the background
    screen.fill(BLACK)

    # 2. Draw the player rectangle
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    # 3. Update the display to show new drawings
    pygame.display.flip()

pygame.quit()
