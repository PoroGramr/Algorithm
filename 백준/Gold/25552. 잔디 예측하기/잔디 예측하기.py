import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    before = [list(input().strip()) for _ in range(N)]
    D = int(input().strip())
    after  = [list(input().strip()) for _ in range(N)]

    # 1) 초기 잔디가 사라졌다면 즉시 불가능
    for i in range(N):
        for j in range(M):
            if before[i][j] == 'O' and after[i][j] == 'X':
                print("NO")
                return

    # 2) 초기 'O'를 시작점으로 하고, 최종 격자에서 'O'인 칸만 확산 대상으로 BFS
    vis = [[False]*M for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if before[i][j] == 'O':
                vis[i][j] = True
                q.append((i, j))

    # 맨해튼 거리 ≤ D인 후보 좌표를 사각형 범위 내에서 검사
    while q:
        x, y = q.popleft()
        # 사각형 경계로 먼저 제한
        x_min = max(0, x - D)
        x_max = min(N - 1, x + D)
        y_min = max(0, y - D)
        y_max = min(M - 1, y + D)

        for nx in range(x_min, x_max + 1):
            # 맨해튼 거리로 추가 필터링
            rem = D - abs(nx - x)
            # |ny - y| <= rem  →  y - rem <= ny <= y + rem
            ny_lo = max(y_min, y - rem)
            ny_hi = min(y_max, y + rem)
            # 위에서 y_min/y_max로 자른 뒤 다시 좁혔으니 구간만 훑으면 됨
            for ny in range(ny_lo, ny_hi + 1):
                if not vis[nx][ny] and after[nx][ny] == 'O':
                    vis[nx][ny] = True
                    q.append((nx, ny))

    # 3) 최종 격자의 'O'가 하나라도 미방문이면 불가능
    for i in range(N):
        for j in range(M):
            if after[i][j] == 'O' and not vis[i][j]:
                print("NO")
                return

    print("YES")

if __name__ == "__main__":
    solve()