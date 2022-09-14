import pygame
from hex.board import Board
from hex.constants import COL, GREEN, HEX_SIZE, ROW, WHITE


class HexBoard():
    def __init__(self, window):
        self.board = Board(ROW, COL)
        self.window = window
        self.neighbours = []

    def update(self):
        """
        Update the display of the game.
        """
        self.board.draw(self.window)
        self.drawNeighbours()
        pygame.display.update()

    def select(self, row, col):
        """
        Check if selected cell is free, and place a piece of the color of the
        player's turn on that cell.

        Parameters
        ----------
        row : int
            Row of the cell
        col : int
            Column of the cell
        """
        self.neighbours = self.board.neighboursXY(row, col)
        print("all neighbours", self.neighbours)

    def drawNeighbours(self):
        for neighbour in self.neighbours:
            if neighbour == ROW*COL:
                for col in range(COL+1):
                    pygame.draw.rect(self.window, GREEN, ((col+1/2)*HEX_SIZE, 0, HEX_SIZE, HEX_SIZE))
                    pygame.draw.rect(self.window, WHITE, ((col+1/2)*HEX_SIZE, 0, HEX_SIZE, HEX_SIZE), 1)
            elif neighbour == ROW*COL+1:
                for col in range(COL+1):
                    pygame.draw.rect(self.window, GREEN, ((COL/2 + col)*HEX_SIZE, (ROW+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE))
                    pygame.draw.rect(self.window, WHITE, ((COL/2 + col)*HEX_SIZE, (ROW+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE), 1)

            elif neighbour == ROW*COL+2:
                for row in range(ROW):
                    pygame.draw.rect(self.window, GREEN, (row/2 * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE))
                    pygame.draw.rect(self.window, WHITE, (row/2 * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE),1)

            elif neighbour == ROW*COL+3:
                for row in range(ROW):
                    pygame.draw.rect(self.window, GREEN, ((COL+1 + row/2) * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE))
                    pygame.draw.rect(self.window, WHITE, ((COL+1 + row/2) * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE),1)

            else:
                row, col = neighbour
                pygame.draw.rect(self.window, GREEN, (((col+row/2+1)*HEX_SIZE), (row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE))
                pygame.draw.rect(self.window, WHITE, (((col+row/2+1)*HEX_SIZE), (row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE), 1)








