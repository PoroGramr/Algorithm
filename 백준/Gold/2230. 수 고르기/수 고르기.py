N, M = map(int, input().split())

data = []

for _ in range(N):
    data.append(int(input()))


data.sort()

l,r = 0, 0
answer = float('inf')
while l < N and r < N:
    diff = data[r] - data[l]
    
    if diff >= M:
        answer = min(diff, answer)
        l += 1
    else:
        r += 1


print(answer)    
    
    
    