a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]

a,b  = int(a), int(b)
c = a + b
c = str(c)
c = c[::-1]
print(int(c))