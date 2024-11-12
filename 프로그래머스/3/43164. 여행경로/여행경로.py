from collections import defaultdict

def solution(tickets):
    data = defaultdict(list)
    
    for start, end in tickets:
        data[start].append(end)
    
    # pop으로 꺼내 쓰기에 알파벳 역순으로 정렬해야 나중에 알파벳 순으로 정렬됌
    for start in data:
        data[start].sort(reverse = True)
    
    # 경로 저장용 리스트
    route = []
    
    # dfs를 활용하기 위한 스택
    stack = ["ICN"]
    
    while stack:
        # print(stack, route)
        
        # 현재의 공항
        currentAirport = stack[-1]
        
        # 현재의 공항의 이동 가능한 다음 공항 중 알파벳이 빠른 공항을 스택에 삽입
        if data[currentAirport]:
            nextAirport = data[currentAirport].pop()
            stack.append(nextAirport)
        
        # 더이상 이동할 수 있는 공항이 없다면 스택에서 pop하여 route에 삽입
        
        else:
            route.append(stack.pop())
    
    # 역순으로 저장되기에 다시 리버스해줌
    answer = route[::-1]
    return answer

"""
stack의 route의 진행 과정 예시
['ICN'] []
['ICN', 'ATL'] []
['ICN', 'ATL', 'ICN'] []
['ICN', 'ATL', 'ICN', 'SFO'] []
['ICN', 'ATL', 'ICN', 'SFO', 'ATL'] []
['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'] []
['ICN', 'ATL', 'ICN', 'SFO', 'ATL'] ['SFO']
['ICN', 'ATL', 'ICN', 'SFO'] ['SFO', 'ATL']
['ICN', 'ATL', 'ICN'] ['SFO', 'ATL', 'SFO']
['ICN', 'ATL'] ['SFO', 'ATL', 'SFO', 'ICN']
['ICN'] ['SFO', 'ATL', 'SFO', 'ICN', 'ATL']
"""
