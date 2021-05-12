import math


class Player():
    def __init__(self, game, name, starting_point):
        self.name = name
        self.start = starting_point
        self.position = starting_point

        print(f"{self.name}{self.start}")
        # when players created, they automatically added to the game
        game.add_player(self)

    @staticmethod
    def get_input_letter(player):
        valid_letter = False
        letter = None
        while not valid_letter:
            character = input(
                player.name + ' turn. Enter letter \"p\" for moving player or letter \"w\" for placing a wall: ')
            try:
                letter = character.strip().lower()
                if letter not in ['p', 'w']:
                    raise ValueError
                valid_letter = True
            except ValueError:
                print('Invalid letter. Try again.')
        return letter

    def play(self, game, position):
        # move or place a wall
        self.move(game, position) if self.letter == 'p' else self.place_wall(
            game, position)

    def place_wall(self, game, wall_position):
        if not game.is_wall(wall_position):
            game.add_wall(wall_position)

    def is_winner(self):
        winner = False
        if self.start[0] in range(90, 100):
            if self.name == 'P1' and self.position[0] in range(0, 10):
                winner = True
        if self.start[0] in range(0, 10):
            if self.name == 'P2' and self.position[0] in range(90, 100):
                winner = True
        return winner

    @staticmethod
    def not_valid_position(pos, game, letter, current_position=0):
        if letter == 'p':
            return pos not in game.available_moves() or math.fabs(current_position - pos) not in [1, 10]
        else:
            return pos not in game.available_moves()

    def get_position(self, game):
        valid_square = False
        pos = None
        letter = Player.get_input_letter(self)
        if letter == 'p':
            txt = ' turn. Input adjacent position (0-99). e.g 12 is row 1, col 2: '
        else:
            txt = ' turn. Input position (0-99). e.g 12 is row 1, col 2: '
        while not valid_square:
            square = input(
                self.name + txt)
            try:
                pos = int(square)
                current_position = self.position[0]
                if Player.not_valid_position(pos, game, letter, current_position):
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid position. Try again.')
        self.letter = letter
        return [pos]

    def move(self, game, new_position):
        if game.board[new_position[0]] == ' ':
            game.board[new_position[0]] = self.name
            old_pos = self.position
            game.board[old_pos[0]] = ' '
            self.position = new_position
            if self.is_winner():
                game.winner = self.name
