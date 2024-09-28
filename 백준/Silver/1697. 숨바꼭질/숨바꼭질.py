from collections import deque

def bfs(x,y):
    q = deque()
    v = [0] * 100_001
    # 현재 수빈이의 위치는 방문한 것으로 처리
    v[x] = 1
    
    # 수빈이의 위치를 큐에 삽입
    q.append(x)
    
    while q:
        cx = q.popleft()
        
        # 만약 현재 위치가 동생의 위치라면
        if cx == y:
            return v[cx] - 1
        
        # 1초후 -1,+1위치로 이동했을 경우
        for px in (-1, 1):
            
            nx = cx + px
            if 0 <= nx < 100_001:
                if v[nx] == 0:
                    v[nx] = v[cx] + 1
                    q.append(nx)
        
        # 1초후 *2 위치로 이동했을 경우
        nx = cx * 2
        if 0 <= nx < 100_001: 
            if v[nx] == 0:
                v[nx] = v[cx] + 1
                q.append(nx)
    
        


x,y = map(int, input().split())
answer = bfs(x,y)
print(answer)