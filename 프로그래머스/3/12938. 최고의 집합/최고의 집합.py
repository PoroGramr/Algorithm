"""
자연수 N개로 이루어진 집합 리스트가 있음
이때 각 원소의 합은 S가 되는 집합 리스트 중 곱이 최대가 되는 집합을 리턴하시오!
"""
def solution(n, s):
    
    base = s // n
    if base == 0:
        return [-1]
    extra = s % n
    
    answer = [base] * (n - extra) + [base + 1] * extra
    
    return answer