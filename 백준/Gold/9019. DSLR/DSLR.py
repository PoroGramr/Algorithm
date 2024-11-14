from collections import deque

def bfs(start, end):
    q = deque()
    q.append((start,""))

    v = [0] * 10000
    v[start] = 1

    while q:
        num, com = q.popleft()

        if num == end:
            return com


        D = (num * 2) % 10000
        if v[D] == 0:
            v[D] = 1
            q.append((D, com + "D"))

        S = num - 1
        if S == -1:
            S = 9999
        if v[S] == 0:
            v[S] = 1
            q.append((S, com +"S"))

        # L
        L = (num % 1000) * 10 + num // 1000
        if v[L] == 0:
            v[L] = 1
            q.append((L, com+"L"))

        # R

        R = (num % 10) * 1000 + num // 10
        if v[R] == 0:
            v[R] = 1
            q.append((R, com + "R"))


N = int(input())

commands = []
for _ in range(N):
    a,b = map(int, input().split())
    commands.append((a,b))


for start,end in commands:
    print(bfs(start, end))