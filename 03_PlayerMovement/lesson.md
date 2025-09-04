### Activity 3: Getting the Player to Move
### Time: 60 min
### 🎯 Learning Intention:
Our goal is to make the player move left and right using the arrow keys.
### 👍Success Criteria:
*   I can write code that checks for keyboard presses.
*   I can update the player's X-coordinate based on which key is pressed.
*   The player on the screen moves when I press the left and right arrow keys.
### 💡 New Concepts We'll Learn:
*   **Event Handling (KEYDOWN):** Checking for a specific type of event—when a key on the keyboard is pressed down.
*   **Conditional Statements (if/elif/else):** Code that allows us to make decisions, like "IF the right arrow key is pressed, THEN move the player to the right."
*   **Updating Variables:** Changing the value of a variable, like `player_x`, to move our character.
### 🤔 What is Event Handling?
Remember our `for event in pygame.event.get():` loop? It's like a mail carrier checking a mailbox for new letters. So far, we've only looked for one type of letter: the `pygame.QUIT` letter. But there are many other types! `KEYDOWN` is an event that happens the moment you press a key. We can check which specific key was pressed (like the left arrow or right arrow) and then make something happen in our game.
### 🤔 What are Conditional Statements?
Conditional statements are like choosing your own adventure. They let your program make decisions. The simplest is an `if` statement: "**If** this is true, **then** do that." We can add `elif` (short for "else if") to check for other conditions, and `else` to do something if none of the conditions are met.
Example:
`if weather == "rainy":`
  `print("Bring an umbrella!")`
`elif weather == "sunny":`
  `print("Wear sunglasses!")`
`else:`
  `print("Have a great day!")`
### 🎮 How We'll Use It in Our Game:
*   **Event Handling:** Inside our main game loop, we'll add a new check inside our event `for` loop. We'll check `if event.type == pygame.KEYDOWN`.
*   **Conditional Statements:** Once we know a key has been pressed, we'll use another `if` statement to check *which* key it was. `if event.key == pygame.K_LEFT:` will check for the left arrow key, and `pygame.K_RIGHT` for the right arrow key.
*   **Updating Variables:** Inside our conditional statements, we will change the `player_x` variable. To move right, we will add to `player_x`. To move left, we will subtract from it. We'll also create a `player_speed` variable to control how fast the player moves.
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

player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10

# NEW: Let's create a variable for how fast the player moves.
player_speed = 5
# NEW: We need a variable to track the change in the player's x position.
player_x_change = 0

running = True
while running:
    # Event handling is where we check for player input.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # NEW: Check if a key has been pressed down.
        if event.type == pygame.KEYDOWN:
            # If it's the left arrow key...
            if event.key == pygame.K_LEFT:
                # ...we set the change in x to be negative (move left).
                player_x_change = -player_speed
            # If it's the right arrow key...
            elif event.key == pygame.K_RIGHT:
                # ...we set the change in x to be positive (move right).
                player_x_change = player_speed
        
        # NEW: Check if a key has been released.
        if event.type == pygame.KEYUP:
            # If the left or right arrow key is released...
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # ...we stop the player's movement by setting the change to 0.
                player_x_change = 0

    # NEW: Update the player's actual position.
    # We do this outside the event loop, so it happens every frame.
    player_x += player_x_change

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
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

# Player properties
player_width = 50
player_height = 50
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10
player_speed = 5
player_x_change = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            elif event.key == pygame.K_RIGHT:
                player_x_change = player_speed
        
        # KEYUP event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update player position
    player_x += player_x_change

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    
    # Update display
    pygame.display.update()

pygame.quit()
```
### ⭐ Challenge Task:
Right now, the player can move off the screen! Can you add a new conditional (`if`) statement to prevent this? After you update `player_x`, check `if player_x < 0`. If it is, set `player_x = 0`. Then, add another check to see if the player has gone too far to the right. The right edge is `screen_width - player_width`.
