### Activity 1: Creating the Game Window
### Time: 60 min
### 🎯 Learning Intention:
Our goal is to create a game window on the screen.
### 👍Success Criteria:
*   I can create a Python file and write code in it.
*   When I run my code, a new window appears on my screen.
*   I can close the window and the program stops.
### 💡 New Concepts We'll Learn:
*   **Pygame Library:** A set of tools that makes it easier to build games in Python.
*   **The Game Loop:** The heart of the game that runs continuously, checking for events and updating the screen.
### 🤔 What is a Pygame Library?
Imagine you want to build a house. You could make every single brick and nail yourself, but that would take forever! A library is like a hardware store where you can get pre-made parts like windows, doors, and pipes. Pygame is our "game-making hardware store." It gives us ready-to-use code for drawing shapes, handling player input, and playing sounds. We just need to learn how to put the pieces together.
### 🤔 What is a Game Loop?
A game loop is like the engine of a car. As long as the engine is running, the car can do things like move, play music, and run the air conditioning. Our game loop will run over and over again, very fast. In each cycle, it will check for player actions (like pressing a key), update the game state (like moving a character), and redraw the screen to show what's new. Without a loop, our game would just be a static image.
### 🎮 How We'll Use It in Our Game:
*   **Pygame Library:** We will use the `pygame.init()` command to "turn on" all the tools in our Pygame library. We'll also use it to create a display screen and set its title.
*   **Game Loop:** We will create a `while` loop that keeps our game running. Inside this loop, we'll check if the player has tried to close the window. If they have, we'll stop the loop and exit the game.
### ✍️ Let's Code: Step-by-Step
```python
# First, we need to bring the Pygame library into our program.
# 'import pygame' is like telling Python, "I want to use the Pygame tools."
import pygame

# Before we can use any of Pygame's tools, we have to initialize them.
# pygame.init() sets up everything we need to get started.
pygame.init()

# Now, let's create our game window. We need to decide how big it will be.
# We'll use variables to store the width and height. This makes it easy to change later.
screen_width = 800  # The width of the window in pixels
screen_height = 600 # The height of the window in pixels

# This line creates the actual window. 
# pygame.display.set_mode() takes a tuple (a pair of values) for the dimensions.
screen = pygame.display.set_mode((screen_width, screen_height))

# We can also give our window a title.
# This will appear at the top of the window.
pygame.display.set_caption("Alien Arcade")

# This is the start of our main game loop.
# We create a variable 'running' and set it to True.
# The 'while' loop will continue as long as 'running' is True.
running = True
while running:
    # Inside the loop, we need to check for events.
    # An event is any action that happens, like a mouse click or key press.
    # pygame.event.get() gets a list of all events that have happened.
    for event in pygame.event.get():
        # We check if the event type is pygame.QUIT.
        # This event happens when you click the 'X' button on the window.
        if event.type == pygame.QUIT:
            # If the 'X' is clicked, we set 'running' to False.
            # This will make the 'while' loop stop on its next check.
            running = False

# After the loop has finished, we need to clean up.
# pygame.quit() is the opposite of pygame.init(). It shuts down the Pygame library.
pygame.quit()
```
### ✅ Full Code for This Activity:
```python
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the display surface
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Alien Arcade")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
```
### ⭐ Challenge Task:
Can you change the variables for `screen_width` and `screen_height` to make the window rectangular instead of square? Try making it `1000` pixels wide and `400` pixels tall. What happens if you make it really small, like `200` by `200`? Also, try changing the window title to your own name!
