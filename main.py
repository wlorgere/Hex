#TODO
# Afficher à qui est le tour actuel
# Créer IA avec deep learning
# Créer la méthode de calcul de "connectivité" d'un plateau


import pygame
from AI.alphaBeta import AlphaBeta
from AI.minmax import Minmax
from AI.transposition import Transposition
from hex.constants import FPS, WIDTH, HEIGHT, HEX_SIZE
from hex.game import Game
from time import time

pygame.init()

players = {"RED": "Transposition", "BLUE": "human"}

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hex')

def get_row_col_from_mouse(pos):
    """
    Convert the position where the mouse clicked to a number of row and column.

    Parameters
    ----------
    pos : [type]
        [description]

    Returns
    -------
    tuple of int
        Row and column where the mouse clicked
    """
    (x,y) = pos
    row = y // HEX_SIZE - 1
    col =  int((x-(row+2)*HEX_SIZE/2-1) // HEX_SIZE)
    print("clicked", row, col)
    return row, col

def main():
    run = True
    game = Game(window)
    clock = pygame.time.Clock()

    if "Minmax" in players.values():
        print("yay, AI")
        aiMinimax = Minmax()
    if "AlphaBeta" in players.values():
        print("yay, AI")
        aiAlphaBeta = AlphaBeta()
    if "Transposition" in players.values():
        print("yay, AI")
        aiTransposition = Transposition()
    

    game.update()
    while run:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        winner = game.winner()

        if winner != None:
            #TODO Showing the winner
            #TODO Proposing another game
            print("winner", winner)
            run = False
            break

        if players[game.turn] == "human":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        if players[game.turn] == "Minmax":
            print("AI turn")
            t1 = time()
            res = aiMinimax.find_best_move(game.board, game.turn)
            t2 = time()
            print(res)
            print("found in",t2-t1, "seconds")
            row, col = res
            game.select(row, col)

        if players[game.turn] == "AlphaBeta":
            print("AI turn")
            t1 = time()
            res = aiAlphaBeta.find_best_move(game.board, game.turn)
            t2 = time()
            print(res)
            print("found in",t2-t1, "seconds")
            row, col = res
            game.select(row, col)

        if players[game.turn] == "Transposition":
            print("AI turn")
            t1 = time()
            res = aiTransposition.find_best_move(game.board, game.turn)
            t2 = time()
            print(res)
            print("found in",t2-t1, "seconds")
            row, col = res
            game.select(row, col)


        game.update()
        clock.tick(FPS)
    pygame.quit()

if __name__=="__main__":
    main()
