from collections import defaultdict

def solution(tickets):
    
    data = defaultdict(list)
    
    for start, end  in tickets:
        data[start].append(end)
    
    for start in data:
        data[start].sort(reverse = True)
        
        
    route = []
    stack = ["ICN"]
    
    while stack:
        currentAirport = stack[-1]
        
        if data[currentAirport]:
            nextAirport = data[currentAirport].pop()
            stack.append(nextAirport)
        else:
            route.append(stack.pop())
    
    answer = route[::-1]
    return answer