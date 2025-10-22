from collections import Counter

def solution(topping):
    answer = 0
    
    right = Counter(topping)  # 오른쪽 전체 토핑 카운트
    left = set()              # 왼쪽 토핑 종류 집합
    
    for t in topping:
        # 왼쪽에 추가
        left.add(t)
        
        # 오른쪽에서 제거
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        
        # 종류 수 비교
        if len(left) == len(right):
            answer += 1
            
    return answer
