from player import Player
import time


class Game():
    B_S = 10
    nb_players = 0
    players = []

    def __init__(self, board_size=10):
        self.board_size = board_size
        self.board = [' ' for i in range(self.board_size*self.board_size)]
        self.winner = None

    @classmethod
    def print_board_with_numbers(cls):
        number_board = [[str(j)
                         for j in range(i*cls.B_S, (i+1)*cls.B_S)] for i in range(cls.B_S)]
        for row in number_board:
            print(' | '.join([num.rjust(3) for num in row]))

    @classmethod
    def add_player(cls, player):
        cls.players.append(player)
        cls.nb_players = len(cls.players)

    def add_wall(self, position):
        pass

    def is_wall(self, position):
        pass

    def empty_squares(self):
        return ' ' in self.board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def draw(self):
        for row in [self.board[i*self.board_size:(i+1) * self.board_size] for i in range(self.board_size)]:
            print(' | '.join([str(j).rjust(3) for j in row]))

    def play(self):
        Game.print_board_with_numbers()
        x_player, y_player = Game.players[0:3]
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
            if self.winner:
                print(f'{self.winner} wins!')
                return True
            # return player_name ends the loop and exits the game

            # switches players
            player_name = 'P2' if player_name == 'P1' else 'P1'
            time.sleep(.7)
        print('No body wins!')


if __name__ == '__main__':
    game = Game()
    Player(game, 'P1', (95,))
    Player(game, 'P2', (5,))
    game.play()
