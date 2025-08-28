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
    
    heap = []
    done = 0
    while done < sumJob:
        
        while curIdx < sumJob and jobs[curIdx][0] <= time:
            req, dur = jobs[curIdx]
            heapq.heappush(heap, (dur, req))
            curIdx += 1
        
        if heap:
            runTime, req= heapq.heappop(heap)
            time += runTime
            sumTime += (time - req)
            done += 1
        
        else:
            if curIdx < sumJob:
                time = jobs[curIdx][0]
        
    return sumTime // sumJob