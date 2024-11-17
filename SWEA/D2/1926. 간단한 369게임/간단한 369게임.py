n = int(input())
ans = []
for i in range(1, n+1):
    num = list(str(i))
    mCount = 0
    if "3" in num or "6" in num or "9"in num:
        three = num.count("3")
        six = num.count("6")
        nine = num.count("9")
        mCount = three + six + nine

        ans.append("-" * mCount)

    else:
        ans.append(str(i))

print(*ans)
