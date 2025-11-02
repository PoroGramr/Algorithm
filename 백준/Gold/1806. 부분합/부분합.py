N, S = map(int, input().split())

data = list(map(int, input().split()))

left = 0
cur = 0
ans = float("inf")


for right in range(N):
    cur += data[right]
    
    while cur >= S:
        ans = min(ans, right - left + 1)
        cur -= data[left]
        left += 1

print(0 if ans == float('inf') else ans)