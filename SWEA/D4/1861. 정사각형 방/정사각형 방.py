def dfs(y, x):
    # 이미 계산된 결과가 있다면 그 값을 반환
    if dp[y][x] != -1:
        return dp[y][x]

    # 이동할 수 있는 방의 개수 (시작 위치는 1)
    tmpCount = 1

    for py, px in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + py, x + px

        # 현재 좌표에서 인접한 방으로 이동할 수 있는 조건 확인
        if 0 <= ny < N and 0 <= nx < N and data[y][x] + 1 == data[ny][nx]:
            tmpCount = max(tmpCount, 1 + dfs(ny, nx))

    # 계산된 결과를 메모이제이션
    dp[y][x] = tmpCount
    return dp[y][x]


T = int(input())

for i in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    
    # 메모이제이션을 위한 dp 테이블 (-1로 초기화)
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    countData = []

    # 모든 좌표에 대해 dfs 수행
    for y in range(N):
        for x in range(N):
            count = dfs(y, x)
            countData.append([data[y][x], count])

    # 움직일 수 있는 방의 수가 큰 순서대로, 같다면 방의 번호가 작은 순으로 정렬
    countData.sort(key=lambda x: (-x[1], x[0]))

    # 정답 출력
    answer = countData[0]
    print(f"#{i} {answer[0]} {answer[1]}")
