T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    data = []

    for _ in range(N):
        v, c = map(int, input().split())
        data.append((v, c))

    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if data[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - data[i-1][0]] + data[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
    print(f"#{t} {dp[N][K]}")



