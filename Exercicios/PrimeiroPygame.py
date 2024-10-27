import pygame
pygame.init() #inicializa o pygame
pygame.display.set_mode((680, 500))
running =  True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        pygame.BUTTON_MIDDLE = True
        if event.type == pygame.QUIT:
            running = False