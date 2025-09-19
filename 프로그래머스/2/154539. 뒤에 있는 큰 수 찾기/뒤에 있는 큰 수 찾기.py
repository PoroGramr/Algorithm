def solution(numbers):
    n = len(numbers)
    ans = [-1] * n
    stack = []  

    for i in range(n - 1, -1, -1):
        x = numbers[i]
        # 현재 값보다 작거나 같은 후보들은 제거 (가장 가까운 '큰' 수만 남기기 위해)
        while stack and stack[-1] <= x:
            stack.pop()
        # 스택 top이 바로 뒤에 있는 가장 가까운 큰 수
        if stack:
            ans[i] = stack[-1]
        # 현재 값을 다음 원소들의 후보로 push
        stack.append(x)
    return ans