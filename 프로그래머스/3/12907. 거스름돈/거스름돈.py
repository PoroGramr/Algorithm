"""
5, [    1,  2, 5]

0:      1    
1:      1
2:      1
3:      1 + 1 dp[3] += dp[1]
4:      1 + 2 dp[4] += dp[2]
5:      1 + 2 + 1 dp[5] +=dp[3]

5원 = 3원만드는 방법 + 2원 만드는 방법
for coins
dp[i] = dp[i] + dp[i-coin]
"""
def solution(n, money):
    answer = 0
    
    memo = [0] * (n + 1)
    
    # 0원을 만드는 방법은 1가지
    memo[0] = 1
    
    for coin in money:
        for i in range(coin, n+1): # 1 ~ 5 2 ~ 5 5 ~ 5
            memo[i] = memo[i] + memo[i - coin]
    answer = memo[i] %1_000_000_007 
    return answer