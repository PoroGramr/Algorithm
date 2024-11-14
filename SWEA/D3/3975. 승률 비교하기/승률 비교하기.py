T = int(input())
ans = []
for t in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    alice = A / B
    bob = C / D

    if bob > alice:
        ans.append(f"#{t} BOB")
    elif bob < alice:
        ans.append(f"#{t} ALICE")
    elif bob == alice:
        ans.append(f"#{t} DRAW")

for a in ans:
    print(a)
