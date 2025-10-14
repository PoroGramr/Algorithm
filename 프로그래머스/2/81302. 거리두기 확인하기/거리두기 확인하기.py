"""
대기실은 5개
각 대기실은 5x5크기
응시자들 끼리는 맨해튼 거리가 3이상으로 앉아야 함
단, 응시자들 자리 사이가 파티션으로 막혀있는 경우에는 허용
P : 응시자, O : 테이블, X : 파티션

의사코드
1. 상하좌우
2. 직선 2칸
3. 대각선1칸

"""
def in_range(y, x): 
    return 0 <= y < 5 and 0 <= x < 5
# 상하좌우 체크
def udlr(y,x, place):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for py,px in zip(dy,dx):
        ny,nx = y + py, x + px
        if in_range(ny,nx) and place[ny][nx] == "P":
            return False
    return True
    
# 직선 2칸 체크
def plusTwo(y,x,place):
    # 사람과 사람간 거리
    dy = [-2,2,0,0]
    dx = [0,0,-2,2]
    
    # 사람과 사람 사이 파티션 거리
    pcy = [-1,1,0,0]
    pcx = [0,0,-1,1]
    
    for i in range(4):
        py = dy[i]
        px = dx[i]
        
        # 사람이 있는지 체크
        ny,nx = y + py, x + px
        if in_range(ny,nx) and place[ny][nx] == "P":
            bpy, bpx = y + pcy[i], x + pcx[i]
            
            # 만약 사람과 사람 사이 파티션이 존재한다면
            if place[bpy][bpx] == "X":
                continue
            else:
                return False
    
    return True
# 대각선
def cross(y,x,place):
    #좌측위, 우측위, 좌측아래, 우측 아래 순서
    dy = [-1,-1,1,1]
    dx = [-1,1,-1,1]
    
    # 파티션이 존재하는 좌표
    part = [[[-1,0],[0,-1]],
           [[-1,0],[0,1]],
           [[0,-1],[1,0]],
           [[0,1],[1,0]]]
    
    for i in range(4):
        py = dy[i]
        px = dx[i]
            
        ny,nx = y + py, x + px
        if in_range(ny,nx) and  place[ny][nx] == "P":
            bpyOne = y + part[i][0][0]
            bpxOne = x + part[i][0][1]
            bpyTwo = y + part[i][1][0]
            bpxTwo = x + part[i][1][1]
            if place[bpyOne][bpxOne] == "X" and place[bpyTwo][bpxTwo] == "X":
                continue
            else:
                return False
    return True
    
def checkPlace(place):
    for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    if udlr(y,x,place) and plusTwo(y,x,place) and cross(y,x,place):
                        continue
                    else:
                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        check = checkPlace(place)
        answer.append(check)
        
    return answer