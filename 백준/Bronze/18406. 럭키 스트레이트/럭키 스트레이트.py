data = input()

data = list(data)

n = len(data) // 2 - 1

sum1 = 0
for i in range(0, n + 1):
    sum1 += int(data[i])

sum2 = 0
for j in range(n+1, len(data)):
    sum2 += int(data[j])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
