di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]
tb = [0,2,1,4,3]

T = int(input())

for t in range(1, T+1):
    # 한변의 있는 셀의 개수, 격리 시간, 미생물 군집의 개수
    N, M, K = map(int, input().split())

    # i,j, 미생물 수, 이동 방향
    data = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):
        for i in range(len(data)):
            data[i][0] = data[i][0] + di[data[i][3]]
            data[i][1] = data[i][1] + dj[data[i][3]]
            # 만약 경계선 이라면
            if data[i][0] == 0 or data[i][0] == N - 1 or data[i][1] == 0 or data[i][1] == N -1:
                # 군집의 수 절반
                data[i][2] //= 2

                # 이동 방향 반대
                data[i][3] = tb[data[i][3]]


        data.sort(key = lambda x : (x[0],x[1], x[2]), reverse = True)

        i = 1
        while i < len(data):
            if data[i- 1][0:2] == data[i][0:2]:
                data[i-1][2] += data[i][2]
                data.pop(i)
            else:
                i += 1

    ans = 0
    for a in data:
        ans += a[2]
    print(f"#{t} {ans}")

