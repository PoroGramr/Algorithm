def solution(number: str, k: int) -> str:
    stack = []
    for d in number:
        while k > 0 and stack and stack[-1] < d:
            stack.pop()
            k -= 1
        stack.append(d)
    if k > 0:  # 아직 덜 지웠으면 뒤에서 자름
        stack = stack[:-k]
    return ''.join(stack)
