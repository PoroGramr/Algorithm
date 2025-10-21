N = int(input())

data = list(map(int, input().split()))
data.sort()

l,r = 0,N-1
sum = 0

good = float('inf')
answer = [data[0],data[-1]]
while l < r:
    sum = data[l] + data[r]
    
    if abs(sum) < abs(good):
        answer[0] = data[l]
        answer[1] = data[r]
        good = sum
    
    if sum < 0:
        l += 1
    
    else:
        r -= 1
    
answer.sort()
for i in answer:
    print(i, end =" ")
