for i in range(10):
    n ,data = map(str, input().split())
    # 입력받은 문자열을 문자 하나씩 리스트로 변환
    data = list(data)
    
    # 스택으로 사용하기 위해 리스트를 뒤집음
    data = data[::-1]
    
    # 스택 선언
    stack = []
    
    # 만약 data가 다 pop되면 탈풀
    while data:
        
        # 첫번째 루프를 위한 if
        if not stack:
            stack.append(data.pop())
            continue
          
        # 만약 스택의 top과 data의 top이 같다면
        if stack[-1] == data[-1]:
            stack.pop()
            data.pop()
            continue
            
        # 아닐 경우 그냥 pop
        else:
            stack.append(data.pop())
    
    
    print(f"#{i+1} ",end="")
    for k in stack:
        print(k,end="")
    print("")
            
            
        
         