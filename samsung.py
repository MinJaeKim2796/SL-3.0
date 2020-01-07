#saumsung.py

import requests
from bs4 import BeautifulSoup

#선수명 포지션 타수 안타 2루타 3루타 홈런 사구 장타율 출루율 오피에스
response1 = requests.get('http://www.ncdinos.com/stats/batterstats?season=2017&positionCount=&teamCode=SS&satisfy=&recordType=&recordCode=&ordFld=&ordWay=&page=1&playerName=')
response2 = requests.get('http://www.ncdinos.com/stats/batterstats?season=2017&positionCount=&teamCode=SS&satisfy=&recordType=&recordCode=&ordFld=&ordWay=&page=2&playerName=')

#parsing
soup1 = BeautifulSoup(response1.content, 'html.parser')
soup2 = BeautifulSoup(response2.content, 'html.parser')

table1 = soup1.find('table', {'class': 'tb_grade mg01'})
table2 = soup2.find('table', {'class': 'tb_grade mg01'})


#data1 = list()
#data2 = list()

data = dict()   # key : 이름, value : [...](list)

for tr in table1.find_all('tr'):
    tds = list(tr.find_all('td'))
    #print(tds)
    for td in tds:
        
        name = tds[1].text #선수명
        position = int(tds[3].text) #포지션
        atbat = int(tds[5].text) #타수
        #0타수이면 정보를 받아오지 않음
        if atbat == 0:
            continue
        hit = int(tds[7].text) # 안타
        double = int(tds[8].text) #2루타
        tripple = int(tds[9].text) #3루타
        homerun = int(tds[10].text) #홈런
        walk = int(tds[13].text) #볼넷
        long = float(tds[17].text) #장타율
        go = float(tds[18].text) #출루율
        ops = round(float(long + go),3) #ops
        dp = int(tds[15].text) #병살
        #data1.append([name,position,atbat,hit,double,tripple,homerun,walk,ops])
        #data[name] = list()
        data[name]= [position,atbat,hit-(double+tripple+homerun),double,tripple,homerun,walk,ops,dp]
        
for tr in table2.find_all('tr'):
    tds = list(tr.find_all('td'))
    #print(tds)
    for td in tds :
        
        name = tds[1].text #선수명
        position = int(tds[3].text) #포지션
        atbat = int(tds[5].text) #타수
        #0타수이면 정보를 받아오지 않음
        if atbat == 0:
            continue
        hit = int(tds[7].text) # 안타
        double = int(tds[8].text) #2루타
        tripple = int(tds[9].text) #3루타
        homerun = int(tds[10].text) #홈런
        walk = int(tds[13].text) #볼넷
        long = float(tds[17].text) #장타율
        go = float(tds[18].text) #출루율
        ops = round(float(long + go),3) #ops
        dp = int(tds[15].text) #병살
        #data2.append([name,position,atbat,hit,double,tripple,homerun,walk,ops])
        #data[name] = list()
        data[name]= [position,atbat,hit-(double+tripple+homerun),double,tripple,homerun,walk,ops,dp]

starter = ["0","1","2","3","4","5","6","7","8","9"] #스타터 9명

for p in data.keys():
    index = int( data[p][0] )   #position
    xktn = int( data[p][1] )    #atbat
    #동일 포지션에서 타수가 많은 선수 선발
    if int(data.get(starter[index], [0,0])[1]) < xktn:
        dh = starter[index]
        starter[index] = p
    else:
        dh=p
    #지명타자 선발
    if int(data.get(starter[1], [0,0])[1]) < int(data.get(dh,[0,0])[1]):
        starter[1] = dh

#print(starter)


#data3 = data1 + data2


#똑같은 선수 정리
        '''
player = list()
for i in data3:
    if i not in player:
        player.append(i)

data3 = player[:]
'''
#

#이름순 정렬

'''
for i in range(len(data3)):
    for j in range(i,len(data3)):
            if int(data3[i][0]) < int(data3[j][0]):
                data3[i], data3[j] = data3[j], data3[i]
             
'''
#print(data)


#ops순으로 정렬
'''
player = data3[:]
for i in range(len(player)):
    for j in range(i,len(player)):
            if float(player[i][-1]) < float(player[j][-1]):
                player[i], player[j] = player[j], player[i]
'''

response3 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO12&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response4 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO12&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#out 후 1 -> 2+

response5 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO12P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response6 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO12P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#out 후 1 -> 2+ 확률


response7 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO23&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response8 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO23&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#out 후 2 -> 3+


response9 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO23P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response10 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO23P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#out 후 2 -> 3+ 확률


response11 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO34&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response12 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO34&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#out 후 3 -> 홈

response13 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO34P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response14 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TO34P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#out 후 3 -> 홈 확률

#parsing
soup3 = BeautifulSoup(response3.content, 'html.parser')
soup4 = BeautifulSoup(response4.content, 'html.parser')

soup5 = BeautifulSoup(response5.content, 'html.parser')
soup6 = BeautifulSoup(response6.content, 'html.parser')

soup7 = BeautifulSoup(response7.content, 'html.parser')
soup8 = BeautifulSoup(response8.content, 'html.parser')

soup9 = BeautifulSoup(response9.content, 'html.parser')
soup10 = BeautifulSoup(response10.content, 'html.parser')

soup11 = BeautifulSoup(response11.content, 'html.parser')
soup12 = BeautifulSoup(response12.content, 'html.parser')

soup13 = BeautifulSoup(response13.content, 'html.parser')
soup14 = BeautifulSoup(response14.content, 'html.parser')
#


table3 = soup3.find('div', {'id' : 'fixcolhide'})
table4 = soup4.find('div', {'id' : 'fixcolhide'})

table5 = soup5.find('div', {'id' : 'fixcolhide'})
table6 = soup6.find('div', {'id' : 'fixcolhide'})

table7 = soup7.find('div', {'id' : 'fixcolhide'})
table8 = soup8.find('div', {'id' : 'fixcolhide'})

table9 = soup9.find('div', {'id' : 'fixcolhide'})
table10 = soup10.find('div', {'id' : 'fixcolhide'})

table11 = soup11.find('div', {'id' : 'fixcolhide'})
table12 = soup12.find('div', {'id' : 'fixcolhide'})

table13 = soup13.find('div', {'id' : 'fixcolhide'})
table14 = soup14.find('div', {'id' : 'fixcolhide'})



o12 = dict() #out 1루주자가 2루이상 진루

for tr in table3.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12 = tds[3].text #out 후 1루 -> 2루 이상
            
            o12[name] = list()
            o12[name].append(int(out12))

for tr in table4.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12 = tds[3].text #out 후 1루 -> 2루 이상
           
            o12[name] = list()
            o12[name].append(int(out12))


#out후  1루주자가 2루이상 진루 확률

for tr in table5.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12_p = tds[3].text #out 후 1루 -> 2루 이상 확률
            
            o12[name].append(float(out12_p))

for tr in table6.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12_p = tds[3].text #out 후 1루 -> 2루 이상 확률

            o12[name].append(float(out12_p))
            

o23 = dict() #out 2루주자가 3루이상 진루

for tr in table7.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23 = tds[3].text #out 후 2루 -> 3루 이상

            o23[name] = list()
            o23[name].append(int(out23))
            

for tr in table8.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23 = tds[3].text # out 후 2루 -> 3루 이상

            o23[name] = list()
            o23[name].append(int(out23))

#out 2루주자가 3루이상 진루 확률

for tr in table9.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23_p = tds[3].text # out 후 2루 -> 3루 이상 확률
            o23[name].append(float(out23_p))

for tr in table10.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23_p = tds[3].text#out후 2루 -> 3루 이상 확률
            o23[name].append(float(out23_p))


o34 = dict() #out 3루주자가 홈 진루

for tr in table11.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34 = tds[3].text # 땅볼 out 후 3루 -> 홈

            o34[name] = list()
            o34[name].append(int(out34))

for tr in table12.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34 = tds[3].text #out 후 3루 -> 홈
            o34[name] = list()
            o34[name].append(int(out34))

#out 3루주자가 홈 진루 확률


for tr in table13.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34_p = tds[3].text #out 후 3루 -> 홈 확률

            o34[name].append(float(out34_p))
            
for tr in table14.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34_p = tds[3].text  #out 후 3루 -> 홈 확률

            o34[name].append(float(out34_p))

response15 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH13&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response16 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH13&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 1 -> 3+


soup15 = BeautifulSoup(response15.content, 'html.parser')
soup16 = BeautifulSoup(response16.content, 'html.parser')

table15 = soup15.find('div', {'id' : 'fixcolhide'})
table16 = soup16.find('div', {'id' : 'fixcolhide'})


h13 = dict() #안타 후 1루 주자 -> 3루 이상 진루

for tr in table15.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13 = tds[3].text # hit 후 1루 -> 3루 이상

            h13[name] = list()
            h13[name].append(int(hit13))

for tr in table16.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13 = tds[3].text # hit 후 1루 -> 3루 이상

            h13[name] = list()
            h13[name].append(int(hit13))


response17 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH13P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response18 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH13P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 1 -> 3+ 확률


soup17 = BeautifulSoup(response17.content, 'html.parser')
soup18 = BeautifulSoup(response18.content, 'html.parser')

table17 = soup17.find('div', {'id' : 'fixcolhide'})
table18 = soup18.find('div', {'id' : 'fixcolhide'})

#안타 후 1루 주자 -> 3루 이상 진루 확률

for tr in table17.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13_p = tds[3].text # hit 후 1루 -> 3루 이상 확률
            #h13_p.append([name,hit13_p])
            h13[name].append(float(hit13_p))

for tr in table18.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13_p = tds[3].text # hit 후 1루 -> 3루 이상 확률
            #h13.append([name,hit13_p])
            h13[name].append(float(hit13_p))


response19 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH24&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response20 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH24&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 2 -> 홈


soup19 = BeautifulSoup(response19.content, 'html.parser')
soup20 = BeautifulSoup(response20.content, 'html.parser')

table19 = soup19.find('div', {'id' : 'fixcolhide'})
table20 = soup20.find('div', {'id' : 'fixcolhide'})

h24 = dict() #안타 2루주자가 홈 진루

for tr in table19.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24 = tds[3].text # 안타 후 2루 -> 홈

            h24[name] = list()
            h24[name].append(int(hit24))

for tr in table20.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24 = tds[3].text # 안타 후 2루 -> 홈
        
            h24[name] = list()
            h24[name].append(int(hit24))

response21 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH24P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response22 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TH24P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 2 -> 홈 확률


soup21 = BeautifulSoup(response21.content, 'html.parser')
soup22 = BeautifulSoup(response22.content, 'html.parser')

table21 = soup21.find('div', {'id' : 'fixcolhide'})
table22 = soup22.find('div', {'id' : 'fixcolhide'})

#안타 2루주자가 홈 진루 확률

for tr in table21.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24_p = tds[3].text # 안타 후 2루 -> 홈 확률

            h24[name].append(float(hit24_p))

for tr in table22.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24_p = tds[3].text # 안타 후 2루 -> 홈 확률

            h24[name].append(float(hit24_p))
response23 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TD14&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response24 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TD14&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#2루타 후 1 -> 홈


soup23 = BeautifulSoup(response23.content, 'html.parser')
soup24 = BeautifulSoup(response24.content, 'html.parser')

table23 = soup23.find('div', {'id' : 'fixcolhide'})
table24 = soup24.find('div', {'id' : 'fixcolhide'})


d14 = dict() #2루타 후 1루 주자 -> 홈

for tr in table23.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            double14 = tds[3].text # 2루타후 1루 -> 홈

            d14[name] = list()
            d14[name].append(int(double14))

for tr in table24.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            double14 = tds[3].text # 2루타후 1루 -> 홈
            d14[name] = list()
            d14[name].append(int(double14))

response25 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TD14P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response26 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=10&o1=TD14P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#2루타 후 1 -> 홈 확률


soup25 = BeautifulSoup(response25.content, 'html.parser')
soup26 = BeautifulSoup(response26.content, 'html.parser')

table25= soup25.find('div', {'id' : 'fixcolhide'})
table26 = soup26.find('div', {'id' : 'fixcolhide'})

for tr in table25.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            double14_p = tds[3].text # 2루타후 1루 -> 홈 확률

            d14[name].append(float(double14_p))

for tr in table26.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            double14_p = tds[3].text # 2루타후 1루 -> 홈 확률

            d14[name].append(float(double14_p))




#크롤링 했으나 이것은 주자의 기록이기 때문에 사용하지 않는다.
#4.0 version 사용예정
'''
response3 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G12&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response4 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G12&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#땅볼 out 후 1 -> 2+

response5 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G12P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response6 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G12P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#땅볼 out 후 1 -> 2+ %


response7 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G23&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response8 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G23&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#땅볼 out 후 2 -> 3+


response9 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G23P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response10 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G23P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#땅볼 out 후 2 -> 3+ 확률


response11 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G34&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response12 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G34&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#땅볼 out 후 3 -> 홈

response13 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G34P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response14 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_G34P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#땅볼 out 후 3 -> 홈 확률

#parsing
soup3 = BeautifulSoup(response3.content, 'html.parser')
soup4 = BeautifulSoup(response4.content, 'html.parser')

soup5 = BeautifulSoup(response5.content, 'html.parser')
soup6 = BeautifulSoup(response6.content, 'html.parser')

soup7 = BeautifulSoup(response7.content, 'html.parser')
soup8 = BeautifulSoup(response8.content, 'html.parser')

soup9 = BeautifulSoup(response9.content, 'html.parser')
soup10 = BeautifulSoup(response10.content, 'html.parser')

soup11 = BeautifulSoup(response11.content, 'html.parser')
soup12 = BeautifulSoup(response12.content, 'html.parser')

soup13 = BeautifulSoup(response13.content, 'html.parser')
soup14 = BeautifulSoup(response14.content, 'html.parser')
#


table3 = soup3.find('div', {'id' : 'fixcolhide'})
table4 = soup4.find('div', {'id' : 'fixcolhide'})

table5 = soup5.find('div', {'id' : 'fixcolhide'})
table6 = soup6.find('div', {'id' : 'fixcolhide'})

table7 = soup7.find('div', {'id' : 'fixcolhide'})
table8 = soup8.find('div', {'id' : 'fixcolhide'})

table9 = soup9.find('div', {'id' : 'fixcolhide'})
table10 = soup10.find('div', {'id' : 'fixcolhide'})

table11 = soup11.find('div', {'id' : 'fixcolhide'})
table12 = soup12.find('div', {'id' : 'fixcolhide'})

table13 = soup13.find('div', {'id' : 'fixcolhide'})
table14 = soup14.find('div', {'id' : 'fixcolhide'})



g12 = dict() #땅볼 out 1루주자가 2루이상 진루

for tr in table3.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12 = tds[3].text # 땅볼 out 후 1루 -> 2루 이상
            #g12.append([name,out12])
            g12[name] = list()
            g12[name].append(out12)

for tr in table4.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12 = tds[3].text # 땅볼 out 후 1루 -> 2루 이상
            #g12.append([name,out12])
            g12[name] = list()
            g12[name].append(out12)


#g12_p = [] #땅볼 out 1루주자가 2루이상 진루 확률

for tr in table5.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12_p = tds[3].text # 땅볼 out 후 1루 -> 2루 이상 확률
            #g12_p.append([name,out12_p])
            g12[name].append(out12_p)

for tr in table6.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out12_p = tds[3].text # 땅볼 out 후 1루 -> 2루 이상 확률
            #g12_p.append([name,out12_p])
            g12[name].append(out12_p)
            

g23 = dict() #땅볼 out 2루주자가 3루이상 진루

for tr in table7.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23 = tds[3].text # 땅볼 out 후 2루 -> 3루 이상
            #g23.append([name,out23])
            g23[name] = list()
            g23[name].append(out23)
            

for tr in table8.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23 = tds[3].text # 땅볼 out 후 2루 -> 3루 이상
            #g23.append([name,out23])
            g23[name] = list()
            g23[name].append(out23)

#g23_p = [] #땅볼 out 2루주자가 3루이상 진루 확률

for tr in table9.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23_p = tds[3].text # 땅볼 out 후 2루 -> 3루 이상 확률
            g23[name].append(out23_p)

for tr in table10.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out23_p = tds[3].text # 땅볼 out 후 2루 -> 3루 이상 확률
            g23[name].append(out23_p)


g34 = dict() # 땅볼 out 3루주자가 홈 진루

for tr in table11.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34 = tds[3].text # 땅볼 out 후 3루 -> 홈
            #g34.append([name,out34])
            g34[name] = list()
            g34[name].append(out34)

for tr in table12.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34 = tds[3].text # 땅볼 out 후 3루 -> 홈
            #g34.append([name,out34])
            g34[name] = list()
            g34[name].append(out34)

#g34_p = [] # 땅볼 out 3루주자가 홈 진루 확률


for tr in table13.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34_p = tds[3].text # 땅볼 out 후 3루 -> 홈 확률
            #g34_p.append([name,out34_p])
            g34[name].append(out34_p)
            
for tr in table14.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            out34_p = tds[3].text  # 땅볼 out 후 3루 -> 홈 확률
            #g34_p.append([name,out34_p])
            g34[name].append(out34_p)

response15 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F23&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response16 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F23&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#뜬공 out 후 2 -> 3+


soup15 = BeautifulSoup(response15.content, 'html.parser')
soup16 = BeautifulSoup(response16.content, 'html.parser')

table15 = soup15.find('div', {'id' : 'fixcolhide'})
table16 = soup16.find('div', {'id' : 'fixcolhide'})


f23 = dict() #뜬공 out 2루주자가 3루이상 진루
for tr in table15.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly23 = tds[3].text # 뜬공 out 후 2루 -> 3루 이상
            #f23.append([name,fly23])
            f23[name] = list()
            f23[name].append(fly23)

for tr in table16.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly23 = tds[3].text # 뜬공 out 후 2루 -> 3루 이상
            #f23.append([name,fly23])
            f23[name] = list()
            f23[name].append(fly23)


response17 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F23P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response18 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F23P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#뜬공 out 후 2 -> 3+ 확률


soup17 = BeautifulSoup(response17.content, 'html.parser')
soup18 = BeautifulSoup(response18.content, 'html.parser')

table17 = soup17.find('div', {'id' : 'fixcolhide'})
table18 = soup18.find('div', {'id' : 'fixcolhide'})

#f23_p = [] #뜬공 out 2루주자가 3루이상 진루

for tr in table17.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly23_p = tds[3].text # 뜬공 out 후 2루 -> 3루 이상 확률
            #f23_p.append([name,fly23_p])
            f23[name].append(fly23_p)

for tr in table16.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly23_p = tds[3].text # 뜬공 out 후 2루 -> 3루 이상 확률
            #f23_p.append([name,fly23_p])
            f23[name].append(fly23_p)


response19 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F34&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response20 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F34&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#뜬공 out 후 3 -> 홈


soup19 = BeautifulSoup(response19.content, 'html.parser')
soup20 = BeautifulSoup(response20.content, 'html.parser')

table19 = soup19.find('div', {'id' : 'fixcolhide'})
table20 = soup20.find('div', {'id' : 'fixcolhide'})

f34 = dict() #뜬공 out 3루주자가 홈 진루

for tr in table19.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly34 = tds[3].text # 뜬공 out 후 3루 -> 홈
            #f34.append([name,fly34])
            f34[name] = list()
            f34[name].append(fly34)

for tr in table20.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly34 = tds[3].text # 뜬공 out 후 3루 -> 홈
            #f34.append([name,fly34])
            f34[name] = list()
            f34[name].append(fly34)

response21 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F34P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response22 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_F34P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#뜬공 out 후 3 -> 홈 확률


soup21 = BeautifulSoup(response21.content, 'html.parser')
soup22 = BeautifulSoup(response22.content, 'html.parser')

table21 = soup21.find('div', {'id' : 'fixcolhide'})
table22 = soup22.find('div', {'id' : 'fixcolhide'})

#f34_p = [] #뜬공 out 3루주자가 홈 진루 확률


for tr in table21.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly34_p = tds[3].text # 뜬공 out 후 3루 -> 홈 확률
            #f34_p.append([name,fly34_p])
            f34[name].append(fly34_p)

for tr in table22.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            fly34_p = tds[3].text # 뜬공 out 후 3루 -> 홈 확률
            #f34_p.append([name,fly34_p])
            f34[name].append(fly34_p)

#

response23 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H13&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response24 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H13&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 1 -> 3+


soup23 = BeautifulSoup(response23.content, 'html.parser')
soup24 = BeautifulSoup(response24.content, 'html.parser')

table23 = soup23.find('div', {'id' : 'fixcolhide'})
table24 = soup24.find('div', {'id' : 'fixcolhide'})


h13 = dict() #안타 후 1루 주자 -> 3루 이상 진루

for tr in table23.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13 = tds[3].text # hit 후 1루 -> 3루 이상
            #h13.append([name,hit13])
            h13[name] = list()
            h13[name].append(hit13)

for tr in table24.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13 = tds[3].text # hit 후 1루 -> 3루 이상
            #h13.append([name,hit13])
            h13[name] = list()
            h13[name].append(hit13)

response25 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H13P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response26 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H13P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 1 -> 3+ 확률


soup25 = BeautifulSoup(response25.content, 'html.parser')
soup26 = BeautifulSoup(response26.content, 'html.parser')

table25= soup25.find('div', {'id' : 'fixcolhide'})
table26 = soup26.find('div', {'id' : 'fixcolhide'})


#h13_p = [] #안타 후 1루 주자 -> 3루 이상 진루 확률

for tr in table25.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13_p = tds[3].text # hit 후 1루 -> 3루 이상 확률
            #h13_p.append([name,hit13_p])
            h13[name].append(hit13_p)

for tr in table26.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit13_p = tds[3].text # hit 후 1루 -> 3루 이상 확률
            #h13.append([name,hit13_p])
            h13[name].append(hit13_p)

            


response27 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H24&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response28 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H24&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 2 -> 홈 


soup27 = BeautifulSoup(response27.content, 'html.parser')
soup28 = BeautifulSoup(response28.content, 'html.parser')

table27 = soup27.find('div', {'id' : 'fixcolhide'})
table28 = soup28.find('div', {'id' : 'fixcolhide'})

h24 = dict() #안타 2루주자가 홈 진루

for tr in table27.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24 = tds[3].text # 안타 후 2루 -> 홈
            #h24.append([name,hit24])
            h24[name] = list()
            h24[name].append(hit24)

for tr in table28.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24 = tds[3].text # 안타 후 2루 -> 홈
            #h24.append([name,hit24])
        
            h24[name] = list()
            h24[name].append(hit24)

response29 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H24P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response30 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_H24P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#안타 후 2 -> 홈 확률 


soup29 = BeautifulSoup(response29.content, 'html.parser')
soup30 = BeautifulSoup(response30.content, 'html.parser')

table29 = soup29.find('div', {'id' : 'fixcolhide'})
table30 = soup30.find('div', {'id' : 'fixcolhide'})

#h24_p = [] #안타 2루주자가 홈 진루 확률

for tr in table29.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24_p = tds[3].text # 안타 후 2루 -> 홈 확률
            #h24_p.append([name,hit24_p])
            h24[name].append(hit24_p)

for tr in table30.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            hit24_p = tds[3].text # 안타 후 2루 -> 홈 확률
            #h24_p.append([name,hit24_p])
            h24[name].append(hit24_p)

response31 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_D14&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response32 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_D14&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#2루타 후 1 -> 홈 


soup31 = BeautifulSoup(response31.content, 'html.parser')
soup32 = BeautifulSoup(response32.content, 'html.parser')

table31 = soup31.find('div', {'id' : 'fixcolhide'})
table32 = soup32.find('div', {'id' : 'fixcolhide'})

d14 = dict() #2루타 1루주자가 홈 진루

for tr in table31.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            double14 = tds[3].text # 2루타 후 1루 -> 홈
            #d14.append([name,double14])
            d14[name] = list()
            d14[name].append(double14)

for tr in table32.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            dobule14 = tds[3].text # 2루타 후 1루 -> 홈
            #d14.append([name,dobule14])
            d14[name] = list()
            d14[name].append(double14)


response33 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_D14P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response34 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=12&o1=BR_D14P&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')
#2루타 후 1 -> 홈 확률 


soup33 = BeautifulSoup(response33.content, 'html.parser')
soup34 = BeautifulSoup(response34.content, 'html.parser')

table33 = soup33.find('div', {'id' : 'fixcolhide'})
table34 = soup34.find('div', {'id' : 'fixcolhide'})

#d14_p = [] #2루타 1루주자가 홈 진루 확률

for tr in table33.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            double14_p = tds[3].text# 2루타 후 1루 -> 홈 확률
            #d14_p.append([name,double14_p])
            d14[name].append(double14_p)

for tr in table34.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            double14_p = tds[3].text# 2루타 후 1루 -> 홈 확률
            #d14_p.append([name,double14_p])
            d14[name].append(double14_p)
'''

response35 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=8&o1=GDPN&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=')
response36 = requests.get('http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=2017&ye=2017&se=0&te=%EC%82%BC%EC%84%B1&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=8&o1=GDPN&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=30&si=&cn=')

soup35 = BeautifulSoup(response35.content, 'html.parser')
soup36 = BeautifulSoup(response36.content, 'html.parser')

table35 = soup35.find('div', {'id' : 'fixcolhide'})
table36 = soup36.find('div', {'id' : 'fixcolhide'})


dp = dict() #병살타 상황

for tr in table35.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            dp_1 = tds[3].text #병살타
            #dp.append([name,dp_1])
            #dp[name] = list()
            dp[name] = [int(data[name][-1]), int(dp_1)]

for tr in table36.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        if td.find('a'):
            name = td.find('a').text #선수명
            if name not in starter:
                continue
            dp_1 = tds[3].text #병살타
            #dp.append([name,dp_1])
            #dp[name] = list()
            dp[name] = [int(data[name][-1]), int(dp_1)]


'''
for i in range(len(g12_p)):
    for j in range(len(g12)):
        if g12_p[i][0] == g12[j][0]:
            g12[j].append(g12_p[i][1])


for i in range(len(g23)):
    for j in range(len(g12)):
        if g23[i][0] == g12[j][0]:
            g12[j].append(g23[i][1])


for i in range(len(g23_p)):
    for j in range(len(g12)):
        if g23_p[i][0] == g12[j][0]:
            g12[j].append(g23_p[i][1])

for i in range(len(g34)):
    for j in range(len(g12)):
        if g34[i][0] == g12[j][0]:
            g12[j].append(g34[i][1])


for i in range(len(g34_p)):
    for j in range(len(g12)):
        if g34_p[i][0] == g12[j][0]:
            g12[j].append(g34_p[i][1])


for i in range(len(f23)):
    for j in range(len(g12)):
        if f23[i][0] == g12[j][0]:
            g12[j].append(f23[i][1])

for i in range(len(f23_p)):
    for j in range(len(g12)):
        if f23_p[i][0] == g12[j][0]:
            g12[j].append(f23_p[i][1])

for i in range(len(f34)):
    for j in range(len(g12)):
        if f34[i][0] == g12[j][0]:
            g12[j].append(f34[i][1])

for i in range(len(f34_p)):
    for j in range(len(g12)):
        if f34_p[i][0] == g12[j][0]:
            g12[j].append(f34_p[i][1])

for i in range(len(h13)):
    for j in range(len(g12)):
        if h13[i][0] == g12[j][0]:
            g12[j].append(h13[i][1])

for i in range(len(h13_p)):
    for j in range(len(g12)):
        if h13_p[i][0] == g12[j][0]:
            g12[j].append(h13_p[i][1])

for i in range(len(h24)):
    for j in range(len(g12)):
        if h24[i][0] == g12[j][0]:
            g12[j].append(h24[i][1])

for i in range(len(h24_p)):
    for j in range(len(g12)):
        if h24_p[i][0] == g12[j][0]:
            g12[j].append(h24_p[i][1])

for i in range(len(d14)):
    for j in range(len(g12)):
        if d14[i][0] == g12[j][0]:
            g12[j].append(d14[i][1])

for i in range(len(d14_p)):
    for j in range(len(g12)):
        if d14_p[i][0] == g12[j][0]:
            g12[j].append(d14_p[i][1])
            
for i in range(len(g12)):
    for j in range(len(player)):
            if g12[i][0] == player[j][0]:
                for k in range(16):
                    player[j].append(g12[i][k+1])

print(player)
'''

'''
with open('samsung.txt', 'w') as file:
    file.write('name\tpos\tatbat\tsingle\tdouble\ttriple\thomerun\twalk\tOPS\tg12\tg12_p\tg23\tg23_p\tg34\tg34_p\tf23\tf23_p\tf34\tf34_p\th13\th13_p\th24\th24_p\td14\td14_p\n')
    for i in player:
        file.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\n'.format(i[0], i[1], i[2]
                                                         , i[3], i[4], i[5], i[6], i[7], i[8]
                                                       ,i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24]))

'''


#samsung.txt에 주전들의 기록을 출력

with open('samsung.txt', 'w') as file:

    #file.write(starter)
    file.write('name position atbat single double triple homerun walk OPS\n')
    for i in range(1,10):
        file.write(starter[i] + " " + '{} {} {} {} {} {} {} {}'.format(data[starter[i]][0], data[starter[i]][1], data[starter[i]][2], data[starter[i]][3], data[starter[i]][4],data[starter[i]][5], data[starter[i]][6], data[starter[i]][7]) + '\n')

    file.write('\n')
    file.write("진루기록 : out12 out23 out34 single13 single24 double14 doubleout\n")
    for name in o12.keys():
        file.write(name +" " + '{} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(o12[name][0], o12[name][1], o23[name][0], o23[name][1], o34[name][0], o34[name][1], h13[name][0], h13[name][1], h24[name][0], h24[name][1], d14[name][0], d14[name][1], dp[name][0], dp[name][1]) + '\n' )
