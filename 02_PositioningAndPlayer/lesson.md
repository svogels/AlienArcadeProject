### Activity 2: Understanding Positioning & Creating the Player
### Time: 60 min
### 🎯 Learning Intention:
Our goal is to draw our player on the game window.
### 👍Success Criteria:
*   I can explain how the coordinate system works in Pygame.
*   I can create variables to store the player's position and size.
*   I can draw a rectangle on the screen to represent the player.
### 💡 New Concepts We'll Learn:
*   **Coordinates (X and Y):** A system for telling the computer exactly where to draw something on the screen.
*   **RGB Colors:** A way to mix red, green, and blue light to create any color you can imagine.
*   **Drawing Shapes:** Using Pygame commands to draw simple shapes like rectangles.
### 🤔 What are Coordinates?
Imagine your screen is a piece of graph paper. To tell a friend where to put a dot, you'd give them two numbers: how many squares to go across, and how many squares to go down. Computers do the same thing! The "across" number is called the **X-coordinate**, and the "down" number is the **Y-coordinate**. In Pygame, the starting point (0, 0) is at the **top-left corner** of the screen.
### 🤔 What are RGB Colors?
Your computer screen creates colors by mixing different amounts of red, green, and blue light. An RGB value is a set of three numbers, each from 0 to 255, that tells the computer how much of each color to use.
*   `(255, 0, 0)` is pure red (all red, no green, no blue).
*   `(0, 255, 0)` is pure green.
*   `(0, 0, 255)` is pure blue.
*   `(0, 0, 0)` is black (no light).
*   `(255, 255, 255)` is white (all lights at full intensity).
We'll use these "color codes" to paint our player and other game objects.
### 🎮 How We'll Use It in Our Game:
*   **Coordinates:** We will use X and Y variables to control the player's position. By changing these variables, we will be able to move our player around the screen in the next activity.
*   **RGB Colors:** We will define a few color variables using RGB tuples to make our code more readable. For example, we'll create a `WHITE` color for our player.
*   **Drawing Shapes:** We will use the `pygame.draw.rect()` function to draw the player on the screen. This function needs to know *where* to draw (the screen), *what color* to use, and *the position and size* of the rectangle.
### ✍️ Let's Code: Step-by-Step
```python
# Let's start with the code from our last activity.
import pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade")

# NEW: Let's define some colors using RGB values.
# This makes it easy to reuse colors without memorizing the numbers.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# NEW: Player properties. We'll create variables for our player's size and position.
# This keeps all the player's information organized.
player_width = 50
player_height = 50
# We want to start the player at the bottom-center of the screen.
# The X position is the screen's width divided by 2.
# The Y position is the screen's height minus the player's height.
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10 # 10 pixels from the bottom

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # NEW: Drawing goes inside the game loop.
    # First, we fill the screen with a background color.
    # If we don't do this, we'll see a "trail" of the player as it moves.
    screen.fill(BLACK)

    # NEW: Now, let's draw the player.
    # We use pygame.draw.rect(). It needs:
    # 1. The surface to draw on (our 'screen').
    # 2. The color (we defined 'WHITE').
    # 3. A Rect object, which is a tuple of (x, y, width, height).
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # NEW: After drawing everything, we need to update the display.
    # pygame.display.update() tells Pygame to show the new frame.
    pygame.display.update()

pygame.quit()
```
### ✅ Full Code for This Activity:
```python
import pygame

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Arcade")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player properties
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.update()

pygame.quit()
```
### ⭐ Challenge Task:
Can you change the player's starting position? Try making it start in the top-left corner. What about the bottom-right corner? Also, try changing the player's color. Create a new `BLUE` color variable and use it to draw the player.
