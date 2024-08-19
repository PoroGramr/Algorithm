def solution(a, b):
    # 문제이해
    # - 입력으로 a,b 가 들어온다.
    # - 둘 다 홀수, 하나만 홀수 , 홀수가 없을 때 에 따라 결과를 리턴
    
    
    # 아이디어
    # - a,b 를 입력받는다
    # - a, b 의 홀수 여부를 체크한다.
    # - - 여부에 따라 결과 값 계산
    
    # 제한사항
    # O(1)
    
    if (a % 2 == 1 ) and (b % 2 == 1):
        return a ** 2 + b ** 2
    elif (a % 2 == 0 ) and (b % 2 == 1) or (a % 2 == 1 ) and (b % 2 == 0):
        return 2 * (a + b)
    else:
        return abs(a - b)
        
    answer = 0
    return answer