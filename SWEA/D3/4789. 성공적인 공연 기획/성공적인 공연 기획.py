T = int(input())
for t in range(1, T + 1):

    # 기립에 필요한 관객수 리스트
    data = list(map(int, input()))

    # 추가로 불러야 할 관객
    plusAud = 0

    # 현재 관객수 카운트
    curAud = 0

    # 관객수 인덱스 조회 를 위한 변수
    # 인덱스는 곧 해당 인덱스의 관객이 기립하기에 필요한 관객수를 의미한다.
    i = 0

    # 리스트의 마지막 직전 요소까지만 조회가 필요하기에 조건문 설정
    while i != len(data) - 1:
        curAud += data[i]

        # 만약 현재 관객수보다 다음인덱스 기립에 필요한 관중수가 부족할경우
        if curAud < i+1:

            # 강제로 다음 인덱스 관객수를 증가시키고
            data[i+1] += 1

            # 추가로 불러야할 관객수 카운트 +1
            plusAud += 1

        # 인덱스도 +1
        i += 1
    
    print(f"#{t} {plusAud}")

