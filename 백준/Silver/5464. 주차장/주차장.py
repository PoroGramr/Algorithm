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
inout = []

wait = deque()

for _ in range(M * 2):
    inout.append(int(input()))


park = []

parkCar = [-1 for _ in range(N)] 
# 주차장 빈자리 번호
for i in range(N):
    heapq.heappush(park,i)


answer = 0


for cmd in inout:
    if cmd > 0:
        if park:
            parkNum = heapq.heappop(park)
            parkCar[parkNum] = cmd
    
        else:
            wait.append(cmd)

    else:
        for i in range(N):
            if parkCar[i] == -cmd:
                answer += cost[i] * car[(-cmd) - 1]
                heapq.heappush(park, i)
                parkCar[i] = -1

                if wait:
                    next = wait.popleft()
                    ni = heapq.heappop(park)
                    parkCar[ni] = next
                
                break
    
print(answer)
            



