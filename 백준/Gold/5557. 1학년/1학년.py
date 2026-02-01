"""
중간에 나오는 수가 모두 0 이상 20 이하
"""


N = int(input())

data = list(map(int, input().split()))

# dp[i][v] = i번째 수까지 사용해서 값 v를 만드는 경우의 수
dp = [[0 for i in range(21)] for _ in range(N)]

dp[0][data[0]] = 1
numP = data[0]
numM = data[0]


for i in range(1, N-1):
    for v in range(21):
        if dp[i-1][v] > 0:
            numP = v + data[i]
            numM = v - data[i]
            
            if 0 <= numP <= 20:
                dp[i][numP] += dp[i-1][v]

            if 0 <= numM <= 20:
                dp[i][numM] += dp[i-1][v]

print(dp[N - 2][data[-1]])