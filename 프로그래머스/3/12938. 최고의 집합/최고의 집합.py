"""
자연수 N개로 이루어진 집합 리스트가 있음
이때 각 원소의 합은 S가 되는 집합 리스트 중 곱이 최대가 되는 집합을 리턴하시오!
"""
def solution(n, s):
    
    quo = s // n
    if quo == 0:
        return [-1]
    rem = s % n
    answer = [quo] * n
    i = 0
    while 0 < rem:
        if i >= n:
            i %= n
        answer[i] += 1
        rem -= 1
        i += 1
    answer.sort()
    return answer