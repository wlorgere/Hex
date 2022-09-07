import pygame
from .board import Board
from .constants import ROW, COL, RED, BLACK, BLUE

class Game:
    """
    A game of Hex

    Attributes
    ----------
    board : Board
        A representation of the board of the current game.
    turn : tuple of integers
        The color of the player's turn.
    window
        The window to display the game.
    """

    def __init__(self, window):
        self.board = Board(ROW, COL)
        self.turn = RED
        self.window = window

    def update(self):
        """
        Update the display of the game.
        """
        self.board.draw(self.window)
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
        #Check if the selected cell is inside the board
        in_board = (1 <= row <= ROW) and (1 <= col <= COL)
        if (in_board
                and self.board.board[row-1][col-1] == BLACK):
            #Place a piece on the board
            self.board.board[row-1][col-1] = self.turn
            #Update the connections on the board
            self.union(row, col)
            #Change turn
            self.change_turn()
        else:
            #TODO print a message to tell the player to chose a correct cell
            pass


    def union(self, row, col):
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
        pos = (row-1)*COL + (col-1)

        #Change the color of the played cell in the trees
        self.board.connections.trees[pos]["color"] = self.turn
        #Find the neighbours of the played cell
        neighbours = self.board.neighbours(row, col)

        for x in neighbours:
            self.board.connections.union(x, pos)

    def winner(self):
        """
        Find the winner of the game if there is any, otherwise return None.

        Returns
        -------
        tuple of int
            Winner of the game
        """

        
        return self.board.winner()


    def change_turn(self):
        """
        Change the player's turn.
        """
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED