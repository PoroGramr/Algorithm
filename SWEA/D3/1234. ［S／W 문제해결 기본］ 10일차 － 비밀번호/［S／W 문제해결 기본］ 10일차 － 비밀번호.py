for i in range(10):
    n ,data = map(str, input().split())
    data = list(data)
    data = data[::-1]
    stack = []
    
    while data:
        if not stack:
            stack.append(data.pop())
            continue
        if stack[-1] == data[-1]:
            stack.pop()
            data.pop()
            continue
        else:
            stack.append(data.pop())
    print(f"#{i+1} ",end="")
    for k in stack:
        print(k,end="")
    print("")
            
            
        
         