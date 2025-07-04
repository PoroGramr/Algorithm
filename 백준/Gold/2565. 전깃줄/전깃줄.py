n = int(input())

data = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)
data.sort(key = lambda  x: x[0])

lis = []

for a,b in data:
    lis.append(b)
    
dp = [1] * n
for i in range(n):
    for j in range(i):
        if lis[i] > lis[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))