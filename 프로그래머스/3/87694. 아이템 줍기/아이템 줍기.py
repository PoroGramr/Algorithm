from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    # 보다 명확한 경계선 처리를 위해 보드의 좌표를 2배로 함
    # 101로 설정해도 정답은 출력되지만 안정적인 연산을 위해 넉넉히 102로 초기화
    board = [[0] * 102 for _ in range(102)]
    
    
    # board의 경계선 처리
    for x1,y1,x2,y2 in rectangle:
        # 좌표도 똑같이 2배해줌
        # 좌측하단 x, 좌측하단 y,  우측상단 x,  우측상단 y
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        
        # 경계선 처리
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if x1 < j < x2 and y1 < i < y2:
                    board[i][j] = -1
                # 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리일 때 1로 채움
                elif board[i][j] != -1:
                    board[i][j] = 1
        
    # 캐릭터와 아이템의 좌표도 2배 처리
    cX, cY, iX, iY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
        
        
    # 방문 체크 배열
    v = [[0] * 102 for _ in range(102)]
        
    # bfs를 위한 큐 생성
    q = deque()
    q.append((cY, cX))
    v[cY][cX] = 1
        
    while q:
        cy, cx = q.popleft()
        if cy == iY and cx == iX:
            break
            
        for py, px in ((0,-1),(0,1),(1,0),(-1,0)):
            ny, nx = cy + py, cx + px
            
            # 방문체크와 동시에 이동경로를 카운트
            if 0 <= ny < 102 and 0 <= nx < 102 and board[ny][nx] == 1 and v[ny][nx] == 0:
                q.append((ny,nx))
                v[ny][nx] = v[cy][cx] + 1
    
    answer = v[iY][iX] // 2
    return answer