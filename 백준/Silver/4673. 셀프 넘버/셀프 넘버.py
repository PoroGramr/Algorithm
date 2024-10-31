ori = set(i for i in range(1, 10001))

data = set()

for i in range(1, 10001):
    tmp = i
    i = str(i)
    for s in range(len(i)):
        tmp += int(i[s])
    data.add(tmp)

ans = sorted(ori- data)
for x in ans:
    print(x)
