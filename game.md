# game.py : main.py에서 import되는 파일

Code URL : https://github.com/MinJaeKim2796/SL3.0/blob/master/game.py

 1) Line 16-41 : 타격 기록이 들어가도록 하는 Class
 
 2) Line 57-105 : samsung.txt 파일을 열어 진루 기록을 비어있는 Dict에 넣음

 3) Line 142-396 : 타격 결과로 인한 주자들의 움직임을 구현하고 출력하는 함수
   - 24가지 야구 상황 적용 : 주자(8) - 없음, 1루, 2루, 3루, 1-2루, 1-3루, 2-3루, 만루 / 아웃카운트(3) - 무사, 1사, 2사

 4) Line 398-430 : 9이닝 동안 실시하며 경기가 종료된 후 총점을 출력하는 함수
 
 5) Line 434-694 : 입력한 라인업에 따라 Simulation이 실행되고 평균 점수를 출력하는 함수
