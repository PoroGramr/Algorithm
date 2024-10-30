#    # 상,하,좌,우
di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]
     # 반대방향에 대한 인덱스
tb = [0,2,1,4,3]

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        # 1. 1칸 이동처리, 경계면이라면 -> //2, 방향 반대 처리
        for i in range(len(data)):
            # [0]:i [1]:j, [2]:n, [3]:dr
            data[i][0] = data[i][0] + di[data[i][3]]
            data[i][1] = data[i][1] + dj[data[i][3]]
            # 만약 다음 이동 좌표가 경계면이라면
            if data[i][0] == 0 or data[i][0] == N - 1 or data[i][1] == 0 or data[i][1] == N - 1:
                data[i][2] //= 2
                data[i][3] = tb[data[i][3]]
        # 2. 내림차순 정렬
        data.sort(key = lambda  x : (x[0], x[1], x[2]), reverse = True)

        # 3. 같은 좌표 합치기
        i = 1
        while i < len(data):
            if data[i-1][0:2] == data[i][0:2]:
                data[i-1][2] += data[i][2]
                data.pop(i)
            else:
                i += 1




    ans  = 0
    for lst in data:
        ans += lst[2]

    print(f"#{t} {ans}")
