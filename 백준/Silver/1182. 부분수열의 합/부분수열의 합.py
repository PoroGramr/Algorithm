from collections import defaultdict

n, S = map(int, input().split())

data = list(map(int, input().split()))

dp = defaultdict(int)
dp[0] = 1


for x in data:
    ndp = defaultdict(int)
    
    for s, cnt in dp.items():
        ndp[s] += cnt
        ndp[s + x] += cnt
    
    dp = ndp


ans = dp[S]
if S == 0:
    ans -= 1
print(ans)