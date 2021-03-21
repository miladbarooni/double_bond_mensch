import pygame 
import random
import time
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
board_image_x , board_image_y = 100, 40
zero = pygame.image.load("Images/Dice/0.png")
one = pygame.image.load("Images/Dice/1.png")
two = pygame.image.load("Images/Dice/2.png")
three = pygame.image.load("Images/Dice/3.png")
four = pygame.image.load("Images/Dice/4.png")
five = pygame.image.load("Images/Dice/5.png")
six = pygame.image.load("Images/Dice/6.png")
board_image = pygame.image.load("Images/board.png")
#initial the dice
dice_list = [zero, one, two, three, four, five, six]
dice_image = zero

# Loading player images
red_1 = pygame.image.load("Images/Player/red.png")
red_2 = pygame.image.load("Images/Player/red.png")
red_3 = pygame.image.load("Images/Player/red.png")
red1_coordinate = (565 ,320)
# red_2_x, red_2_y = 
# red_3_x, red_3_y = 

def distance_check(point1, point2):
    xs = point1[0] - point2[0]
    ys = point1[1] - point2[1]
    res = pow (pow(xs, 2) + pow(ys, 2), 0.5)
    if (res < 10):
        return True
    return False

def board_logo ():
    screen.blit(board_image,(board_image_x, board_image_y))
    screen.blit(shiraz_university, (shiraz_logo_x, shiraz_logo_y))

current_player = red_1
points = [(616, 309),(602, 245),(555, 202),
(556, 131),
(497, 98),
(439, 134),
(437, 197),
(497, 230),
(391, 241),
(380, 308),
(310, 314),
(260, 363),
(193, 362)
]
wait_for_point_selection = False
#Game Loop
running = True
while running:
    screen.fill((255,255,255))
    # showing the current dice image
    screen.blit(dice_image, (20, 10))
    screen.blit(red_1,red1_coordinate)
    for event in pygame.event.get():
        
            

        # when click on the quit
        if event.type == pygame.QUIT:
            running = False
        # when click on dice
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            # f = open("points.txt", "a")
            # f.write(str(event.pos) + "\n")
            # f.close()
            print (x, y)
            if dice_image.get_rect().collidepoint(x, y):
                dice_number = random.randint(1,6)
                dice_image = dice_list[dice_number]
            elif wait_for_point_selection == True:
                for point in points:
                    if distance_check(event.pos, point):
                        red1_coordinate = (point[0] -12, point[1] -12)
                        break
                wait_for_point_selection = False
            elif distance_check(red1_coordinate, [x-12,y-12]) and wait_for_point_selection == False:
                current_player = red_1
                wait_for_point_selection = True
            
                


    board_logo()
    # pygame.draw.lines(screen, (0,0,0), False, points, 3)
    pygame.display.update()