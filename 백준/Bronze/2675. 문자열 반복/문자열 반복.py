T = int(input())

for _ in range(1, T + 1):
    N, s = map(str, input().split())
    data = list(s)

    for k in range(len(data)):
        for _ in range(int(N)):
            print(data[k], end="")
    print("")
