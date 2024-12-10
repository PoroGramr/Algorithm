import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

# 산술 평균
num1 = round(sum(nums) / n)

# 중앙값
nums.sort()
num2 = nums[n // 2]

# 최빈값
check = [0] * 8001
for x in nums:
    check[x + 4000] += 1

max_count = max(check)
popul = []

for i in range(8001):
    if check[i] == max_count:
        popul.append(i - 4000)

num3 = popul[0] if len(popul) == 1 else popul[1]

# 범위
num4 = nums[-1] - nums[0]

# 출력
print(num1)
print(num2)
print(num3)
print(num4)
