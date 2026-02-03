"""
N : 주차 공간의 수 , M : 차량의 수
N개의 줄동안 주차 공간들의 단위 무게당 요금 s의 단위 무게당 요금 Rs
다음 M개의 줄에는 차량들의 무게를 나타내는 정수들이 주어진다. 1 ~ M까지 번호로 구분
출입순서와는 상관 x
그 다음 2m개의 줄에는 차량들의 주차장 출입 순서를 나타내는 정수들이 한줄씩
양의 정수는 입장
음의 정수는 출차

"""

import sys,heapq
from collections import deque
input = sys.stdin.readline

# N : 주차 공간의 수 , M : 차량의 수
N, M = map(int, input().split())

#주차 공간들의 단위 무게당 요금
cost = []
for _ in range(N):
    cost.append(int(input()))

# 차량들의 무게 1~M까지 번호로 구분
car = []
for _ in range(M):
    car.append(int(input()))

# 차량들의 입출차 내역
q = deque()
wait = deque()
for _ in range(M * 2):
    q.append(int(input()))

park = [-1 for _ in range(N)]
emptyPark = N

answer = 0

while q:
    
    crt = q.popleft()
    # 차가 출입
    if crt > 0:
        
        # 주차장에 빈자리가 있다면
        if emptyPark > 0 :
            emptyPark -= 1
            
            # 빈자리에 주차
            for i in range(N):
                if park[i] == -1:
                    park[i] = crt
                    break

        # 주차장에 빈자리가 없다면
        else:
            wait.append(crt)
            
        continue
        

    # 차가 출차
    else:
        for i in range(N):
            # 주차장 출차 처리
            if park[i] == -crt:
                park[i] = -1
                emptyPark += 1
                answer += car[(-crt) - 1] * cost[i]
                if wait:
                    waitCar = wait.popleft()
                    park[i] = waitCar
                    emptyPark -= 1
            
                break  
        continue           
    
print(answer)
            



