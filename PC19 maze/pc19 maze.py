from random import *
inFile = open('MAZE.TXT','r')
maze_file = inFile.read()
maze = [['' for i in range(11)]for j in range(10)]
y=0
x=0
for i in maze_file: ##Create Board
    if i =='\n':
        y+=1
        x=0
    else:
        maze[x][y]=i
        x+=1
        
for i in range(11): ##Clear prize  and character
    for j in range(10):
        if maze[j][i] == 'P':
            maze[j][i] = '.'
        if maze[j][i] == 'O':
            maze[j][i] = '.'

maze[4][5] = 'O' ##Place character
prize = False ##Place prize
while  prize != True:
    prize_location_x = randint(0,9)
    prize_location_y = randint(0,10)
    if maze[prize_location_x][prize_location_y] == 'X' or (prize_location_x == 4 and prize_location_y == 5):
        pass
    else:
        prize = True
        maze[prize_location_x][prize_location_y] = 'P'

    
won = False
x = 4 ##Coordinates of O
y = 5
previous = None
answer = ''
while won == False:
    for i in range(11): ##Print Board
        for j in range(10):
            print(maze[j][i],end='')
        print()
    print()
    print('1. "U" Player moves up')
    print('2. "D" Player moves down')
    print('3. "L" Player moves left')
    print('4. "R" Player moves right')
    print('5. "" Previous  move')
    previous = answer
    answer = input('>>> ')
    if answer == '' and previous != None:
        answer = previous

    if answer.upper() == 'U': ##UP
        if maze[x][y-1] == 'X':
            pass
        else:
            maze[x][y-1] = 'O'
            maze[x][y] = '.'
            y -= 1
    elif answer.upper() == 'D': ##Down
        if maze[x][y+1] == 'X':
            pass
        else:
            maze[x][y+1] = 'O'
            maze[x][y] = '.'
            y+=1
    elif answer.upper() == 'L': ##Left
        if maze[x-1][y] == 'X':
            pass
        else:
            maze[x-1][y] = 'O'
            maze[x][y] = '.'
            x-=1
    elif answer.upper() == 'R': ##Right
        if maze[x+1][y] == 'X':
            pass
        else:
            maze[x+1][y] = 'O'
            maze[x][y] = '.'
            x+=1
    if maze[x][y]==maze[prize_location_x][prize_location_y]:
        won = True
        print('YOU WON')
        
        
inFile.close()
    
