from collections import deque

def solution(n, computers):
    answer = 0
    v = [0] * n
    q = deque()
    for i in range(n):
        if v[i] == 0:
            answer += 1
            v[i] = 1
            q.append(i)
            
            while q:
                current = q.popleft()
                for j, nei in enumerate(computers[current]):
                    if v[j] == 0 and nei == 1:
                        v[j] = 1
                        q.append(j)

    return answer