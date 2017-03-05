class Player:
    def __init__(self,x,y):   #constructor
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def move_to(self, x, y):
        self.x = x
        self.y = y
    def calc_next(self, dx, dy):
        return [self.x +dx, self.y+dy]

# player = Player(3, 5)  # player.x = 3 and player.y = 2
#
# player.print()
# player.move(1, 0)
# player.print()
# player.move_to(6, 9)
# player.print()
# print(player.calc_next(1, 4))
# player.print()