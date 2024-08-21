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
    answer = [] # stack
    
    for ar in arr:
        if not answer: # stack is empty
            answer.append(ar)
        else:
            if answer[-1] != ar: # peek != value
                answer.append(ar) # push
    
    return answer