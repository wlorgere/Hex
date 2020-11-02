import pygame
from .board import Board
from .constants import ROW, COL, RED, BLACK, BLUE

class Game:
    def __init__(self, window):
        self.board = Board(ROW, COL)
        self.turn = RED
        self.window = window

    def update(self):
        self.board.draw(self.window)
        pygame.display.update()

    def select(self, row, col):
        in_board = (1 <= row <= ROW) and (1 <= col <= COL)
        if (in_board
                and self.board.board[row-1][col-1] == BLACK):
            self.board.board[row-1][col-1] = self.turn
            self.union(row, col)
            self.change_turn()

    def union(self, row, col):
        pos = (row-1)*COL + (col-1)
        self.board.graph.arbres[pos]["color"] = self.turn
        neighbours = self.board.neighbours(row, col)
        for x in neighbours:
            self.board.graph.union(x, pos)

    def winner(self):
        return self.board.winner()


    def change_turn(self):
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED