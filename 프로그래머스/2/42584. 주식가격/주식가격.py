"""
문제 이해
prices가 각각 다른 주식이 아니라 같은 주식이다.
즉, 주식 하나의 가격 변동을 적어놓은 리스트이다.
- 입력 : 초당 주식가격이 저장된 [리스트] 숫자
- 출력 : 주식 가격이 떨어지지 않은 단위 기간(초) 수 

아이디어
- [1, 2, 3, 2, 3]
- [0, 0, 1, 0, 0]

- stack = [(0,1), (1,2), (2,3)
- (3, 2): 스택 안에서 나보다 주식가격이 큰 기수를 빼기
    - stack.pop() : 주식 가격이 유지된 기간을 계산(3 - 2) : 1
- 기본적으로 해당 초수의 주식가격을 쌓는다.
- 스택 안에 나보다 가격이 큰 기간이 저장되어있다면 -> 해당 기간의 가격은 유지되지 못함
    - pop 해주고 cur - popped (기간)
- 종료된 후에도 Stack 남아있는 값들은 마지막 종료 시기를 기준으로 유지기간을 계산

...

제한사항
- prices n : 100,000 100k
- O(n*n) : 100k * 100k = 10,000 M -> x
"""
def solution(prices):
    # answer를 초기화
    answer = [0] * len(prices)
    stack = [] # (sec, price)
    
    # 주식 가격이 유지되지 못한 기간을 업데이트
    
    for sec in range(len(prices)): # sec : 0 ~ len(prices) 
        while stack and prices[sec] < stack[-1][1]:
            popped = stack.pop()
            answer[popped[0]] = sec - popped[0]
        stack.append((sec, prices[sec]))
       #  [0,0,1,0,0]
    
    
    # 종료된 후에도 Stack 남아있는 값들은 마지막 종료 시기를 기준으로 유지기간을 계산
    while stack:
        popped = stack.pop()
        answer[popped[0]] = (len(prices) - 1) - popped[0]
    # 	[4, 3, 1, 1, 0]
        
    return answer