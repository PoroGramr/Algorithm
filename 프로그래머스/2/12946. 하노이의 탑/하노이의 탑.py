"""
- 하노이 탑의 조건
 - 1. 한 번에 하나의 원판만 옮길 수 있음
 - 2. 큰 원판이 작은 원판 위에 있어서는 안됨
 
- hanoi(4) = hanoi(3) -> 2 + 4 ->3 + hanoi(3) -> 3
- hanoi(3) = hanoi(2)  + 3-> 2 + hanoi(2)
"""
answer = []
def hanoi(n, a, b, c):
    if n == 1:
        answer.append([a,c])
        return
    
    # n: 원판의 갯수, a: 현재 위치, b: 거쳐갈 곳, c: 목적지
    hanoi(n-1, a, c, b) # a -> b
    answer.append([a,c]) # 원판 옮기기
    hanoi(n-1, b, a, c) # b -> c
    
    
def solution(n):
    hanoi(n,1,2,3)
    return answer