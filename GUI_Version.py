#----------------------------------------------Algorithm------------------------------------------
import random
anyindex = random.randint(0,6)
board = [
    [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ],
    [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ],
    [
        [1, 0, 0, 4, 8, 9, 0, 0, 6],
        [7, 3, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 1, 2, 9, 5],
        [0, 0, 7, 1, 2, 0, 6, 0, 0],
        [5, 0, 0, 7, 0, 3, 0, 0, 8],
        [0, 0, 6, 0, 9, 5, 7, 0, 0],
        [9, 1, 4, 6, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 7],
        [8, 0, 0, 5, 1, 2, 0, 0, 4]
    ],
    [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ],
    [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ],
    [
        [2, 0, 0, 3, 0, 0, 0, 0, 0],
        [8, 0, 4, 0, 6, 2, 0, 0, 3],
        [0, 1, 3, 8, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 3, 9, 0],
        [5, 0, 7, 0, 0, 0, 6, 2, 1],
        [0, 3, 2, 0, 0, 6, 0, 0, 0],
        [0, 2, 0, 0, 0, 9, 1, 4, 0],
        [6, 0, 1, 2, 5, 0, 8, 0, 9],
        [0, 0, 0, 0, 0, 1, 0, 0, 2]
    ],
    [
        [0, 0, 0, 3, 8, 0, 0, 9, 2],
        [0, 0, 0, 6, 0, 0, 8, 0, 0],
        [0, 2, 0, 0, 0, 5, 0, 0, 0],
        [9, 0, 1, 0, 0, 0, 0, 8, 0],
        [0, 8, 2, 0, 0, 0, 1, 6, 0],
        [0, 6, 0, 0, 0, 0, 7, 0, 5],
        [0, 0, 0, 9, 0, 0, 0, 5, 0],
        [0, 0, 5, 0, 0, 4, 0, 0, 0],
        [6, 1, 0, 0, 7, 8, 0, 0, 0]
    ]
]
#Solvedboard will be changed after algo is run
Solvedboard = [
    [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ],
    [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ],
    [
        [1, 0, 0, 4, 8, 9, 0, 0, 6],
        [7, 3, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 1, 2, 9, 5],
        [0, 0, 7, 1, 2, 0, 6, 0, 0],
        [5, 0, 0, 7, 0, 3, 0, 0, 8],
        [0, 0, 6, 0, 9, 5, 7, 0, 0],
        [9, 1, 4, 6, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 7],
        [8, 0, 0, 5, 1, 2, 0, 0, 4]
    ],
    [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ],
    [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ],
    [
        [2, 0, 0, 3, 0, 0, 0, 0, 0],
        [8, 0, 4, 0, 6, 2, 0, 0, 3],
        [0, 1, 3, 8, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 2, 0, 3, 9, 0],
        [5, 0, 7, 0, 0, 0, 6, 2, 1],
        [0, 3, 2, 0, 0, 6, 0, 0, 0],
        [0, 2, 0, 0, 0, 9, 1, 4, 0],
        [6, 0, 1, 2, 5, 0, 8, 0, 9],
        [0, 0, 0, 0, 0, 1, 0, 0, 2]
    ],
    [
        [0, 0, 0, 3, 8, 0, 0, 9, 2],
        [0, 0, 0, 6, 0, 0, 8, 0, 0],
        [0, 2, 0, 0, 0, 5, 0, 0, 0],
        [9, 0, 1, 0, 0, 0, 0, 8, 0],
        [0, 8, 2, 0, 0, 0, 1, 6, 0],
        [0, 6, 0, 0, 0, 0, 7, 0, 5],
        [0, 0, 0, 9, 0, 0, 0, 5, 0],
        [0, 0, 5, 0, 0, 4, 0, 0, 0],
        [6, 1, 0, 0, 7, 8, 0, 0, 0]
    ]
]

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r,c)
    return None       

def print_board(board):
    for r in range(9):
        if r%3 == 0 and r!=0:
                print("---------------------------------")
        for c in range(9):
            if c%3 == 0 and c != 0:
                print(" |  ", end = "")
            print(str(board[r][c]) + "  " , end = "")
        print()

def valid(board, num, pos):

    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_X = pos[1] // 3   
    box_Y = pos[0] // 3   

    for r in range(box_Y*3, box_Y*3 + 3):
        for c in range(box_X*3, box_X*3 + 3):
            if board[r][c] == num and pos != (r, c):
                return False
    return True

def Solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):        
        if valid(board, i, (row,column)):
            board[row][column] = i
            
            if Solve(board):
                return True
            
            board[row][column] = 0
    return False

Solve(Solvedboard[anyindex])

#------------------------------------------------------GUI Code---------------------------------------------------

import pygame, sys
from pygame.locals import *

#Initialize the game
pygame.init()

# Global variables to set the size of the grid
WINDOWMULTIPLIER = 5 
WINDOWSIZE = 81

WINDOWWIDTH = WINDOWMULTIPLIER*WINDOWSIZE
WINDOWHEIGHT = WINDOWMULTIPLIER*WINDOWSIZE

SQUARESIZE = WINDOWWIDTH//3
CELLSIZE = SQUARESIZE //3

Mouse_state = False
ro = 1
co = 1

#Font for displaying numbers
font = pygame.font.Font('freesansbold.ttf', CELLSIZE-5)

#Number of frames per second
FPS = 10
# Set up the colours
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
LIGHTGRAY = (200, 200, 200)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
pygame.display.set_caption("Sudoku Solver by Aihab")
icon = pygame.image.load("sudoku.png")
pygame.display.set_icon(icon)

def drawGrid():
     ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0,y), (WINDOWWIDTH, y))
    
    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, SQUARESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH, y))

    return None

def show_number(number, r, c):
    lol = number
    num = font.render(str(lol), True, (0, 0, 0))
    DISPLAYSURF.blit(num, (c*CELLSIZE+11, r*CELLSIZE+5))

def main():
    global DISPLAYSURF, ro, Mouse_state, co

    while True: #main game loop
        DISPLAYSURF.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()      #(x,y)
        click = pygame.mouse.get_pressed()  #(Left Click, Scroll Button, Right Click)

        #Taking inputs from player
        if click[0] == 1:
                Mouse_state = True
                ro = mouse[1]//CELLSIZE
                co = mouse[0]//CELLSIZE
        if Mouse_state is True:        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if Solvedboard[anyindex][ro][co] == 1:
                        board[anyindex][ro][co] = 1
                    else:
                        DISPLAYSURF.blit(font.render(str(1), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                                 
                if event.key == pygame.K_2:
                    if Solvedboard[anyindex][ro][co] == 2:
                        board[anyindex][ro][co] = 2
                    else:
                        DISPLAYSURF.blit(font.render(str(2), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                        
                if event.key == pygame.K_3:
                    if Solvedboard[anyindex][ro][co] == 3:
                        board[anyindex][ro][co] = 3
                    else:
                        DISPLAYSURF.blit(font.render(str(3), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                        
                if event.key == pygame.K_4:
                    if Solvedboard[anyindex][ro][co] == 4:
                        board[anyindex][ro][co] = 4
                    else:
                        DISPLAYSURF.blit(font.render(str(4), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                        
                if event.key == pygame.K_5:
                    if Solvedboard[anyindex][ro][co] == 5:
                        board[anyindex][ro][co] = 5
                    else:
                        DISPLAYSURF.blit(font.render(str(5), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                        
                if event.key == pygame.K_6:
                    if Solvedboard[anyindex][ro][co] == 6:
                        board[anyindex][ro][co] = 6
                    else:
                        DISPLAYSURF.blit(font.render(str(6), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                        
                if event.key == pygame.K_7:
                    if Solvedboard[anyindex][ro][co] == 7:
                        board[anyindex][ro][co] = 7
                    else:
                        DISPLAYSURF.blit(font.render(str(7), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                       
                if event.key == pygame.K_8:
                    if Solvedboard[anyindex][ro][co] == 8:
                        board[anyindex][ro][co] = 8
                    else:
                        DISPLAYSURF.blit(font.render(str(8), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                        
                if event.key == pygame.K_9:
                    if Solvedboard[anyindex][ro][co] == 9:
                        board[anyindex][ro][co] = 9
                    else:
                        DISPLAYSURF.blit(font.render(str(9), True, (255, 0, 0)), (co*CELLSIZE+11, ro*CELLSIZE+5))
                        
                Mouse_state = False

        #Solving all at once
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(9):
                    for j in range(9):
                        board[anyindex][i][j] = Solvedboard[anyindex][i][j]
            
        for r in range(9):
            for c in range(9):
                number = board[anyindex][r][c]
                if number != 0:
                    show_number(number, r, c)

        
        drawGrid()
        pygame.display.update()

main()