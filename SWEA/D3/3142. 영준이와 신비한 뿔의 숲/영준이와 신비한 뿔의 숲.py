T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    y = 2*M - N

    x = N -M

    print(f"#{t} {y} {x}")







