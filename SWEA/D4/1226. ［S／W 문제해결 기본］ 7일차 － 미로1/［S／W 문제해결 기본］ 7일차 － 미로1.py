def dfs(y, x):
    global ans

    for py, px in ((0,1), (0,-1), (1,0), (-1,0)):
        ny, nx = y + py, x + px

        if data[ny][nx] == 3:
            ans = 1
            return

        if 0 <= ny < 16 and 0 <= nx < 16 and data[ny][nx] == 0 and v[ny][nx] == 0:
            v[ny][nx] = 1
            dfs(ny,nx)
            v[ny][nx] = 0

        
for _ in range(1, 11):
    T = int(input())

    data = [list(map(int, input())) for _ in range(16)]
    v = [[0] * 16 for _ in range(16)]
    ans = 0

    dfs(1,1)

    print(f"#{T} {ans}")