T = int(input())

for t in range(1, T+1):
    data = list(map(str, input().split()))

    for i in range(len(data)):
        data[i] = data[i][::-1]
    print(*data)