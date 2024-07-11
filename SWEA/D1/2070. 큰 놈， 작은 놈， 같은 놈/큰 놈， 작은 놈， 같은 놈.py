def compare(a,b):
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")

n = int(input())

for i in range(0,n):
    data  = list(map(int, input().split()))
    print("#", end="")
    print(i + 1, end=" ")
    compare(data[0],data[1])