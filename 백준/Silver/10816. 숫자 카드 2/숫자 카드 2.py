N = int(input())

S = list(map(int, input().split()))

M = int(input())

C = list(map(int, input().split()))

S.sort()


cnt = {}

for s in S:
    if s in cnt:
        cnt[s] += 1
    else:
        cnt[s] = 1
answer = []

for c in C:
    if c in cnt:
        answer.append(cnt[c])
    else:
        answer.append(0)
print(*answer)