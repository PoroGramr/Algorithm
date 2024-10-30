T = int(input())
count = 0
for t in range(1, T+1):
    data = list(map(str, input()))
    error = False


    for i in range(len(data) - 1):
        if data[i] != data[i+1] and data[i] in data[i+1:]:
            error = True
            break

    if not error:
        count += 1

print(count)