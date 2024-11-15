py = [0,-1,1,0,0] # 0은 제외, 상하좌우
px = [0,0,0,-1,1] # 0은 제외, 상하좌우
tp = [0,2,1,4,3]


T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split()) # 가로세로, 격리시간, 군집의 개수

    micro = []

    for _ in range(K):
        y,x,m,p = map(int, input().split()) # 세로, 가로, 미생물 수, 이동방향
        micro.append([y,x,m,p])

    # M 시간동안 격리
    for _ in range(M):
        # 이동 처리
        i = 0
        for i in range(len(micro)):
            micro[i][0] = micro[i][0] + py[micro[i][3]]
            micro[i][1] = micro[i][1] + px[micro[i][3]]

            # 소독약 처리
            if micro[i][0] == 0 or micro[i][1] == 0 or micro[i][0] == N -1 or micro[i][1] == N - 1:

                # 미생물 절반
                micro[i][2] //= 2
                # 방향 반대
                micro[i][3] = tp[micro[i][3]]

        micro.sort(key = lambda x : (x[0], x[1], x[2]), reverse=True)

        i = 1
        while i < len(micro):
            if micro[i-1][0:2] == micro[i][0:2]:
                micro[i-1][2] += micro[i][2]
                micro.pop(i)
            else:
                i += 1
    ans = 0
    for a in micro:
        ans += a[2]
    print(f"#{t} {ans}")




