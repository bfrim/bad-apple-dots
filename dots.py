import pygame

pygame.init()

window = pygame.display.set_mode((600, 400))

frame_one = pygame.image.load('1frameman.png')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    window.fill((0, 0, 0))

    i = 2
    while i < 600:
        j = 2
        while j < 400:
            color = frame_one.get_at((i, j))
            r, g, b = color[:3]
            brightness = (r + g + b) / 3

            if brightness >= 50:
                pygame.draw.circle(window, (255, 255, 255), [i, j], 1)
            j += 4
        i += 4

    pygame.display.flip()

# Quit Pygame
pygame.quit()
