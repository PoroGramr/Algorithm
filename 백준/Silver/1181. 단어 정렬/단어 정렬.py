n = int(input())

data = []

for _ in range(n):
    insert = input()
    data.append((insert, len(insert)))

data = set(data)
data = list(data)

data.sort(key = lambda x : (x[1],x[0] ))

for i in range(len(data)):
    print(data[i][0])