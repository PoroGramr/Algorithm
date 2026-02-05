import sys
import heapq
input = sys.stdin.readline

maxh, minh = [], []
level = {}

N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    level[P] = L
    heapq.heappush(maxh, (-L, -P))
    heapq.heappush(minh, (L, P))

M = int(input())
for _ in range(M):
    ops = input().split()
    op = ops[0]

    if op == "recommend":
        num = int(ops[1])

        if num == 1:
            while maxh:
                L = -maxh[0][0]
                P = -maxh[0][1]

                if P in level and level[P] == L:
                    print(P)
                    break
                heapq.heappop(maxh)

        else:  # num == -1
            while minh:
                L, P = minh[0]

                if P in level and level[P] == L:
                    print(P)
                    break
                heapq.heappop(minh)

    elif op == "add":
        P = int(ops[1])
        L = int(ops[2])

        level[P] = L
        heapq.heappush(maxh, (-L, -P))
        heapq.heappush(minh, (L, P))

    elif op == "solved":
        P = int(ops[1])
        if P in level:
            del level[P]
