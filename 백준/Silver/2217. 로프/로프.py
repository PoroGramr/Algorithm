n = int(input())

data = []

for _ in range(n):
    data.append(int(input()))

data.sort()

answer = 0

for i in range(n):
    answer = max(answer, data[i] * (n - i))

print(answer)