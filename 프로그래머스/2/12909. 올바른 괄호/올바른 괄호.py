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
    stack = []
    for pa in s:
        if pa == "(":
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    
    if not stack:
        return True
    else:
        return False
