N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# dp[y][x][d]
# d = 0: 가로, 1: 세로, 2: 대각선
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 시작 상태: (0,0)-(0,1), 끝점 (0,1), 가로
dp[0][1][0] = 1

for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            continue

        # 가로
        if x - 1 >= 0:
            dp[y][x][0] += dp[y][x-1][0] + dp[y][x-1][2]

        # 세로
        if y - 1 >= 0:
            dp[y][x][1] += dp[y-1][x][1] + dp[y-1][x][2]

        # 대각선
        if y - 1 >= 0 and x - 1 >= 0:
            if board[y-1][x] == 0 and board[y][x-1] == 0:
                dp[y][x][2] += (
                    dp[y-1][x-1][0]
                    + dp[y-1][x-1][1]
                    + dp[y-1][x-1][2]
                )

# 도착 지점에서 세로 + 대각선
print(
    dp[N-1][N-1][0]
  + dp[N-1][N-1][1]
  + dp[N-1][N-1][2]
)