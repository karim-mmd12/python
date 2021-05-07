from player import Player


class Quoridor():
    @classmethod
    def print_board_with_numbers(cls):
        pass


def play(game, p1, p2):

    Quoridor.print_board_with_numbers()

    player_name = 'p1'
    # check if empty squares around player only-no walls or other player
    while game.empty_squares():
        if player_name == 'p1':
            position = p1.move()
        else:
            position = p2.move()

        print(f"{player_name} moves to position {position}")
        game.draw()


if __name__ == '__main__':
    p1 = Player('p1')
    p2 = Player('p2')
    q = Quoridor()
    play(q, p1, p2)
