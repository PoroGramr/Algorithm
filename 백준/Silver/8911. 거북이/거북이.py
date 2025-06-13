'''
상근이는 2차원 평면 위에서 움직일 수 있는 거북이 로봇 하나를 가지고 있다. 이 거북이에게 내릴 수 있는 명령은 다음과 같다.
F: 한 눈금 앞으로
B: 한 눈금 뒤로
L: 왼쪽으로 90도 회전
R: 오른쪽으로 90도 회전
'''

T = int(input())

direstions = [(1,0), (0,1), (-1,0),(0,-1)]

for _ in range(T):
    S = input()
    
    did =  1
    x = 0
    y = 0

    minx = 0
    miny = 0
    maxx = 0
    maxy = 0

    for s in S:
        if s == "L":
            did = (did+1) % 4
        if s == "R":
            did = (did+3) % 4
        
        if s == "F":
            x += direstions[did][0]
            y += direstions[did][1]
        
        if s == "B":
            x -= direstions[did][0]
            y -= direstions[did][1]
        
        minx = min(minx,x)
        miny = min(miny,y)
        maxx = max(maxx,x)
        maxy = max(maxy,y)


    print((maxx-minx) *(maxy-miny))           