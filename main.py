import pygame 
import random
import time
color_dict = {"red":(255,0,0), "blue":(0,0,255), "green":(0,255,0), "yellow":(255,255,0)}
#init
pygame.init()
# create the screen
screen = pygame.display.set_mode((1000, 800))
# Set Title(Caption) for the screen.
pygame.display.set_caption("Double Bond Mensch")
# Set Icon for screen.
icon = pygame.image.load("Images/logo.png")
pygame.display.set_icon(icon)
points = [(588, 331),
(642, 269),
(626, 194),
(565, 140),
(565, 65),
(500, 25),
(435, 65),
(435, 140),
(500, 180),
(374, 193),
(358, 270),
(410, 330),
(280, 280),
(220, 335),
(140, 335),
(105, 400),
(140, 470),
(220, 470),
(260, 400),
(280, 522),
(358, 531),
(411, 472),
(375, 607),
(435, 660),
(435, 735),
(500, 775),
(565, 735),
(565, 660),
(500, 620),
(626, 606),
(642, 530),
(586, 468),
(719, 521),
(779, 470),
(858, 470),
(896, 400),
(858, 335),
(779, 335),
(740, 400),
(721, 280),

# green home 
(580, 310),
(600, 290),
(620, 270),
# blue home
(420, 310),
(400, 290), 
(380, 270),
# yellow home
(580, 490), 
(600, 510), 
(620, 530),
# red home
(420, 490), 
(400, 510),
(380, 530)
]


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

class DoubleBond:
    def __init__ (self, start_pos, end_pos, color):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.visibility = False
        self.color = color
    def toggle (self):
        self.visibility = not self.visibility
    def locate(self):
        if self.visibility:
            pygame.draw.line(screen, color_dict[self.color], self.start_pos, self.end_pos)

class Home:
    def __init__(self, corners, middle_positions, color):
        self.middle_positions = middle_positions
        self.corners = corners[:]
        self.double_bonds = []
        self.color = color
        for i in range(5):
            d_x = corners[i][0] - corners[i+1][0]
            d_y = corners[i][1] - corners[i+1][1]
            if (d_x == 0):
                if (corners[i][0]>500):
                    start_pos = (corners[i][0]-10, corners[i][1])
                    end_pos = (corners[i+1][0]-10, corners[i+1][1])
                    new = DoubleBond(start_pos, end_pos, self.color)
                    self.double_bonds.append(new)
                else:
                    start_pos = (corners[i][0]+10, corners[i][1])
                    end_pos = (corners[i+1][0]+10, corners[i+1][1])
                    new = DoubleBond(start_pos, end_pos, self.color)
                    self.double_bonds.append(new)
            
            

        
    
    def distance_check(self, clicked_pos):
        for middle_pos in self.middle_positions:
            xs = (middle_pos[0]) - clicked_pos[0]
            ys = (middle_pos[1]) - clicked_pos[1]
            res = pow (pow(xs, 2) + pow(ys, 2), 0.5)
            if (res < 10):
                corners = self.corners[:]
                sorted_corners = []
                for corner in corners:
                    xs = (corner[0]) - middle_pos[0]
                    ys = (corner[1]) - middle_pos[1]
                    res = pow (pow(xs, 2) + pow(ys, 2), 0.5)
                    sorted_corners.append((res, corner))
                
                sorted_corners.sort(key=lambda x:x[0])
                print (sorted_corners)
                # print (sorted_corners[0][1], sorted_corners[1][1])
                if (self.color == "yellow" or self.color == "blue"):
                    d_x = sorted_corners[0][1][0] - sorted_corners[1][1][0]
                    d_y = sorted_corners[0][1][1] - sorted_corners[1][1][1]
                    if (d_x == 0):
                        print ("hello")
                        print (color_dict[self.color])
                        line = (sorted_corners[0][1] - 5, sorted_corners[1][1])
                        # pygame.draw.line(screen, color_dict[self.color], sorted_corners[0][1], sorted_corners[1][1])
                    else:
                        print ("hello2")
                        m = d_y/d_x
                
        return
    
class Player:
    def __init__ (self, init_pos, home, bonds, p_image, color):
        piece1 = Piece(init_pos[0], p_image)
        piece2 = Piece(init_pos[1], p_image)
        piece3 = Piece(init_pos[2], p_image)
        self.pieces = [piece1, piece2, piece3]
        self.home = Home(home, bonds, color)
        self.color = color



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
yellow_bond = [(529, 636),(465, 639),(432, 696),(461, 754),(535, 755),(568, 697)]
yellow_init = [(580, 490), (600, 510), (620, 530)]
yellow_home = points[23:29]
yellow_player = Player(yellow_init, yellow_home, yellow_bond, "Images/Player/yellow.png", "yellow")


green_bond = [(817, 331),(876, 362),(878, 431),(816, 468),(759, 434),(758, 367)]
green_init = [(580, 310),(600, 290),(620, 270)]
green_home = points[33:39]
green_player = Player(green_init, green_home, green_bond, "Images/Player/green.png", "green")

blue_bond = [(432, 99),(465, 160),(536, 159),(568, 98),(533, 41),(463, 44)]
blue_init = [(420, 310), (400, 290), (380, 270)]
blue_home = points[3:9]
blue_player = Player(blue_init, blue_home, blue_bond, "Images/Player/blue.png", "blue")

red_bond = [(180, 332),(239, 365),(241, 431),(177, 467),(122, 432),(123, 364)]
red_init = [(420, 490), (400, 510),(380, 530)]
red_home = points[13:19]
red_player = Player(red_init, red_home, red_bond, "Images/Player/red.png", "red" )
players = [red_player, blue_player, yellow_player, green_player]



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




# for i  in range(4):
#     print (i)
#     for j in range(10*i+4, 10*i+9):
#         d_x = points[j][0] - points[j+1][0]
#         d_y = points[j][1] - points[j+1][1]
#         if (d_x == 0):
#             print ("infinit")
#         else:
#             m = d_y/d_x
#             print (m)



# Control Variable
select_piece = True
current_player = red_player
current_piece = red_player.pieces[0]
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
        for double_bond in player.home.double_bonds:
            double_bond.locate()

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
            # f = open("yellow.txt", "a")
            # f.write(str(event.pos) + ",\n")
            # f.close()
            x, y = event.pos
            # print (x, y)
            # when waiting for selecting a piece

            for player in players:
                player.home.distance_check(event.pos)

            if select_piece:
                
                x, y = event.pos
                for player in players:
                    for piece in player.pieces:
                        if piece.distance_check(event.pos):
                            current_player = player
                            select_piece = False
                            current_piece = piece
                            break
            # when waiting for selectiopen("blue.txt", "a")
            # f.write(str(event.pos) + ",\n")
            # f.close()ng a position
            else:
                for point in points:
                    if distance_check(point, event.pos):
                        
                        current_piece.move(point)
                        select_piece = True

            
           
            
            
                


    

    pygame.display.update()