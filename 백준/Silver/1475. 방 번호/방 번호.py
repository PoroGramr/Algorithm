inNum = input()

count = [0] * 10

for i in range(len(inNum)):
    num = int(inNum[i])

    if num == 6 or num == 9:
        if count[6] <= count[9]:
            count[6] += 1
        else:
            count[9] += 1
    else:
        count[num] += 1 

print(max(count))