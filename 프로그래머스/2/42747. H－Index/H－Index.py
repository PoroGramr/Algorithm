"""
발행한 논문을 역으로 정렬
- 역으로 정렬한 경우 논문 목록의 (index + 1)이 h 이상 인용된 논문 수와 같음
"""
def solution(citations):
    answer = 0
    sortedCit = sorted(citations, key = lambda x : -x)
    
    for i in range(len(sortedCit)):
        if sortedCit[i] >= i+1:
            answer = i+1
        else:
            break
    return answer