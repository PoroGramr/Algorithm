
def dfs(y,x,ox): # y, x, 시작 x 좌표
    global ans
    if y == 99:
        if data[y][x] == 2:
            ans = ox
        return

    for py,px in ((0,-1),(0,1), (1,0)):
        ny,nx = y + py, x + px
        if 0 <= ny < 100 and 0 <= nx < 100 and data[ny][nx] !=0 and v[ny][nx] == 0:
            v[ny][nx] = 1
            dfs(ny,nx,ox)
            return # 한 방향으로 이동 후 되돌아가지 않기 위해 바로 리턴 제일 중요!!!!



for t in range(1, 11):
    n = int(input())
    data = []

    # 사다리의 데이터 리스트를 입력 받음
    for _ in range(100):
        data.append(list(map(int, input().split())))

    # 정답 출력용 변수
    ans = 9999

    # 모든 x좌표를 탐색하며 정답 추출
    for x in range(0,100):
        if data[0][x] == 1:
            v = [[0] * 100 for _ in range(100)]
            v[0][x] = 1
            dfs(0,x,x) # y,x, 시작 x 좌표

    print(f"#{n} {ans}")
