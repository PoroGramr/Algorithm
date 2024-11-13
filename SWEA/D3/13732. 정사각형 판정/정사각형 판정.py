
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
    check = True
    
    if maxX - minX != maxY - minY:
        check = False
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


