from game import Game
from player import Player

if __name__ == '__main__':
    game = Game()
    Player(game, 'P1', (95,))
    Player(game, 'P2', (5,))
    game.board[95] = 'P1'
    game.board[5] = 'P2'
    game.play()
