from copy import deepcopy

# 0 상 1 우 2 하 3 좌
cctv_dir = {
    1 : [[0],[1],[2],[3]],
    2 : [[0,2], [1,3]],
    3 : [[0,1],[1,2],[2,3],[3,0]],
    4 : [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5 : [[0,1,2,3]]
}

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for y in range(N):
    for x in range(M):
        if 1 <= data[y][x] <= 5:
            cctvs.append((y, x, data[y][x]))

answer = float('inf')

def watch(board, y, x, directions):
    for d in directions:
        ny, nx = y, x
        while True:
            ny += dy[d]
            nx += dx[d]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                break
            if board[ny][nx] == 6:
                break
            if board[ny][nx] == 0:
                board[ny][nx] = -1

def dfs(depth, board):
    global answer
    if depth == len(cctvs):
        count = sum(row.count(0) for row in board)
        answer = min(answer, count)
        return
    
    y, x, cctv_type = cctvs[depth]
    for dirs in cctv_dir[cctv_type]:
        new_board = deepcopy(board)
        watch(new_board, y, x, dirs)
        dfs(depth + 1, new_board)

dfs(0, data)
print(answer)
