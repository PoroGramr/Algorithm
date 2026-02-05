N, S = map(int, input().split())

data = list(map(int, input().split()))

l,r = 0,0

answer = float('inf')


tmpSum = data[0]

while l < N and r < N:
    if tmpSum >= S:
        answer = min((r - l + 1), answer)
        tmpSum -= data[l]
        l += 1
        
    else:
        r += 1
        if r < N:
            tmpSum += data[r]

if answer == float('inf'):
    print(0)
else:
    print(answer)        
    