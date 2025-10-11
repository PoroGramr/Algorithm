def solution(n, k):
    
    free = n// 10
    k -= free
    answer = n * 12000 + k * 2000
    return answer