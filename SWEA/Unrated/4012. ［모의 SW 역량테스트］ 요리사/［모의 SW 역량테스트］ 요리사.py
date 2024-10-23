def dfs(n,alst, blst):
    global ans
    if n == N:
        if len(alst) == M:
            asum = bsum = 0
            for i in range(M):
                for j in range(M):
                    asum += data[alst[i]][alst[j]]
                    bsum += data[blst[i]][blst[j]]
            ans = min(ans, abs(asum-bsum))

        return
    
    dfs(n+1, alst+[n], blst)

    dfs(n+1, alst, blst+[n])








T = int(input())

for t in range(1, T+1):
    N = int(input())
    M = N // 2
    data  = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    
    ans = 20000 * N * N

    dfs(0,[],[])

    print(f"#{t} {ans}")