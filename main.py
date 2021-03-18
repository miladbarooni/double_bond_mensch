import pygame 

#init
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000, 800))
# Set Title(Caption) for the screen.
pygame.display.set_caption("Double Bond Mensch")
# Set Icon for screen.
icon = pygame.image.load("Images/logo.png")
pygame.display.set_icon(icon)
# Shiraz University Logo
shiraz_university = pygame.image.load("Images/Shiraz_University_logo.png")
shiraz_university.convert()
rect = shiraz_university.get_rect()
shiraz_logo_x, shiraz_logo_y = 420, 320


def initial_board ():
   
    screen.blit(shiraz_university, (shiraz_logo_x, shiraz_logo_y))

    

#Game Loop
running = True

while running:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        # print (event)
        if event.type == pygame.QUIT:
            running = False
    initial_board()
    pygame.display.flip()
    pygame.display.update()