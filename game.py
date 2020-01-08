#game.py

import random

#import samsung

inning = 0
score = [0,0,0,0,0,0,0,0,0,0]   #score[0] 총점 score[i]는 i회 점수
#Base = [0,0,0,0,0,0,0,0]        #Base[0, 1루, 2루 3루, 주자 홈인.. ] 1 주자 있음, 0 주자 없음
Base = [0,0,0,0]                #Base[0,1루,2루,3루] 1 주자 있음, 0 주자 없음
outcount = 0                    #Outcount
#hit = "Out"                     #타격 상황



class Player:
    
    def __init__(self, name=str(), position=int(), atbat=0, single=0, double=0, tripple=0, homerun=0, bb=0, ops=0.0):
        self.Name = name
        self.Position = int(position)
        self.atBat = int(atbat)
        self.Single = int(single)
        self.Double = int(double)
        self.Tripple = int(tripple)
        self.Homerun = int(homerun)
        self.BB = int(bb)
        self.Out = self.atBat - ( self.Single + self.Double + self.Tripple + self.Homerun )
        self.OPS = float(ops)
        self.Average = ( self.Single + self.Double + self.Tripple + self.Homerun ) / ( self.Single + self.Double + self.Tripple + self.Homerun + self.Out )

        #4.0 version 에서 사용할 예정
        #실행 가능하지만 통계자료로 활용하지 않음
        '''
        self.record = [0,0,0,0,0,0]    #Single, Double, Tripple, Homerun, BB, Out
        self.xkdbf = 0.0               #기록 타율
        self.Txkdbf = list()
        '''


    def __str__(self):
        return self.Name



'''
player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
player5 = Player()
player6 = Player()
player7 = Player()
player8 = Player()
player9 = Player()
'''
# key : 선수명, value : player
SL = dict()

file = open('samsung.txt', 'r')

line = file.readline()  #tag

line = file.readline()
while line != '\n':
    line = line.strip()
    line = line.split()
    SL[line[0]] = Player(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
    # name position atbat single double triple homerun walk OPS 로 배열되어 있음
    line = file.readline()

line = file.readline()  #tag
#print(line)


#진루기록
for line in file:
    line = line.strip()
    line = line.split()
    #print(line)
    
    SL[line[0]].Out12a = int(line[1])
    SL[line[0]].Out12 = round( int(line[1]) / (float(line[2]) * 0.01) )

    SL[line[0]].Out23a = int(line[3])
    SL[line[0]].Out23 = round( int(line[3]) / (float(line[4]) * 0.01) )

    SL[line[0]].Out34a = int(line[5])
    SL[line[0]].Out34 = round( int(line[5]) / (float(line[6]) * 0.01) )

    SL[line[0]].Single13a = int(line[7])
    SL[line[0]].Single13 = round( int(line[7]) / (float(line[8]) * 0.01) )

    SL[line[0]].Single24a = int(line[9])
    SL[line[0]].Single24 = round( int(line[9]) / (float(line[10]) * 0.01) )

    SL[line[0]].Double14a = int(line[11])
    if int(line[11]) == 0:
        SL[line[0]].Double14 = 0
    else:
        SL[line[0]].Double14 = round( int(line[11]) / (float(line[12]) * 0.01) )

    SL[line[0]].Doubleplay = int(line[13])
    SL[line[0]].Doubleplayc = int(line[14])

file.close()


#타순 배열
battingorder = [i-i for i in range(0,10)]


#임의의 타순
L = list(SL.keys())
for i in range(1,10):
    battingorder[i] = SL[L[i-1]]
    



'''
if __name__ == "__main__":

    player1=Player('구자욱',564,105,39,10,21,63) 
    player2=Player('박해민',570,122,25,8,7,50)
    player3=Player('러프',515,93,38,0,31,60)
    player4=Player('이승엽',472,73,30,5,24,47)
    player5=Player('이원석',411,70,20,1,18,34)
    player6=Player('강한울',412,113,9,3,0,26)
    player7=Player('김헌곤',356,70,13,2,9,29)
    player8=Player('조동찬',353,69,23,0,10,22)
    player9=Player('이지영',302,60,10,2,0,20)
'''



'''
def Advance():
    pass
'''

# 타격 결과
def Batting(player,p=0):    #p는 방송 알림 유무 1 print함

    global inning
    global score
    global Base
    global outcount
    scorep = 0  #병살타 쳤을때 점수 제거
    dp= 0       #더블플레이 신호

    x = random.randint(1, player.atBat) #1부터 타석수까지 난수발생 후 판정
    #print(x)

    if p:
        print(player.Name)

    if x <= player.Single: #Single

        #player.record[0] += 1
        
        if p:
            print("Single")

        #3루 주자는 무조건 홈인
        if Base[3]:
            Base[3] = 0
            score[inning] += 1
            if p:
                print("Scored")

        #2루 주자는 진루율에 따라 3루진루 혹은 홈인
        if Base[2]:
            y = random.randint(1, player.Single24)
            if y <= player.Single24a:
                Base[2] = 0
                score[inning] += 1
                if p:
                    print('Scored')

            else:
                Base[3] = 1
                Base[2] = 0

        #1루 주자는 진루율에 따라 2루진루 혹은 2루진루
        if Base[1]:
            y = random.randint(1, player.Single13)
            if (y <= (player.Single13a)) and (not Base[3]):
                Base[3] = 1
                Base[1] = 0
            else:
                Base[2] = 1
                Base[1] = 0

        Base[1] = 1     #1루타 친 타자주자

    elif x <= player.Single + player.Double: #Double

        #player.record[1] += 1
        
        if p:
            print("Double")

        #3루 주자는 무조건 홈인
        if Base[3]:
            Base[3] = 0
            score[inning] += 1
            if p:
                print("Scored")

        #2루 주자는 무조건 홈인
        if Base[2]:
            Base[2] = 0
            score[inning] += 1
            if p:
                print("Scored")

        #1루 주자는 진루율에 따라 3루진루 혹은 홈인
        if Base[1]:
            if player.Double14 == 0:
                Base[3] = 1
                Base[1] = 0
            else:    
                y = random.randint(1, player.Double14)
                if y <= player.Double14a:
                    Base[1] = 0
                    score[inning] += 1
                    if p:
                        print("Scored")
                else:
                    Base[3] = 1
                    Base[1] = 0

        Base[2] = 1    #2루타 친 타자주자    
        
    elif  x <= player.Single + player.Double +player.Tripple: #Triple

        #player.record[2] += 1
        
        if p:
            print("Tripple")

        #3루 주자는 무조건 홈인
        if Base[3]:
            Base[3] = 0
            score[inning] += 1
            if p:
                print("Scored")

        #2루 주자는 무조건 홈인
        if Base[2]:
            Base[2] = 0
            score[inning] += 1
            if p:
                print("Scored")

        #1루 주자는 무조건 홈인
        if Base[1]:
            Base[1] = 0
            score[inning] += 1
            if p:
                print("Scored")

        Base[3] = 1     #3루타 친 타자주자   

    elif x <= player.Single + player.Double +player.Tripple + player.Homerun: #Homerun

        #player.record[3] += 1
        
        if p:
            print("Homerun")

        #홈런은 모두 홈인    
        if Base[3]:
            Base[3] = 0
            score[inning] += 1
            if p:
                print("Scored")
        if Base[2]:
            Base[2] = 0
            score[inning] += 1
            if p:
                print("Scored")
        if Base[1]:
            Base[1] = 0
            score[inning] += 1
            if p:
                print("Scored")
        score[inning] += 1
        if p:
            print("Scored")


    elif x <= player.Single + player.Double +player.Tripple + player.Homerun + player.BB: #BB

        #player.record[4] += 1
        
        if p:
            print("BB")

        
        if Base[1]:
            if Base[2]:
                if Base[3]:
                    #만루상황에선 1점득점후 만루 유지
                    score[inning] += 1
                    if p:
                        print("Scored")
                else:
                    #주자 12루 시 만루로 바뀜
                    Base = [0,1,1,1]
            else:
                #1루 주자 있고 2루 주자 없으면 3루주자 유무와 상관없이 1루2루 주자 채워짐
                Base[2] = 1
        else:
            #1루주자 없을시 1루 진루
            Base[1] = 1

    else:       #Out

        #player.record[5] += 1
        
        if p:
            print("Out")
        #outcount += 1

        #2아웃이면 아웃처리 후 이닝 종료
        if outcount == 2:
            outcount += 1

        #1아웃이나 0아웃일 경우 병살타 처리    
        else:
            y = random.randint(1, player.Doubleplayc)
            if Base[1] and (y <= player.Doubleplay):
                outcount += 2
                if Base[3]:
                    z = random.randint(1, player.Out34)
                    if z <= player.Out34a:
                        scorep = 1
                        Base[3] = 0

                        if Base[2]:
                            Base[3] = 1
                            Base[2] = 0

                        Base[1] = 0

                    else:
                        if Base[2]:
                            Base[3] = 1
                            Base[2] = 1
                            Base[1] = 0
                        else:
                            Base[2] = 0
                            Base[1] = 0                            
                            
                elif Base[2]:
                    z = random.randint(1, player.Out23)
                    if z <= player.Out23a:
                        Base[3] = 1
                        Base[2] = 0
                        Base[1] = 0
                    else:
                        Base[1] = 0
                else:
                    Base = [0,0,0,0]
                if (outcount < 3) and scorep:
                    score[inning] += 1
                    if p:
                        print('Scored')
            else:
                outcount += 1
                if Base[3]:
                    z = random.randint(1, player.Out34)
                    if z <= player.Out34a:
                        score[inning] += 1
                        if p:
                            print("Scored")
                        Base[3] = 0

                if Base[2] and (not Base[3]):
                    z = random.randint(1, player.Out23)
                    if z <= player.Out23a:
                        Base[3] = 1
                        Base[2] = 0
                        
                if Base[1] and (not Base[2]):
                    z = random.randint(1, player.Out12)
                    if z <= player.Out12a:
                        Base[2] = 1
                        Base[1] = 0
        
    if p:
        print("Base : %d %d %d"%(Base[1],Base[2],Base[3]))
        print("%d Out"%outcount)

    return

def game(p=0):
    global inning
    global score
    global Base
    global outcount
    global battingorder

    batter = 1


    inning = 1
    score=[0,0,0,0,0,0,0,0,0,0]
    Base = [0,0,0,0]
    outcount = 0

    while inning <= 9: #9회까지
        if p:
            print("")
            print("%d inning"%inning)
            print("batter is %d"%((batter-1)%9 + 1))
        Base = [0,0,0,0]
        while outcount < 3:
            Batting( battingorder[(batter-1)%9 + 1], p) #승부
            batter += 1

        inning += 1 #이닝 종료
        outcount = 0

    for i in score: #총점계산
        score[0] += i

    print("Score Board", score)
    return



def simulation(E, pr=0):

    lineup = str()

    file = open(E, "r")

    line = file.readline() #tag

    lineup += line

    battingorder[0] = line

    line = file.readline()
    lineup += line
    while line != '\n':

        #print(line)
        line.strip()
        p = line.split()
        battingorder[int(p[0])] = SL[p[1]]
        line = file.readline()
        lineup += line

    line = file.readline()

    while line != '\n':
        lineup += line
        line = file.readline()


    #BO = game.battingorder[:]
     
    file.close()

    '''
    for i in range(1,10):
        game.battingorder[i].record = [0,0,0,0,0,0]
    '''


    games = 1000 * 1000 #게임수 결정


    T = list()
    '''
    for i in range(1,10):
        game.battingorder[i].Txkdbf = list()
    '''

    for j in range(0,1000):
        tscore = 0

        '''
        for i in range(1,10):
            game.battingorder[i].record = [0,0,0,0,0,0]
        '''
            
        for i in range(0,1000): 
            #print(i, "games")

######################################################################################################
            game(pr)
######################################################################################################


            tscore += score[0]
        '''
        for i in range(1,10):
            game.battingorder[i].tkdbf = ( game.battingorder[i].record[0] + game.battingorder[i].record[1] + game.battingorder[i].record[2] + game.battingorder[i].record[3] ) / ( game.battingorder[i].record[0] + game.battingorder[i].record[1] + game.battingorder[i].record[2] + game.battingorder[i].record[3] + game.battingorder[i].record[5] )
            game.battingorder[i].Txkdbf.append(game.battingorder[i].tkdbf)
        '''
            
        average = tscore / 1000
            
        T.append(average)



    average = 0
    for i in T:
        average += i
    average = average / 1000

    '''
    Tkdbf = 0
    for i in range(1,10):
        for j in game.battingorder[i].Txkdbf:
            Tkdbf += j

        Tkdbf = Tkdbf / 1000
    '''

    file = open(E, "w")

    file.write( lineup )

    file.write(str(average) + " " + str(1000*1000) + '\n')

    file.close()

    #####

    sc = list()
    ga = list()

    with open(E,"r") as file:

        line = file.readline()
        lineup += line
        while line != '\n':
            line = file.readline()
            lineup += line

        for line in file:
            line = line.strip()
            line = line.split()
            sc.append(float(line[0]))
            ga.append(int(line[1]))
    ave=0
    gg=0
    for av in sc:
        ave += av

    average = ave / (len(ga)-1)


    with open(E,"a") as file:
        file.write('\n')
        file.write(str(average))



def test(E, pr=0):

    lineup = str()

    file = open(E, "r")

    line = file.readline() #tag

    lineup += line

    battingorder[0] = line

    line = file.readline()
    lineup += line
    while line != '\n':

        #print(line)
        line.strip()
        p = line.split()
        battingorder[int(p[0])] = SL[p[1]]
        line = file.readline()
        lineup += line

    line = file.readline()

    while line != '\n':
        lineup += line
        line = file.readline()


    #BO = game.battingorder[:]
     
    file.close()

    '''
    for i in range(1,10):
        game.battingorder[i].record = [0,0,0,0,0,0]
    '''


    games = 100 * 100 #게임수 결정


    T = list()
    '''
    for i in range(1,10):
        game.battingorder[i].Txkdbf = list()
    '''

    for j in range(0,100):
        tscore = 0

        '''
        for i in range(1,10):
            game.battingorder[i].record = [0,0,0,0,0,0]
        '''
            
        for i in range(0,100): 
            #print(i, "games")

######################################################################################################
            game(pr)
######################################################################################################


            tscore += score[0]
        '''
        for i in range(1,10):
            game.battingorder[i].tkdbf = ( game.battingorder[i].record[0] + game.battingorder[i].record[1] + game.battingorder[i].record[2] + game.battingorder[i].record[3] ) / ( game.battingorder[i].record[0] + game.battingorder[i].record[1] + game.battingorder[i].record[2] + game.battingorder[i].record[3] + game.battingorder[i].record[5] )
            game.battingorder[i].Txkdbf.append(game.battingorder[i].tkdbf)
        '''
            
        average = tscore / 100
            
        T.append(average)



    average = 0
    for i in T:
        average += i
    average = average / 100

    '''
    Tkdbf = 0
    for i in range(1,10):
        for j in game.battingorder[i].Txkdbf:
            Tkdbf += j

        Tkdbf = Tkdbf / 1000
    '''

    file = open(E, "w")

    file.write( lineup )

    file.write(str(average) + " " + str(100*100) + '\n')

    file.close()

    #####

    sc = list()
    ga = list()

    with open(E,"r") as file:

        line = file.readline()
        lineup += line
        while line != '\n':
            line = file.readline()
            lineup += line

        for line in file:
            line = line.strip()
            line = line.split()
            sc.append(float(line[0]))
            ga.append(int(line[1]))
    ave=0
    gg=0
    for av in sc:
        ave += av

    average = ave / (len(ga)-1)


    with open(E,"a") as file:
        file.write('\n')
        file.write(str(average))
