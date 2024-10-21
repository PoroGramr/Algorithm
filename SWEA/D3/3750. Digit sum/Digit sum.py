t = int(input())
data = []
for T in range(1, t+1):
    n = list(input())
    tmp = 0
    while len(n) != 1:
        tmp = 0
        for p in n:
            tmp += int(p)
        
        n = list(str(tmp))


    data.append(int(n[0]))

for a in range(len(data)):
    print(f"#{a+1} {data[a]}")
