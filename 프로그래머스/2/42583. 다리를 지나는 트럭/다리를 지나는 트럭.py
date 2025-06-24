'''
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해신 순으로 건너려 함
모든 트럭이 다리를 건너려면 최소 몇초가 걸리는 가
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    
    answer = 0
    current = 0
    while trucks or current > 0:
        out = bridge.popleft()
        current -= out
        answer += 1
        
        if trucks and (trucks[0] + current <= weight):
            cT = trucks.popleft()
            bridge.append(cT)
            current += cT
        else:
            bridge.append(0)
            
        
    
    return answer