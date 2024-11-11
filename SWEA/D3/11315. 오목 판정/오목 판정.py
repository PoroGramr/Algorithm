T = int(input())

for t in range(1, T + 1):
    N = int(input())
    data = []

    for _ in range(N):
        data.append(list(map(str, input())))
    answerCheck = False

    # 가로
    for y in range(N):
        for x in range(N + 1 - 5):

            if data[y][x] == "o" and data[y][x+1] == "o" and data[y][x+2] == "o" and data[y][x+3] == "o" and data[y][x+4] == "o":
                answerCheck = True
                break

    # 세로
    for y in range(N + 1 - 5):
        for x in range(N):
            if data[y][x] == "o" and data[y + 1][x] == "o" and data[y + 2][x] == "o" and data[y + 3][x] == "o" and \
                    data[y + 4][x] == "o":
                answerCheck = True
                break

    # 대각선 좌->우
    for y in range(N + 1 - 5):
        for x in range(N + 1 - 5):
            if data[y][x] == "o" and data[y+1][x+1] == "o" and data[y+2][x+2] == "o" and data[y+3][x+3] == "o" and data[y+4][x+4] == "o":
                answerCheck = True
                break

    # 대각선 우 -> 좌

    for y in range(4,N):
        for x in range(N + 1 - 5):
            if data[y][x] == "o" and data[y - 1][x + 1] == "o" and data[y - 2][x + 2] == "o" and data[y - 3][x + 3] == "o" and data[y - 4][x + 4] == "o":
                answerCheck = True
                break





    if answerCheck:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")