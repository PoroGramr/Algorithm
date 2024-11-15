T = int(input())

for t in range(1, T + 1):
    A, B, C = map(int, input().split())

    ans = C // min(A, B)

    print(f"#{t} {ans}")