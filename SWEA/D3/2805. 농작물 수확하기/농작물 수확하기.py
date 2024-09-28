n = int(input())

for i in range(n):
    le = int(input())
    answer = 0
    
    data =[list(map(str, input())) for _ in range(le)]
    if len(data) == 1:
        answer = int(data[0][0])
    else:
        cen = le // 2

        # 상단
        for t in range(0, cen):
            for p in range(cen -t , cen + t + 1):
                answer += int(data[t][p])

        # 중간
        for k in data[cen]:
            answer += int(k)

        # 하단
        for b in range(cen + 1, le):
            cb = le - b
            for m in range(cen - cb + 1, cen + cb):
                answer += int(data[b][m])
            
    print(f"#{i+1} {answer}")