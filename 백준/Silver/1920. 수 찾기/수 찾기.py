N = int(input())

A = list(map(int, input().split()))

M = int(input())

B = list(map(int, input().split()))


A.sort()

def binS(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return 1
        
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        
    
    return 0

for b in B:
    print(binS(A,b))