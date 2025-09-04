import pygame
import random

pygame.mixer.init()
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade")

# Fonts and Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 74)

# Sounds
try:
    shoot_sound = pygame.mixer.Sound('laser.wav')
    explosion_sound = pygame.mixer.Sound('explosion.wav')
except pygame.error:
    print("Warning: Sound files not found.")
    class DummySound:
        def play(self): pass
    shoot_sound = DummySound()
    explosion_sound = DummySound()

# Game State and Timer
score = 0
game_over = False
game_duration = 30  # seconds
start_time = pygame.time.get_ticks()

# Player, Alien, Bullet setup...
player_width, player_height = 50, 50
player_x, player_y = (screen_width / 2) - (player_width / 2), screen_height - player_height - 10
player_speed, player_x_change = 5, 0

alien_width, alien_height = 50, 50
alien_x, alien_y = 0, 50
alien_speed = 3
alien_rect = pygame.Rect(alien_x, alien_y, alien_width, alien_height)

bullet_width, bullet_height = 5, 15
bullet_speed = 10
bullets = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: player_x_change = -player_speed
                elif event.key == pygame.K_RIGHT: player_x_change = player_speed
                elif event.key == pygame.K_SPACE:
                    bullet_x = player_x + (player_width / 2) - (bullet_width / 2)
                    bullet = pygame.Rect(bullet_x, player_y, bullet_width, bullet_height)
                    bullets.append(bullet)
                    shoot_sound.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

    if not game_over:
        # Update positions
        player_x += player_x_change
        if player_x < 0: player_x = 0
        elif player_x > screen_width - player_width: player_x = screen_width - player_width

        alien_x += alien_speed
        if alien_x > screen_width - alien_width or alien_x < 0: alien_speed = -alien_speed
        alien_rect.x, alien_rect.y = alien_x, alien_y

        # Move bullets and check collision
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.y < 0: bullets.remove(bullet)
            elif bullet.colliderect(alien_rect):
                explosion_sound.play()
                bullets.remove(bullet)
                score += 1
                alien_x = random.randint(0, screen_width - alien_width)

        # Check timer
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        time_left = game_duration - elapsed_time
        if time_left <= 0:
            game_over = True

    # Drawing
    screen.fill(BLACK)
    if not game_over:
        pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, GREEN, alien_rect)
        for bullet in bullets:
            pygame.draw.rect(screen, RED, bullet)
        
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        timer_text = font.render(f"Time: {int(time_left)}", True, WHITE)
        screen.blit(timer_text, (screen_width - 150, 10))
    else:
        # Game Over Screen
        game_over_msg = large_font.render("Game Over", True, RED)
        final_score_msg = font.render(f"Final Score: {score}", True, WHITE)
        screen.blit(game_over_msg, (screen_width/2 - game_over_msg.get_width()/2, screen_height/2 - game_over_msg.get_height()/2))
        screen.blit(final_score_msg, (screen_width/2 - final_score_msg.get_width()/2, screen_height/2 + 30))

    pygame.display.update()

pygame.quit()
