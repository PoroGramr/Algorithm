N = int(input())
data = []
for _ in range(N):
    key = list(map(str, input().split()))
    if len(key) == 1:
        com = key[0]
        if com == "pop_front":
            if data:
                out = data.pop(0)
                print(out)
            else:
                print("-1")
        elif com == "pop_back":
            if data:
                out = data.pop()
                print(out)
            else:
                print("-1")
        elif com == "size":
            print(len(data))
        elif com == "empty":
            if data:
                print("0")
            else:
                print("1")
        elif com == "front":
            if data:
                print(data[0])
            else:
                print("-1")
        elif com == "back":
            if data:
                print(data[-1])
            else:
                print("-1")
    # 명령어와 정수가 입력으로 들어올 떄
    else:
        com, num = key[0], key[1]
        if com == "push_front":
            data.insert(0, num)
        elif com == "push_back":
            data.append(num)


