from collections import deque

def bfs(s):
    q = deque()
    q.append(s)  # 시작점 s를 큐에 추가
    visited = [False] * (len(nei))  # 방문 체크 리스트
    visited[s] = True  # 시작점 방문 처리

    large = s  # 가장 큰 번호를 저장할 변수
    last_level = []  # 마지막 레벨의 노드들을 저장할 리스트

    while q:
        size = len(q)  # 현재 레벨의 노드 수
        last_level = []  # 매번 레벨이 바뀔 때 노드를 초기화

        for _ in range(size):
            n = q.popleft()
            last_level.append(n)  # 현재 레벨의 노드를 저장

            for p in nei[n]:  # 현재 노드의 자식 노드들 탐색
                if not visited[p]:  # 방문하지 않은 노드만 큐에 추가
                    q.append(p)
                    visited[p] = True  # 방문 처리

    # 마지막 레벨의 노드 중 가장 큰 번호를 반환
    return max(last_level)


for t in range(1, 11):

    # 입력받는 데이터의 길이, 시작점
    cul, st = map(int, input().split())

    # 입력받는 데이터 (from to from to....)
    data = list(map(int, input().split()))

    # 가장 큰 값을 바탕으로 리스트 생성
    big = max(data)
    nei = [[] for _ in range(big + 1)]  # 인접 리스트 생성

    # 연락망 데이터 입력
    for i in range(0, len(data), 2):
        nei[data[i]].append(data[i+1])

    ans = bfs(st)
    print(f"#{t} {ans}")
