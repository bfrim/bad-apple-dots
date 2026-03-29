import pygame
import os

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((600, 400))

# create font to display loading message with default font
font = pygame.font.Font(None, 24)
text_surface = font.render("Loading 2,190 frames...", True, (255, 255, 255))
window.blit(text_surface, (5, 5))
pygame.display.flip()

# old code for a single frame
# frame_one = pygame.image.load('1frameman.png')
# frames = os.listdir("video-frames/frames")
# frames = sorted(frames)

frames_path = "video-frames/frames"
filenames = sorted(os.listdir(frames_path))

# Preloading frames for improved performance.
preloaded_frames = []
for i in filenames:
    path = os.path.join(frames_path, i)
    frame = pygame.image.load(path).convert()
    frame = pygame.transform.scale(frame, (600, 400))
    preloaded_frames.append(frame)

curr_frame = 0

FPS = 10

# move music below loop, prevents it from playing prematurely.
pygame.mixer.music.load("ressources/MUSIC.mp3")
pygame.mixer.music.play(-1)

# this will make the animation sync with the music even if we drag the window around
# (this used to be a problem because it would pause the animation until the title bar was let go)
start_time = pygame.time.get_ticks()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # calculate current frame based on elapsed time
    # (Current Time - Start Time) / (1000ms / FPS)
    elapsed_time = pygame.time.get_ticks() - start_time
    curr_frame = int(elapsed_time / (1000 / FPS))

    # kill animation if we run out of frames
    curr_frame += 1
    if curr_frame >= len(preloaded_frames):
        break

    window.fill((0, 0, 0))

    # old code for a single frame
    # filename = frames[curr_frame]
    # frame = pygame.image.load("video-frames/frames/" + filename)
    # frame = pygame.transform.scale(frame, (600, 400))

    # cutting down on ressources by changing the above to this new line
    frame = preloaded_frames[curr_frame]

    i = 2
    while i < 600:
        j = 2
        while j < 400:
            color = frame.get_at((i, j))
            r, g, b = color[:3]
            brightness = (r + g + b) / 3
            if brightness >= 50:
                pygame.draw.circle(window, (255, 255, 255), [i, j], 1)
            j += 4
        i += 4

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
