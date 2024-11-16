T = 10

for t in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    count = 0
    for i in range(2, len(data)- 2):
        left1 = data[i-1]
        left2 = data[i-2]
        right1 = data[i+1]
        right2 = data[i+2]

        high = max(left1, left2, right1, right2)
        if data[i] > high:
            count += data[i] - high

    
    print(f"#{t} {count}")


