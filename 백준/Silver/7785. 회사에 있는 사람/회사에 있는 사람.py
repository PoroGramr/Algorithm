N = int(input())

data = set()

for _ in range(N):
    name, inst = map(str, input().split())
    
    if inst == "enter":
        data.add(name)
    else:
        data.discard(name)

data = list(data)

data.sort(reverse = True)
for d in data:
    print(d)