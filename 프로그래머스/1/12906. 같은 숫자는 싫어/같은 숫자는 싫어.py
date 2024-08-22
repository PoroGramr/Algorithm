"""
문제이해
- 0에서 9로 이루어진 배열이 주어짐
- 연속된 숫자는 하나만 남기고 제거
- 입력 : 숫자[리스트]
- 출력 : 숫자-연속이제거된[리스트]

아이디어
- 스택 필요
- arr을 순회
    - arr에 요소를 스택에 push
    - 스택에 현재 쌓여있는 요소의 값과 다르면 push
    - peek != arr -> push

제한사항
-
"""

def solution(arr):
    # 스택을 선언
    stack = []
    
    # arr을 순회하며 요소를 검사
    for num in arr:
        
        # 만약 스택이 비워져있다면(맨 처음 for문 시작시)
        if not stack:
            stack.append(num)
            
        # 스택의 peek값과 num 값이 같지 않다면 push
        elif stack[-1] != num:
            stack.append(num)
    
    return stack