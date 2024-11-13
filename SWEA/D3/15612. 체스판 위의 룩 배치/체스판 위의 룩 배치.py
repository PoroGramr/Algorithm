T = int(input())

for t in range(1, T + 1):
    data = []

    for _ in range(8):
        data.append(list(map(str, input())))

    lookCount = 0
    lookXY = []
    isTrue = False

    # 룩 개수 카운트
    for i in range(8):
        for j in range(8):
            if data[i][j] == "O":
                lookCount += 1
                lookXY.append((i,j))
    
    # 룩의 개수가 8개일 경우에만 다음 행렬 체크 진행
    if lookCount == 8:
        isTrue = True
    
    
    # 행렬 체크
    if isTrue:
        for cy, cx in lookXY:
            for p in range(0, 8):
                
                # cy, cx 본인 좌표는 탐색하지 않아야 함
                if p != cx and data[cy][p] == "O":
                    isTrue = False
                if p != cy and data[p][cx] == "O":
                    isTrue = False

    # 모든 조건을 만족시 isTrue 는 True
    if isTrue:
        print(f"#{t} yes")
    else:
        print(f"#{t} no")



