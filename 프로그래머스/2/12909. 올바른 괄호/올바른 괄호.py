"""
문제 이해
'('가 있다면 반드시 뒤에 ')'가 있어서 두 짝이 모두 지어진다면 -> true
짝이 지어지지 않고 남는 '(' or ')' 가 있다면 -> false
- 입력 : 문자열 ('('과')'으로만 구성됨)
- 출력 : true or false

아이디어
- stack
    - "열린 괄호"를 만나면 push
    - "닫힌 괄호"를 만나면 pop
- 작업을 마치고 stack이 비워져있다면 true

요구사항
-

"""

def solution(s):
    # 스택을 선언
    stack = []
    
    # 입력 s의 문자 하나하나 순회
    for pa in s:
        
        # 만약 문자가 "(" 라면 stack에 push
        if pa == "(":
            stack.append(pa)
            
        # 만약 문자가 ")"라면 
        else:
            
            # 스택이 비어있다면 올바르지 않은 괄호이기에 return False
            if not stack:
                return False
            # 스택이 비어있지 않다면 스택에 "("가 존재 -> 올바른 괄호 -> 짝이 맞음
            # 괄호 짝이 맞기에 pop
            stack.pop()
    
    # 모든 문자를 순회하고 스택에 문자가 남아있다 -> 짝이 맞지 않는다 -> 올바르지 않은 괄호
    if stack:
        return False
    
    # 모든 문자를 순회하고 스택이 비었다 -> 짝이 맞음 -> 올바른 괄호
    else:
        return True
            