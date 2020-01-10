import game

#import time

n = int( input("몇 개의 라인업을 실행하시겠습니까? ") )
m = int( input("몇 번 실행하시겠습니까?(x10000) ") )

print("라인업 이름을 입력하세요.(엔터키로 구분)")

E=list()

for i in range(0,n):
    E.append( input("Who\'s lineup? ") + 'lineup.txt' )

for i in range(0,n):
    for j in range(0,m):
        game.test(E[i])
