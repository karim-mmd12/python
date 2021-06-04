from player import Player
import random


class AI(Player):
    def __init__(self, game, name, starting_point):
        super().__init__(game, name, starting_point)

    def get_position(self, game):
        # random generator that will give you a new valid position either for wall or for moving a player
        # wall = '###' board[' ', 'AI']
        self.position = random.randint(0, 99)
        print(self.position)
