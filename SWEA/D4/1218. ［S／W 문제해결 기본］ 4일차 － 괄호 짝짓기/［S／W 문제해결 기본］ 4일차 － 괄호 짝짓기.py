T = 10

for t in range(1, T + 1):
    M = int(input())
    data = list(map(str, input()))

    stack = []
    for i in range(M):
        if data[i] == "{" or data[i] == "[" or data[i] == "(" or data[i] == "<":
            stack.append(data[i])
        else:
            if data[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(data[i])
            if data[i] == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(data[i])
            if data[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(data[i])
            if data[i] == ">":
                if stack[-1] == "<":
                    stack.pop()
                else:
                    stack.append(data[i])

    if stack:
        print(f"#{t} 0")
    else:
        print(f"#{t} 1")


