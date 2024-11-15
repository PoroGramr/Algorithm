T = int(input())

for t in range(1, T + 1):
    N, D = map(int, input().split())


    x = 101

    start = x - D
    end = x + D

    dis = end - start + 1

    if N % dis == 0:
        ans = N // dis
    else:
        ans = N // dis + 1

    print(f"#{t} {ans}")