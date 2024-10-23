def dfs(n,alst, blst):
    global ans
    if n == N:
        if len(alst) == M: # a음식에 선택된 재료의 개수가 절반일 경우
            asum = bsum = 0 # 음식맛의 합 구하기
            for i in range(M):
                for j in range(M):
                    asum += data[alst[i]][alst[j]]
                    bsum += data[blst[i]][blst[j]]
            ans = min(ans, abs(asum - bsum))
        return

    # a음식에 추가
    dfs(n+1, alst+[n], blst)
    # b음식에 추가
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