n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))
    

nums.sort()

maxCount = 1
curCount = 1
value = float('inf')
answer = nums[0]


for i in range(1,n):
    if nums[i] == nums[i - 1]:
        curCount += 1
    else:
        curCount = 1
    
    
    if maxCount < curCount and value > nums[i]:
        answer = nums[i]
        maxCount = curCount

print(answer)
    