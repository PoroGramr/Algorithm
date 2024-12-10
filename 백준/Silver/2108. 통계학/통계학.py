import sys
input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))


# 신술 평균
num1 = round(sum(nums) / n)

# 중앙값
numsCopy = sorted(nums)
num2 = numsCopy[n // 2]

# 최빈값
check = [0] * 8001
for n in nums:
    cn = n + 4000

    check[cn] += 1

maxn = max(check)

popul = []

for c in range(len(check)):
    if check[c] == maxn:
        popul.append(c-4000)

num3 = 0
if len(popul) == 1:
    num3 = popul[0]
else:
    num3 = popul[1]

# 범위
num4  = max(nums) - min(nums)

print(num1)
print(num2)
print(num3)
print(num4)









