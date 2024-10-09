for i in range(1, 11):
    N = int(input())

    data = [list(map(str, input())) for _ in range(8)]
    
    count = 0

    if N == 1:
        count = 64

    else:

        # 가로
        for y in range(8):
            for x in range(0, 8-N + 1):
                ori = ""
                for a in range(x, x+N):
                    ori += data[y][a]
            
                oriR = ori[::-1]
                if ori == oriR:
                    count += 1

        # 세로
        for x in range(8):
            for y in range(0, 8-N + 1):
                ori = ""
                for b in range(y, y+N):
                    ori  += data[b][x]
            
                oriR = ori[::-1]
                
                if ori == oriR:
                    
                    count += 1

    print(f"#{i} {count}")