T = int(input())
dct = {}
rDct = {}
i, j = 1, 1
for n in range(1, 50_000):
    dct[n] = (i,j)
    rDct[(i,j)] = n
    i, j = i -1, j + 1

    if i < 1:
        i, j = j , 1


for t in range(1, T + 1):
    p, q = map(int, input().split())

    # 1. p, q 값의 좌표로 전환
    pi, pj = dct[p]
    qi, qj = dct[q]

    # 2. 좌표를 값으로 변환
    ans = rDct[(pi + qi, pj + qj)]

    print(f"#{t} {ans}")