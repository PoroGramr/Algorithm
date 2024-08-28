"""
1. 가로형 명함과 세로형 명함의 타입을 통일 시킨다.
가로형 명함: w > h
세로형 명함: h < w

2. 전체 명함의 최대 가로 * 최대 세로 -> 지갑의 크기를 계산한다.
"""

def solution(sizes):
    answer = 0
    
    max_width = -1
    max_height = -1
    
    for s in sizes:
        s.sort() # 작은게 앞에, 큰게 뒤에 -> 세로형 명함
        
        max_width = max(max_width, s[1])
        max_height = max(max_height, s[0])
        
    answer = max_width*max_height
        
    return answer