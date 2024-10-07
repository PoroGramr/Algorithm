from collections import deque



def bfs(j):
    q = deque()
    q.append(j)
    v[j] = 1

    while q:
        nei = q.popleft()
        
        # 이웃들 데이터를 바탕으로 아직 방문되지 않았다면 방문한 후 v = 1  
        for node in data[nei]:
            if v[node] != 1:
                q.append(node)
                v[node] = 1

T = int(input())

for i in range(1, T+1):
    N,M = map(int, input().split()) # N명의 사람, M개의 줄의 걸쳐서 관계를 나타냄
    data = [[] for _ in range(N+1)]

    # 관계를 리스트로 표현
    for _ in range(M):
        a,b = map(int, input().split())
        data[a].append(b)
        data[b].append(a)
    
    v = [0 for _ in range(N+1)]

    answer = 0

    # 인덱스 1부터 순차적으로 bfs 시작
    # 방문하지 않았을 경우에만 시작
    # bfs가 실행 될 때마다 카운트 + 1
    for k in range(1,N+1):
        if v[k] == 0:
            bfs(k)
            answer += 1
    
    print(f"#{i} {answer}")


    
