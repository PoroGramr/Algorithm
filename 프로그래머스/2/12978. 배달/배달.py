"""
다익스트라 알고리즘 : 최단 경로 탐색 활용
- 마을이랑 마을 사이의 소요시간(경로)가 주어지고
- 주어진 제한시간 k 안에 배달할 수 있는 마을싀 숫자를 찾는 문제

- 입력 
    - N : 마을 갯수 -> 노드의 수
    - road : 경로 정보 -> 엣지의 정보
    - K : 제한시간

- 출력
    - 기준마을 1번으로부터 소요시간이 K 이하인 마을의 수

자료 구조
1. 경로가 저장되어 있는 그래프
2. 각 노드까지 거리를 저장할 공간
3. 그래프를 순회할 큐

문제 해결 아이디어
1. 다익스트라 알고리즘 수행
2.K 이하인 마을의 수 세기
"""
from collections import deque

def solution(N, road, K):
    # 자료구조 만들기
    
    # 그래프 만들기
    # N + 1 개의 빈 리스트 만들어짐
    graph = []
    for i in range(N + 1): # 마을의 번호가 1부터 이므로 +1 한다. 0번노드는 사용하지 않는다.
        graph.append([])
    
    for a,b,c in road: # from, to ,distance
        graph[a].append((b, c)) # (node, distance)
        graph[b].append((a, c))
        # 방향성이 없으므로 양쪽 전부 더하기
        
    """
        [[], 
        [(2, 1), (4, 2)], 
        [(1, 1), (3, 3), (5, 2)], 
        [(2, 3), (5, 1)], 
        [(1, 2), (5, 2)], 
        [(2, 2), (3, 1), (4, 2)]]
    """
    
    # 노드까지의 거리를 저장
    distance = [float("inf")] * (N + 1)
    distance[1] = 0 # 기준점 1번 노드
    
    # graph를 순회할 queue
    queue = deque([])
    queue.append((1,0)) # node, distance # 1번 노드를 입력
    
    # 다익스트라 알고리즘을 실행
    while queue:
        curNode, curDist = queue.popleft()
        
        for node, dist in graph[curNode]:
            newDist = curDist + dist
            if distance[node] > newDist:
                distance[node] = newDist
                queue.append((node, distance[node]))

    print(distance)
    # 문제 결과에 맞게 결과 출력
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1


    return answer