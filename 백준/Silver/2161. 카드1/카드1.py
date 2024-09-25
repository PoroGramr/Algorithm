from collections import deque
n = int(input())
data = [i for i in range(1, n+1)]
queue = deque(data)
left = []
while len(queue) != 1:
    left.append(queue.popleft())
    queue.append(queue.popleft())
left.append(queue.popleft())
for k in left:
    print(f"{k} ",end="")
    