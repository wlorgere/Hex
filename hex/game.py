import pygame
from .board import Board
from .constants import ROW, COL

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
        self.turn = "RED"
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
        in_board = (0 <= row <= ROW-1) and (0 <= col <= COL-1)
        if (in_board
                and self.board.board[row][col] == "BLACK"):
            #Place a piece on the board
            self.board.move(row,col,self.turn)
            
            #Change turn
            self.change_turn()
        else:
            #TODO print a message to tell the player to chose a correct cell
            pass


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
        if self.turn == "RED":
            self.turn = "BLUE"
        else:
            self.turn = "RED"