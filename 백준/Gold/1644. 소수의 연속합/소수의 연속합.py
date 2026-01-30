n = int(input())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, n + 1) if is_prime[i]]

l, r = 0,0
cSum  = 0
answer = 0

while r < len(primes):
    cSum += primes[r]
    
    while cSum >= n:
        if cSum == n:
            answer += 1
        cSum -= primes[l]
        l += 1

    r += 1


print(answer)
    