
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def playerinput():
    marker = ''
    while not (marker == 'X' or marker =='O'):
        marker = input('Player 1 : Choose X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

playerinput()

def place_marker(board , marker ,position):
    board[position]= marker 

place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board,mark):
    return (    (board[7] == mark and board[8] == mark and board[9] == mark) or 
                (board[4] == mark and board[5] == mark and board[6] == mark) or 
                (board[1] == mark and board[2] == mark and board[3] == mark) or 
                (board[7] == mark and board[4] == mark and board[1] == mark) or 
                (board[8] == mark and board[5] == mark and board[2] == mark) or 
                (board[9] == mark and board[6] == mark and board[3] == mark) or 
                (board[7] == mark and board[5] == mark and board[3] == mark) or 
                (board[9] == mark and board[5] == mark and board[1] == mark)    )

display_board(test_board)
win_check(test_board,'X')

import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def spacecheck(board,position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        if spacecheck(board,i):
            return False
    return True

def player_choice(board):
    position = 0 
    while position not in [1,2,3,4,5,6,7,8,9] or not spacecheck(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position

def playagain():
    input('Play again? Yes or NO')
    return choice == 'Yes'
