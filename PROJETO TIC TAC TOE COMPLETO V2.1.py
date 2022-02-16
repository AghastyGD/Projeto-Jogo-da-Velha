#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output
def display_board (board):
    
    clear_output()
    print ('   |   |   ')
    print (' '+board[7]+' | ' +board[8]+' | '+board[9])
    print ('   |   |   ')
    print ('--------------')
    print ('   |   |   ')
    print (' '+board[4]+' | ' +board[5]+' | '+board[6])
    print ('   |   |   ')
    print ('--------------')
    print ('   |   |   ')
    print (' '+board[1]+' | ' +board[2]+' | '+board[3])
    print ('   |   |   ')


# In[ ]:


def player_input():
   
    
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Você quer ser X ou O?').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[ ]:


def place_marker(board, marker, position):
    board[position] = marker


# In[ ]:


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #Condição de Vitória pelo topo
    (board[4] == mark and board[5] == mark and board[6] == mark) or #Pelo Meio
    (board[1] == mark and board[2] == mark and board[3] == mark) or #Por Baixo
    (board[7] == mark and board[4] == mark and board[1] == mark) or #Pelo Lado Esquerdo
    (board[8] == mark and board[5] == mark and board[2] == mark) or #Pelo Centro
    (board[9] == mark and board[6] == mark and board[3] == mark) or #Pelo lado direito
    (board[7] == mark and board[5] == mark and board[3] == mark) or #Diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) #Diagonal


# In[ ]:


## NB: Esse código é opcional, ele serve apenas para retornar a condição dos Jogadores aleatoriarmente!
## Ex: Se o Player 1 escolher X, o Jogador Nr 2 automaticamente usará 'O' e se tornará o primeiro a jogar.

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[ ]:


def space_check(board, position):
    
    return board[position] == ' '


# In[ ]:


def space_check(board, position2):
    
    return board[position2] == ' '


# In[ ]:


def full_board_check(board):
    for i in range(0,10):
        if space_check(board, i):
            return False
        
    return True


# In[ ]:


def player_choice(board):
    position = ' '
    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Escolha sua jogada (1-9) JOGADOR NR 1 ')
    
    return int(position)


# In[ ]:


def player_choice2(board):
    position2 = ' '
    
    while position2 not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position2)):
        position2 = input('Escolha sua jogada (1-9) JOGADOR NR 2 ')
    
    return int(position2)


# In[ ]:


def replay():
    
    return input('Quer jogar novamente? "SIM" ou "NÃO"').lower().startswith('s')


# In[ ]:


print('Bem Vindo ao Jogo da Velha ')
nome1 = input('Digite o seu nome JOGADOR NR 1 ')
nome2 = input('Digite o seu nome JOGADOR NR 2 ')
              
while True:
    # Defina o jogo
    #pass
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+' começa!')
    
    game_on = True
    
    while game_on:
        #Vez do Jogador 1
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
        
        # Checa a vitória
        if win_check(board, player1_marker):
            display_board(board)
            print('Parabéns',nome1.upper(),'Você venceu!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 2'
                
        #Vez do Jogador 2
        if turn == 'Player 2':
            display_board(board)
            position = player_choice2(board)
            place_marker(board, player2_marker, position)
        
        # Checa a vitória
        if win_check(board, player2_marker):
            display_board(board)
            print('Parabéns',nome2.upper(),'Você venceu!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 1'
                
    if not replay():
        break


# In[ ]:




