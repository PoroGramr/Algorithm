from collections import deque


def bfs(place,y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    q = deque()
    visited = [[-1 for _ in range(5)] for _ in range(5)]
    
    q.append((y,x,0))
    visited[y][x] = 1
    
    while q:
        cy,cx,dist = q.popleft()
        
        if dist >= 2:
            continue
        
        for py,px in zip(dy,dx):
            ny,nx = cy + py, cx + px
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == -1:
                visited[ny][nx] = 1
                if place[ny][nx] == "P":
                    return False
                elif place[ny][nx] == 'O':    # 빈 자리면 탐색 계속
                    q.append((ny, nx, dist+1))
                
    return True
    


def check(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == "P":
                if not bfs(place,y,x):
                    return 0
    return 1

def solution(places):
    
    answer = []
    
    for place in places:
        answer.append(check(place))
    
    
    return answer