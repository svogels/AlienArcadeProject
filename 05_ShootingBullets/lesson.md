### Activity 5: Shooting Bullets
### Time: 60 min
### 🎯 Learning Intention:
Our goal is to make the player shoot a bullet when the spacebar is pressed.
### 👍Success Criteria:
*   I can detect when the spacebar is pressed.
*   When the spacebar is pressed, a new "bullet" rectangle appears at the player's position.
*   The bullet moves up the screen until it disappears.
### 💡 New Concepts We'll Learn:
*   **Lists:** A type of variable that can hold a collection of items, like a list of all the bullets currently on the screen.
*   **For Loops:** A way to repeat a block of code for each item in a list.
*   **Collision Detection (Simple):** Checking if two shapes are overlapping.
### 🤔 What is a List?
Imagine you have a shopping list. You can add items to it (`milk`, `bread`), remove items (`bread`), and check what's on it. A Python `list` is just like that, but for data. We can create an empty list called `bullets` and whenever the player shoots, we add the new bullet's rectangle to this list. This lets us keep track of multiple bullets on the screen at once.
### 🤔 What is a For Loop?
A `for` loop is different from the `while` loop we've been using. Our `while running:` loop goes on forever (as long as `running` is true). A `for` loop, on the other hand, goes through a list of items one by one and does something with each of them. For example, `for bullet in bullets:` means "for every single bullet that is currently in our `bullets` list, do the following...". This is perfect for moving and drawing every bullet on the screen.
### 🎮 How We'll Use It in Our Game:
*   **Lists:** We will create an empty list called `bullets = []`. When the player presses the spacebar, we will create a new rectangle for the bullet and `append()` it to our `bullets` list.
*   **For Loops:** We will create a `for` loop that iterates through the `bullets` list. Inside this loop, we will update the Y-coordinate of each bullet to make it move up the screen. We will also draw each bullet.
*   **Collision Detection:** We'll add a simple check. If a bullet's Y-coordinate is less than 0, it means it has gone off the top of the screen, and we can remove it from our list.
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
GREEN = (0, 255, 0)
# NEW: A color for our bullets
RED = (255, 0, 0)

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

# NEW: Bullet properties
bullet_width = 5
bullet_height = 15
bullet_speed = 10
# NEW: This list will hold all the bullets we shoot.
bullets = []

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
            # NEW: Check if the spacebar is pressed
            elif event.key == pygame.K_SPACE:
                # Create a new bullet rectangle. It starts at the player's center.
                bullet_x = player_x + (player_width / 2) - (bullet_width / 2)
                bullet_y = player_y
                # Add the new bullet to our list.
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    alien_x += alien_speed
    if alien_x > screen_width - alien_width or alien_x < 0:
        alien_speed = -alien_speed

    # NEW: Move and manage bullets
    # We loop through a copy of the list to safely remove items.
    for bullet in bullets[:]:
        # Move the bullet up the screen
        bullet.y -= bullet_speed
        # If the bullet goes off the top of the screen...
        if bullet.y < 0:
            # ...remove it from our list.
            bullets.remove(bullet)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, GREEN, (alien_x, alien_y, alien_width, alien_height))
    
    # NEW: Draw all the bullets in our list
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    
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
RED = (255, 0, 0)

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
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))
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

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, GREEN, (alien_x, alien_y, alien_width, alien_height))
    
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    
    pygame.display.update()

pygame.quit()
```
### ⭐ Challenge Task:
Can you make the bullets wider or taller? Try changing the `bullet_width` and `bullet_height` variables. Also, try making the bullets faster or slower by changing `bullet_speed`. What happens if you make the speed a negative number?
