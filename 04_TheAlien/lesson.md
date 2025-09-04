### Activity 4: Creating the Alien
### Time: 60 min
### 🎯 Learning Intention:
Our goal is to create an alien enemy that moves automatically across the top of the screen.
### 👍Success Criteria:
*   I can create variables for the alien's properties (size, position, speed).
*   I can draw the alien on the screen.
*   The alien moves back and forth across the screen without my input.
### 💡 New Concepts We'll Learn:
*   **Game State:** Keeping track of all the important information in our game, like the positions of the player and the alien.
*   **Boundary Checking:** Using conditional statements (`if`) to detect when an object reaches the edge of the screen and making it change direction.
### 🤔 What is Game State?
The "state" of a game is a snapshot of everything that's happening at a single moment. It includes the player's score, the alien's position, the number of lives left, etc. We store this state in variables. Our game loop's job is to constantly update this state based on player input and game rules, and then draw the new state to the screen. By creating variables for our alien, we are adding to our game's state.
### 🤔 What is Boundary Checking?
Imagine a robot vacuum cleaner. It moves in a straight line until it bumps into a wall, and then it turns around. Boundary checking is the same idea in our code. We will constantly check the alien's X-coordinate. If it goes too far to the left (less than 0) or too far to the right (past the screen's width), we'll tell it to reverse its direction. We do this by "flipping" the sign of its speed variable (e.g., from 5 to -5).
### 🎮 How We'll Use It in Our Game:
*   **Game State:** We will create a new set of variables just for the alien: `alien_x`, `alien_y`, `alien_width`, `alien_height`, and `alien_speed`. This keeps the alien's information separate from the player's.
*   **Boundary Checking:** Inside the main game loop, after we update the alien's position, we will add an `if` statement. This statement will check if `alien_x` is outside the screen boundaries. If it is, we will reverse the `alien_speed` by multiplying it by -1.
### ✍️ Let's Code: Step-by-Step
```python
import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# NEW: A color for our alien
GREEN = (0, 255, 0)

# Player properties
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10
player_speed = 5
player_x_change = 0

# NEW: Alien properties
alien_width = 50
alien_height = 50
alien_x = 0 # Start at the top-left
alien_y = 50
alien_speed = 3 # It moves on its own, so we give it a speed directly

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    # Boundary checking for the player
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # NEW: Update alien position
    # The alien moves automatically every frame.
    alien_x += alien_speed

    # NEW: Boundary checking for the alien
    # If the alien hits the right side OR the left side...
    if alien_x > screen_width - alien_width or alien_x < 0:
        # ...reverse its direction by flipping its speed.
        alien_speed = -alien_speed

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    # NEW: Draw the alien
    pygame.draw.rect(screen, GREEN, (alien_x, alien_y, alien_width, alien_height))
    
    pygame.display.update()

pygame.quit()
```
### ✅ Full Code for This Activity:
```python
import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Player properties
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10
player_speed = 5
player_x_change = 0

# Alien properties
alien_width = 50
alien_height = 50
alien_x = 0
alien_y = 50
alien_speed = 3

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # Update alien position
    alien_x += alien_speed

    # Alien boundary checking
    if alien_x > screen_width - alien_width or alien_x < 0:
        alien_speed = -alien_speed

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, GREEN, (alien_x, alien_y, alien_width, alien_height))
    
    # Update display
    pygame.display.update()

pygame.quit()
```
### ⭐ Challenge Task:
Can you make the alien move faster or slower? Try changing the `alien_speed` variable. What happens if you make it a bigger number, like 10? What about a smaller number, like 1? Also, try changing the alien's starting position (`alien_x` and `alien_y`) so it starts in the middle of the screen.
