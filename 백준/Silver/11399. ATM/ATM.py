a = int(input())
d = list(map(int, input().split()))

d.sort()

result = 0
x = 0

for i in range (a):
    x+=d[i]
    result+=x

print(result)