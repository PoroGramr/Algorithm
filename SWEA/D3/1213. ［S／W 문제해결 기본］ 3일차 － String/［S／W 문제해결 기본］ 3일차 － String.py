T = 10

for t in range(1, T+1):
    a = int(input())
    ck = list(input())
    ckL = len(ck)
    data = list(map(str, input()))
    ans  = 0
    for i in range(len(data) - 1):
        if data[i:i+ckL] == ck:
            ans += 1
    print(f"#{t} {ans}")



