import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

done = False
game_finish = False
game_lose = False

# Draw background
COLOR_WHITE = (200, 255, 255)
roger = pygame.image.load("mario.png")
square_image = pygame.image.load("square.png")
box_image = pygame.image.load("box.png")
gate_image = pygame.image.load("gate.png")
win_image = pygame.image.load("win.png")
lose_image = pygame.image.load("lose.png")

x = 100
y = 100

SQUARE_SIZE = 32


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def cal_next_position(self, dx, dy):
        return [self.x + dx, self.y + dy]


class Box:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def cal_next_position(self, dx, dy):
        return [self.x + dx, self.y + dy]


class Gate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def play_sound(file_name):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(0)

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(1, 1)
        self.box = Box(6,6)
        self.gate = Gate(7, 7)


    def move_player(self, dx, dy):
        [next_player_x, next_player_y] = self.player.cal_next_position(dx, dy)
        [next_box_x, next_box_y] = self.box.cal_next_position(dx, dy)
        if self.check_inside(next_player_x, next_player_y):
            if next_player_x == self.box.x and next_player_y == self.box.y:
                if self.check_inside(next_box_y, next_box_y):
                    self.box.move(dx, dy)
                    self.player.move(dx, dy)
                    play_sound("Laser_Shoot.wav")
            else:
                play_sound("Laser_Shoot.wav")
                self.player.move(dx, dy)

    def check_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def check_win(self):
        if self.box.x == self.gate.x and self.box.y == self.gate.y:
            return True
        return False

    def check_lose(self):
        if [self.box.x, self.box.y] == [0, 0] or [self.box.x, self.box.y] == [self.width - 1, 0] or [self.box.x,
                                                                                                     self.box.y] == [0,
                                                                                                                     self.height - 1]:
            return True
        return False


map = Map(10, 10)
# Draw images

while not done:

    key_arrow = None

    # Get events
    dx, dy = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1

                # x -= SQUARE_SIZE


                # Process game events
    if dx != 0 or dy != 0:
        map.move_player(dx, dy)
        if map.check_win():
            print("you win!")
            game_finish = True
        if map.check_lose():
            print("you lose")
            game_lose = True
            # Repaint!
    screen.fill(COLOR_WHITE)

    for y in range(map.height):
        for x in range(map.width):
            screen.blit(square_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))

    screen.blit(roger, (map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))
    screen.blit(box_image, (map.box.x * SQUARE_SIZE, map.box.y * SQUARE_SIZE))
    screen.blit(gate_image, (map.gate.x + SQUARE_SIZE, map.gate.y * SQUARE_SIZE))

    if game_finish == True:
        screen.blit(win_image, (100, 100))

    if game_lose == True:
        screen.blit(lose_image, (100, 100))
    pygame.display.flip()
