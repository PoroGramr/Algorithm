T = int(input())

for t in range(1, T+1):
    data = []
    for _ in range(9):
        data.append(list(map(int, input().split())))
    ans = -1
    for i in range(9):
        count = set()
        for j in range(9):
            count.add(data[i][j])
        if len(count) == 9:
            continue
        else:
            ans = 0
            break
    if ans != 0:

        for j in range(9):
            count = set()
            for i in range(9):
                count.add(data[i][j])
            
            if len(count) == 9:
                continue
            else:
                ans = 0
                break
    
    if ans != 0:
        for i in range(0, 8,3):
            count = set()
            for y in range(i,i+3):
                for x in range(i, i + 3):
                    count.add(data[y][x])

            if len(count) == 9:
                ans = 1
                continue
            else:
                ans = 0
                break
    
    if ans != 0:
        for i in range(0, 8,3):
            count = set()
            for y in range(i,i+3):
                for x in range(3, 6):
                    count.add(data[y][x])

            if len(count) == 9:
                ans = 1
                continue
            else:
                ans = 0
                break

    if ans != 0:
        for i in range(0, 8,3):
            count = set()
            for y in range(i,i+3):
                for x in range(6, 9):
                    count.add(data[y][x])

            if len(count) == 9:
                ans = 1
                continue
            else:
                ans = 0
                break



    print(f"#{t} {ans}")
