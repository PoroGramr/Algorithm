from collections import deque

def bfs(maps,n,m):# 맵 리스트, 세로길이, 가로길이
    
    # 방문 여부 및 이동 거리 저장용 리스트
    v = [[0] * m for _ in range(n)]
    
    # bfs용 큐 생성
    q = deque()
    
    # 시작 좌표 업데이트
    q.append((0,0))
    
    # 시작 좌표 방문 처리
    v[0][0] = 1
    
    while q:
        cy, cx = q.popleft()
        
        # 이동 가능 방향 조회
        for py, px in ((0,1), (0,-1), (1,0), (-1,0)):
            ny, nx = cy + py, cx + px
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                
                # 아직 방문 하지 않은 좌표인 경우 이동거리 업데이트
                if v[ny][nx] == 0:
                    v[ny][nx] = v[cy][cx] + 1
                    q.append((ny,nx))
    
    # 최종 목적지에 도달했다면 이동 거리 리턴
    if v[n-1][m-1] != 0:
        return v[n-1][m-1]
    
    # 최종 목적지에 도달하지 못했다면 -1 리턴
    else:
        return -1

                    

def solution(maps):
    # 맵의 세로 길이
    n = len(maps)
    
    # 맵의 가로 길이
    m = len(maps[0])
    
    # bfs를 통한 정답 출력
    answer = bfs(maps, n, m) # 맵 리스트, 세로길이, 가로길이
    return answer