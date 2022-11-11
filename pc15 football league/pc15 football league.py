def CreateUpdateFile():
    inFile = open('NEWFILE.TXT','a')
    results_file = open('RESULTS.TXT','r')
    results = results_file.read()
    results = results.split('\n')
    results_file.close()
    for i in results:
        if i == '':
            break
        else:
            score = i.split()
            inFile.write(score[0]+',')
            if int(score[1]) > int(score[3]):
                inFile.write('W,'+score[1]+','+score[3]+'\n')
                inFile.write(score[2]+','+'L,'+score[3]+','+score[1]+'\n')
            elif int(score[1]) < int(score[3]):
                inFile.write('L,'+score[1]+','+score[3]+'\n')
                inFile.write(score[2]+','+'W,'+score[3]+','+score[1]+'\n')
            else:
                inFile.write('D,'+score[1]+','+score[3]+'\n')
                inFile.write(score[2]+','+'D,'+score[3]+','+score[1]+'\n')
    inFile.close()

def ComputeTeamStat(teamname):
    inFile = open('NEWFILE.TXT','r')
    results = inFile.read()
    results = results.split()
    P = 0
    W = 0
    D = 0
    L = 0
    GF = 0
    GA = 0
    for i in results:
        games = i.split(',')
        if games[0] == teamname:
            P+=1
            if games[1] == 'W':
                W+= 1
            if games[1] == 'L':
                L += 1
            if games[1] == 'D':
                D +=1
            GF+= int(games[2])
            GA += int(games[3])
    return str('{0:<10}{1:^5}{2:^5}{3:^5}{4:^5}{5:^5}{6:^5}{7:^5}{8:>10}'.format(teamname,P,W,D,L,GF,GA,GF-GA,str(int(W)*3+int(D))))
    inFile.close()

def GenerateTable():
    pass
points = {}
GD = {}
teams_file = open('TEAMS.TXT','r')
teams = teams_file.read()
teams=teams.split()
teams_file.close()
print('{0:<10}{1:^5}{2:^5}{3:^5}{4:^5}{5:^5}{6:^5}{7:^5}{8:>10}'.format('Team','P','W','D','L','GF','GA','GD','Points'))
print('-'*55)
for i in teams:
    points[i] = ComputeTeamStat(i).split()[8]
    GD[i] = ComputeTeamStat(i).split()[7]
for i in range(len(points)-1):
    for j in range(len(points)-1):
        if points[teams[j]] < points[teams[j+1]]:
            temp = points[teams[j]]
            points[teams[j]] = points[teams[j+1]]
            points[teams[j+1]] = temp
                                    
            
    

