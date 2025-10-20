from collections import deque


def bfs(y,x,maps):
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    q = deque()
    q.append((0,0))
    
    visited = [[-1 for _ in range(x)] for _ in range(y)]
    visited[0][0] = 1
    while q:
        cy,cx = q.popleft()
        
        for py,px in zip(dy,dx):
            ny = cy + py
            nx = cx + px
            if 0 <= ny < y and 0 <=nx < x and visited[ny][nx] == -1 and maps[ny][nx] == 1:
                q.append((ny,nx))
                visited[ny][nx] = visited[cy][cx] + 1

    return visited[y-1][x-1]
def solution(maps):
    y = len(maps)
    x = len(maps[0])
    answer = bfs(y,x,maps)
    return answer