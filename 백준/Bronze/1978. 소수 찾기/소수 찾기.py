def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())

data = list(map(int, input().split()))

answer = 0

for a in range(N):
    num = data[a]
    
    if num == 1:
        continue
    else:
        if isPrime(num):
            answer += 1

print(answer)