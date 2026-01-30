N, M = map(int, input().split())

data = list(map(int,input().split()))
    

l,r = 0,0
cSum = 0
answer = float('inf')
while r < N:
    cSum += data[r]
    
    while cSum >= M:
        answer = min(answer, r - l + 1)
        cSum -= data[l]
        l += 1
        
    
    r += 1


print(answer if answer != float('inf') else 0)