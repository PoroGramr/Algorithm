"""
문제 이해
    - 입력:
        테스트 케이스의 번호 : 정수
        8개의 숫자를 입력 받음  : 정수 리스트
    - 출력:
        모든 사이클을 돌린 후 암호
아이디어:
    완전 탐색으로 진행
    일종의 큐?
    마지막 숫자가 0이 되면 종료
    01234
    i = 0
    while data[-1] != 0:
        tmp = data.pop(0)
        tmp -= (i+1)
        i = (i+1) % 5
        data.append(tmp)
    print(*data)
"""
for t in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))

    # 1 ~ 5 사이클을 돌기 위한 변수
    i = 0
    while True:
        # 헤드 pop
        tmp = data.pop(0)

        # 1 ~ 5 사이클을 돌며 -연산
        tmp -= (i + 1)

        # 사이클을 위한 인덱스 값 변화
        i = (i + 1) % 5

        # 만약 연산한 값이 0보다 작거나 같다면 반복문 중단
        if tmp <= 0:
            data.append(0)
            break
        
        # 0보다 크다면 계속해서 연산
        else:
            data.append(tmp)

    # 결과 출력
    print(f"#{t} ", end="")
    print(*data)
