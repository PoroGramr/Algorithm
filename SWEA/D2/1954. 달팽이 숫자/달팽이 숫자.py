T = int(input())
     # 우, 하, 좌, 상
di = [0,1,0,-1]
dj = [1,0,-1,0]

for t in range(1, T+1):
    n = int(input())
    data = [[0] * n for _ in range(n)]
    i, j, cnt, dr = 0,0,1,0
    data[i][j] = cnt
    cnt += 1

    while cnt <= n * n:
        ni, nj = i + di[dr], j + dj[dr]
        if 0 <= ni < n and 0 <= nj < n and data[ni][nj] == 0:
            i, j  = ni, nj
            data[i][j] = cnt
            cnt += 1
        else:
            dr = (dr + 1) % 4

    
    
    print(f"#{t}")
    for lst in data:
        print(*lst)

