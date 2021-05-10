from player import Player
import time


class Game():
    def __init__(self, board_size=10):
        self.board_size = board_size
        self.board = [' ' for i in range(self.board_size*self.board_size)]

    def print_board_with_numbers(self):
        number_board = [[str(j)
                         for j in range(i*self.board_size, (i+1)*self.board_size)] for i in range(self.board_size)]
        for row in number_board:
            print(' | '.join([num.rjust(3) for num in row]))

    def empty_squares(self):
        return ' ' in self.board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def draw(self):
        for row in [self.board[i*self.board_size:(i+1) * self.board_size] for i in range(self.board_size)]:
            print(' | '.join([str(j).rjust(3) for j in row]))

    def play(self, game, x_player, y_player):

        game.print_board_with_numbers()

        player_name = 'P1'
        # check if still empty squares in board
        while self.empty_squares():
            if x_player.name == player_name:
                position = x_player.get_position(self)
            else:
                position = y_player.get_position(self)
            x_player.move(self, tuple(position)) if player_name == 'P1' else y_player.move(
                self, tuple(position))
            print(f"{player_name} moves to position {position}")
            # draw board
            self.draw()
            # check winner
            # return player_name ends the loop and exits the game
            # switches player
            player_name = 'P2' if player_name == 'P1' else 'P1'
            time.sleep(.7)
        print('No body wins!')


if __name__ == '__main__':
    p1 = Player('P1', (95,))
    p2 = Player('P2', (5,))
    q = Game()
    q.play(q, p1, p2)
