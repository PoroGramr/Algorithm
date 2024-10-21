t = int(input())

for T in range(1, t+1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(input())
    
    data = set(data)
    data = list(data)
    data.sort(key = lambda x : (len(x), x))
    
    print(f"#{T}")
    for p in data:
        print(p)