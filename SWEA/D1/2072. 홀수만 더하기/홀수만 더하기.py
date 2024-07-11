n = int(input())

for i in range(0,n):
    data = list(map(int, input().split()))
    sum = 0
    
    for k in data:
        if k % 2 != 0 :
        	sum += k
        
    print("#", end="")
    print(i + 1, end=" ")
    print(sum)