"""

이중 for문으로 모든 점을 탐색
좌표를 바탕으로 bfs

"""
from collections import deque
def bfs(y,x):
    q = deque()
    q.append((y,x))
    
    # 이동 횟수 카운드
    count = 1
    
    while q:
        cy, cx = q.popleft()

        for py, px in ((0,-1), (0,1), (1,0), (-1,0)):
            ny, nx = cy + py, cx + px
            
            # 이동이 가능할때 마다 이동횟수 카운트 1씩 증가
            if 0 <= ny < N and 0 <= nx < N and data[ny][nx] == data[cy][cx] + 1:
                count += 1
                q.append((ny,nx))
    
    # 이동가능한 모든 경우의 수를 시행했을 경우 방의 숫자와 이동횟수를 리턴
    return data[y][x], count

T = int(input())

for t in range(1, T+1):
    N = int(input())

    data = []

    for _ in range(N):
        data.append(list(map(int, input().split())))
        
    # 출력으로 쓸 방의 번호
    roomNum = 0
    
    # 출력으로 쓸 이동횟수
    count = 0
    
    # 모든 좌표를 탐색
    for i in range(N):
        for j in range(N):
            
            # bfs의 결과로 해당 방의 번호와 이동 횟수가 리턴
            tRoom, tCount = bfs(i,j)
            
            # 만약 이동 횟수는 같은데 방번호가 더 작은 숫자라면
            if tCount == count :
                
                # 출력으로 사용할 방 번호 변경
                if tRoom < roomNum:
                    roomNum = tRoom
            
            # 이동횟수가 더 많다면 출력으로 사용할 방 번호와 이동횟수를 변경
            elif tCount > count:
                roomNum = tRoom
                count = tCount



    print(f"#{t} {roomNum} {count}")
