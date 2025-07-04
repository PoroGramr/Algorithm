n = int(input())
data = list(map(int, input().split()))


answers=[1 for _ in range(n)]

# 리스트의 요소 하나씩 기준으로 좌측은 가장 긴 수열 우축은 가장 짧은 수열 계산
maxdp = [1 for _ in range(n)]
for a in range(n):
    for b in range(a):        
        if data[a] > data[b]:
            maxdp[a] = max(maxdp[a], maxdp[b] + 1)

    # print(i, data[i], maxdp)
mindp = [1 for _ in range(n)]
for c in range(n-1,-1,-1):
    for d in range(n-1,c,-1):
        if data[c] > data[d]:
            mindp[c] = max(mindp[c], mindp[d] + 1)

answers = [0] * n
for i in range(n):
    answers[i] = maxdp[i] + mindp[i] - 1


print(max(answers))