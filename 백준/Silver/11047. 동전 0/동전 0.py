N, M = map(int, input().split())

money = []

for _ in range(N):
    money.append(int(input()))

i = len(money) - 1

while i != 0:
    if M < money[i]:
        i -= 1
    else:
        break
coins = 0
while M != 0:
    coins += M // money[i]
    M %= money[i]
    i -= 1
print(coins)




