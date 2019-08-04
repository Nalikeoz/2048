from Board import Board

ROTATIONS_DIC = {
    "W": 1,
    "D": 2,
    "S": 3,
    "A": 0
}
END_GAME_COMMAND = 'END'
BOARD_SIZE = 4


class Game(object):
    def __init__(self):
        self.board = Board()
        self.playing = True

    def is_end_game(self):
        for line in self.board.board:
            for value in line:
                if value == 0:
                    return False
        return True

    def run_game(self):
        while self.playing and not self.is_end_game():
            print self.board
            command = raw_input('> ')
            if command.upper() in ROTATIONS_DIC:
                self.board.rotate_matrix_left(ROTATIONS_DIC[command.upper()])
                self.board.move_left()
                self.board.rotate_matrix_left(BOARD_SIZE - ROTATIONS_DIC[command.upper()])

            elif command.upper() == END_GAME_COMMAND:
                self.playing = False

            else:
                print 'Unknown command!'
        raw_input('Game Over!')


game = Game()
game.run_game()