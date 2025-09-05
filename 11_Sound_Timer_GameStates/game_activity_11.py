import pygame
import random

# (Assume you have 'laser.wav' and 'explosion.wav' in the same folder)

pygame.init()
pygame.mixer.init() # --- NEW

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade - Activity 11")

# -- Sounds --
try:
    laser_sound = pygame.mixer.Sound("laser.wav")
    explosion_sound = pygame.mixer.Sound("explosion.wav")
except pygame.error:
    print("Warning: Sound files not found. Game will be silent.")
    laser_sound = None
    explosion_sound = None


# -- Colours and Fonts --
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
PLAYER_COLOR, ALIEN_COLOR, BULLET_COLOR = (66, 135, 245), (239, 68, 68), (255, 255, 0)
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

# -- Game State --
score = 0
game_over = False
start_time = pygame.time.get_ticks()
GAME_DURATION = 30000 # 30 seconds

# -- Entity Properties --
player_rect = pygame.Rect((screen_width - 50) / 2, screen_height - 60, 50, 50)
alien_rect = pygame.Rect(100, 50, 40, 40)
alien_speed = 3
bullets = []
PLAYER_SPEED, BULLET_SPEED = 5, 10

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# -- Main Game Loop --
running = True
while running:
    time_elapsed = pygame.time.get_ticks() - start_time
    time_remaining = max(0, (GAME_DURATION - time_elapsed) // 1000)

    # -- Event Handling --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 5, 10)
                bullets.append(bullet)
                if laser_sound: laser_sound.play()

    if not game_over:
        # -- Player Movement --
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_rect.right < screen_width:
            player_rect.x += PLAYER_SPEED

        # -- Game Logic --
        alien_rect.x += alien_speed
        if alien_rect.left <= 0 or alien_rect.right >= screen_width:
            alien_speed *= -1

        for bullet in bullets[:]:
            bullet.y -= BULLET_SPEED
            if bullet.colliderect(alien_rect):
                score += 10
                bullets.remove(bullet)
                alien_rect.x = random.randint(0, screen_width - alien_rect.width)
                if explosion_sound: explosion_sound.play()
            elif bullet.bottom < 0:
                bullets.remove(bullet)
        
        if time_remaining == 0:
            game_over = True

    # -- Drawing --
    screen.fill(BLACK)
    if game_over:
        draw_text("Game Over", large_font, WHITE, screen, screen_width / 2, screen_height / 2 - 50)
        draw_text(f"Final Score: {score}", font, WHITE, screen, screen_width / 2, screen_height / 2 + 20)
    else:
        pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
        pygame.draw.rect(screen, ALIEN_COLOR, alien_rect)
        for bullet in bullets:
            pygame.draw.rect(screen, BULLET_COLOR, bullet)
        draw_text(f"Score: {score}", font, WHITE, screen, 60, 30)
        draw_text(f"Time: {time_remaining}", font, WHITE, screen, screen_width - 80, 30)

    pygame.display.flip()
    pygame.time.Clock().tick(60) # Limit frame rate

pygame.quit()
