big = 0
idx = 0
data = []
for i in range(9):
    data.append(int(input()))

for j in range(len(data)):
    if data[j] > big:
        big = data[j]
        idx = j + 1
print(big)
print(idx)
