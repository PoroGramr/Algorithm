
dic = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR": 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

T = int(input())
for t in range(1, T + 1):
    t, s  = map(str, input().split())
    data = list(map(str, input().split()))
    soData = []
    for s in data:
        soData.append(dic[s])

    soData.sort()

    ansData = []

    for a in soData:
        for key, value in dic.items():
            if value == a:
                ansData.append(key)
                break


    print(f"{t}")
    print(*ansData)