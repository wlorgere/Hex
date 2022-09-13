import pygame
from .constants import BLACK, COLORS, WHITE, RED, BLUE, HEX_SIZE, ROW, COL
from .connections import Connections

#TODO put all neighbors in cache, so we don't have to recompute them everytime§

class Board:
    """
    A board of hex

    Attributes
    ----------
    board : matrix of int
        Represent the board of the current game. The state of each cell is
        represented by a tuple of integers, corresponding to the RGB
        representation of the color of the cell.
    row : int
        Number of rows
    col : int
        Number of columns
    connections : Connections
        A representation of the connections between cells, using trees.
    """
    def __init__(self, row, col):
        self.board = []
        self.row = row
        self.col = col
        self.create_board()
        self.connections = Connections(row, col)

    def __repr__(self):
        return self.board.__repr__()

    def create_board(self):
        """
        Initialize the board with all black cells.
        """
        self.board = [["BLACK" for _ in range(self.col)] for _ in range(self.row)]

    def move(self, row, col, turn):
        self.board[row][col] = turn
        self.union(row, col, turn)

    def union(self, row, col, turn):
        """
        Update the connections on the board by making union with the neighbours
        of the played cell.

        Parameters
        ----------
        row : int
            Row of the played cell
        col : int
            Column of the played cell
        """
        pos = row*COL + col

        #Change the color of the played cell in the trees
        self.connections.trees[pos]["color"] = turn
        #Find the neighbours of the played cell
        neighbours = self.neighbours(row, col)

        for x in neighbours:
            self.connections.union(x, pos)
    
    def neighbours(self, row, col):
        """
        Find the neighbours of a cell.

        Parameters
        ----------
        row : int
            The row of the cell
        col : int
            The column of the cell

        Returns
        -------
        set of tuples of int
            A set containing all the cells that are neighbours of the given cell
        """
        res = set()

        #Ajout des bords
        if row == 0:
            res.add(ROW*COL)
        if row == ROW-1:
            res.add(ROW*COL + 1)
        if col == 0:
            res.add(ROW*COL + 2)
        if col == COL-1:
            res.add(ROW*COL + 3)

        #Ajout des voisins
        for x2 in range(row-1, row+2):
            for y2 in range(col-1, col+2):
                if ((row != x2 or col != y2)
                    and (0 <= x2 < ROW)
                    and (0 <= y2 < COL)):
                    res.add(x2*COL + y2)

        return res


    def winner(self):
        """
        Find a winner in the current game, if there is any. Return None if there
        is no winner.

        Returns
        -------
        tuple of int
            The color of the winner
        """
        if self.connections.trees[COL*ROW]["parent"] == self.connections.trees[COL*ROW + 1]["parent"]:
            return "BLUE"
        if self.connections.trees[COL*ROW + 2]["parent"] == self.connections.trees[COL*ROW + 3]["parent"]:
            return "RED"
        return None

    def draw_hex(self, window):
        """
        Draw an empty board of hex.

        Parameters
        ----------
        window
            The window to display the game.
        """
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

    def draw_pieces(self, window):
        """
        Draw the pieces of the current game of hex.

        Parameters
        ----------
        window
            The window to display the game.
        """
        for row in range(self.row):
            for col in range(self.col):
                pygame.draw.rect(window, COLORS[self.board[row][col]], (((col+row/2+1)*HEX_SIZE), (row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE))
                pygame.draw.rect(window, WHITE, (((col+row/2+1)*HEX_SIZE), (row+1)*HEX_SIZE, HEX_SIZE, HEX_SIZE), 1)


    def draw(self, window):
        """
        Draw the board of the current game of hex.

        Parameters
        ----------
        window
            The window to display the game.
        """
        self.draw_hex(window)
        self.draw_pieces(window)