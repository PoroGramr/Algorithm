import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

# 1. 왼쪽 -> 오른쪽으로 LIS 계산
increase_dp = [1] * n
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

# 2. 오른쪽 -> 왼쪽으로 LDS 계산 (실제로는 뒤집은 배열의 LIS)
decrease_dp = [1] * n
for i in range(n - 1, -1, -1): # n-1부터 0까지 역순으로
    for j in range(n - 1, i, -1): # n-1부터 i+1까지 역순으로
        if data[i] > data[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

# 3. 두 DP 테이블을 합쳐서 바이토닉 수열 길이 계산
result_dp = [0] * n
for i in range(n):
    # data[i]가 산봉우리이므로 중복 계산되어 1을 빼준다.
    result_dp[i] = increase_dp[i] + decrease_dp[i] - 1

print(max(result_dp))