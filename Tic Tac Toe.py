import os
from random import randint
def display_board(board):
    os.system("cls")
    print('   |   |  ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('---|---|---')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('---|---|---')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   | ')

def player_input():
    global player1
    global computer
    f=True
    while(f):
        player1 = input("Player 1: Please pick a marker 'X' or 'O' : ")
        player1=player1.upper()
        if player1=='X':
            computer='O'
            print('Player 1 is X\nComputer is O')
            print('Player 1 will go first\n')
            f=False
        elif player1=='O':
            computer='X'
            print('Player 1 is O\nComputer is X')
            print('Computer will go first\n')
            f=False
        else:
            print('You have entered the wrong value/nPlease try again!')

def computer_choice(board):
    c=True
    while(c):
        temp= randint(1,9)
        
        if space_check(board,temp):
            position=temp
            c=False
    return position

def place_marker(board, marker, position):
    
    board[position]=marker
def win_check(board, mark):
    mark=mark.upper()
    if mark=='X':
        if (board[1]=='X' and board[2]=='X' and board[3]=='X') or (board[4]=='X' and board[5]=='X' and board[6]=='X') or (board[7]=='X' and board[8]=='X' and board[9]=='X') or (board[1]=='X' and board[5]=='X' and board[9]=='X') or (board[3]=='X' and board[5]=='X' and board[7]=='X') or (board[1]=='X' and board[4]=='X' and board[7]=='X') or (board[2]=='X' and board[5]=='X' and board[8]=='X') or (board[3]=='X' and board[6]=='X' and board[9]=='X'):
            
            return 'X'     
    else:
        if (board[1]=='O' and board[2]=='O' and board[3]=='O') or (board[4]=='O' and board[5]=='O' and board[6]=='O') or(board[7]=='O' and board[8]=='O' and board[9]=='O') or (board[1]=='O' and board[5]=='O' and board[9]=='O') or (board[3]=='O' and board[5]=='O' and board[7]=='O') or (board[1]=='O' and board[4]=='O' and board[7]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O') or (board[3]=='O' and board[6]=='O' and board[9]=='O'):
            return 'O' 
    return True   

def space_check(board, position): 
    if board[position] == ' ':
        return True
    else:
        return False
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    c=True
    while(c):
        temp=int(input('Please choose your position from (1 to 9)'))    
        if space_check(board,temp):
            position=temp
            c=False
        else:
            print('Position occupied please try different value')
    return position

def replay():
    while(True):
        val=input('Type Yes to play again and NO to exit : ')
        if val.lower()=='yes':
            test_board = ['#','1','2','3','4','5','6','7','8','9']
            display_board(test_board)
            return True
        elif val.lower()=='no':
            return False

#main logic
test_board = ['#','1','2','3','4','5','6','7','8','9']
display_board(test_board)
print('Welcome to Tic Tac Toe!')
player1=''
computer=''
while(True):
    player_input()
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    g=input('Hit Enter to start playing')
        
    display_board(board)
    while (True):
        if player1 == 'X':
            pos=player_choice(board)
        else:
            pos=computer_choice(board) 
        place_marker(board,'X',pos)
        display_board(board)
        k=win_check(board,'X')
        if k=='X' or k=='O':
            if (player1=='X' and k=='X') or (player1=='O' and k=='O'):
                print('Player 1 won the game!\n\n')
            elif (computer=='X' and k=='X') or (computer=='O' and k=='O'):
                print('Computer won the game!\n\n')
            break
        if full_board_check(board) :
            print('Match is DRAW')
            break
        if player1 == 'X':
            pos=computer_choice(board)
        else:
            pos=player_choice(board)
        place_marker(board,'O',pos)
        display_board(board)
        k=win_check(board,'O')
        if k=='X' or k=='O':
            if (player1=='X' and k=='X') or (player1=='O' and k=='O'):
                print('Player 1 won the game!\n\n')
            elif (computer=='X' and k=='X') or (computer=='O' and k=='O'):
                print('Computer won the game!\n\n')
            break
        if full_board_check(board) :
            print('Match is DRAW')
            break
    if not replay():
        break
