T = int(input())

for t in range(1, T+1):

    count = [0] * 101
    n = int(input())
    data = list(map(int, input().split()))
    for d in data:
        count[d] += 1
    ans = 0

    for c in range(1, len(count)):
        if count[ans] <= count[c]:
            ans = c

    print(f"#{t} {ans}")
            