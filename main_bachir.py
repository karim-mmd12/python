# we need to use the Game class, we have to import the class from the file name game.py
from game import Game
from player import Player
from ai import AI

# name variable set to main when the file executed from the terminal
if __name__ == '__main__':
    # object instance
    game = Game()
    # we created 2 players called p1 and p2. player1 at pos 95 and player2 at pos 5.
    # x_player is the p1 and y_player is the p2
    Player(game, 'P1', (95,))
    Player(game, 'P2', (5,))
    # AI(game, 'AI', (5,))
    # board: list of length 100.
    game.board[95] = 'P1'
    game.board[5] = 'P2'
    # game.board[5] = 'AI'
    # here we start the game
    game.play()
