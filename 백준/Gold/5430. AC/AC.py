T = int(input())

for t in range(1, T + 1):
    # 명령어 리스트
    command = input()
    command = command.replace("RR", "")  # 불필요한 RR 제거

    # 리스트의 길이
    n = int(input())

    # 입력받은 문자열을 정수 리스트로 변환
    nums = input().strip("[]")
    if nums:
        data = list(map(int, nums.split(",")))
    else:
        data = []

    # 뒤집힌 상태를 나타내는 플래그
    reversed_flag = False
    error_flag = False

    # 명령어 수행
    for cmd in command:
        if cmd == "R":
            reversed_flag = not reversed_flag  # 뒤집힌 상태 토글
        elif cmd == "D":
            if data:
                if reversed_flag:
                    data.pop()  # 뒤집힌 상태라면 마지막 요소 제거
                else:
                    data.pop(0)  # 일반 상태라면 첫 번째 요소 제거
            else:
                error_flag = True
                break

    # 결과 출력
    if error_flag:
        print("error")
    else:
        if reversed_flag:
            data.reverse()  # 최종 상태에서만 한번 뒤집음
        print(f"[{','.join(map(str, data))}]")
