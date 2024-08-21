"""
문제 이해 / 아이디어
- queue에서 프로세스 하나 꺼내기 (dequeue)
- 대기중인 queue 조회 
    - 우선순위가 높은 프로세스가 있으면 (enqueue)
    - 없으면 실행하기
- location에 해당하는 프로세스가 몇번째로 실행되는지 확인하기


제한 사항
- n : 100
"""

from collections import deque
def solution(priorities, location):
    
    # [2, 1, 3, 2]
    # -> [0:2, 1:1, 2:3, 3:2]
    
    # 큐 채우기
    queue = deque([]) #(loc, priorites)
    for loc, pri in enumerate(priorities):
        queue.append((loc,pri)) # 튜플
    # 	deque([(0, 2), (1, 1), (2, 3), (3, 2)])
        
        
    # - queue에서 프로세스 하나 꺼내기 (dequeue)
    # - 대기중인 queue 조회 
    #     - 우선순위가 높은 프로세스가 있으면 (enqueue)
    #     - 없으면 실행하기
    # - location에 해당하는 프로세스가 몇번째로 실행되는지 확인하기
    order = 0
    while queue:
        cur = queue.popleft()
        
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[0] == location:
                return order
        