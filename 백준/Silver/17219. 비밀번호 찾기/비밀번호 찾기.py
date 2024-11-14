from collections import defaultdict

N, M = map(int, input().split())

sites = defaultdict(list)

for _ in range(N):
    address, pw = map(str, input().split(" "))
    sites[address] = pw

for _ in range(M):
    find = input()
    print(sites[find])