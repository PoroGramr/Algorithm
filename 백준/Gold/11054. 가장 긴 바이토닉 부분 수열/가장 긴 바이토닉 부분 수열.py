n = int(input())
data = list(map(int, input().split()))


answers=[1 for _ in range(n)]

# 리스트의 요소 하나씩 기준으로 좌측은 가장 긴 수열 우축은 가장 짧은 수열 계산
for i in range(n):
    maxdp = [1 for _ in range(n)]
    for a in range(0,i+1):
        for b in range(a):        
            if data[a] > data[b]:
                maxdp[a] = max(maxdp[a], maxdp[b] + 1)

    # print(i, data[i], maxdp)
    mindp = [1 for _ in range(n)]
    for c in range(i,n):
        for d in range(i,c+1):
            if data[c] < data[d]:
                mindp[c] = max(mindp[c], mindp[d] + 1)

    answer = max(mindp) + max(maxdp) - 1
    answers.append(answer) 


print(max(answers))