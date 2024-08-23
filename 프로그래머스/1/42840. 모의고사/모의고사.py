"""
문제이해
- 각 3명의 수포자는 각각 본인들만의 패턴으로 정답을 찍음
- 1번 : 1 2 3 4 5 반복
- 2번 : 2 1 2 3 2 4 2 5 반복
- 3번 : 3 3 1 1 2 2 4 4 5 5 반복

- 입력 : 1번 문제부터 마지막 문제까지의 정답이 순서대로 담긴 리스트
- 출력 : 가장 높은 점수를 받은 사람의 번호 리스트, 동일한 점수를 받은 사람이 여러명일 경우
오름차순으로 정렬

아이디어
- Brute Force
- 문제랑 답이랑 다 비교
    - 패턴에 따라 답을 입력 -> 문제번호 % 패턴수 => 어떻게 답했는지 확인

제한사항
- n : 10,000
"""
def solution(answers):
    supo =[
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5 ,5]
    ]
    
    # 각 수포자별 정답 갯수 저장 리스트
    correct = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        # idx 문제 번호, ans 정답
        for i in range(3):
            if ans == supo[i][idx % len(supo[i])]:
                correct[i] += 1
                
    MAX = max(correct) # 가장 많이 맞춘 정답 수
    
    answer = []
    
    for idx, cor in enumerate(correct):
        if cor == MAX:
            answer.append(idx+1)
    return answer