N, M = map(int, input().split())
hear = set()
saw = set()

for _ in range(N):
    hear.add(input())

for _ in range(M):
    saw.add(input())



ans = sorted(hear & saw)

print(len(ans))
print("\n".join(ans))
