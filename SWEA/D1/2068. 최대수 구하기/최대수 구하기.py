n = int(input())

for i in range(0,n):
    data = list(map(int,input().split()))
    data.sort()
    print("#",end="")
    print(i+1, end=" ")
    print(data[-1])
    