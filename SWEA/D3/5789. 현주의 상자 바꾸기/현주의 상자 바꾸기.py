T = int(input())

for t in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * (N + 1) # 0번 상자는 폐기할거임

    task = []
    for i in range(1, Q + 1):
        L , R = map(int ,input().split())
        for k in range(L ,R + 1):
            box[k] = i

    answer = box[1::]

    print(f"#{t} ", end="")
    print(*answer)


