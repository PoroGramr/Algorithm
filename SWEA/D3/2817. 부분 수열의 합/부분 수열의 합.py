def check(i,n):
    global ans
    v = [0] * (N + 1)
    if n == K:
        ans += 1
        return
    elif n > K:
        return

    if i + 1 <= len(data):
        check(i+1, n+data[i])

        check(i + 1, n)
    





T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))

    ans = 0 
    check(0,0)  # index, sum
    print(f"#{t} {ans}")