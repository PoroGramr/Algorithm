# BFS

from collections import deque


def bfs(i,j):
    # count를 전역 변수로 받음
    global count
    
    # bfs 함수가 실행될때마다 카운트 +1
    count += 1
    v[i][j] = 1
    for pi,pj in ((1,0), (-1,0), (0,1), (0,-1)):
        ci, cj = i + pi, j + pj
        if 0 <= ci < N and 0 <= cj < N and data[ci][cj] == 1 and v[ci][cj] == 0:
            bfs(ci,cj)
        
N = int(input())

data = [list(map(int, input())) for _ in range(N)]  # 입력 데이터 리스트
v = [([0] * N)  for _ in range(N)]                  # 방문 리스트
answer = []


for i in range(N):
    for j in range(N):
        
        # 데이터가 1이고 아직 방문하지 않은 점이라면 bfs 함수로 향한다.
        if data[i][j] == 1 and v[i][j] == 0:
            
            # 세대수 체크를 위한 count 변수 초기화
            # bfs 함수가 실행되기 직전마다 초기화됨, 이후 bfs 함수에서 전역 변수로 사용
            count = 0
            
            # bfs로 count 변수 값을 설정(단지별 세대수) 
            bfs(i,j)
            
            # bfs로 계산한 단지별 세대수를 리턴
            answer.append(count)
    
# 요구사항에 따라 길이를 먼저 출력하고 리스트의 요소들을 출력한다        
print(len(answer))
answer.sort()
for k in answer:
    print(k)
        
