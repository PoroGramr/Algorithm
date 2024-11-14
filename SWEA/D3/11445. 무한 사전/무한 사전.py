T = int(input())
for t in range(1, T + 1):
    a = input().rstrip()
    b = input().rstrip()

    if a+"a" != b:
        print(f"#{t} Y")
    else:
        print(f"#{t} N")