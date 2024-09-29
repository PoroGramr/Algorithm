n = int(input())

for i in range(n):
    answer = 0
    a,b,c = map(int, input().split())
    data = [a,b,c]
    ac = data.count(a)
    bc = data.count(b)
    cc = data.count(c)
    if ac == 1 or ac == 3:
        answer = a
    elif bc == 1 or bc == 3:
        answer = b
    elif cc == 1 or cc == 3:
        answer = c
    print(f"#{i+1} {answer}")