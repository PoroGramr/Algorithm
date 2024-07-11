n = int(input())

for i in range(0,n):
    data = list(map(int, input().split()))
    print("#", end="")
    print(i + 1, end=" ")
    print(round(sum(data) / len(data)))