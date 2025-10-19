def solution(m, n, puddles):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    puset = {(y,x) for x,y in puddles}
    dp[1][1] = 1
    for y in range(1,n + 1):
        for x in range(1, m + 1):
            if (y,x) in puset or (y == 1 and x == 1):
                continue
            dp[y][x] = (dp[y][x-1] + dp[y-1][x]) % 1000000007
            
            
    answer = dp[n][m]
    return answer