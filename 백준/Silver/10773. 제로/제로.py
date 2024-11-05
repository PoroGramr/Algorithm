N = int(input())
data = []
for i in range(N):
    num = int(input())

    if num !=0:
        data.append(num)
    else:
        data.pop(-1)
print(sum(data))