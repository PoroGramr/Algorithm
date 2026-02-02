K, L = map(int, input().split())

data = {}

for i in range(L):
    number = input()
    data[number] = i

sortStudent = sorted(data, key = lambda x : data[x])

for i in range(0, min(K, len(sortStudent))):
    print(sortStudent[i])


