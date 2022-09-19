from copy import deepcopy
from AI.aiBasicClass import AIBasicClass
from hex.board import Board
import pygame

from hex.constants import FPS, HEIGHT, WIDTH
class Minmax(AIBasicClass):
    def find_best_move(self, board: Board, turn, window, clock):
        def recursion(board: Board, player, debug=False):
            winner = board.winner()

            if winner != None:
                return (-1, None)

            value = float("-inf")
            nextPlayer = "BLUE" if player == "RED" else "RED"

            test = [[0 for _ in range(board.row)] for _ in range(board.col)]
            for i in range(board.row):
                for j in range(board.col):
                    if (i,j) == (1,1) and debug:
                         print("case milieu")
                    if(board.board[i][j] == "BLACK"):
                        currentBoard = deepcopy(board)
                        currentBoard.move(i, j, player)
                        eval, move  = recursion(currentBoard, nextPlayer)
                        eval = -eval
                        test[i][j] = eval
                        if eval > value:
                            if debug:
                                print("change move", value, eval, i, j)
                            value = eval
                            nextMove = i,j


            if debug:
                print("test", test)
                print("move", nextMove)
            return value, nextMove
        
        eval, move = recursion(board, turn, True)


        return move

