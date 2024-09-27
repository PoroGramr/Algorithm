from collections import deque


def dfs(i,j):
    q = deque()
    v[i][j] = 1
    count = 1           # 세대수를 카운트하기 위한 변수
    q.append((i,j))
    while q:
        ci,cj = q.popleft()
        for pi,pj in ((0,1), (0,-1),(1,0), (-1,0)): # 위,아래,오른,왼 모든 방향을 체크한다
        
            ni, nj = ci + pi, cj + pj
            
            # 방향의 좌표가 데이터 내에 위치하고, 데이터에서는 1이며(집이먀), 아직 방문하지 않은(카운트하지 않은)세대일 경우
            if 0 <= nj < N and 0 <= ni < N and v[ni][nj] == 0 and data[ni][nj] == 1:
                count += 1
                q.append((ni,nj))
                v[ni][nj] = 1
    return count
        
        
    

N = int(input())

data = [list(map(int, input())) for _ in range(N)]  # 입력 데이터 리스트
v = [([0] * N)  for _ in range(N)]                  # 방문 리스트
answer = []


for i in range(N):
    for j in range(N):
        
        # 데이터가 1이고 아직 방문하지 않은 점이라면 dfs 함수로 향한다.
        if data[i][j] == 1 and v[i][j] == 0:
            
            # dfs함수는 단지별 세대수를 리턴
            answer.append(dfs(i,j))
    
# 요구사항에 따라 길이를 먼저 출력하고 리스트의 요소들을 출력한다        
print(len(answer))
answer.sort()
for k in answer:
    print(k)
        
