from collections import deque

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 문서의 개수 N과 목표 문서의 위치 M 입력
    N, M = map(int, input().split())
    # 문서의 중요도 리스트 입력
    data = list(map(int, input().split()))

    # (문서 중요도, 원래 위치) 형태로 deque에 저장
    queue = deque([(data[i], i) for i in range(N)])
    # 출력 순서 카운트
    order = 0

    while queue:
        # 현재 문서가 가장 중요한 문서인지 확인
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            # 출력 순서 증가
            order += 1
            # 출력한 문서가 목표 문서라면 현재 순서를 출력
            if queue[0][1] == M:
                print(order)
                break
            # 출력 완료한 문서는 큐에서 제거
            queue.popleft()
        else:
            # 중요도가 낮은 문서는 뒤로 보냄
            queue.append(queue.popleft())
