# *SL 3.0*

SL 3.0 : 2017시즌 삼성라이온즈 타자들의 기록을 기반으로 타순의 평균득점을 비교하는 소프트웨어

2017 KHU

[*Introduction to Software Convergence*]  Term project



## 1. game.py : main.py에서 import되는 파일

Code URL : https://github.com/MinJaeKim2796/SL3.0/blob/master/game.py

 1) Line 16-41 : 타격 기록이 들어가도록 하는 Class
 
 2) Line 57-105 : samsung.txt 파일을 열어 진루 기록을 비어있는 Dict에 넣음

 3) Line 142-396 : 타격 결과로 인한 주자들의 움직임을 구현하고 출력하는 함수
   - 24가지 야구 상황 적용
   
    1) 주자(8) - 없음, 1루, 2루, 3루, 1-2루, 1-3루, 2-3루, 만루
    2) 아웃카운트(3) - 무사, 1사, 2사

 4) Line 398-430 : 9이닝 동안 실시하며 경기가 종료된 후 총점을 출력하는 함수
 
 5) Line 434-694 : 입력한 라인업에 따라 Simulation이 실행되고 평균 점수를 출력하는 함수


## 2. main.py : Simulation이 진행되는 파일

Code URL : https://github.com/MinJaeKim2796/SL3.0/blob/master/main.py

  1) Line 13 : Simulation을 실행하기 위해서 기본적으로 ‘~lineup.txt’라는 파일이 존재해야 함
   - testlineup.txt, 100lineup.txt 등의 파일이 있어야 하며 실행을 위해 test, 100을 입력
   
   
## 3. samsung.py : 삼성라이온즈 타자들의 타격 및 진루 기록을 크롤링 한 후 9명을 선발해내는 파일

Code URL : https://github.com/MinJaeKim2796/SL3.0/blob/master/samsung.py

 1) Line 7-69 : NC 다이노스 홈페이지에서 타격 기록 크롤링
   - 선수명, 포지션, 타수, 안타, 2루타, 3루타, 홈런, 볼넷, OPS, 병살타

 2) Line 71-84 : 동일 포지션에서 타수가 많은 선수와 지명타자 선발 

 3) Line 124-558, 1160-1194 : 야구 통계 기록 사이트 STATIZ(http://www.statiz.co.kr) 에서 진루 기록 크롤링
   - Out 시 1루 주자가 2루 이상 진루, 2루 주자가 3루 이상 진루, 3루 주자가 홈 진루 / 안타 시 1루 주자가 3루 이상 진루, 2루 주자가 홈 진루 / 2루타 시 1루 주자가 홈 진루에 관한 횟수 및 확률, 병살타 상황 횟수

 4) Line 1299-1309 : samsung.txt에 타격 기록과 진루 기록을 입력
 
 
## 4. test.py : main.py와 동일하게 Simulation이 진행되는 파일

Code URL : https://github.com/MinJaeKim2796/SL3.0/blob/master/test.py

  1) 10,000회 단위로 Simulation이 실행됨(main.py는 1,000,000회 단위로 실행)

  2) main.py는 실행시간이 오래 소요되기 때문에 상대적으로 파일 실행시간을 줄이는 소규모 버전 파일


## 5. visualization.py : Simulation 후 평균 득점을 보여주는 파일

Code URL : https://github.com/MinJaeKim2796/SL3.0/blob/master/visualization.py

  1) Line 3-54 : 감독, 개발자 기준의 라인업으로 Simulation을 진행한 후 각각의 파일에 평균 득점을 저장

  2) Line 58-67 : 저장한 평균 득점 시각화


## 6. visualization2.py : visualization.py와 동일하게 평균 득점을 보여주는 파일

Code URL : https://github.com/MinJaeKim2796/SL3.0/blob/master/visualization2.py

  1) visualization2.py는 감독, 개발자 기준 라인업에 무작위로 선정된 라인업의 Simulation 평균 득점도 시각화 가능
