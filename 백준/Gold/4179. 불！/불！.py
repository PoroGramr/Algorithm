from collections import deque

def bfs(data):
    global ans

    q = deque()

    # 지훈이와 불의 초기 위치를 큐에 추가
    q.append((0, jy, jx))  # 지훈의 초기 위치
    for fire in firelst:
        q.append((-1, fire[0], fire[1]))

    while q:
        time, y, x = q.popleft()

        # 지훈이 탈출 가능성 체크
        if time > -1 and data[y][x] != "F" and (y == 0 or x == 0 or y == n - 1 or x == m - 1):
            ans = min(ans, time + 1)
            break  # 탈출 성공 시 함수 종료
            
        # 상하좌우 이동
        for py, px in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + py, x + px
            if 0 <= ny < n and 0 <= nx < m and data[ny][nx] != "#":
                # 지훈이 이동
                if time > -1 and data[ny][nx] == ".":
                    data[ny][nx] = "_"  # 이미 방문한 자리 표시
                    q.append((time + 1, ny, nx))

                # 불 확산
                elif time == -1 and data[ny][nx] != "F":
                    data[ny][nx] = "F"
                    q.append((-1, ny, nx))

n, m = map(int, input().split())
data = []
firelst = []
for i in range(n):
    data.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        if data[i][j] == "J":
            jy, jx = i, j  # 지훈의 좌표 저장
        elif data[i][j] == "F":
            firelst.append([i,j])

ans = float("inf")  # 초기값 설정
bfs(data)
if ans == float("inf"):
    ans = "IMPOSSIBLE"

# 결과 출력
print(ans)
