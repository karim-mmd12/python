import time


class Game():
    # board size
    B_S = 10
    nb_players = 0
    # player1 and player2
    players = []
    WALL = '###'
    # constructor of the class
    # board_size is 10x10

    # board size is by default 10
    def __init__(self, board_size=10):
        self.board_size = board_size
        # range(0,99)
        # i = 0, 1,2,3,4....99
        self.board = [' ' for i in range(self.board_size*self.board_size)]
        self.winner = None
        self.walls_count = 2

    @classmethod
    def print_board_with_numbers(cls):
        # for i in range(10)
        # for j in range(20, 30) j= '0','1',2,3,4,5....9
        # 10,11,12.....19
        # 20,21
        # number_board = [[0,1,2,3,....9],[10,11,12,13,14...19],[20,21,....29]...[90,91,92,....99]]
        number_board = [[str(j)
                         for j in range(i*cls.B_S, (i+1)*cls.B_S)] for i in range(cls.B_S)]
        for row in number_board:
            print(' | '.join([num.rjust(3) for num in row]))

    @classmethod
    def add_player(cls, player):
        cls.players.append(player)
        cls.nb_players = len(cls.players)

    def add_wall(self, position):
        self.board[position[0]] = Game.WALL

    def is_wall(self, position):
        return self.board[position[0]] == Game.WALL

    def empty_squares(self):
        # return true or false
        # board= ['###', 'p1', ' ', 'p2' ]
        return ' ' in self.board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def draw(self):
        count = 0
        print('   '.join([str(i).rjust(3) for i in range(10)]))
        for row in [self.board[i*self.board_size:(i+1) * self.board_size] for i in range(self.board_size)]:
            print(str(count) + ' . '.join([str(j).rjust(3) for j in row]))
            print('\n')
            count += 1

    def play(self):
        # board with numbers
        Game.print_board_with_numbers()
        # x_player is the p1 and y_player is the p2
        x_player, y_player = Game.players[0:2]
        player_name = 'P1'
        # check if still empty squares in board
        # ['p1','p2','###','###',]
        while self.empty_squares():
            if x_player.name == player_name:
                position = x_player.get_position(self)
            else:
                position = y_player.get_position(self)
            x_player.play(self, tuple(position)) if player_name == 'P1' else y_player.play(
                self, tuple(position))
            # tuple([95])
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
