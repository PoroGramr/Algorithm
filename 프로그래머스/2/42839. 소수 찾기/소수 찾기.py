from math import sqrt
from itertools import permutations

def is_prime(n):
    
    if n in (0, 1):
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

def solution(numbers):
    digits = list(numbers)
    primes = set()

    # 길이 1 ~ 전체 길이까지 모든 순열 생성
    for L in range(1, len(digits) + 1):
        for p in permutations(digits, L):
            num = int(''.join(p))  # 앞자리 0 자동 처리(예: '011' -> 11)
            if is_prime(num):
                primes.add(num)

    return len(primes)