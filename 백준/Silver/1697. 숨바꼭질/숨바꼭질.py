from collections import deque

def bfs(x,y):
    q = deque()
    v = [0] * 100_001
    v[x] = 1
    
    q.append(x)
    
    while q:
        cx = q.popleft()
        if cx == y:
            return v[cx] - 1
        
        for px in (-1, 1):
            
            nx = cx + px
            if 0 <= nx < 100_001:
                if v[nx] == 0:
                    v[nx] = v[cx] + 1
                    q.append(nx)
                    
        nx = cx * 2
        if 0 <= nx < 100_001: 
            if v[nx] == 0:
                v[nx] = v[cx] + 1
                q.append(nx)
    
        


x,y = map(int, input().split())
answer = bfs(x,y)
print(answer)