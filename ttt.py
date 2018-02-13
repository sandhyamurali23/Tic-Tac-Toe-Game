
#MINMAX AND ALPHA BETA PRUNING ALGORITHM: REFERENCE from geeksforgeeks


# ttt.py
# Plays Tic Tac Toe Game and selects 
# 
# 
#
# Author: Sandhya Murali,(sm2290@g.rit.edu)



DIMENSION=3  #Specifies dimension of the board 
board = [['~'] * DIMENSION for i in range(DIMENSION)] #initializing board
count_nodes=0  #count nodes of the tree for each move


def displayboard(board):
    
    """
     displays the current state of the board
     :param board-> current state of the board 
    """
        
    for row in board:
        for item in row:
            print(item, end=" ")
        print()
    return board


def movesLeft(board):
    
    """
      checks if moves are left on the current state of the board
     :param board: current state of the board  
     :return: True if moves are left and False if no moves are left
    """

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if board[i][j]=='~': #checks for empty space on board
                return True

    return False


def check_winner(board):
    
    """
      checks the winner of the game. 
     :param board-> current state of the board  
     :return : -1 if X is winner, 1 if 0 wins and 0 if its a draw   
    """
    
    #checks for major diagonal
    major_diag=board[0][0]  
    flag=0

    for row in range(DIMENSION):
        if board[row][row]==major_diag:
            flag=1
        else:
            flag=0
            break

    if flag==1:
        if major_diag=='0':
            return 1

        elif major_diag=='X':
            return -1

    
    #checks for minor diagonal
    minor_diag=board[0][DIMENSION-1]
    flag=0
    col=DIMENSION-1
    for row in range(DIMENSION):
        if board[row][col]==minor_diag:
            flag=1
            col=col-1
            if col<0:
                break
        else:
            flag=0
            break

    if flag==1:
        if minor_diag=='0':
            return 1

        elif minor_diag=='X':
            return -1

    
    #checks rows
    row_temp=board[0][0]
    for row in range(DIMENSION):

        col=0
        row_temp=board[row][col]
        flag=0

        while col<DIMENSION:
            if board[row][col]==row_temp:
                flag=1
                col=col+1
            else:
                flag=0
                break

        if flag==1:
            break

    if flag==1:
        if row_temp == '0':
            return 1

        elif row_temp == 'X':
            return -1


    #checks column
    col_temp = board[0][0]
    for col in range(DIMENSION):

        row = 0
        col_temp = board[row][col]
        flag = 0

        while row < DIMENSION:
            if board[row][col] == col_temp:
                flag = 1
                row = row + 1
            else:
                flag = 0
                break

        if flag == 1:
            break

    if flag == 1:
        if col_temp == '0':
            return 1

        elif col_temp == 'X':
            return -1

    return 0


def alphabeta(board,depth,player,alpha,beta):
    
    """
    performs alpha beta prunning to choose optimum move for maximizer 0. 
    :param board-> current state of the board  
    :param player-> current player(X or 0) 
    :param depth-> track of levels while performing Depth First Search 
    :param alpha-> maximizer paramater 
    :param beta-> minimizer parameter 
    :return : returns optimum move based on score achieved  
    """
    global count_nodes
    score = check_winner(board)  #checks winner

    if score == 1:   #if 0(computer) wins
        return score

    if score == -1:  #if X(user) wins
        return score

    if movesLeft(board) == False:  #if there is draw ie when board is filled
        return 0

    if (player == '0'): #maximizers function

        
        for i in range(DIMENSION):

            for j in range(DIMENSION):
                if board[i][j] == '~':
                    board[i][j] = '0'
                    count_nodes = count_nodes + 1  #count nodes generated for the tree
                    val=alphabeta(board, depth + 1, check_opponent(player),alpha,beta)
                    board[i][j] = '~'
                    alpha=max(val,alpha)
                    if beta<=alpha:
                        return beta
        return alpha

    else:  #minimizers function
      
        for i in range(DIMENSION):
            for j in range(DIMENSION):

                if board[i][j] == '~':
                    board[i][j] = 'X'
                    count_nodes = count_nodes + 1 #count nodes generated for tree
                    val = alphabeta(board, depth + 1, check_opponent(player), alpha, beta)
                    board[i][j] = '~'
                    beta = min(beta, val)
                    if beta<=alpha:
                        return alpha
        return beta


def minmax(board,depth,player):
    
    """
    performs minmax algorithm to choose optimum move for maximizer 0. 
    :param board-> current state of the board  
    :param player-> current player(X or 0) 
    :param depth-> track of levels while performing Depth First Search.
    :return : returns optimum move based on score achieved  
    """
        
    global count_nodes #count nodes generated for tree

    score=check_winner(board)

    if score==1: #if computer(0) wins
        return score

    if score==-1: #if user(X) wins
        return score

    if movesLeft(board)==False: #if there is a draw when no moves are available on the board
        return 0

    if(player=='0'):  #maximizers turn

        best=-99999
        for i in range(DIMENSION):

            for j in range(DIMENSION):
                if board[i][j]=='~':
                    board[i][j]='0'
                    count_nodes=count_nodes+1
                    best=max(best,minmax(board,depth+1,check_opponent(player)))
                    board[i][j]='~'

        return best


    else: #minimizers turn
        best=9999
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if board[i][j]=='~':
                    board[i][j]='X'
                    count_nodes = count_nodes + 1
                    best=min(best,minmax(board,depth+1,check_opponent(player)))
                    board[i][j]='~'


    return best



def check_opponent(player):
    
    """
    checks the enemy of the player
    :param player-> current player(X or 0) 
    :return : returns opponent player
    """
    
    if player=='X':
        return '0'
    else:
        return 'X'


def bestMove_minmax(board):
    
    """
    returns the best move for the machine using minmax algorithm
    :param board->current state of the board
    :return : returns best row and best column
    """
    global count_nodes #count nodes generated for the tree
    best_val=float('-inf') #best_val->initialized to infinity
    choices=[]  #list of optimum choices
    count=0  # count for iteration
    summation=0 #adds up the nodes generated for every tree for each move
    print('----------MINMAX--------')
    print()
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if board[i][j]=='~':
                count=count+1
                board[i][j]='0'
                count_nodes=1
                val=minmax(board,0,check_opponent('0'))
                summation=summation+count_nodes
                count_nodes=0
                board[i][j]='~'

                if val>best_val: 
                    best_val = val #keeps track of best val and choice
                    choices=[[i,j]]

                elif val==best_val:
                    choices.append([i, j])

    best_row=choices[0][0]  #best row and column value
    best_col=choices[0][1]



    return best_row,best_col,best_val,summation


def bestMove_alphabeta(board):
    
    """
    returns the best move for the machine using alpha beta prunning
    :param board->current state of the board
    :return : returns best row and best column
    """
    global count_nodes #count nodes for the tree generated
    best_val=float('-inf')
    choices=[] #list of optimum choices
    count=0 #iteration count
    summation=0 #adds up the nodes generated for every tree for each move
    
    print('---------- ALPHA BETA------')
    print()
    for i in range(DIMENSION):

        for j in range(DIMENSION):
            if board[i][j]=='~':
                board[i][j]='0'
                count=count+1
                count_nodes=1
                val=alphabeta(board,0,check_opponent('0'),-2,2)
                summation=summation+count_nodes
                board[i][j]='~'
                count_nodes=0

                if val>best_val:
                    best_val = val
                    choices=[[i,j]]


                elif val==best_val:
                    choices.append([i, j])

    best_row=choices[0][0]
    best_col=choices[0][1]



    return best_row,best_col,best_val,summation



def pushmove(board,x,y,turn):
    
    """
    places the move for the player
    :param board->current state of the board
    :param x->x position
    :param y->y position
    :param turn->determines turn of the player
    :return : returns current state of the board
    """

    if turn=='0':

        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if x==i and y==j and board[i][j]=='~':
                    board[i][j]='0'
                    break

    if turn=='X':

        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if x==i and y==j and board[i][j]=='~':
                    board[i][j]='X'
                    break
    return board


def check_if_occupied(board,x,y):
    
    """
    checks if board is occupied
    :param board->current state of the board
    :param x->x position
    :param y->y position
    :return : returns True if moves are available;otherwise returns False
    """

    if board[x][y]!='~':
        return True
    return False

def tictactoe():
    
    """
    plays tictactoe
    
    """

    global board #board state

    board=displayboard(board) #display board
    print()
   
    
    while(True):
        print('------------------------')
        print('Your Turn')
        print()
        x=input("enter x")
        y=input("enter y")
        
        if int(x)<0 or int(y)<0 or int(x)>=DIMENSION or int(y)>=DIMENSION: #checks if it is within specified dimension
            continue
        else:
            break
    board=pushmove(board,int(x),int(y),'X') #places move
    board=displayboard(board)


    flag=0 #keep track of players turn


    while(check_winner(board)!=1 or check_winner(board)!=-1 or not movesLeft(board)): 

        if flag==0:
            print()
            print('------------------------')
            print('Computer Turn')
            print()
            best_row,best_col,best_val,summation=bestMove_minmax(board) #determines best column and best row to make a move
            board=pushmove(board,best_row,best_col,'0')
            print()
            print('best row chosen : ', best_row)
            print('best column chosen : ', best_col)
            print('total number of states :',summation)
            print()
            board=displayboard(board) #displays board
            print()

            board[best_row][best_col]='~' 

            best_row, best_col, best_val,summation = bestMove_alphabeta(board)
            board = pushmove(board, best_row, best_col, '0') #places move
            print()
            print('best row chosen : ', best_row) 
            print('best column chosen : ', best_col)
            print('total number of states :',summation)
            print()
            board = displayboard(board)
            print()

            if check_winner(board)==1 or check_winner(board)==-1 or not movesLeft(board): #checks if game is over
                break
            flag=1

        if flag==1:
            print()
            print('-----------------------')
            print('Your Turn ')
            print()
            x = input("enter x")
            y = input("enter y")
            print()
            
            if int(x)<0 or int(y)<0 or int(x)>=DIMENSION or int(y)>=DIMENSION:
                continue
            check=check_if_occupied(board,int(x),int(y)) #checks if occupied
            if check==True:
                continue
            board = pushmove(board, int(x), int(y), 'X') #places move
            board = displayboard(board)
            if check_winner(board)==1 or check_winner(board)==-1 or not movesLeft(board):
                break
            flag=0
    print()
    if check_winner(board)==-1:
        print('YOU WIN!')

    elif check_winner(board)==1:
        print(' YOU LOST!')

    elif not movesLeft(board):
        print('DRAW')


def main():
    """
    This is the main method
    
    """
    tictactoe()


if __name__ == '__main__':
    main()


















