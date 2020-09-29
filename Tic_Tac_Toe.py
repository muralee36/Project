#!/usr/bin/env python
# coding: utf-8

# In[9]:


# my 6th project
# TIC TAC TOE GAME

from IPython.display import clear_output

# function to display board

def display_board(my_list):
    clear_output()
    print('     |       | ')
    print(' '+my_list[7] +'   |   ' + my_list[8]+'   |  '+my_list[9])
    print('     |       | ')
    print('-'*19)
    print('     |       | ')
    print(' '+my_list[4] +'   |   ' + my_list[5]+'   |  '+my_list[6])
    print('     |       | ')
    print('-'*19)
    print('     |       | ')
    print(' '+my_list[1] +'   |   ' + my_list[2]+'   |  '+my_list[3])
    print('     |       | ')
    
# function to choose x or y

def player_choice():
    x=False
    while not x:
        choice=input('PLAYER 1 : DO YOU WANT TO PLAY AS X or O : ')
        if choice.upper() in ['X','O']:
            x=True
        else:
            print('ENTER VALID CHOICE')
    if choice.upper()=='X':
        return ['X','O']
    else:
        return ['O','X']
    
#function to get player location

def player_input():
    x=False
    while not x:
        no=input('ENTER YOUR LOCATION [1-9]: ')
        if no.isdigit() and no in ['1','2','3','4','5','6','7','8','9']:
            x=True
        else:
            print('ENTER VALID LOCATION  ')
    return int(no)

# function to check if location is vacant

def position_vacant(board,position):
    return board[position]==' '

# function to mark position

def player_marker(board,position,player):
    board[position]=player

# function to check if player won

def win_check(board,player):
    return ((board[1]==board[2]==board[3]==player) or 
            (board[4]==board[5]==board[6]==player) or 
            (board[7]==board[8]==board[9]==player) or
            (board[7]==board[5]==board[3]==player) or
            (board[9]==board[5]==board[1]==player) or
            (board[7]==board[4]==board[1]==player) or
            (board[8]==board[5]==board[2]==player) or
            (board[9]==board[6]==board[3]==player))

# function to check if board is empty

def full_check(board):
    return not ' ' in board

# function to check if player wants to replay

def replay():
    x=False
    while not x:
        choice=input('DO YOU WANT TO REPLAY [Y/N] : ')
        if choice.upper() in ['Y','N']:
            x=True
        else:
            print('ENTER VALID CHOICE !')
    if choice.upper()=='Y':
        return True
    else:
        return False

#function to select who goes first

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

print('WELCOME TO TIC TAC TOE ')
while True:
    # board with empty strings from loc 1-9
    board=['invalid',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    #player selects his/her marker
    player1_mark,player2_mark=player_choice()
    #choose whose going first
    turn=choose_first()
    choice=input('ARE YOU READY ? : ')
    
    if choice.upper()[0]=='Y':
        game_on=True
    else:
        game_on=False
    #game starts
    while game_on:
        #player 1 gameplay
        if turn=='Player 1':
            display_board(board)
            x=False
            while not x:
                marker=player_input()
                if position_vacant(board,marker):
                    player_marker(board,marker,player1_mark)
                    x=True
                else:
                    print('LOCATION NOT VACANT')
                    
            if win_check(board,player1_mark):
                display_board(board)
                print('CONGRATULATIONS PLAYER 1 WINS !!!!!')
                game_on=False
                break
            elif full_check(board):
                display_board(board)
                print('OOH!! THE GAME IS DRAW')
                game_on=False
                break
            else:
                turn='Player 2'
        else:
            display_board(board)
            x=False
            while not x:
                marker=player_input()
                if position_vacant(board,marker):
                    player_marker(board,marker,player2_mark)
                    x=True
                else:
                    print('LOCATION NOT VACANT')
                    
            if win_check(board,player2_mark):
                display_board(board)
                print('CONGRATULATIONS PLAYER 2 WINS !!!!!')
                game_on=False
                break
            elif full_check(board):
                display_board(board)
                print('OOH!! THE GAME IS DRAW')
                game_on=False
                break
            else:
                turn='Player 1'
    if not replay():
        break
            


# In[ ]:




