def solution(numbers):
    # 문제 이해
    # - 입력 : 0 ~ 9 중 일부가 들어있는 숫자 리스트
    # - 출력 : 0 ~ 9 중 찾을수 없는 숫자들의 합 
    # 아이디어
    # 0 ~ 9 까지의 set을 만든다.
    # numbers를 set으로 만든다.
    # 둘 의 차집합을 구한다.
    # 차집합의 요소들의 합을 구한다.
    # 제한사항
    # n : 9 -> 맘대로 풀어야지
    
    checkNum = [i for i in range(0,10)]
    
    numbers = set(numbers)
    checkNum = set(checkNum)
    dif = checkNum.difference(numbers)
    
    answer = sum(dif)
    
    
    return answer