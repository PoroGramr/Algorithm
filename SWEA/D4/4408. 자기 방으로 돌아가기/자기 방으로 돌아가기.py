T = int(input())

for t in range(1, T+1):
    N = int(input()) # 돌아가야 할 학생등의 수

    # 0은 무시하고 나머지 1 ~ 200 만 사용
    """
    방 - 통로
    1,2 - 1
    3,4 - 2
    5,6 = 3
    7,8 - 4
    9,10 - 5
    
    위 처럼 통로에 인덱싱을 하기 위해선
    (방 번호 + 1) // 2 연산을 통해 할 수 있음
    """

    data = [0] * 201

    for _ in range(N):
        currentRoom, originalRoom = map(int, input().split())
        
        # 현재 방 번호가 원래 방 번호보다 클 경우 둘을 바꿔 줌
        if currentRoom > originalRoom:
            currentRoom, originalRoom = originalRoom, currentRoom
        
        start = (currentRoom  + 1 ) // 2
        end = (originalRoom + 1) // 2
        
        for check in range(start, end + 1):
            data[check] += 1

    print(f"#{t} {max(data)}")
