#TODO
# Ajouter la détection d'un gagnant
# Afficher à qui est le tour actuel
# Créer IA MinMax
# Créer IA avec deep learning
# Créer la méthode de calcul de "connectivité" d'un plateau
# Ajouter de l'audio


import pygame
from hex.constants import WIDTH, HEIGHT, BLUE, HEX_SIZE
from hex.game import Game

FPS = 60

pygame.init()

players = {"RED": "human", "BLUE": "human"}

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
    row = y // HEX_SIZE
    col =  int((x-(row-1)*HEX_SIZE/2-1) // HEX_SIZE)
    return row, col

def main():
    run = True
    game = Game(window)
    clock = pygame.time.Clock()

    while run:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        winner = game.winner()

        if winner != None:
            #TODO Showing the winner
            #TODO Proposing another game
            print(winner)
            run = False
        if players[game.turn] == "human":

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
        if players[game.turn] == "Minmax":
            pass

        game.update()
        clock.tick(FPS)
    pygame.quit()

main()
