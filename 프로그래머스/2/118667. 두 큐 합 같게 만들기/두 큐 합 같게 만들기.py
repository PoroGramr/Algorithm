"""
문제 이해
- 큐가 2개 주어짐
- 두 큐 중 하나를 골라 하나에서 dequeue, 다른 하나로 enqueue
    - 두 큐의 원소의 합을 같도록 조정
    - dequeue and enqueue를 하나로 침
- 두 큐의 합을 2로 나눈 값 -> 우리가 만들어야 하는 큐 하나의 합

- 입력 : queue1, queue2 : [리스트]
- 출력 : 최소 횟수
    - 각 큐의 원소의 합을 같게 만들 수 없다면 -1 리턴

아이디어
- 만약 두큐의 합이 홀수 -> 실패 (리턴 -1)
- 반복을 계속하다가 결국 답이 안나왔을 떄 -> 실패 (리턴 -1)
- MAX Iter : queue * 3

"""


from collections import deque

def solution(queue1, queue2):
    
    answer = 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    totalSum = sum1 + sum2
    
    # 두 큐의 합 / 2 가 홀수인 경우
    if totalSum % 2 == 1:
        return -1
    
    # 반복을 통래 만들어야하는 목표 합
    goal = totalSum // 2
    
    # 종료를 위한 최대 반복 수
    MAXITER = len(queue1) * 3
    
    # queue1 < queue2 queue1 -> queue2
    # queue1 > queue2 queue2 -> queue1
    
    iteration = 0
    while iteration < MAXITER:
        if sum1 > goal:
            item = queue1.popleft()
            sum1 -= item
            queue2.append(item)
            sum2 += item
        elif sum1 < goal:
            item = queue2.popleft()
            sum2 -= item
            queue1.append(item)
            sum1 += item
        elif sum1 == goal:
            return iteration
        
        iteration += 1
    
    return -1
    
    