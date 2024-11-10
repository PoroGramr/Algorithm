"""
입력
    암호문의 개수 N
    암호문 뭉치 정수 리스트
    명령어의 개수 M
    명령어 뭉치 문자열 리스트
출력
    암호문 뭉치를 수정하고 첫 10개의 암호문

암호문의 종류는 3가지
I x,y,s : 앞에서 x번째 암호문 바로 다음에 y개의 암호문을 삽입 s는 삽입합 암호문
D x,y : 앞에서 x번째 암호문 바로 다음부터 y개의 암호문을 삭제
A y,s : 암호문 뭉치 맨 뒤에 y 개의 암호문을 덧붙인다.s는 덧붙일 암호문

마치 큐처럼 선입 선출 방식으로 명령문을 수행해야 할 듯

아이디어
1. 암호문 리스트를 입력 받음
2. 명령어의 수 입력 받음
2-1. 명령어 리스트 입력받음
while commanCount !=0:
    if command[0] == ~~~:
for i in range(10):
print(data[i])
"""

T = 10

for t in range(1, T + 1):
    # 암호문의 개수
    N = int(input())

    # 암호문 리스트
    enc = list(map(int, input().split()))

    # 명령어의 개수
    M = int(input())

    # 명령어 리스트
    commands = list(map(str, input().split()))
    # 명령어의 개수를 카운트 해 반복문을 탈출 -> 모든 명령어를 실행
    commandCount = 0

    while commandCount != M:
        # I x,y,s : 앞에서 x번째 암호문 바로 다음에 y개의 암호문을 삽입 s는 삽입합 암호문
        if commands[0] == "I":
            #print(1)
            commands.pop(0)
            x = int(commands.pop(0)) # 앞에서 x번쨰
            y = int(commands.pop(0)) # y개의 암호문을 삽입
            
            # pop한 순서대로 enc에 삽입할 시 순서가 역순으로 삽입됌
            # 리스트 2개를 활용해 명령문에 적힌 순서해도 삽입되도록 함
            apEnc = []
            for _ in range(y):
                apEnc.append(commands.pop(0))
            for _ in range(y):
                enc.insert(x,int(apEnc.pop()))

        # D x,y : 앞에서 x번째 암호문 바로 다음부터 y개의 암호문을 삭제
        elif commands[0] == "D":
            #print(2)
            commands.pop(0)
            x = int(commands.pop(0))
            y = int(commands.pop(0))
            for _ in range(y):
                enc.pop(x)
        # A y,s : 암호문 뭉치 맨 뒤에 y 개의 암호문을 덧붙인다.s는 덧붙일 암호문
        elif commands[0] == "A":
            #print(3)
            commands.pop(0)
            y = int(commands.pop(0))
            
            # pop한 순서대로 enc에 삽입할 시 순서가 역순으로 삽입됌
            # 리스트 2개를 활용해 명령문에 적힌 순서해도 삽입되도록 함
            appEnc = []
            for _ in range(y):
                appEnc.append(int(commands.pop(0)))
            for _ in range(y):
                enc.append(int(appEnc.pop()))

        commandCount += 1
    print(f"#{t} ",end="")
    for i in range(10):
        print(enc[i], end=" ")
    print("")


