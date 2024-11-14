from collections import defaultdict

N , M = map(int, input().split())

num  = defaultdict(list)
name = defaultdict(list)
for i in range(N):
    poke = input()
    num[i + 1].append(poke)
    name[poke].append(i + 1)

#data.sort()

for _ in range(M):
    com = input()

    if com.isalpha():
        print(*name[com])
    else:
        print(*num[int(com)])