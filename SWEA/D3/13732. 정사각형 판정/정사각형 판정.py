
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = []

    for _ in range(N):
        data.append(list(map(str, input())))
    minX = minY = 99
    maxX = maxY = -1

    for y in range(N):
        for x in range(N):
            if data[y][x] == "#":
                minX = min(minX,x)
                minY = min(minY,y)

                maxX = max(maxX,x)
                maxY = max(maxY,y)
    
    # 정사각형인지 확인
    check = True
    
    # 서로 길이의 차가 다르면 정사각형이 아님
    if maxX - minX != maxY - minY:
        check = False
    
    # 좌표안이 모둔 "#"인지 확인
    else:
        for i in range(minY, maxY + 1):
            for j in range(minX, maxX + 1):
                if data[i][j] != "#":
                    check = False
                    break
            if not check:
                break

    if check:
        print(f"#{t} yes")
    else:
        print(f"#{t} no")


