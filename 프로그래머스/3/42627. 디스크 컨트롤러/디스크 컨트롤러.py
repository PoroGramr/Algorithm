import heapq

def solution(jobs):
    jobs.sort()
    
    # 일의 총 개수
    sumJob = len(jobs)
    
    # 현재 job idx
    curIdx = 0
    
    # 시각
    time = 0
    
    # 대기시간의 합
    sumTime = 0
    
    # 완료된 작업의 수
    done = 0
    
    # 대기 큐
    heap = []
    
    # 작업이 다 완료될때 까지 루프
    while done < sumJob:
        
        # 아직 남은 작업이 있고, 진행할 작업이 요청받은 시간이 현재 시각 이하인경우
        while curIdx < sumJob and jobs[curIdx][0] <= time:
            req, dur = jobs[curIdx]
            # 정렬 기준에 맞게 힙에 삽입
            heapq.heappush(heap, (dur, req))
            curIdx += 1
        
        # 힙에 작업이 존재한다면 작업
        if heap:
            runTime, req= heapq.heappop(heap)
            time += runTime
            sumTime += (time - req)
            done += 1
        
        # 만역 아직 시간이 지나지 않아 대기큐에는 작업이 안 둘어왔지만 해야할 작업이 남아있는 경우
        else:
            if curIdx < sumJob:
                time = jobs[curIdx][0]
        
    return sumTime // sumJob