import heapq

def solution(a,b):
    # b가 a보다 값이 커서 이겨야 함!
    # b의 최대한 최소 값으로 a를 이겨야 함!
    a.sort()
    b.sort()


    
    answer = 0
    
    i = 0
    j = 0
    
    length = len(a)
    
    visitedA = [False * length]
    visitedB = [False * length]
    while i < length and j < length:
            if a[i] < b[j]:
                answer += 1
                i += 1
                j += 1
            else:
                j += 1
                
    return answer