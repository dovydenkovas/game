import pygame
import random


class Ball:
    def __init__(self, texture):
        self.ball = pygame.image.load(f"../res/{texture}.png")
        self.ballrect = self.ball.get_rect()
        self.speed = [random.randint(8, 20), random.randint(8, 20)]
        self.ballrect.x = random.randint(1, width-100)
        self.ballrect.y = random.randint(1, height-100)

    def update(self):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0:
            self.speed[0] = random.randint(8, 20)

        if self.ballrect.right > width:
            self.speed[0] = -random.randint(8, 20)

        if self.ballrect.top < 0:
            self.speed[1] = random.randint(8, 20)

        if self.ballrect.bottom > height:
            self.speed[1] = -random.randint(8, 20)


# Init
pygame.init()
size = width, height = 800, 600
speed = [8, 8]
background_color = 31, 156, 81

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

balls = []
for i in range(1, 9):
    balls.append(Ball(f"ball-{random.randint(1,4)}"))

n = 0

is_mainloop = True
while is_mainloop:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_mainloop = False

    for ball in balls:
        ball.update()

    n += 1
    if n > 30:
        n = 0
        balls.append(Ball(f"ball-{random.randint(1,4)}"))


    # Draw all elements
    screen.fill(background_color)
    for ball in balls:
        screen.blit(ball.ball, ball.ballrect)
    pygame.display.flip()

    clock.tick(30)