N,M = map(int, input().split())

data = list(map(int, input().split()))

s,e = 0,0
sum = data[0]
answer = 0

while True:
    if sum == M:
        answer += 1
    
    if sum >= M:
        s += 1
        sum -= data[s-1]
    else:
        if e == N - 1:
            break
        e += 1
        sum += data[e]


print(answer)