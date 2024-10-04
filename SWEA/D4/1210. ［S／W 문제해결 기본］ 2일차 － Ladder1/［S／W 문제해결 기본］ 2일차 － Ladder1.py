from collections import deque

def dfs(y,x):
        v = [[0 for _ in range(100)] for _ in range(100)]
        q = deque()
        q.append((y,x))
        v[y][x] = 1
        
        while q:
            cy,cx = q.popleft()
        
            # 사다리타기의 우선순위인 좌우 -> 아래 순으로 진행
            for py,px in ((0,1),(0,-1),(1,0)):
                ny ,nx = cy + py, cx + px
                if 0 <= ny < 100 and 0 <= nx <100:
                    
                    # 만약 다음 좌표의 데이터 값이 2라면 True를 리턴
                    if data[ny][nx] == 2:
                        return True
					
                    # 계속해서 dfs 실행
                    if data[ny][nx] == 1 and v[ny][nx] == 0:
                        q.append((ny,nx))
                        v[ny][nx] = 1
                        #
                        break
        return False



for I in range(1,11):
    i = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int,input().split())))
        
    answer = 0
    
    # 0,0 ~ 0,100 까지 dfs를 실행
    for x in range(0,100):
        if data[0][x] == 1:
            
            # dfs를 실행하며 데이터 리스트에서 2를 만난다면 True를 리턴
            # 해당 x 값이 정답
            if dfs(0,x):
                answer = x
                
    print(f"#{I} {answer}")
            