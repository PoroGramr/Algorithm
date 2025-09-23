def solution(routes):

    routes.sort(key = lambda x : (x[1], x[0]))
    
    # 첫번째 차 진출 지점 기준으로 연산 시작        
    answer = 1
    lastCam = routes[0][1]
    
    
    for i in range(1, len(routes)):
        s = routes[i][0]
        e = routes[i][1]
        
        # 만약 이전 진출 차량과 이동 경로 겹치는 부분이 있다면 카메라수 추가 x
        if s <= lastCam and e >= lastCam:
            continue
            
        # 이전 진출 차량과 이동 경로가 겹치지 않는다면 카메라수 추가 O, 새로운 카메라 위치 설정
        else:
            answer += 1
            lastCam = e
        
    return answer