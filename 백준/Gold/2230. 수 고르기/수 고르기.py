N,M = map(int, input().split())

data = []

for _ in range(N):
    data.append(int(input()))


data.sort()

answer = float('inf')

l,r = 0,0


while l < N and r < N:
    diff = data[r] - data[l]
    
    if diff >= M:
        answer = min(answer, diff)
        l += 1
    else:
        r += 1
    
    

print(answer)