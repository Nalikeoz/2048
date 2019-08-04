import random
import numpy as np

SIZE = 4
FOUR_CHANCE = 10
TWO_CHANGE = 90


class Board(object):
    def __init__(self):
        self.board = np.zeros(shape=(SIZE, SIZE))  # [[0 for i in range(SIZE)] for j in range(SIZE)]
        for i in range(2):
            self.generate_number()

    def generate_number(self):
        random_i, random_j = self.get_random_cell()
        while self.board[random_i][random_j] != 0:
            random_i, random_j = self.get_random_cell()

        if random.randint(0, 100) < FOUR_CHANCE:
            self.board[random_i][random_j] = 4
        else:
            self.board[random_i][random_j] = 2

    @staticmethod
    def get_random_cell():
        random_i = random.randint(0, SIZE - 1)
        random_j = random.randint(0, SIZE - 1)
        return [random_i, random_j]

    @staticmethod
    def remove_zeroes(row):
        row = [value for value in row if value != 0]
        while len(row) != SIZE:
            row.append(0)
        return row

    def move_left(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(reversed(row)):
                row = self.remove_zeroes(row)
                if j + 1 != SIZE and row[j] == row[j + 1]:
                    row[j] += row[j + 1]
                    row[j + 1] = 0

            self.board[i] = row
        self.generate_number()

    def rotate_matrix_left(self, amount):
        self.board = np.rot90(self.board, amount)

    def __str__(self):
        board_str = ''
        for line in self.board:
            for value in line:
               board_str += '[' + str(int(value)) + ']  '
            board_str += '\n'
        return board_str


