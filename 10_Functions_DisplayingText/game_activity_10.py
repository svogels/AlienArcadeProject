import pygame
import random

# -- Setup --
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade - Activity 10")

# -- Colours and Fonts --
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_COLOR = (66, 135, 245)
ALIEN_COLOR = (239, 68, 68)
BULLET_COLOR = (255, 255, 0)
font = pygame.font.Font(None, 36) # --- NEW

# -- Game State Variables --
score = 0
player_x = (screen_width - 50) / 2
player_y = screen_height - 50 - 10
alien_x = 100
alien_y = 50
alien_speed = 3
bullets = []

# -- Constants --
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ALIEN_WIDTH, ALIEN_HEIGHT = 40, 40
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
PLAYER_SPEED = 5
BULLET_SPEED = 10

# --- NEW: Functions ---
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def draw_elements(player_rect, alien_rect, bullets):
    screen.fill(BLACK)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.draw.rect(screen, ALIEN_COLOR, alien_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)
    draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)
    pygame.display.flip()

# -- Main Game Loop --
running = True
while running:
    # -- Event Handling --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + (PLAYER_WIDTH / 2) - (BULLET_WIDTH / 2)
                bullet_y = player_y
                new_bullet = pygame.Rect(bullet_x, bullet_y, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(new_bullet)

    # -- Player Movement --
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < screen_width - PLAYER_WIDTH:
        player_x += PLAYER_SPEED

    # -- Game Logic --
    alien_x += alien_speed
    if alien_x <= 0 or alien_x >= screen_width - ALIEN_WIDTH:
        alien_speed *= -1

    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    alien_rect = pygame.Rect(alien_x, alien_y, ALIEN_WIDTH, ALIEN_HEIGHT)

    # This is a global variable, we need to tell the function we are modifying it
    # In a better structure, we would pass score in and return the new score
    # For now, this is the simplest way to show functions
    
    temp_score = score
    for bullet in bullets[:]:
        bullet.y -= BULLET_SPEED
        if bullet.colliderect(alien_rect):
            temp_score += 10
            bullets.remove(bullet)
            alien_x = random.randint(0, screen_width - ALIEN_WIDTH)
        elif bullet.bottom < 0:
            bullets.remove(bullet)
    score = temp_score

    # -- Drawing --
    draw_elements(player_rect, alien_rect, bullets)

pygame.quit()
