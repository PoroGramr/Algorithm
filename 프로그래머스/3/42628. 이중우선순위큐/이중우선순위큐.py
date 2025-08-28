import heapq
def solution(operations):
    heap = []
    answer = []
    
    for oper in operations:
        op, num = oper.split(" ")
        num = int(num)
        
        if op == "I":
            heapq.heappush(heap,num)
        elif op == "D" and num == -1:
            if heap:
                heapq.heappop(heap)
        elif op == "D" and num == 1:
            if heap:
                maxVal = max(heap)
                heap.remove(maxVal)
                heapq.heapify(heap)
    
    if heap:
        curMax = max(heap)
        curMin = heapq.heappop(heap)
        answer = [curMax,curMin]
    else:
        answer =[0,0]
    return answer