"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    elif terminal(board):
        return X
    else:
        count_x=0
        count_o=0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==X:
                    count_x+=1
                elif board[i][j]==O:
                    count_o+=1
        if count_x>count_o:
            return O
        else:
            return X                
            

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts=set()
    if board==initial_state():
        for i in range(len(board)):
            for j in range (len(board[i])):
                acts.add((i,j))
        return acts
    
    elif terminal(board):
        return None
    
    else:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==EMPTY:
                    acts.add((i,j))
        return acts            
        


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print(board[action[0]][action[1]])
    # print(board)
    # print(action)
    # try:
    #     print(board)
        
    # except TypeError:
    #     print('board faregh')
    
    # try:
    #     print(action)
    # except TypeError:
    #     print('action fargha')  
    
    # try:
    #     print(action[0])
    # except TypeError:
    #     print('pb f action 0') 
        
    # try:
    #     print(action[1])
    # except TypeError:
    #     print('pb f action 1')                
    
    resultat=copy.deepcopy(board)          
        
            
    # current=player(board)
    resultat[action[0]][action[1]]=player(board)
    return resultat


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0]==X and board[0][1]==X and board[0][2]==X) or (board[1][0]==X and board[1][1]==X and board[1][2]==X) or (board[2][0]==X and board[2][1]==X and board[2][2]==X) or (board[0][0]==X and board[1][0]==X and board[2][0]==X) or (board[0][1]==X and board[1][1]==X and board[2][1]==X) or (board[0][2]==X and board[1][2]==X and board[2][2]==X) or (board[0][0]==X and board[1][1]==X and board[2][2]==X) or (board[2][0]==X and board[1][1]==X and board[0][2]==X):
        return X
    elif (board[0][0]==O and board[0][1]==O and board[0][2]==O) or (board[1][0]==O and board[1][1]==O and board[1][2]==O) or (board[2][0]==O and board[2][1]==O and board[2][2]==O) or (board[0][0]==O and board[1][0]==O and board[2][0]==O) or (board[0][1]==O and board[1][1]==O and board[2][1]==O) or (board[0][2]==O and board[1][2]==O and board[2][2]==O) or (board[0][0]==O and board[1][1]==O and board[2][2]==O) or (board[2][0]==O and board[1][1]==O and board[0][2]==O):
        return O
    else:
        return None
            
         
            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptyset=set()
    if winner(board)!=None:
        return True
    else:
        for i in range(len(board)):
          for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                emptyset.add(board[i][j])
        if len(emptyset)==0:
            return True
        else:
            return False      
        
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

def minvalue(state):
    v=math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v=min(v,maxvalue(result(state, action)))
    return v

def maxvalue(state):
    v=-math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v=max(v, minvalue(result(state, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board)==X:
            act=max(actions(board), key= lambda action: minvalue(result(board, action)))
            return act
        
        if player(board)==O:
            act=min(actions(board), key= lambda action: maxvalue(result(board, action)))
            return act
            
            
            
        
        
    
