from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N):
    current = input().rstrip()
    if len(current) < M:
        continue
    dict[current] = dict.get(current, 0) + 1

sortedDict = sorted(dict.items(), key =lambda x : [-x[1], -len(x[0]), x[0]] )
for name, count in sortedDict:
    print(name)