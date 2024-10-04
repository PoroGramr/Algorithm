from collections import deque

def dfs(y,x):
        v = [[0 for _ in range(100)] for _ in range(100)]
        q = deque()
        q.append((y,x))
        v[y][x] = 1
        while q:
            cy,cx = q.popleft()
            
            
            
            for py,px in ((0,1),(0,-1),(1,0)):
                ny ,nx = cy + py, cx + px
                if 0 <= ny < 100 and 0 <= nx <100:
                    if data[ny][nx] == 2:
                        return True

                    if data[ny][nx] == 1 and v[ny][nx] == 0:

                        q.append((ny,nx))

                        v[ny][nx] = 1
                        break
        return False



for I in range(1,11):
    i = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int,input().split())))
        
    answer = 0
    for x in range(0,100):
        if data[0][x] == 1:
            if dfs(0,x):
                answer = x
                break
    print(f"#{I} {answer}")
            