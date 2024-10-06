for i in range(1,11):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    big = 0

    # 각 행의 합
    for y in range(100):
        rowSum = 0
        for x in range(100):
            rowSum += data[y][x]
        big = max(rowSum, big)

    # 각 열의 합
    for x in range(100):
        colSum = 0
        for y in range(100):
            colSum += data[y][x]
        big = max(colSum,big)
    
    # 대각선의 합 1.  0,0 -> 99,99
    croosSum1 = 0
    for xy in range(100):
        croosSum1 += data[xy][xy]
    
    big = max(croosSum1, big)

    # 대각선의 합 2. 0,99 -> 99,0
    crossSum2 = 0
    for yx in range(100):
        x == abs(99 - yx)
        crossSum2 += data[yx][x]
    big =  max(crossSum2,big)

    print(f"#{i} {big}")


