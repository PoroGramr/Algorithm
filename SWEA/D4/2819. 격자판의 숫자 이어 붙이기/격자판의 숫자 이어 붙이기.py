def dfs(n, num, y, x):
    if n == CNT:
        sset.add(num)
        return

    for py, px in ((0,1), (0,-1), (1,0), (-1,0)):
        ny , nx = y + py, x + px

        if 0 <= ny < N and 0 <=nx < N:
            dfs(n+1, num*10 + data[ny][nx], ny, nx)


T = int(input())

for i in range(1, T+1):
    N , CNT = 4, 7
    data = [list(map(int, input().split())) for _ in range(N)]

    sset  = set()

    # 가능한 모든 위치 순회

    for y in range(N):
        for x in range(N):
            dfs(1, data[y][x], y, x)
    print(f"#{i} {len(sset)}")

