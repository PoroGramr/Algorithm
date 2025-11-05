N = int(input())

data = list(map(int, input().split()))

data.sort()

l,r = 0 , N - 1

answer = data[l] + data[r]
mix = [data[l], data[r]]

while l < r:
    curSum = data[l] + data[r]
    
    if abs(curSum) < abs(answer):
        mix[0] = data[l]
        mix[1] = data[r]
        answer = curSum
    
    if curSum < 0:
        l += 1
    
    else:
        r -= 1

mix.sort()

for m in mix:
    print(m, end = " ")