T = int(input())

for t in range(1, T + 1):
    N = int(input())

    data = []

    for _ in range(N):
        data.append(int(input()))

    all = sum(data)

    cen = all // N

    count = 0
    for i in data:
        if i > cen:
            count += i - cen

    print(f"#{t} {count}")







