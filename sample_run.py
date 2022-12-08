import pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen
size = [400, 600]
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the tetromino
x_position = 100
y_position = 0

# Speed in pixels per frame
speed = 1

# Create the tetromino
tetromino = [[1, 1, 1],
             [0, 1, 0]]

# Rotate the tetromino
tetromino = list(zip(*reversed(tetromino)))

# Main game loop
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the position of the tetromino
    y_position += speed

    # Draw the screen
    screen.fill(BLACK)

    # Draw the tetromino
    for row in range(len(tetromino)):
        for column in range(len(tetromino[row])):
            if tetromino[row][column] == 1:
                pygame.draw.rect(screen, WHITE, [x_position + column * 20, y_position + row * 20, 20, 20])

    # Update the screen
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()