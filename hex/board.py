import pygame
from .constants import BLACK, WHITE, RED, BLUE, HEX_SIZE, ROW, COL
from .union import Union


class Board:
    def __init__(self, row, col):
        self.board = []
        self.row = row
        self.col = col
        self.create_board()
        self.graph = Union(row, col)

    def create_board(self):
        self.board = [[BLACK for _ in range(self.col)] for _ in range(self.row)]

    def draw_hex(self, window):
        window.fill(BLACK)

        # Cotés bleus
        for col in range(self.col+1):
            # Haut
            pygame.draw.rect(window, BLUE, ((col+1/2)*HEX_SIZE, 0, HEX_SIZE, HEX_SIZE))
            pygame.draw.rect(window, WHITE, ((col+1/2)*HEX_SIZE, 0, HEX_SIZE, HEX_SIZE), 1)

            # Bas
            pygame.draw.rect(window, BLUE, ((self.col/2 + col)*HEX_SIZE, (self.row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE))
            pygame.draw.rect(window, WHITE, ((self.col/2 + col)*HEX_SIZE, (self.row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE), 1)

        # Cotés rouges
        for row in range(self.row):
            # Gauche
            pygame.draw.rect(window, RED, (row/2 * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE))
            pygame.draw.rect(window, WHITE, (row/2 * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE),1)

            #Droite
            pygame.draw.rect(window, RED, ((self.col+1 + row/2) * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE))
            pygame.draw.rect(window, WHITE, ((self.col+1 + row/2) * HEX_SIZE, (row+1) * HEX_SIZE, HEX_SIZE, HEX_SIZE),1)

    def neighbours(self, row, col):
        res = set()

        #Ajout des bords
        if row == 1:
            res.add(ROW*COL)
        if row == ROW:
            res.add(ROW*COL + 1)
        if col == 1:
            res.add(ROW*COL + 2)
        if col == COL:
            res.add(ROW*COL + 3)

        #Ajout des voisins
        for x2 in range(row-1, row+2):
            for y2 in range(col-1, col+2):
                if ((row != x2 or col != y2)
                    and (0 < x2 <= ROW)
                    and (0 < y2 <= COL)):
                    res.add((x2-1)*COL + (y2-1))

        return res


    def winner(self):
        if self.graph.arbres[COL*ROW]["parent"] == self.graph.arbres[COL*ROW + 1]["parent"]:
            return BLUE
        if self.graph.arbres[COL*ROW + 2]["parent"] == self.graph.arbres[COL*ROW + 3]["parent"]:
            return RED
        return None

    def draw_pieces(self, window):
        for row in range(self.row):
            for col in range(self.col):
                pygame.draw.rect(window, self.board[row][col], (((col+row/2+1)*HEX_SIZE), (row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE))
                pygame.draw.rect(window, WHITE, (((col+row/2+1)*HEX_SIZE), (row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE), 1)


    def draw(self, window):
        self.draw_hex(window)
        self.draw_pieces(window)