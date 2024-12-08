import pygame
import sys

pygame.init()

# Set up the screen
ssize = [900, 900]
screen = pygame.display.set_mode(ssize, pygame.RESIZABLE)
sizemult = [1, 1]
font = pygame.font.SysFont("Menlo", 20)
fsize = font.size("Menlo")

# Set up colors
BLACK = (0, 0, 0)
TRANSPARENT_BLACK = (0, 0, 0, 0)

# Define lines
lines = []

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update sizemult if window size changes
    if ssize != pygame.display.get_surface().get_size():
        ssize = pygame.display.get_surface().get_size()
        sizemult = [ssize[0] / 30, ssize[1] / 30]

    # Draw lines onto a transparent surface
    transparent_surface = pygame.Surface(ssize, pygame.SRCALPHA)
    transparent_surface.fill(TRANSPARENT_BLACK)

    try:
        for line in lines:
            pygame.draw.line(transparent_surface, (127, 127, 0, line[3]), (line[0], line[1]), (line[2]), int(min(sizemult[0], sizemult[1])) - 2)
    except: pass

    # Blit the transparent surface onto the screen
    screen.blit(transparent_surface, (0, 0))

    # Update alpha values of lines
    for i in range(len(lines)):
        lines[i][3] += 1  # Increase alpha value
        if lines[i][3] >= 255:
            lines[i][3] = 255  # Cap alpha value
            break

    # Generate new lines randomly
    # Here you can replace this part with your own logic to generate lines
    # I'm just generating random lines for demonstration
    if pygame.time.get_ticks() % 100 == 0:  # Add new line every 100 milliseconds
        start_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        end_pos = (start_pos[0] + 50, start_pos[1] + 50)
        lines.append([start_pos[0], start_pos[1], end_pos[0], end_pos[1], 0])  # Add line with alpha 0

    pygame.display.flip()

pygame.quit()
sys.exit()