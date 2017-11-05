import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
box = pygame.Rect(615, 335, 40, 40)
pox = pygame.Rect(615, 335, 40, 40)
print(pygame.__version__)
clock = pygame.time.Clock()
delta = 0.0
while True:
    # closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    #ticking
    delta += clock.tick()/1000.0

    # playing
    keys = pygame.key.get_pressed()
    if keys [pygame.K_RIGHT]:
        box.x +=10
    if keys[pygame.K_LEFT]:
        box.x -=10
    if keys[pygame.K_DOWN]:
        box.y +=10
    if keys[pygame.K_UP]:
        box.y -=10
    if keys [pygame.K_d]:
        pox.x +=10
    if keys[pygame.K_a]:
        pox.x -=10
    if keys[pygame.K_s]:
        pox.y +=10
    if keys[pygame.K_w]:
        pox.y -=10

    # rendering
    screen.fill ((0,0,23))
    pygame.draw.rect(screen, (255, 255, 255), box)
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), pox)
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1270, 250, 30, 240))
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 250, 10, 240))
    pygame.display.flip()