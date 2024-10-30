from collections import deque

def bfs(tlst):
    # 1. 3개의 좌표를 1로 저장(벽으로 변경)
    for i,j in tlst:
        data[i][j] = 1

    # 2. 변수 생성 및 큐 초기화
    q = deque()
    w = [[0] * M for _ in range(N)]
    cnt = CNT - 3 # 남은 0의 개수 (max값을 찾을 변수)
    for ti,tj in vir:
        q.append((ti,tj))
        w[ti][tj] = 1

    # 3. 큐에 데이터 있는 동안 한개 꺼내서 처리
    while q:
        ci, cj = q.popleft()

        # 3.1 4방향 범위내 미방문 칸 바이러스 감염
        for pi, pj in ((-1,0), (1,0), (0,-1),(0,1)):
            ni,nj = ci +pi, cj + pj

            if 0 <= ni < N and 0 <= nj < M and data[ni][nj]  == 0 and w[ni][nj] == 0:
                q.append((ni,nj))
                w[ni][nj] = 1
                cnt -= 1
    # 4. 벽 원상복구
    for i, j in tlst:
        data[i][j] = 0

    return cnt

# def dfs(n, tlst):
#     global ans
#
#     if n == 3: # 3개의 좌표를 모두 선택한 경우
#         ans = max(ans, bfs(tlst))
#         return
#
#     for i in range(CNT):
#         if v[i] == 0:
#             v[i] = 1
#             dfs(n+1, tlst+[blk[i]])
#             v[i] = 0


N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

# 1. 빈칸위치, 바이러스 위치를 저장
blk = []
vir = []

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            blk.append((i,j))
        elif data[i][j] == 2:
            vir.append((i,j))

CNT = len(blk)
v = [0] * CNT
ans = 0
# 1. 백트래킹으로 풀이
# dfs(0,[])
# print(ans)

# 2 루프 CNT개 중에 3개를 선택(가능한 모든 조합)
for i in range(CNT - 2):
    for j in range(i+1, CNT - 1):
        for k in range(j + 1, CNT):
            ans = max(ans, (bfs([blk[i], blk[j], blk[k]])))
print(ans)

