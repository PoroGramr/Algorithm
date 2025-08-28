import heapq


#[0초에 요청들어옴, 3ms 소요]
def solution(jobs):
    jobs.sort()
    heap = []
    n = len(jobs)
    time = 0
    idx  = 0
    total = 0
    done = 0
    
    while done < n:
        while idx < n and jobs[idx][0] <= time:
            req, dur = jobs[idx]
            heapq.heappush(heap, (dur, req))
            idx += 1
        
        if heap:
            dur, req = heapq.heappop(heap)
            time += dur
            total += time - req
            done += 1
        else:
            time = jobs[idx][0]
    
    return total // n
    
    