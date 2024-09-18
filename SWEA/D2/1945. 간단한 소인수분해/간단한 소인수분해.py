n = int(input())
# 소수들을 바탕으로 연산하기 위한 리스트
prime = [2,3,5,7,11]



for i in range(n):
    num = int(input())
    
    # 각 숫자들을 카운트 하기 위한 리스트
    count = [0,0,0,0,0]
    
    # prime으 소수들을 하나하나씩 연산함
    for k in range(len(prime)):
        
        # ex.  2로 나눠서 나눠지지 않을때까지 계속 반복
        while num % prime[k] == 0:
            num //= prime[k]
            count[k] += 1
        
    print(f"#{i+1} ", end="")
    for a in count:
        print(a, end =" ")
    print("")
        
    
        
