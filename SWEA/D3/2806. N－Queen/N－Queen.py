def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        #   N * N 에서 우측 상향 대각선 -> 합이 같음
        #     ""  에서 좌측 상향 대각선 -> 차가 같음
        if v1[j]==v2[n+j]==v3[n-j] == 0:
            v1[j]=v2[n+j]=v3[n-j] = 1
            dfs(n+1)
            v1[j]=v2[n+j]=v3[n-j] = 0
            


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = 0
    # v 배열 3개 : 열, 대각선 2개
    v1, v2,v3 = [[0] * (2*N) for _ in range(3)]
    """
    v1 = [0, 0]
    v2 = [0, 0]
    v3 = [0, 0]
    """
    
    dfs(0)

    print(f"#{t} {ans}")
    

