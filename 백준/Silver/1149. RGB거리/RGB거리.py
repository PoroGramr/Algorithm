N = int(input())

dp = [[0,0,0] for _ in range(N)]

home = []

for _ in range(N):
    home.append(list(map(int, input().split())))

dp[0][0] = home[0][0]
dp[0][1] = home[0][1]
dp[0][2] = home[0][2]

for i in range(1,N):
    dp[i][0] = home[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = home[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = home[i][2] + min(dp[i-1][0], dp[i-1][1])
    

answer = min(dp[N-1])

print(answer)