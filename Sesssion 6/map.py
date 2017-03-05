from player import Player


class Map:
    def __init__(self, width, height):
        self.player  = Player(0,0)
        self.width   = width
        self.height  = height

    def print(self):
        for j in range(self.width):
            for i in range(self.height):
                if i == self.player.x and j == self.player.y:
                    print("P ", end="")
                else:
                    print("- ", end="")
            print()

    def move_player(self, dx, dy):
        self.player.move(dx, dy)

    def process_input(self, move):  # direction = W, S, A, D
        direction = move.upper()
        if direction == "W":
            dx , dy = 0,-1
        elif direction == "S":
            dx, dy = 0,1
        elif direction == "A":
            dx, dy = -1 , 0
        elif direction == "D":
            dx, dy = 1,0

        self.move_player(dx, dy)

    def loop(self):
        while True:
            move = input("Your move?: ")
            self.process_input(move)
            self.print()



map = Map(8, 8)
map.loop()