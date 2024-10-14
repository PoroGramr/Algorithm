def check_row():
    global ans
    for y in range(N):
        cnt = 0
        for x in range(N):
            if data[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:  # 마지막까지 이어질 경우
            ans += 1

def check_col():
    global ans
    for x in range(N):
        cnt = 0
        for y in range(N):
            if data[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:  # 마지막까지 이어질 경우
            ans += 1

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    check_row()  # 가로 탐색
    check_col()  # 세로 탐색

    print(f"#{t} {ans}")
