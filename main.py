import pygame 
import random
import time
#init
pygame.init()

class Piece:
    def __init__(self, init_coordinate, image):
        self.position = init_coordinate
        self.img = pygame.image.load(image)

    def move(self, destination):
        self.position = destination

    def locate (self):
        relax_coordinate = list(self.position)
        relax_coordinate[0], relax_coordinate[1] = relax_coordinate[0] - 12.5, relax_coordinate[1] - 12.5
        relax_position = tuple(relax_coordinate)
        screen.blit(self.img, relax_position)

    def distance_check(self, clicked_pos):
        xs = (self.position[0]) - clicked_pos[0]
        ys = (self.position[1]) - clicked_pos[1]
        res = pow (pow(xs, 2) + pow(ys, 2), 0.5)
        if (res < 10):
            return True
        return False

class Player:
    def __init__ (self, first_piece, second_piece, third_piece, p_image):
        piece1 = Piece(first_piece, p_image)
        piece2 = Piece(second_piece, p_image)
        piece3 = Piece(third_piece, p_image)
        self.pieces = [piece1, piece2, piece3]



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
shiraz_logo_x, shiraz_logo_y = 435, 333
board_image_x , board_image_y = 100, 20
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
players = []
red_player = Player((580, 310),(600, 290),(620, 270),"Images/Player/red.png" )
players = [red_player]
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


points = [(640, 270),
(625, 190),
(565, 140),
(570, 60),
(500, 20),
(433, 59),
(431, 140),
(499, 177),
(372, 192),
(358, 269),
(280, 280),
(221, 330),
(259, 398),
(141, 332),
(104, 398),
(143, 466),
(220, 468),
(280, 523),
(359, 529),
(375, 606),
(429, 656),
(434, 735),
(497, 774),
(500, 620),
(565, 657),
(567, 735),
(627, 608),
(643, 529),
(720, 518),
(778, 465),
(856, 465),
(895, 398),
(742, 397),
(777, 332),
(859, 332),
(720, 277)
]
wait_for_point_selection = False
wait_for_piece_selection = True
select_piece = True
#Game Loop
running = True
while running:
    screen.fill((255,255,255))
    board_logo()
    # showing the current dice image
    screen.blit(dice_image, (20, 10))
    # locate all pieces of players on the board
    for player in players:
        for piece in player.pieces:
            piece.locate()
    for event in pygame.event.get(): 

        # when click on the quit
        if event.type == pygame.QUIT:
            running = False

        # when mouse click on the dice image
        if event.type == pygame.MOUSEBUTTONDOWN and dice_image.get_rect().collidepoint(event.pos[0], event.pos[1]):
            dice_number = random.randint(1,6)
            dice_image = dice_list[dice_number]

        # when mouse click anywhere else
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # f = open("points.txt", "a")
            # f.write(str(event.pos) + "\n")
            # f.close()
            
            # when waiting for selecting a piece
            if select_piece:
                print ("I'm waiting")
                x, y = event.pos
                for player in players:
                    for piece in player.pieces:
                        if piece.distance_check(event.pos):
                            print ("hello")
                            select_piece = False
                            current_piece = piece
                            break
            # when waiting for selecting a position
            else:
                for point in points:
                    if distance_check(point, event.pos):
                        print ("I'm trying to move it")
                        current_piece.move(point)
                        select_piece = True

            
           
            # print (x, y)

            # Changing the dice
            # if wait_for_point_selection == True:
            #     for point in points:
            #         if distance_check(event.pos, point):
            #             # red1_coordinate = (point[0] -12, point[1] -12)
            #             break
            #     wait_for_point_selection = False
            # elif  wait_for_piece_selection:
            #     # distance_check(red1_coordinate, [x-12,y-12])
            #     wait_for_point_selection = True
            
                


    

    pygame.display.update()