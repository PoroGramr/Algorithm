def dfs(num, y,x,s):
    if num == 7:
        nums.add(int(s))
        return

    for py, px in ((0,-1),(0,1),(1,0),(-1,0)):
        ny, nx = y + py, x + px
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(num + 1, ny,nx, s + str(data[ny][nx]))

T = int(input())

for t in range(1, T + 1):
    data = []

    for _ in range(4):
        data.append(list(map(int, input().split())))

    nums = set()
    for i in range(4):
        for j in range(4):
            dfs(1, i,j,str(data[i][j]))

    ans = len(nums)
    print(f"#{t} {ans}")