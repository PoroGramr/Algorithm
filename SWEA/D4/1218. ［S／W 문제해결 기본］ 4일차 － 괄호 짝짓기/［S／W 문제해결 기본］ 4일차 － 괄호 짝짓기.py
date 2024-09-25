for i in range(10):
    m = int(input())
    # 문자열을 리스트로 입력받음
    data = list(input())
    
    # 스택을 이용하여 문제를 해결하기 위해 리스트를 뒤집음
    data = data[::-1]
    
    # 스택 선언
    stack = []
    
    # data의 모든 요소를 pop할때까지 반복
    while data:
        
        # 반복문의 첫번째 루프에서는 단순히 data를 pop해서 stack에 append한다
        if not stack:
            stack.append(data.pop())
            continue
            
        # 만약 stack의 top과 data의 top이 짝이라면 둘다 pop 해준다
        else:
            if (stack[-1] == "{" and data[-1] == "}" ) or (stack[-1] == "[" and data[-1] == "]" ) or (stack[-1] == "(" and data[-1] == ")" ) or (stack[-1] == "<" and data[-1] == ">" ):
                stack.pop()
                data.pop()
             
            # 짝이 아니라면 stack에 append
            else:
                stack.append(data.pop())
    
    answer = 0
    
    # 만약 짝이 맞지 않는다면
    if stack:
        answer = 0
    
    # 모두 짝이 맞는다면
    else:
        answer = 1
    print(f"#{i+1} {answer}")                              
                                                                                                  