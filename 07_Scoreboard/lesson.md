### Activity 7: Creating a Scoreboard
### Time: 60 min
### 🎯 Learning Intention:
Our goal is to display the player's score on the screen and increase it when they hit an alien.
### 👍Success Criteria:
*   I can create a variable to keep track of the score.
*   I can render text and display it on the game window.
*   The score increases by one every time a bullet hits the alien.
### 💡 New Concepts We'll Learn:
*   **Fonts and Text Rendering:** How to create text objects in Pygame and draw them onto the screen.
*   **Blitting:** The process of drawing one image or surface onto another.
### 🤔 What is Text Rendering?
We can't just tell Pygame to "write the score on the screen." We have to go through a few steps. First, we need to create a `Font` object, which is like choosing a font style and size in a word processor. Then, we use that font to `render()` our text. This creates a new, special image (a `Surface`) of our text. It's like creating a rubber stamp of the words "Score: 10".
### 🤔 What is Blitting?
"Blit" is a funny-sounding word that just means copying pixels from one place to another. Once we have our "rubber stamp" image of the score, we need to stamp it onto our main `screen`. The `screen.blit()` command does exactly this. It takes the text surface and a position (X and Y coordinates) and draws the text at that location. We have to do this every single frame, because our `screen.fill(BLACK)` call erases everything, including the old score.
### 🎮 How We'll Use It in Our Game:
*   **Score Variable:** We will create a new variable, `score = 0`, at the beginning of our program.
*   **Text Rendering:** We will create a `Font` object using `pygame.font.Font()`. Inside our game loop, we will `render()` the current score into a text surface.
*   **Blitting:** We will use `screen.blit()` to draw the text surface onto our main screen in the top-left corner.
*   **Updating Score:** When a bullet collides with the alien, right after we play the explosion sound, we will add the line `score += 1`.
### ✍️ Let's Code: Step-by-Step
```python
import pygame
import random

# ... (initialization and setup code)

# NEW: Score variable
score = 0
# NEW: Font object. 'None' uses the default Pygame font. 36 is the size.
font = pygame.font.Font(None, 36)

# ... (player, alien, bullet variables)

running = True
while running:
    # ... (event handling code)

    # ... (position update code)

    # Bullet and collision logic
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
        elif bullet.colliderect(alien_rect):
            explosion_sound.play()
            bullets.remove(bullet)
            # NEW: Increase the score
            score += 1
            alien_x = random.randint(0, screen_width - alien_width)
            alien_y = 50

    # Drawing
    screen.fill(BLACK)
    
    # ... (draw player, alien, bullets)

    # NEW: Render the score text
    # The 'True' is for anti-aliasing (makes the text look smoother).
    # WHITE is the color of the text.
    score_text = font.render(f"Score: {score}", True, WHITE)
    
    # NEW: Blit the score text onto the screen
    # We'll put it at position (10, 10), which is the top-left corner.
    screen.blit(score_text, (10, 10))
    
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

# Colors and Font
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font = pygame.font.Font(None, 36)

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

# Game Variables
score = 0

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
            score += 1
            alien_x = random.randint(0, screen_width - alien_width)
            alien_y = 50

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, GREEN, alien_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    # Render and blit score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()

pygame.quit()
```
### ⭐ Challenge Task:
Can you change the font and size of the score? You can use a specific font file (like `arial.ttf`) by changing the font line to `font = pygame.font.Font('arial.ttf', 48)`. You'll need to have the font file in your project folder. Also, try changing the color of the score text. Create a new `YELLOW` color variable and use it in the `font.render()` function.
