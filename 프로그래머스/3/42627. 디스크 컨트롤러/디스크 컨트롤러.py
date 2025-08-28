import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간 순으로 정렬
    heap = []
    
    time, idx, total = 0, 0, 0
    length = len(jobs)
    
    while idx < length or heap:
        # 현재 시각(time)까지 들어온 작업을 heap에 추가 (소요시간 기준)
        while idx < length and jobs[idx][0] <= time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        if heap:
            dur, start = heapq.heappop(heap)
            time += dur
            total += (time - start)  # 대기시간 = 완료시각 - 요청시각
        else:
            # 아직 요청된 작업이 없으면 시각을 다음 요청시각으로 이동
            time = jobs[idx][0]
    
    return total // length
