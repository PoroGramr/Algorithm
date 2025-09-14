def solution(routes):
    
    routes.sort(key = lambda x : (x[1], x[0]))
    
    print(routes)
            
    answer = 1
    lastCam = routes[0][1]
    for i in range(1, len(routes)):
        s = routes[i][0]
        e = routes[i][1]
        
        if s <= lastCam and e >= lastCam:
            continue
        else:
            answer += 1
            lastCam = e
    return answer