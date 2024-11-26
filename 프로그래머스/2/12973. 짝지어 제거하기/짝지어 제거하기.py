def solution(s):
    answer = 0
    
    stack = []
    stack.append(s[0])
    for i in range(1,len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
        
    if stack:
        answer = 0
    else:
        answer = 1
    return answer