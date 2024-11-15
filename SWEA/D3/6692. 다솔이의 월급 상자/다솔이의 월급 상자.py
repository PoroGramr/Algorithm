T = int(input())

for t in range(1, T + 1):
    N = int(input())

    data = []
    count = 0.000000
    for _ in range(N):
        a, b = map(float, input().split())
        count += a*b

    print(f"#{t} {count}")
