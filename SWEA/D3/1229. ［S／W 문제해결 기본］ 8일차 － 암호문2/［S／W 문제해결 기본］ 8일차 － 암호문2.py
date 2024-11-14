T = 10
for t in range(1, T + 1):

    # 원본 암호문의 길이
    N = int(input())

    # 원본 암호문
    enc = list(map(int, input().split()))

    # 명령어의 개수
    N = int(input())

    # 명령어
    commands = list(map(str, input().split()))

    # 실행된 명령어의 수 카운트
    i = 0


    while len(commands) != 0:
        # 현재 명령어
        cc = commands.pop(0)

        # x의 위치 바로 다음에 y개의 숫자 s들을 삽입
        if cc == "I":
            i += 1
            x = int(commands.pop(0))
            y = int(commands.pop(0))

            # 삽입할 숫자들의 리스트
            inLst = []

            for _ in range(y):
                inLst.append(int(commands.pop(0)))

            # 리스트의 숫자들은 암호문에 역순으로 삽입해야함
            for _ in range(y):
                enc.insert(x, inLst.pop())

        # x의 위치 바로 다음부터 y개의 숫자를 삭제
        elif cc == "D":
            i+=1
            x = int(commands.pop(0))
            y = int(commands.pop(0))

            for _ in range(y):
                enc.pop(x)



    print(f"#{t} ",end="")
    for e in range(10):
        print(enc[e], end=" ")
    print("")