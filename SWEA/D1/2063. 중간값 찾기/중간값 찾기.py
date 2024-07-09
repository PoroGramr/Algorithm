T = int(input())

data = list(map(int, input().split()))

data.sort()

print(data[(T // 2)])