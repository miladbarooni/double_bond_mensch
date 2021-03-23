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



yellow_home = points[23:29]
green_home = points[33:39]
blue_home = points[3:9]
red_home = points[13:19]

corners = yellow_home + red_home + blue_home + green_home


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

class Bond:
    def __init__ (self, middle_pos, color):
        self.visibility = False
        self.middle_pos = middle_pos
        self.color = color
        sorted_corners = []
        for corner in corners:
            xs = (corner[0]) - self.middle_pos[0]
            ys = (corner[1]) - self.middle_pos[1]
            res = pow (pow(xs, 2) + pow(ys, 2), 0.5)
            sorted_corners.append((res, corner))
            
            sorted_corners.sort(key=lambda x:x[0])
        self.first = sorted_corners[0][1]
        self.second = sorted_corners[1][1]
        d_x = self.first[0] - self.second[0]
        d_y = self.first[1] - self.second[1]

        if d_x == 0 and self.middle_pos[0] > 500:
            self.start_pos = (self.first[0] - 7, self.first[1])
            self.end_pos =  (self.second[0] - 7, self.second[1])
        elif d_x == 0 and self.middle_pos[0] < 500:
            self.start_pos = (self.first[0] + 5, self.first[1])
            self.end_pos =  (self.second[0] + 5, self.second[1])
        elif d_y == 0 and self.middle_pos[1] < 400:
            self.start_pos = (self.first[0], self.first[1]+5)
            self.end_pos =  (self.second[0], self.second[1]+ 5)
        elif d_y == 0 and self.middle_pos[1] > 400:
            self.start_pos = (self.first[0], self.first[1]-13)
            self.end_pos =  (self.second[0], self.second[1]-13)

        else:
            
            m = d_x / d_y
            if self.middle_pos[1] < 100 :
                self.start_pos = (self.first[0], self.first[1]+5)
                self.end_pos =  (self.second[0], self.second[1]+5)

            elif self.middle_pos[1] < 700 and self.middle_pos[1] > 600:
                self.start_pos = (self.first[0], self.first[1]+10)
                self.end_pos =  (self.second[0], self.second[1]+10)

            elif self.middle_pos[1] > 700:
                self.start_pos = (self.first[0], self.first[1]-8)
                self.end_pos =  (self.second[0], self.second[1]-8)

            elif self.middle_pos[1] >100 and self.middle_pos[1] < 200:
                self.start_pos = (self.first[0], self.first[1]-8)
                self.end_pos =  (self.second[0], self.second[1]-8)

            elif self.middle_pos[1] > 200 and self.middle_pos[1] < 400 and ( (self.middle_pos[0] > 125 and self.middle_pos[0] < 500) or self.middle_pos[0] > 875):
                self.start_pos = (self.first[0]-8, self.first[1]+5)
                self.end_pos =  (self.second[0]-8, self.second[1]+5)
            elif self.middle_pos[1] > 200 and self.middle_pos[1] < 400 and (self.middle_pos[0] < 125 or self.middle_pos[0] < 875):
                self.start_pos = (self.first[0]+8, self.first[1]+5)
                self.end_pos =  (self.second[0]+8, self.second[1]+5)
            elif self.middle_pos[1] > 400 and self.middle_pos[1] < 600 and ( (self.middle_pos[0] > 125 and self.middle_pos[0] < 500) or self.middle_pos[0] > 875):
                self.start_pos = (self.first[0]-8, self.first[1]-5)
                self.end_pos =  (self.second[0]-8, self.second[1]-5)
            elif self.middle_pos[1] > 400 and self.middle_pos[1] < 600 and (self.middle_pos[0] < 125 or self.middle_pos[0] < 875):
                self.start_pos = (self.first[0]+8, self.first[1]-5)
                self.end_pos =  (self.second[0]+8, self.second[1]-5)

        # m = d_x/d_y
        # if (m<0 and self.middle_pos[1] < 200) or ():
        #     self.start_pos = 

    def toggle (self):
        self.visibility = not self.visibility
    def locate(self):
        if self.visibility:
            pygame.draw.line (screen, color_dict[self.color], self.start_pos, self.end_pos, 5)
    def distance_check(self, clicked_pos):
        xs = (self.middle_pos[0]) - clicked_pos[0]
        ys = (self.middle_pos[1]) - clicked_pos[1]
        res = pow (pow(xs, 2) + pow(ys, 2), 0.5)
        if (res < 10):
            return True
        return False
            
class Player:
    def __init__ (self, init_pos, p_image, color):
        piece1 = Piece(init_pos[0], p_image)
        piece2 = Piece(init_pos[1], p_image)
        piece3 = Piece(init_pos[2], p_image)
        self.pieces = [piece1, piece2, piece3]
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
yellow_init = [(580, 490), (600, 510), (620, 530)]
yellow_player = Player(yellow_init, "Images/Player/yellow.png", "yellow")


green_init = [(580, 310),(600, 290),(620, 270)]
green_player = Player(green_init, "Images/Player/green.png", "green")

blue_init = [(420, 310), (400, 290), (380, 270)]
blue_player = Player(blue_init, "Images/Player/blue.png", "blue")

red_init = [(420, 490), (400, 510),(380, 530)]
red_player = Player(red_init, "Images/Player/red.png", "red" )
players = [red_player, blue_player, yellow_player, green_player]

yellow_bond = [(529, 636),(465, 639),(432, 696),(461, 754),(535, 755),(568, 697)]
green_bond = [(817, 331),(876, 362),(878, 431),(816, 468),(759, 434),(758, 367)]
blue_bond = [(432, 99),(465, 160),(536, 159),(568, 98),(533, 41),(463, 44)]
red_bond = [(180, 332),(239, 365),(241, 431),(177, 467),(122, 432),(123, 364)]

# making all bonds with their color
bonds = []
for mid in yellow_bond:
    new = Bond(mid, "yellow")
    bonds.append(new)
for mid in red_bond:
    new = Bond(mid, "red")
    bonds.append(new)
for mid in blue_bond:
    new = Bond(mid, "blue")
    bonds.append(new)
for mid in green_bond:
    new = Bond(mid, "green")
    bonds.append(new)



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
    for bond in bonds:
        bond.locate()
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

            for bond in bonds:
                if bond.distance_check(event.pos):
                    bond.toggle()

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