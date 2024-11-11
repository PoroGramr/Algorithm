T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    data = [[0] * (N + 1) for _ in range(N + 1)]
    m = N // 2

    data[m][m] = data[m+1][m+1] = 2
    data[m][m+1] = data[m+1][m] = 1
    bcnt = wcnt = 0
    
    for _ in range(M):
        si, sj, d = map(int, input().split())
        data[si][sj] = d
        
        for di, dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
            r = []
            for mul in range(1, N):
                ni ,nj = si + di * mul, sj + dj * mul
                if 1 <= ni <= N and 1 <= nj <= N:
                    if data[ni][nj] == 0:
                        break
                    elif data[ni][nj] == d:
                        while r:
                            ti, tj = r.pop()
                            data[ti][tj] = d
                        break
                    else:
                        r.append((ni,nj))
                else:
                    break

    for lst in data:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f"#{t} {bcnt} {wcnt}")