def rotate(data):
    dataR = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dataR[i][j] = data[N-1-j][i]

    return dataR



T = int(input())

for t in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    data1 = rotate(data)
    data2 = rotate(data1)
    data3 = rotate(data2)
    print(f"#{t}")
    for a,b,c in zip(data1, data2, data3):
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}')
