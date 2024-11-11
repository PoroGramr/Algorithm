T = int(input())

for t in range(1, T + 1):
    H, W = map(int, input().split()) # 높이, 너비

    data = []
    for _ in range(H):
        data.append(list(map(str, input())))

    commandLen = int(input())

    commands = list(map(str, input()))

    # 현재 전차의 좌표와 바라보는 방향를 저장
    # 바라보는 방향은 1: 상, 2 : 하 , 3 : 좌, 4 : 우
    cy, cx, cp = 0, 0, 0

    # 현재 전차의 좌표와 바라보는 방향을 찾아 저장
    for y in range(H):
        for x in range(W):
            # 상
            if data[y][x] == "^":
                cy = y
                cx = x
                cp = 1
                break
            # 하
            elif data[y][x] == "v":
                cy = y
                cx = x
                cp = 2
                break
            # 좌
            elif data[y][x] == '<':
                cy = y
                cx = x
                cp = 3
                break
            # 우
            elif data[y][x] == ">":
                cy = y
                cx = x
                cp = 4
                break



    # 명령어가 다 실행될 때 까지 반복
    while commands:
        com = commands.pop(0)

        # Shoot
        if com == "S":
            # 전차가 상 방향을 바라봄
            if cp == 1:
                for findWall in range(cy - 1, -1, -1):
                    # 벽돌 벽을 만날 경우
                    if data[findWall][cx] == "*":
                        data[findWall][cx] = "."
                        break
                    # 강철 벽을 만날 경우
                    elif data[findWall][cx] == "#":
                        break

            # 전차가 하 방향을 바라봄
            elif cp == 2:
                for findWall in range(cy + 1, H):
                    # 벽돌 벽을 만날 경우
                    if data[findWall][cx] == "*":
                        data[findWall][cx] = "."
                        break
                    # 강철 벽을 만날 경우
                    elif data[findWall][cx] == "#":
                        break

            # 전차가 좌 방향을 바라봄
            elif cp == 3:
                for findWall in range(cx - 1, -1, -1):
                    # 벽돌 벽을 만날 경우
                    if data[cy][findWall] == "*":
                        data[cy][findWall] = "."
                        break
                    # 강철 벽을 만날 경우
                    elif data[cy][findWall] == "#":
                        break

            # 전차가 우 방향을 바라봄
            elif cp == 4:
                for findWall in range(cx + 1, W):
                    # 벽돌 벽을 만날 경우
                    if data[cy][findWall] == "*":
                        data[cy][findWall] = "."
                        break
                    # 강철 벽을 만날 경우
                    elif data[cy][findWall] == "#":
                        break

        # Up
        elif com == "U":
            cp = 1
            data[cy][cx] = "^"
            ny, nx = cy - 1, cx

            if 0 <= ny < H and 0 <= nx < W and data[ny][nx] == ".":
                data[ny][nx], data[cy][cx] = data[cy][cx], data[ny][nx]
                cy, cx = ny, nx

        # Down
        elif com == "D":
            cp = 2
            data[cy][cx] = "v"
            ny, nx = cy + 1, cx

            if 0 <= ny < H and 0 <= nx < W and data[ny][nx] == ".":
                data[ny][nx], data[cy][cx] = data[cy][cx], data[ny][nx]
                cy, cx = ny, nx

        # Left
        elif com == "L":
            cp = 3
            data[cy][cx] = "<"
            ny, nx = cy , cx - 1

            if 0 <= ny < H and 0 <= nx < W and data[ny][nx] == ".":
                data[ny][nx], data[cy][cx] = data[cy][cx], data[ny][nx]
                cy, cx = ny, nx

        #Right
        elif com == "R":
            cp = 4
            data[cy][cx] = ">"
            ny, nx = cy , cx + 1

            if 0 <= ny < H and 0 <= nx < W and data[ny][nx] == ".":
                data[ny][nx], data[cy][cx] = data[cy][cx], data[ny][nx]
                cy, cx = ny, nx






    print(f"#{t} ", end="")
    for lst in data:
        print("".join(lst))



