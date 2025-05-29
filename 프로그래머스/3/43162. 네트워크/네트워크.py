from collections import deque

def solution(n, computers):
    answer = 0
    
    # 방문 처리를 위한 배열
    v = [0] * n
    q = deque()
    
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            q.append(i)
            answer += 1
            
            while q:
                c = q.popleft()        
                neis = computers[c]
                for n in range(len(neis)):
                    if neis[n] == 1 and v[n] == 0:
                        v[n] = 1
                        q.append(n)
    return answer