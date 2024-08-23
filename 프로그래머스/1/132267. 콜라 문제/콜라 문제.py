"""

"""
import sys
sys.setrecursionlimit(10000)
def solution(a, b, n):
    
    if n < a:
        new_cola = 0
        return new_cola
    
    new_cola = (n // a) * b
    empty_bottle = new_cola + n % a
    
    return new_cola + solution(a,b, empty_bottle)