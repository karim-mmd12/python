from player import Player


class Game():
    def __init__(self, board_size=10):
        self.board = [' ' for i in range(board_size*board_size)]

    @staticmethod
    def print_board_with_numbers():
        number_board = [['0'+str(j) if j < 10 else str(j) for j in range(i*10, (i+1)*10)]
                        for i in range(10)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def empty_squares(self):
        return ' '

    def draw(self):
        pass

    def play(self, p1, p2):

        Game.print_board_with_numbers()

        player_name = 'p2'
        # check if empty squares around player only-no walls or other player
        while self.empty_squares():
            if p1.name == player_name:
                position = p1.get_position()
            else:
                player_name = 'p2'
                position = p2.get_position()

            print(f"{player_name} moves to position {position}")
            self.draw()


if __name__ == '__main__':
    p1 = Player('p1', 95)
    p2 = Player('p2', 5)
    q = Game()
    q.play(p1, p2)
