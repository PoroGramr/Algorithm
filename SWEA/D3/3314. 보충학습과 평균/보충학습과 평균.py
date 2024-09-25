n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    for k in range(len(data)):
        if data[k] < 40:
            data[k] = 40
    all = sum(data)
    answer = all // len(data)
    print(f"#{i+1} {answer}")