# we need to use the Game class, we have to import the class from the file name game.py
from game import Game
from player import Player

if __name__ == '__main__':
    # object instance
    game = Game()
    # we created 2 players called p1 and p2. player1 at pos 95 and player2 at pos 5.
    Player(game, 'P1', (95,))
    Player(game, 'P2', (5,))
    # board: list of length 100.
    game.board[95] = 'P1'
    game.board[5] = 'P2'
    # here we start the game
    game.play()
