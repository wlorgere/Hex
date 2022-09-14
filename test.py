import pygame

from AI.minmax import Minmax
from hex.board import Board
from hex.constants import HEIGHT, WIDTH
from hex.hexBoard import HexBoard
from main import get_row_col_from_mouse

def test1():
    row, col = 3, 3
    board = Board(row, col)
    player = "RED"
    ia = Minmax()
    print(ia.find_best_move(board, player))

FPS = 60

pygame.init()


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hex')

def test2():
    run = True
    game = HexBoard(window)

    clock = pygame.time.Clock()

    while run:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
            game.select(row, col)

        game.update()
        clock.tick(FPS)
    pygame.quit()
    
test1()
