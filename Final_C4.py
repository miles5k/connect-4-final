'''
Miles Ogrady
Connect Four 2 player game Final project
'''

row = 6
column = 7


#board 6x7
board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0] ]


#shows it in to columns and rows
def C4_board():
    for rows in range(0, row):
        for columnn in range(0, column):
        #takes out '[]' and ',' and end makes it so they're next to eachother     
            print(board[rows][columnn],end=' ')
        #puts the board in six rows    
        print("")
            


#drops the pieces onto the board the player selects 
def pieces(column, player):
    column = column - 1
    for rows in range(row-1,-1,-1):
        #if free spot on the board = 0 it will accept
        if board[rows][column]== 0: #puts number on board             
            board[rows][column]= player 
            break

turn = 0
turns = False

#loops turns as well and puts a 1 on the board for player 1 and a 2 on the board for player 2 
while not turns:
    
    if turn == 0:
        print("column selection")
        select = int(input("Player 1 select 1-7: "))
        pieces(select,1)
        C4_board()
        print("player 1 went row", select)

    else:
        print("column selection")
        select = int(input("Player 2 select 1-7: "))
        pieces(select,2)
        C4_board()
        print("player 2 went row", select)
        
    turn += 1
    turn = turn % 2


