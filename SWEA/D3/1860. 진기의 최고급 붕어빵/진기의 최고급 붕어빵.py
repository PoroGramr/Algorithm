"""
문제이해 
    입력
        - 테스트 케이스 T 정수
        - N,M, K 정수 : 자격을 얻은 N명, M초의 시간을 들이면 K개의 붕어빵 만들 수 있음
        - N개의 정수 : 각 사람이 언제 도착하는지 초 단위로 나타냄 0 이상 11,111이하
    출력
        -모든 손님에 대해 기다리는 시간 없이 붕어빵 제공 가능 -> "Possible", 아니라면 "Impossible"
예시 입력
    2 2 2
    3 4 

    -> Possible

    2 2 2
    1 2
    
    -> Impossible

아이디어
    - 손님이 도착하는 시간을 리스트로 받음
    - bread 리스트를 만들어 각 second를 인덱스로 하여 빵의 개수를 순차적으로 계산
        - 계산하며 진행하던 중 빵의 개수가 부족하다면 break
        - 부족하지 않다면 계속 진행
        

        

"""
T = int(input())

for i in range(1, T+1):
    N, M, K = map(int, input().split()) # N명의 손님, M초의 시간에, K개의 빵

    # 손님 도착 시간 리스트
    cos = list(map(int, input().split()))

    # 손님 도착 시간 리스트 정렬
    # (3, 2) 이런식으로 도착 시간이 뒤죽박죽 들어오는 경우가 있음
    cos.sort()

    # 각 second 별 빵 개수 계산하는 리스트
    bread = [0 for _ in range(11112)]

    # 손님 도착시간이 0초인 경우도 있기에 전체 탐색
    for sec in range(11112):
        answer = ""

        # 빵의 개수 계산
        # 0초일 때에도 나머지느 0이므로 0초일 때에는 예외
        if sec % M == 0 and sec != 0:
            bread[sec] = bread[sec - 1] + K
        
        # 빵이 나오는 시간이 아닌경우 이전 second의 빵 개수 그대로 가져옴
        else:
            bread[sec] = bread[sec - 1]

        # 손님 도착에 따른 빵 개수의 변화
        # 손님 도착 시간 리스트를 큐로 사용
        if cos:

            # second가 같다면
            if cos[0] == sec:

                # cos를 popleft
                cos.pop(0)

                # 해당 sec 빵 개수 -1
                bread[sec] -= 1

                # 만약 해당 시간의 빵 개수가 0보다 작다면 Impossible 출력
                if bread[sec] < 0:
                    answer = "Impossible"
                    break
        
        # 빵 개수가 이상없이 잘 소진된다면 Possible 출력
        answer = "Possible"
    
    print(f"#{i} {answer}")
