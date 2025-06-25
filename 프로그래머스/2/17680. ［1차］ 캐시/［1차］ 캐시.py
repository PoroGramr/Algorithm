
from collections import deque
def solution(cacheSize, cities):
    
    for i,x in enumerate(cities):
        cities[i] = x.lower()
        
    time = 0
    cache = deque()
    for i in range(len(cities)):
        if cacheSize == 0:
            time = len(cities) * 5
            break
        curCity = cities[i]
        
        if curCity in cache:
            time += 1
            cache.remove(curCity)
            cache.append(curCity)
        
        else:
            time += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            
            cache.append(curCity)
        
    
    
    answer = time
    return answer