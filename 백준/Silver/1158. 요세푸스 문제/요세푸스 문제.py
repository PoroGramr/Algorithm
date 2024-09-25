from collections import deque
n, k= map(int, input().split())

queue = deque(range(1, n+1))

answer = []

while queue:
    # k개만큼 큐의 top로 보냄
    for _ in range(k - 1):
        queue.append(queue.popleft())
    # k 번쨰 즉, 현재 큐의 tail 을 pop
    answer.append(queue.popleft())

print(str(answer).replace("[", "<").replace("]",">"))