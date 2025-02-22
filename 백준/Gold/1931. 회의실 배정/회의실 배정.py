n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key = lambda x : (x[1], x[0]))

curEnd = data[0][1]
count = 1

for i in range(1, len(data)):
    if data[i][0] >= curEnd:
        count += 1
        curEnd = data[i][1]

print(count)