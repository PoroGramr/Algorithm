T = int(input())

for t in range(1, T + 1):
    N = int(input())
    data = list(map(str, input().split()))

    if N % 2== 0:
        m = N // 2
        deckA = data[0:m]
        deckB = data[m::]
        ans = []
        for _ in range(m):
            ans.append(deckA.pop(0))
            ans.append(deckB.pop(0))
        print(f"#{t}", end=" ")
        print(*ans)

    else:
        m = N // 2
        deckA = data[0:m+1]
        deckB = data[m+1::]
        ans = []
        for _ in range(m):
            ans.append(deckA.pop(0))
            ans.append(deckB.pop(0))
        ans.append(deckA.pop(0))
        print(f"#{t}", end=" ")
        print(*ans)
