"""
dp[1] = 1
dp[2] = 2
dp[3] = 3

dp[n] = dp[n-1] + dp[n-2]
"""
def solution(n):
    
    dp = [-1] * n
    dp[0] = 1
    dp[1] = 2
    
    if n <= 2:
        return n
    
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] = dp[i] % 1_000_000_007
    
    answer = dp[n-1]
    return answer