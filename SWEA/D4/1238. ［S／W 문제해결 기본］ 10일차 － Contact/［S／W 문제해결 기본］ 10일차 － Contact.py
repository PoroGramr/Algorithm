from collections import deque

def bfs(s):
    q = deque()
    v = [0] * 101
    q.append(s)  # 시작점 s를 큐에 추가

    v[s] = 1
    large = s  # large는 s부터 시작해야 함

    while q:
        n = q.popleft()

        if v[large] < v[n] or (v[large] == v[n] and large < n):
            large = n
        

        for p in nei[n]:
            if v[p] == 0:
                q.append(p)
                v[p] = v[n] + 1

    return large



for t in range(1, 11):

    # 입력받는 데이터의 길이, 시작점
    cul , st = map(int, input().split())

    # 입력받는 데이터 (from to from to....)
    data = list(map(int, input().split()))

    # 가장 큰값
    big = max(data)

    # 가장 큰 값을 바탕으로 리스트 생성
    nei = [[] for _ in range(big + 1)]

    for i in range(len(data)):
        if i % 2 == 0:
            continue
        else:
            nei[data[i-1]].append(data[i])

    ans = bfs(st)

    print(f"#{t} {ans}")