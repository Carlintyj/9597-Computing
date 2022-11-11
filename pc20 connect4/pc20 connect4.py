def InitialiseBoard():
    Board = [['-' for i in range(7)]for i in range(6)]
    return Board

def SetUpGame():
    ThisPlayer = 'O'
    GameFinished = False
    return ThisPlayer, GameFinished
    
def OutputBoard(Board):
    print('{:<10}'.format(''),end='')
    for i  in range(1,8):
        print('{:<10}'.format(i),end='')
    print()
    x=1
    for i in Board:
        print('{:<10}'.format(x),end='')
        x+=1
        for j in i:
            print('{:<10}'.format(j),end='')
        print()
    
def ThisPlayerMakesMove(ThisPlayer, board):
    answer = False
    while answer == False:
        print('Player',ThisPlayer + "'s turn")
        column = input('Enter a valid column number (1-7): ')
        if column.isdigit() == True:
            column = int(column)
            if column <= 7 and column >= 1:
                answer = True
            else:
                print('Enter VALID input')
            
    if board[0][column-1] != '-':
        print('Column Full, try again')
    else:
        answer  = True
        for i in  range(6,0,-1):
            if board[i-1][column-1] == '-':
                board[i-1][column-1] = ThisPlayer
                break
    print()
    
def CheckIfThisPlayerHasWon(ThisPlayer,board):
    row = 0
    for i in board:
        for j in i:
            if j == ThisPlayer:
                row+=1
                if row == 4:
                    return True
            else:
                row = 0
    row = 0
    for j in range(6):
        for i in  range(7,0,-1):
                if board[j][i-1] == ThisPlayer:
                    row+=1
                    if row == 4:
                        return True
                else:
                    row = 0
        
def SwapThisPlayer():
    pass

def main():
    board = InitialiseBoard()
    ThisPlayer, GameFinished = SetUpGame()
    OutputBoard(board)
    while GameFinished  == False:
        ThisPlayerMakesMove(ThisPlayer,board)
        OutputBoard(board)
        print(CheckIfThisPlayerHasWon(ThisPlayer,board))
    
          

main()
    
