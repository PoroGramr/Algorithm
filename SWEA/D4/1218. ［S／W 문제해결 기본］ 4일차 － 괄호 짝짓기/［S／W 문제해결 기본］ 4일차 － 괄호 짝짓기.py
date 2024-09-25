"""
'()', '[]', '{}', '<>' 
"""

for i in range(10):
    m = int(input())
    data = list(input())
    data = data[::-1]
    stack = []
    while data:
        if not stack:
            stack.append(data.pop())
            continue
        else:
            if (stack[-1] == "{" and data[-1] == "}" ) or (stack[-1] == "[" and data[-1] == "]" ) or (stack[-1] == "(" and data[-1] == ")" ) or (stack[-1] == "<" and data[-1] == ">" ):
                stack.pop()
                data.pop()
            else:
                stack.append(data.pop())
    answer = 0
    if stack:
        answer = 0
    else:
        answer = 1
    print(f"#{i+1} {answer}")                              
                                                                                                  