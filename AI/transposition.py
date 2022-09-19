from copy import deepcopy
from AI.aiBasicClass import AIBasicClass
from hex.board import Board

from hex.constants import FPS, HEIGHT, WIDTH

class TranspositionTableEntry():
    def __init__(self, value, flag, nextMove):
        self.value = value
        self.flag = flag
        self.nextMove = nextMove

class Transposition(AIBasicClass):
    def __init__(self):
        self.transpositionTable = dict()

    def find_best_move(self, board: Board, turn):
        def recursion(board: Board, player, alpha, beta, debug=False):
            alphaOrig = alpha

            #Check in transposition table
            key = board.__repr__()
            if key in self.transpositionTable:
                if self.transpositionTable[key].flag == 'EXACT':
                    return self.transpositionTable[key].value, self.transpositionTable[key].nextMove
                elif self.transpositionTable[key].flag == 'LOWERBOUND':
                    alpha = max(alpha, self.transpositionTable[key].value)
                elif self.transpositionTable[key].flag == 'UPPERBOUND':
                    beta = max(beta, self.transpositionTable[key].value)

                if alpha >= beta:
                    return self.transpositionTable[key].value, self.transpositionTable[key].nextMove

            #Check winner
            winner = board.winner()
            if winner != None:
                return (-1, None)

            #Recursion
            value = float("-inf")
            nextPlayer = "BLUE" if player == "RED" else "RED"
            ttEntry = TranspositionTableEntry(value, 'EXACT', None)
            test = [[0 for _ in range(board.row)] for _ in range(board.col)]
            for i in range(board.row):
                for j in range(board.col):
                    if debug: 
                        print(i, j)
                    if(board.board[i][j] == "BLACK"):
                        currentBoard = deepcopy(board)
                        currentBoard.move(i, j, player)
                        eval, move  = recursion(currentBoard, nextPlayer, -beta, -alpha)
                        eval = -eval
                        test[i][j] = eval
                        if eval > value:
                            value = eval
                            nextMove = i,j
                        alpha = max(alpha, value)
                        if alpha > beta:
                            break
                if alpha > beta:
                    break

            #Save in transposition table
            ttEntry.value = value
            ttEntry.nextMove = nextMove
            if value <= alphaOrig:
                ttEntry.flag = "UPPERBOUND"
            elif value >= beta:
                ttEntry.flag = "LOWERBOUND"
            else:
                ttEntry.flag = "EXACT"
            self.transpositionTable[key] = ttEntry

            return value, nextMove
        
        eval, move = recursion(board, turn, float("-inf"), float("inf"), True)


        return move

