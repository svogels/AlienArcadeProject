import pygame

# 1. Initialise Pygame
pygame.init()

# 2. Create the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade - Activity 1")

# 3. The Game Loop
running = True
while running:
    # 4. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 5. Quit Pygame
pygame.quit()
