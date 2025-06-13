m = int(input())

answer = 0

found = False

for i in range(m // 2 + 1):
    if(m - 2 * i) % 5 == 0:
        print(i + (m - 2 * i)//5)
        found = True
        break

if not found:
    print(-1)