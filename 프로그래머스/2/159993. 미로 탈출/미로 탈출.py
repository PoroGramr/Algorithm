"""
벽으로 된 칸으로는 이동 불가, 통로만 이동 가능
통로 중 한칸은 미로를 나가는 문이 있음, 레버를 당겨서만 열 수 있음
레버도 통로중 한칸에 존재
출발 지점에서 레버 이동 -> 출구 시에만 탈출 가능
bfs 2번 실행
"""
from collections import deque

def findS(y,x,maps):
    for ty in range(y):
        for tx in range(x):
            if maps[ty][tx] == "S":
                return ty,tx

def findValue(ly,lx,y,x,maps, value):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    sy,sx = ly,lx
    
    q = deque()
    q.append((sy,sx))
    
    visited = [[-1 for _ in range(x)] for _ in range(y)]
    visited[sy][sx] = 0
    
    while q:
        cy,cx = q.popleft()
        
        for py, px in zip(dy,dx):
            ny = cy + py
            nx = cx + px
            
            if 0 <= ny < y and 0 <= nx < x and visited[ny][nx] == -1 and maps[ny][nx] != "X":
                if maps[ny][nx] == value:
                    return ny,nx, visited[cy][cx] + 1
                else:
                    q.append((ny,nx))
                    visited[ny][nx] = visited[cy][cx] + 1

    return -1,-1,-1

def solution(maps):
    y = len(maps)
    x = len(maps[0])
    
    sy,sx = findS(y,x,maps)
    
    ly,lx,cnt = findValue(sy,sx,y,x,maps,"L")
    if ly == -1 and lx == -1:
        return -1
    
    a,b,exit = findValue(ly,lx,y,x,maps,"E")
    
    if exit == -1:
        return -1
    
    answer = cnt + exit
    
    return answer