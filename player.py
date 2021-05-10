class Player():
    def __init__(self, game, name, position):
        self.name = name
        self.start = position
        self.position = position

        print(f"{self.name}{self.start}")
        # when players created, they automatically added to the game
        game.add_player(self)

    def play(self):
        pass

    def place_wall(self, position):
        pass

    def is_winner(self):
        pass

    # return position if empty

    def get_position(self, game):
        valid_square = False
        pos = None
        while not valid_square:
            square = input(
                self.name + ' turn. Input adjacent position (0-99): ')
            try:
                pos = int(square)
                if pos not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid position. Try again.')
        return [pos]

    def move(self, game, new_position):
        if game.board[new_position[0]] == ' ':
            game.board[new_position[0]] = self.name
            old_pos = self.position
            game.board[old_pos[0]] = ' '
            self.position = new_position
            # if self.winner(position, player_name):
            #     self.current_winner = player_name
