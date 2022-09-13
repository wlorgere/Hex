from copy import deepcopy
from AI.aiBasicClass import AIBasicClass
from hex.board import Board
class Minmax(AIBasicClass):
    def find_best_move(self, board: Board, turn):
        def recursion(board: Board, player, debug=False):
            winner = board.winner()

            if winner != None:
                return (1 if winner == player else -1, None)

            value = float("-inf")

            test = [[0 for _ in range(board.row)] for _ in range(board.col)]
            for i in range(board.row):
                for j in range(board.col):
                    if(board.board[i][j] == "BLACK"):
                        current_board = deepcopy(board)
                        current_board.move(i, j, player)
                        player = "BLUE" if player == "RED" else "RED"
                        eval, move  = recursion(current_board, player)
                        eval = - eval
                        test[i][j] = eval

                        if eval > value:
                            if debug:
                                print("change move", value, eval, i, j)
                            value = eval
                            move = i,j

            if debug:
                print("test", test)
                print("move", move)
            return eval, move
        
        eval, move = recursion(board, turn, True)


        return move

