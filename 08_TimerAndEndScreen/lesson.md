### Activity 8: Adding a Timer and End Screen
### Time: 60 min
### 🎯 Learning Intention:
Our goal is to add a countdown timer to the game and show a "Game Over" screen when time runs out.
### 👍Success Criteria:
*   I can display a timer on the screen that counts down every second.
*   When the timer reaches zero, the game stops.
*   A "Game Over" message and the final score are displayed on the screen.
### 💡 New Concepts We'll Learn:
*   **Time Management:** Using Pygame's clock to measure time and create a countdown.
*   **Game States:** Managing different phases of the game, such as the "playing" state and the "game over" state.
### 🤔 What is Time Management in Pygame?
Pygame has a built-in `Clock` that helps us control the flow of time. We can get the number of milliseconds that have passed since the game started. By keeping track of this, we can create a countdown timer. We'll set a start time when the game begins and then, inside the loop, we'll calculate how many seconds are left by subtracting the current time from the total game duration.
### 🤔 What are Game States?
Think of a DVD player. It can be in a "playing" state, a "paused" state, or a "menu" state. Our game is similar. Right now, it only has one state: "playing". We are going to add a "game over" state. We'll use a variable, let's call it `game_over`, and set it to `False` at the start. When the timer runs out, we'll set `game_over = True`. We can then use an `if` statement to change what happens in our game loop. If `game_over` is `False`, we run the normal game logic. If it's `True`, we stop the game and show the end screen instead.
### 🎮 How We'll Use It in Our Game:
*   **Time Management:** We will use `pygame.time.get_ticks()` to get the current time. We'll set a variable for the total game duration (e.g., 30 seconds) and calculate the time remaining. We'll then render and blit this timer to the screen, just like we did with the score.
*   **Game States:** We will create a `game_over = False` variable. Inside the game loop, we'll have a big `if not game_over:` block that contains all our current game logic (moving the player, shooting, etc.). When the timer reaches zero, we'll set `game_over = True`. We'll then add an `else:` block to handle drawing the "Game Over" screen.
### ✍️ Let's Code: Step-by-Step
```python
import pygame
import random

# ... (initialization, setup, variables)

# NEW: Game state and timer variables
game_over = False
game_duration = 30 # Game lasts for 30 seconds
start_time = pygame.time.get_ticks() # Get the time when the game starts (in milliseconds)
large_font = pygame.font.Font(None, 74) # A bigger font for the game over message

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Only handle game input if the game is not over
        if not game_over:
            if event.type == pygame.KEYDOWN:
                # ... (key handling for movement and shooting)

    # --- Game Logic ---
    if not game_over:
        # ... (all the code for updating player, alien, and bullet positions)
        # ... (all the code for collision detection)

        # NEW: Timer logic
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # Convert to seconds
        time_left = game_duration - elapsed_time
        if time_left <= 0:
            time_left = 0
            game_over = True # Set the game state to over

    # --- Drawing ---
    screen.fill(BLACK)

    if not game_over:
        # This is the "playing" state drawing
        # ... (draw player, alien, bullets)
        
        # Render and blit score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # NEW: Render and blit timer
        timer_text = font.render(f"Time: {int(time_left)}", True, WHITE)
        screen.blit(timer_text, (screen_width - 150, 10))
    else:
        # This is the "game over" state drawing
        game_over_text = large_font.render("Game Over", True, RED)
        final_score_text = font.render(f"Final Score: {score}", True, WHITE)
        
        # Center the text on the screen
        screen.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, screen_height/2 - game_over_text.get_height()/2 - 20))
        screen.blit(final_score_text, (screen_width/2 - final_score_text.get_width()/2, screen_height/2 + final_score_text.get_height()/2))

    pygame.display.update()

pygame.quit()
```
### ✅ Full Code for This Activity:
```python
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
```
### ⭐ Challenge Task:
Can you add a "Press R to Restart" message to the game over screen? After the game is over, you'll need to check for a new `KEYDOWN` event for the 'R' key (`pygame.K_r`). If it's pressed, you'll need to reset all the game state variables back to their starting values (score to 0, `game_over` to `False`, `start_time` to the current time, etc.) to start a new game.
