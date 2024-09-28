n = int(input())

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    print(f"#{i+1} {answer}")