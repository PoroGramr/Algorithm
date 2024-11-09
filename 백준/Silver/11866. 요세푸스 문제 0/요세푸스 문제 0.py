N, K = map(int, input().split())

data = [i for i in range(1, N+1)]
ans = []
i = K - 1
while data:
    if i >= len(data):
        i = i % len(data)
    ans.append(data[i])
    data.pop(i)

    i += K - 1
print("<", end="")
print(*ans, sep=", ", end="")
print(">")
