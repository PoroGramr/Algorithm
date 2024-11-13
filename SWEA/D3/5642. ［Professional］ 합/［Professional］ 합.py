T = int(input())

for t in range(1, T + 1):
    N = int(input())
    
    data = list(map(int, input().split()))
    
    # 카데인 알고리즘을 활용한 풀이
    currentSum = data[0]
    maxSum = data[0]

    for i in range(1, N):
        currentSum = max(data[i], currentSum+ data[i])
        maxSum = max(maxSum, currentSum)

    print(f"#{t} {maxSum}")
