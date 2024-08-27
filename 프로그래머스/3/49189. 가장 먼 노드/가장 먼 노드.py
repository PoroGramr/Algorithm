"""
- 노드 번호가 1번부터 있으면, 0번 인덱스 버리고 데이터 구성하기
"""

from collections import deque

def solution(n, edge):
    
    # 주어진 입력을 graph로 만들기: 인접 리스트
    graph = []
    for _ in range(n+1):
        graph.append([])
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 방문리스트를 만들어준다. : DFS와 동일
    level = [-1]*(n+1) # [-1, -1, ..] # visited의 역할
    level[1] = 0
    
    # 그래프를 탐색할 queue를 만들어주고
    queue = deque([])
    queue.append(1) # 탐색을 시작할 기준 노드를 저장해준다.
    
    while queue:
        node = queue.popleft() # 노드를 빼주고
        
        for neighbor in graph[node]: # 인접 노드를 순회
            if level[neighbor] == -1: # 아직 방문한 적 없는 노드
                level[neighbor] = level[node] + 1 # 방문 여부를 업데이트
                queue.append(neighbor)
    
    # 최대값의 갯수 찾기
    answer = 0

    max_level = max(level)
    for l in level:
        if l == max_level:
            answer += 1
    
    return answer