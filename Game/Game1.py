import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

done = False

# Draw background
COLOR_WHILE = (255,255,255)
roger = pygame.image.load("mario.png")
square_image = pygame.image.load("square.png")

x = 100
y = 100

SQUARE_SIZE = 32

class Player:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def cal_next_position(self, dx, dy):
        return [self.x + dx, self.y + dy]

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(1,1)

    def move_player(self, dx, dy):
        [next_player_x, next_player_y] = self.player.cal_next_position(dx, dy)
        if self.check_inside(next_player_x, next_player_y):
            self.player.move(dx, dy)

    def check_inside(self, x, y):
        return 0 <= x < self.width and 0<= y < self.height

map = Map(5,5)
# Draw images

while not done:

    key_arrow = None


    # Get events
    dx, dy = 0 , 0
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
    if dx != 0  or dy != 0:
        map.move_player(dx, dy)
     # Repaint!
    screen.fill(COLOR_WHILE)

    for y in range (map.height):
        for x in range(map.width):
            screen.blit(square_image,(x * SQUARE_SIZE, y * SQUARE_SIZE) )

    screen.blit(roger, (map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))


    pygame.display.flip()